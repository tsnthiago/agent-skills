---
name: spec-driven-development
description: "Spec-Driven Development (SDD) for AI agents: author executable specs, establish interface contracts, enforce test-first verification before code, and avoid context bloat. Inspired by GitHub Next & Matt Pocock prompting standards."
version: 1.0.0
author: BRAIAM / Thiago Nobrega
license: MIT
metadata:
  tags: [spec-driven-development, sdd, architecture, testing, tdd, quality, multi-agent]
---

# Spec-Driven Development (SDD)

Spec-Driven Development is an engineering discipline for autonomous AI agents: **never write implementation code without an explicit, verified specification contract.**

LLMs fail at complex coding tasks when they improvise architecture mid-implementation. SDD anchors agent behavior against a concrete contract (`SPEC.md` or `RFC.md`), establishes clear schemas, defines test harnesses upfront, and validates deliverables deterministically.

---

## When to Use

- Starting any new feature, service, tool, or refactor spanning 2+ files.
- Orchestrating tasks between multiple AI agents (e.g., Planner -> Coder -> Reviewer).
- Building public templates or multi-tenant architectures where API contracts must be rock solid.
- When requirements have edge cases, state machines, or complex data transformations.

### When NOT to Use
- Single-line typo fixes or trivial documentation updates.
- Quick disposable spikes (use throwaway spike prototypes instead).

---

## Core Principles (Do This, Not That)

| Principle | ❌ Anti-Pattern (Improvisation) | ✅ SDD Pattern (Spec-First) |
|---|---|---|
| **Contract** | Writing code directly and figuring out inputs/outputs along the way. | Writing the JSON/Zod/Pydantic schema and function signatures in `SPEC.md` first. |
| **Scope** | Scope creeping during implementation. | Explicit "Non-Goals" section in the spec that blocks distractions. |
| **Testing** | Writing tests after implementation (or skipping tests entirely). | Specifying exact test cases and assertions before writing production code. |
| **Context** | Dumping the entire repository history into the agent prompt. | Bounded project packets: Agent reads only `SPEC.md` + direct dependencies. |
| **Verification** | Claiming "it should work now" without execution. | Running real test runners and attaching verbatim execution output. |

---

## The 4-Phase SDD Workflow

```text
[ Phase 1: SPECIFY ] ──> [ Phase 2: CONTRACT & HARNESS ] ──> [ Phase 3: IMPLEMENT ] ──> [ Phase 4: VERIFY ]
   Problem, Scope,         Types, Schemas, Test Cases          Red-Green-Refactor           Deterministic Proof
   Non-Goals & Edge Cases   (Failing Tests)                     Minimal working code        No fabricated claims
```

### Phase 1: Author the Specification (`SPEC.md`)
Create a dedicated specification document in the project or feature branch:

```markdown
# Specification: [Feature Name]

## 1. Problem Statement & Motivation
- What exact user problem or architectural gap does this solve?

## 2. Goals & Non-Goals
- ✅ **Goals**: Explicit, measurable outcomes.
- ❌ **Non-Goals**: What is deliberately OUT of scope for this iteration.

## 3. Interface & Data Contracts
- Data models (TypeScript interfaces, Pydantic schemas, or JSON Schema).
- API routes / CLI arguments / function signatures.

## 4. State & Edge Cases
- State transitions.
- Failure modes, timeouts, retry policies, and error responses.

## 5. Test Matrix & Acceptance Criteria
- Unit test scenarios (Happy path, boundary values, error conditions).
- Integration / end-to-end verification steps.
```

### Phase 2: Build the Test Harness (Red)
1. Write the test suite matching the test matrix in `SPEC.md`.
2. Run the test suite to confirm it **fails for the expected reason** (Contract defined, no implementation yet).

### Phase 3: Minimal Implementation (Green)
1. Implement the minimal code required to satisfy the specification.
2. Maintain strict adherence to the schema contracts in `SPEC.md`. Do not add unapproved features or arbitrary dependencies.

### Phase 4: Deterministic Verification & Refactor
1. Execute the full test runner (pytest, vitest, cargo test, etc.).
2. Confirm all tests pass.
3. Review against the "Non-Goals" section: ensure zero scope creep.

---

## Verification Checklist

Before marking an SDD task complete, the agent must verify:
- [ ] `SPEC.md` exists and includes Problem, Non-Goals, Schemas, and Test Plan.
- [ ] Interface types/schemas are strictly typed (no loose `any` or untyped dicts).
- [ ] Edge cases (empty inputs, network timeouts, invalid payloads) are covered by tests.
- [ ] Test command was executed with exit code 0 and verbatim output captured.
- [ ] No extraneous files or unauthorized dependencies were introduced.
