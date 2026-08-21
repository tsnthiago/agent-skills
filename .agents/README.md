# Portable Agent Assets (.agents/)

This directory is the canonical home for reusable, multi-agent skills following the open `.agents/` standard.

## Layout

```text
.agents/
  README.md
  skills/
    <skill-name>/
      SKILL.md
      references/
      scripts/
      templates/
      assets/
```

## Compatibility

Skills located in `.agents/skills/` are fully compatible with:
- **Codex CLI / OpenAI Codex**
- **Anthropic Claude Code**
- **Google Antigravity (agy)**
- **Cursor IDE / Windsurf**
- **Nous Hermes Agent**
- **Cline / Roo Code**
- Any LLM orchestrator supporting system prompt injection or dynamic tool/skill loading.

## Rules for Skills
- Each skill must contain a `SKILL.md` with clear trigger conditions, workflow steps, schema/format references, and verification.
- Supporting scripts and reference files must remain self-contained inside the skill's subdirectory (`scripts/`, `references/`, etc.).
- No private credentials, machine-specific absolute paths, or proprietary secrets.
