# Norm Agent library

This repository publishes the `agent` Norm module. The package contract and generated API Skill are defined by [normlanguage/package-template](https://github.com/normlanguage/package-template).

`SKILL.md` is generated from the public declarations with `norm docs . --skill SKILL.md --strict`; update it in the same commit as source changes.

Enable file-backed conversation history with `Agent(..., persistJson: true)`. The default path is `agent-session.json`. Set `sessionPath` to choose a different file. Reopening the same path resumes the saved user messages, assistant outputs, tool calls and tool results. Give each independent conversation its own file and use one writer per file. An explicit `chat(session: ...)` uses that session's storage.
