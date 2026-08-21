---
name: braiam-orchestrator
description: "Universal AI Operating System (BRAIAM OS) orchestrator: multi-agent coordination, 4-tier bounded context architecture, strict privacy boundaries, and delegation across Claude Code, Codex, Antigravity, Cursor, and Hermes."
version: 1.0.0
author: BRAIAM / Thiago Nobrega
license: MIT
metadata:
  tags: [braiam-os, ai-operating-system, multi-agent, context-architecture, delegation, orchestration, governance]
---

# BRAIAM OS: Universal Agentic Operating System Orchestrator

The BRAIAM OS Orchestrator turns any AI agent into an autonomous personal and organizational operating system. It decouples the **agent's mental model and governance protocol** from the underlying LLM runtime, preventing platform lock-in and eliminating context bloat.

---

## Core Mental Model

> **The agent does not need everything in its context window.**  
> It needs a reliable map of what exists, where it lives, strict trust boundaries, and how to retrieve only what the current task requires.

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        BRAIAM CONTROL PLANE                            │
│  (Governance, Constitution, 4-Tier Context, Bounded Project Packets)  │
└──────────────────┬─────────────────────────────────┬───────────────────┘
                   │                                 │
         ┌─────────▼─────────┐             ┌─────────▼─────────┐
         │ Light Orchestrator│             │   Heavy Workers   │
         │ (Hermes / Codex)  ├────────────►│(Claude Code / agy)│
         │ Triage & Strategy │  CLI / SSH  │ Build, Refactor & │
         └───────────────────┘ Delegation  │ Heavy Execution   │
                                           └───────────────────┘
```

---

## When to Use

- Building or operating a comprehensive personal or organizational AI operating system.
- Coordinating multiple specialized agents (e.g., triage agent, coding worker, research assistant).
- Separating private personal data, confidential company operations, and reusable product templates.
- Enforcing bounded context loading across large codebases or note vaults (Obsidian / Notion).
- Running hybrid workflows across cloud VPS, local machines, and different CLI tools (Claude Code, Codex, Antigravity).

---

## 1. Information Boundaries (Privacy First)

Always isolate repositories and contexts by security zone:

1. **Personal Private (`*-life-private`)**: Identity, health, relationships, personal finances, daily logs.
2. **Organization Internal (`*-company-private`)**: Company strategy, operational metrics, client data, billing.
3. **Reusable Product / Template (`*-os`, `agent-skills`)**: Generalized workflows, sanitized code, open skills.
4. **Public**: Open-source repositories, public documentation, published packages.

### Rules of Engagement:
- **Never cross-contaminate:** Private logs must never be committed to template or public repositories.
- **One-Way Promotion Flow:** Private experience → Reusable pattern identified → Sanitized & generalized → PR into template repository.

---

## 2. The 4-Tier Bounded Context Architecture

Do not dump entire repositories or chat histories into prompt context. Use the 4 tiers:

| Tier | Name | Scope & Content | Max Size |
|---|---|---|---|
| **Level 0** | **Always-Loaded Core** | `AGENTS.md`, constitution, non-negotiable policies, current top 3 priorities, repo map. | < 2,000 tokens |
| **Level 1** | **Active Project Packet** | `projects/<name>/BRIEF.md` or `SPEC.md` containing immediate objective, acceptance criteria, constraints. | < 5,000 tokens |
| **Level 2** | **Retrieved Evidence** | Specific files, targeted search matches, or API responses needed for the current step. | On-demand |
| **Level 3** | **Immutable Archive** | Raw transcripts, legacy vaults, media files, full database dumps. **Never** load directly into prompt. | Disk / DB only |

---

## 3. Multi-Agent Delegation Protocol

When delegating between orchestrators (e.g., Hermes / Codex) and execution workers (e.g., Claude Code, Antigravity `agy`):

1. **Lightweight Orchestrator:** Maintains high-level strategy, breaks down tasks using Spec-Driven Development, and assigns self-contained tasks.
2. **Heavy Execution Worker:** Runs in an isolated session, executes filesystem edits, builds, and test runs.
3. **Self-Report Verification:** The orchestrator **never trusts** verbal claims ("task finished successfully"). The orchestrator must independently verify file existence, test results, and git diffs before concluding the task.

---

## 4. Anti-Patterns to Avoid

- ❌ **The Monolithic System Prompt:** Stuffing years of memories, all project docs, and code snippets into one massive prompt.
- ❌ **Blind Delegation:** Spawning subagents without concrete deliverables, schemas, or exit criteria.
- ❌ **Fabricated Output:** Reporting that code compiles or tests pass without running them.
- ❌ **Platform Lock-in:** Hardcoding instructions for only one vendor (e.g., only Cursor or only Claude). Use the standard `.agents/` layout so any tool can execute it.
