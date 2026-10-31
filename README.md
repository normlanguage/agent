# Norm Agent library

This repository publishes the `agent` Norm module. The package contract and generated API Skill are defined by [normlanguage/package-template](https://github.com/normlanguage/package-template).

`SKILL.md` is generated from the public declarations with `norm docs . --output build/api --skill SKILL.md`; update it in the same commit as source changes.

Pass `persist: [JsonPersist(), SqlitePersist()]` to record a conversation in `session/`. Each provider accepts an optional directory, either positional (`JsonPersist("logs")`) or named (`SqlitePersist(directory: "logs")`). The providers generate matching filenames ending in `.jsonl` and `.sqlite`. SQLite uses its bundled driver. With an empty list, recording is disabled.

Each event is appended in order, including the effective model request, streamed text, tool calls, outputs and failures. The SQLite `events` table preserves insertion order in `sequence`. Reuse an Agent or pass an explicit `AgentSession` to continue a conversation. New sessions get separate files.
