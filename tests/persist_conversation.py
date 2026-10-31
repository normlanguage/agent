import json
import shutil
import sqlite3
import subprocess
from contextlib import closing
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from tempfile import TemporaryDirectory
from threading import Thread

requests = []


class Model(BaseHTTPRequestHandler):
    def do_POST(self):
        requests.append(json.loads(self.rfile.read(int(self.headers["Content-Length"]))))
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.end_headers()
        chunk = {"id": "chatcmpl-test", "model": "fixture", "choices": [
            {"index": 0, "delta": {"role": "assistant", "content": "回复"}, "finish_reason": "stop"}
        ]}
        self.wfile.write(f"data: {json.dumps(chunk)}\n\ndata: [DONE]\n\n".encode())


with HTTPServer(("127.0.0.1", 0), Model) as model, TemporaryDirectory() as temporary:
    Thread(target=model.serve_forever, daemon=True).start()
    project = Path(temporary) / "agent"
    project.mkdir()
    for source in Path(__file__).resolve().parents[1].glob("*.norm"):
        shutil.copy(source, project)
    entry = project / "main.norm"
    entry.write_text(f"""package agent
import agent.Agent
import agent.JsonPersist
import agent.SqlitePersist

Void main() {{
  var agent = Agent(apiKey: "test-secret", model: "fixture",
    endpoint: "http://127.0.0.1:{model.server_port}/chat/completions",
    persist: [JsonPersist(), SqlitePersist("logs")])
  agent.chat("第一轮")
  agent.chat("第二轮")
}}
""", encoding="utf-8")
    for _ in range(2):
        subprocess.run(["norm", "run", str(entry)], cwd=project, check=True, timeout=120)
    files = list((project / "logs").glob("*.jsonl"))
    assert len(files) == 2
    assert [m["content"] for m in requests[-1]["messages"]] == ["第一轮", "回复", "第二轮"]
    for path in files:
        text = path.read_text(encoding="utf-8")
        events = [json.loads(line) for line in text.splitlines()]
        assert "test-secret" not in text
        assert [e["input"] for e in events if e["type"] == "run_started"] == ["第一轮", "第二轮"]
        assert [e["text"] for e in events if e["type"] == "text"] == ["回复", "回复"]
        with closing(sqlite3.connect(path.with_suffix(".sqlite"))) as db:
            assert events == [json.loads(row[0]) for row in db.execute("SELECT event FROM events ORDER BY sequence")]
    model.shutdown()
