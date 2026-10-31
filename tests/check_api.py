import json
from pathlib import Path

for path in Path("build/api").rglob("*.api.json"):
    api = json.loads(path.read_text(encoding="utf-8"))
    if not api.get("exported") or not Path(api["source"]["path"]).is_file():
        continue
    declarations = list(api["declarations"])
    while declarations:
        declaration = declarations.pop()
        if declaration.get("visibility") == "private":
            continue
        if not declaration.get("document", {}).get("description", "").strip():
            raise ValueError(f"Missing API documentation in {path}: {declaration['name']}")
        declarations.extend(declaration.get("parameters", []))
        declarations.extend(declaration.get("members", []))
