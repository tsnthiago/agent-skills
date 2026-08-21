# Agent Skills (.agents/skills) 🚀

Collection of open, portable, and production-grade skills for AI Coding Agents following the open `.agents/` standard.

Designed to work seamlessly across **Anthropic Claude Code**, **OpenAI Codex**, **Google Antigravity (`agy`)**, **Cursor IDE**, **Windsurf**, **Nous Hermes Agent**, **Cline**, and **Roo Code**.

---

## 📂 Repository Structure

```text
├── .agents/
│   ├── README.md
│   └── skills/
│       ├── braiam-orchestrator/
│       │   └── SKILL.md
│       ├── spec-driven-development/
│       │   └── SKILL.md
│       ├── braiam-hybrid-worker/
│       │   └── SKILL.md
│       ├── excalidraw/
│       │   ├── SKILL.md
│       │   ├── references/
│       │   └── scripts/
│       └── evolution-api-whatsapp/
│           └── SKILL.md
├── AGENTS.md
└── README.md
```

---

## 🛠️ Published Skills

### 🧠 1. `braiam-orchestrator`
- **Location**: [`.agents/skills/braiam-orchestrator/SKILL.md`](.agents/skills/braiam-orchestrator/SKILL.md)
- **Description**: Universal AI Operating System architecture. Implements 4-tier bounded context architecture (Level 0 Core → Level 1 Project Packet → Level 2 Evidence → Level 3 Archive), privacy boundaries (`*-life-private` vs `*-company-private` vs `*-os`), and multi-agent coordination.

### 📐 2. `spec-driven-development`
- **Location**: [`.agents/skills/spec-driven-development/SKILL.md`](.agents/skills/spec-driven-development/SKILL.md)
- **Description**: Spec-Driven Development (SDD) standard for autonomous agents (inspired by GitHub Next & Matt Pocock prompting standards). Spec-first contracts, non-goals, upfront test harnesses, and deterministic verification.

### ⚡ 3. `braiam-hybrid-worker`
- **Location**: [`.agents/skills/braiam-hybrid-worker/SKILL.md`](.agents/skills/braiam-hybrid-worker/SKILL.md)
- **Description**: Remote and hybrid worker delegation protocol. Efficiently orchestrate Claude Code, OpenAI Codex, and Google Antigravity across local workstations and cloud VPS while optimizing token quotas.

### 🎨 4. `excalidraw`
- **Location**: [`.agents/skills/excalidraw/SKILL.md`](.agents/skills/excalidraw/SKILL.md)
- **Description**: Generates valid hand-drawn Excalidraw diagrams (`.excalidraw` JSON) for system architectures, workflows, sequence diagrams, and flowcharts with client-side encrypted upload script (`scripts/upload.py`).

### 💬 5. `evolution-api-whatsapp`
- **Location**: [`.agents/skills/evolution-api-whatsapp/SKILL.md`](.agents/skills/evolution-api-whatsapp/SKILL.md)
- **Description**: Diagnostic workflows, PostgreSQL database schema inspection, and instance management for self-hosted Evolution API WhatsApp stacks.

---

## 🤖 How to Use with Any AI Agent

### Universal Method (.agents standard)
Place or symlink this `.agents` directory into your project root:
- **Claude Code**: Recognizes `.agents/skills` directly.
- **Codex / Antigravity**: Point to `.agents/skills/<skill-name>/SKILL.md`.
- **Cursor / Windsurf**: Add a reference in `.cursorrules` or prompt:
  ```markdown
  Follow the rules in .agents/skills/spec-driven-development/SKILL.md
  ```
- **Hermes Agent**: Symlink or copy skills into `~/.hermes/skills/`.

---

## 📜 License
MIT License. Created by [Thiago Nobrega](https://github.com/tsnthiago).
