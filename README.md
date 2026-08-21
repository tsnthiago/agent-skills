# Agent Skills (.agents/skills) 🚀

Collection of open, portable, and production-grade skills for AI Coding Agents following the `.agents/` standard.

Designed to work seamlessly across **OpenAI Codex**, **Anthropic Claude Code**, **Google Antigravity (`agy`)**, **Cursor IDE**, **Nous Hermes Agent**, **Cline**, **Roo Code**, and custom LLM workflows.

---

## 📂 Repository Structure

```text
├── .agents/
│   ├── README.md
│   └── skills/
│       └── excalidraw/
│           ├── SKILL.md
│           ├── references/
│           │   ├── colors.md
│           │   ├── dark-mode.md
│           │   └── examples.md
│           └── scripts/
│               └── upload.py
├── AGENTS.md
└── README.md
```

---

## 🛠️ Available Skills

### 🎨 `excalidraw`
- **Location**: [`.agents/skills/excalidraw/SKILL.md`](.agents/skills/excalidraw/SKILL.md)
- **Description**: Generates clean, hand-drawn Excalidraw diagrams (`.excalidraw` JSON) for system architectures, workflows, sequence diagrams, and flowcharts.
- **Features**:
  - Valid Excalidraw v2 JSON envelope generation.
  - Proper container bindings for text inside shapes & arrows (no unlinked text).
  - Built-in AES-GCM client-side encryption upload script (`scripts/upload.py`) to generate instant shareable `https://excalidraw.com/#json=...` links without needing an account.
  - Color palettes, dark mode styling, and architecture templates.

---

## 🤖 Compatibility & How to Use

### 1. Claude Code / Codex / Antigravity / Hermes
Point your agent to the skill directory or include `AGENTS.md` in the project root:
- The agent reads `AGENTS.md` and dynamically loads `.agents/skills/<skill-name>/SKILL.md` when relevant.

### 2. Cursor / Windsurf
Add a reference in `.cursorrules` or prompt:
```markdown
Follow the skills in .agents/skills/excalidraw/SKILL.md when generating diagrams.
```

### 3. Standalone Usage
You can copy `.agents/skills/excalidraw/` directly into any project's `.agents/skills/` directory.

---

## 📜 License
MIT License.
