# Agent Skills (.agents/skills) 🚀

A curated collection of open, portable, and production-grade skills for AI Coding Agents following the open `.agents/` standard.

Designed to work seamlessly across **Anthropic Claude Code**, **OpenAI Codex**, **Google Antigravity (`agy`)**, **Cursor IDE**, **Windsurf**, **Nous Hermes Agent**, **Cline**, and **Roo Code**.

---

## 📂 Repository Structure

```text
├── .agents/
│   ├── README.md
│   └── skills/
│       ├── braiam-orchestrator/
│       ├── spec-driven-development/
│       ├── braiam-hybrid-worker/
│       ├── youtube-channel-outliers/
│       ├── youtube-video-analysis/
│       ├── youtube-viral-shorts-cuts/
│       ├── meeting-viral-shorts-cuts/
│       ├── youtube-innertube-download/
│       ├── youtube-proxy-mine/
│       ├── ai-trend-monitor/
│       ├── twitter-trends/
│       ├── evolution-api-whatsapp/
│       ├── excalidraw/
│       └── langfuse-stats/
├── AGENTS.md
└── README.md
```

---

## 🛠️ Published Skills Catalog

### 🧠 1. Core & Architecture (BRAIAM OS Standard)
* **[`braiam-orchestrator`](.agents/skills/braiam-orchestrator/SKILL.md)**: Universal AI Operating System orchestrator. Implements 4-tier bounded context architecture (Level 0 Core → Level 1 Project Packet → Level 2 Evidence → Level 3 Archive), security boundaries (`*-life-private` vs `*-company-private` vs `*-os`), and multi-agent coordination.
* **[`spec-driven-development`](.agents/skills/spec-driven-development/SKILL.md)**: Spec-Driven Development (SDD) standard for autonomous agents (inspired by GitHub Next & Matt Pocock prompting standards). Spec-first contracts, non-goals, upfront test harnesses, and deterministic verification.
* **[`braiam-hybrid-worker`](.agents/skills/braiam-hybrid-worker/SKILL.md)**: Remote and hybrid worker delegation protocol. Efficiently orchestrates Claude Code, OpenAI Codex, and Google Antigravity across local workstations and cloud VPS while optimizing token quotas.

### 🎥 2. Media & Content Intelligence (YouTube & Video Mining)
* **[`youtube-channel-outliers`](.agents/skills/youtube-channel-outliers/SKILL.md)**: Analyzes YouTube channels, computes statistical baselines, finds outlier videos (views/likes/comments), and extracts the underlying success formula.
* **[`youtube-video-analysis`](.agents/skills/youtube-video-analysis/SKILL.md)**: Deep-dive analysis of individual YouTube videos (metadata, transcripts, comment sentiment, and retention hooks).
* **[`youtube-viral-shorts-cuts`](.agents/skills/youtube-viral-shorts-cuts/SKILL.md)**: Identifies high-retention Short / Reel cut opportunities from long-form YouTube videos with timestamps, hooks, 9:16 framing schemas, and caption guidelines.
* **[`meeting-viral-shorts-cuts`](.agents/skills/meeting-viral-shorts-cuts/SKILL.md)**: Extracts viral Short / Reel cut opportunities from meeting recordings, podcasts, and webinars.
* **[`youtube-innertube-download`](.agents/skills/youtube-innertube-download/SKILL.md)**: High-speed metadata and transcript extraction using YouTube's InnerTube API.
* **[`youtube-proxy-mine`](.agents/skills/youtube-proxy-mine/SKILL.md)**: Multi-proxy rotation and mining for high-volume YouTube data extraction.

### 📡 3. Trends & Social Intelligence
* **[`ai-trend-monitor`](.agents/skills/ai-trend-monitor/SKILL.md)**: Stateful deduplicating AI news curator monitoring TechCrunch, Hacker News, and Google News with zero redundant alerts.
* **[`twitter-trends`](.agents/skills/twitter-trends/SKILL.md)**: Scrapes Brazil & Worldwide trending topics via trends24 without login requirements or API keys.
* **[`evolution-api-whatsapp`](.agents/skills/evolution-api-whatsapp/SKILL.md)**: Diagnostic workflows, PostgreSQL database schema inspection, and instance management for self-hosted Evolution API WhatsApp stacks.

### 🎨 4. Developer Tools & Observability
* **[`excalidraw`](.agents/skills/excalidraw/SKILL.md)**: Generates valid hand-drawn Excalidraw diagrams (`.excalidraw` JSON) for system architectures, workflows, and flowcharts with client-side encrypted upload script (`scripts/upload.py`).
* **[`langfuse-stats`](.agents/skills/langfuse-stats/SKILL.md)**: Setup, troubleshoot, and query local Langfuse observability metrics, token costs, and latency.

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
