# Universal Agent Protocol — Agent Skills

This repository is a public collection of portable, production-grade agent skills following the open `.agents/` standard.

## Quick Start for AI Agents (Codex, Claude Code, Antigravity, Cursor, Hermes, Roo Code)

When working in this repository or consuming its skills:

1. **Discovery**: Look into `.agents/skills/<skill-name>/SKILL.md` when the user asks for capabilities related to a specific domain (e.g., diagramming, analysis, scraping).
2. **Selective Loading**: Load only the specific skill needed for the task to conserve context window.
3. **Execution**: Follow the workflow, parameters, and constraints defined in the skill's `SKILL.md`.
4. **Execution Evidence**: Always run and test any helper scripts against real data; do not fabricate execution outputs.

## Skill Catalog

- **`excalidraw`** (`.agents/skills/excalidraw/SKILL.md`): Generate valid hand-drawn Excalidraw diagram JSON files and upload them to [excalidraw.com](https://excalidraw.com) via AES-GCM encrypted shareable links.
