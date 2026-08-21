---
name: codegraph
description: "Semantic Code Graph Intelligence (Tree-Sitter parsed AST graph): query symbol definitions, call hierarchies, dynamic-dispatch hops, dependencies, and blast-radius across codebases without grepping."
version: 1.0.0
author: Colby McHenry / Hermes Agent
license: MIT
metadata:
  tags: [codegraph, code-intelligence, tree-sitter, ast, graph, search, refactoring, navigation]
---

# CodeGraph: Semantic Code Intelligence

CodeGraph provides structural, tree-sitter parsed semantic code intelligence for AI coding agents. It indexes every symbol, definition, import, export, and call-path across the codebase, enabling sub-millisecond AST queries that replace slow `grep`/`find` and repeated file reads.

---

## When to Use

- Answering structural questions: *"How does X work?", "What calls function Y?", "Where is interface Z implemented?", "What is the blast radius of changing module A?"*
- Tracing dynamic dispatch hops (callbacks, React state/re-renders, event listeners, JSX children) that standard `grep` cannot follow.
- Surveying unfamiliar codebases or large multi-package repositories without blowing up the context window.
- Extracting verbatim, line-numbered source code for specific symbols and their immediate call chains in a single round-trip.

### When NOT to Use
- Searching plain text in non-code assets (markdown docs, pure JSON data, unstructured assets — use `search_files` or `graphify`).
- Single-file edits where the exact location is already known.

---

## Core Principles

1. **Query Before Grepping:** Run `codegraph_explore` or `codegraph query` before starting a multi-turn grep + read loop.
2. **Trust the AST Graph:** Results come from an exact AST parse. Do not waste context re-verifying every symbol with grep.
3. **Single Round-Trip Context:** One query retrieves the target symbol's definition, callers, callees, and dependencies grouped by file.

---

## CLI & MCP Usage

### 1. Installation & Initialization
```bash
# Global install via npm
npm install -g @colbymchenry/codegraph

# Initialize index in the current repository
codegraph init
```

### 2. Querying CodeGraph
```bash
# Natural language structural query
codegraph explore "How does authentication middleware validate JWT tokens?"

# Query specific symbol call paths and blast radius
codegraph explore "AuthService.validateSession"

# Check index status
codegraph status
```

### 3. MCP Server Integration
When configured as an MCP server, agents can directly call the `codegraph_explore` tool:
```json
{
  "query": "find all implementations of Repository interface and their database calls"
}
```

---

## Verification & Output Shape

CodeGraph returns:
- **Symbol Definitions**: Verbatim source with line numbers.
- **Call Chains**: Inbound and outbound function calls.
- **Blast Radius**: Summary of dependent files and consumers that could break upon modification.
