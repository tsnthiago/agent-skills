---
name: braiam-hybrid-worker
description: "Orchestration protocol for hybrid and remote AI workers (Claude Code, OpenAI Codex, Antigravity agy): quota management, SSH execution, deterministic verification, and non-interactive workflows."
version: 1.0.0
author: BRAIAM / Thiago Nobrega
license: MIT
metadata:
  tags: [braiam-os, workers, claude-code, codex, antigravity, hybrid, ssh, automation]
---

# BRAIAM: Hybrid Agent & Worker Orchestration

Protocol for orchestrating remote and local coding agents (such as **Anthropic Claude Code**, **OpenAI Codex CLI**, and **Google Antigravity `agy`**) across heterogeneous machines (e.g., VPS and workstation) to optimize token quotas, reduce latency, and prevent execution stalls.

---

## When to Use

- Delegating heavy code refactoring, test suite execution, or builds from a primary orchestrator to a dedicated CLI worker.
- Running tasks on a remote developer machine (e.g., Windows workstation via SSH/Tailscale) while controlling from a central agent (VPS).
- Preserving primary model quota (e.g. Codex / Claude limits) by routing specialized tasks to the most cost-effective CLI worker.
- Automating batch tasks without interactive prompt blocking.

---

## Core Operational Directives

### 1. Non-Interactive CLI Invocations
Always run worker CLI tools with flags that suppress interactive confirmation dialogs to prevent hanging:
- **Claude Code**: `claude -p "<prompt>" --non-interactive` (or use danger/auto-approve flags when authorized).
- **Codex CLI**: `codex exec "<task>"`
- **Antigravity**: `agy --prompt "<task>"`

### 2. Task Packet Structure
When delegating work to a hybrid worker, provide a self-contained task packet:
1. **Context & Constraints**: Exact files allowed to touch, framework versions, language standards.
2. **Deliverable Contract**: Target branch, file paths, and test command.
3. **Execution Command**: Command to execute and verify.

Example delegation payload:
```json
{
  "task_id": "auth-jwt-refresh",
  "scope_paths": ["src/auth/", "tests/auth/"],
  "goal": "Implement sliding session JWT refresh according to SPEC.md",
  "verification_command": "npm test tests/auth/jwt.test.ts"
}
```

### 3. Quota & Cost Protection
- **Task Batching:** Do not dispatch 10 micro-tasks if they can be combined into one coherent, bounded task.
- **Context Pruning:** Exclude build artifacts (`node_modules/`, `target/`, `dist/`, `.venv/`) from prompts.
- **Fail-Fast Policy:** If a worker fails 2 consecutive iterations on the same error, abort and surface the blocker to the orchestrator rather than burning quota in an infinite loop.

---

## Verification & Hand-off

After a worker finishes:
1. Orchestrator inspects `git status` and `git diff`.
2. Orchestrator executes the test harness independently.
3. Orchestrator reviews that no unauthorized external files were modified.
