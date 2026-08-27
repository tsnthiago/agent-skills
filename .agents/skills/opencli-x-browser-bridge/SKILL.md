---
name: opencli-x-browser-bridge
description: Use when connecting, reading, or approval-gated posting to X through OpenCLI and a user-controlled Chrome Browser Bridge session.
version: 1.0.0
author: Thiago Nobrega / BRAIAM
license: MIT
metadata:
  tags: [x, twitter, opencli, chrome, browser-bridge, social-media, privacy]
  related_skills: [agent-reach]
---

# OpenCLI X Browser Bridge

## Overview

Use OpenCLI with the Browser Bridge when an operator wants an agent to interact with an X account through a Chrome session that is already authenticated on a computer they control. The browser remains the authentication boundary: do not export cookies, tokens, browser profiles, or credentials to an agent, VPS, repository, or chat.

This skill covers validation, narrowly scoped reading, approval-gated writing and recovery from browser-extension attachment failures. It does not bypass X controls, automate abuse, or authorize access to third-party accounts.

## When to Use

- Connecting an agent to an operator-owned X account without the official X API.
- Diagnosing OpenCLI Browser Bridge, browser profile selection, or X adapter attachment.
- Reading an explicitly requested X profile, post, notification, timeline, or search result through the operator's active Chrome session.
- Publishing, replying, quoting, liking, reposting, following, or deleting only after explicit approval of the exact action.

Do not use for:

- password, cookie, `auth_token`, `ct0`, token, profile or header extraction;
- mass scraping, spam, engagement manipulation, bulk following, unsolicited DMs, or evasion of platform restrictions;
- actions against an account the operator does not own or control;
- official X API workflows (use the dedicated API tooling instead).

## Security Model

```text
Agent/orchestrator ── private authenticated channel ──> operator-controlled computer
                                                          │
                                                          ├─ OpenCLI + local daemon
                                                          ├─ OpenCLI Browser Bridge
                                                          └─ Chrome authenticated by operator
                                                                    │
                                                                    ▼
                                                                    X
```

1. The session stays in Chrome. Never move it to a server.
2. Validate identity before reading or writing.
3. Treat every write action as externally consequential.
4. Verify the external result by reading it back.
5. Keep audit records minimal: intent, approval, action type, timestamp and resulting ID/URL — never session material.

## Prerequisites

On the same operating-system user that runs Chrome:

```bash
npm install -g @jackwener/opencli
opencli doctor
```

The operator must independently:

- have Chrome open with a valid X session;
- install and enable the official OpenCLI Browser Bridge;
- keep a private, authenticated channel available if the orchestrator runs remotely.

Do not ask them to paste a cookie or secret into a prompt.

## Procedure

### 1. Diagnose without changing state

```bash
opencli doctor
opencli profile list
```

Expected: daemon available, extension connected and one or more browser profiles listed. Do not assume that the default profile is the connected profile.

### 2. Bind the operation to an explicit profile

Choose the connected profile reported by `profile list`, then validate identity:

```bash
opencli --profile <connected-profile-id> twitter whoami -f json
```

Stop if the returned account is not the intended operator account. Do not perform reads or writes against an ambiguous session.

### 3. Perform delimited reads

Use the explicit profile every time:

```bash
opencli --profile <connected-profile-id> twitter profile <handle> -f json
opencli --profile <connected-profile-id> twitter search 'specific query' -f json
opencli --profile <connected-profile-id> twitter timeline -f json
```

Collect only what the user requested. A working session is not blanket authorization for collection or monitoring.

### 4. Prepare and approve writes

Before any write, state and obtain approval for:

- action type;
- final text where applicable;
- target post/account where applicable;
- intended account, as confirmed by `whoami`.

A user request that includes the exact final post text and asks to publish it counts as approval for that one post. Do not reuse approval for later posts.

### 5. Execute one approved action

Example for an approved post:

```bash
opencli --profile <connected-profile-id> twitter post 'APPROVED TEXT' -f json
```

For replies, quotes, likes, reposts, follows or deletes, first read the target and confirm its ID/URL corresponds to the approved target.

### 6. Verify externally

Parse the returned post ID or URL, then read the exact created/changed object back through OpenCLI. Report success only when this verification matches the approved action.

## Remote-Orchestrator Pattern

If the agent runs on a server but Chrome is on a desktop:

1. Keep the browser and OpenCLI on the desktop.
2. Use a private authenticated channel to request a desktop-side execution.
3. Ensure the command executes in the interactive OS-user context owning Chrome; an SSH/service user may not see the same bridge.
4. Return only exit status and sanitized structured result.
5. Delete transient files once verified.

Never proxy a browser debugging endpoint or copy a Chrome user-data directory to the server merely to make this easier.

## Troubleshooting

### `Cannot access a chrome-extension:// URL of different extension`

This generally means OpenCLI cannot attach to the desired browser context. It occurs before X authentication and therefore does not establish that the X login failed.

Recovery:

1. Close Chrome completely.
2. Temporarily disable other automation, bridge and DevTools extensions.
3. Start Chrome with the intended user profile and open X while authenticated.
4. Run `opencli doctor` and `opencli profile list` under that same interactive OS user.
5. Retry with `--profile <connected-profile-id>`, not the default profile.
6. Re-enable other extensions one at a time only after `twitter whoami` works.

### `doctor` is healthy but X calls fail

- Confirm the command is executing as the OS user who owns Chrome.
- Confirm Chrome is open, the extension is enabled and an X tab exists.
- Select the explicitly connected OpenCLI profile.
- Update OpenCLI only in a controlled window; repeat `doctor` → `profile list` → `whoami` after any update.

### Identity is unexpected

Stop. Close the browser session, have the operator select the intended Chrome profile/account, and repeat identity validation. Never “correct” account selection by guessing.

## Common Pitfalls

1. **Using the default profile.** It may not be the profile bound to the Browser Bridge; always discover and pass `--profile`.
2. **Running under an SSH/service user.** The executable may exist, but the interactive browser session belongs to another OS user.
3. **Treating a green `doctor` as authorization.** It proves bridge connectivity, not correct X identity or permission to write.
4. **Leaking traces.** Browser traces can contain sensitive URLs or state; inspect locally and publish only sanitized diagnoses.
5. **Turning a convenience integration into a bot farm.** Keep actions consented, rate-aware and within platform rules.

## Verification Checklist

- [ ] Chrome and OpenCLI run under the intended interactive OS user.
- [ ] Browser Bridge is connected and `opencli doctor` is healthy.
- [ ] An explicit OpenCLI profile is selected.
- [ ] `twitter whoami` matches the intended account.
- [ ] Reads are limited to the requested scope.
- [ ] Every write has a single, explicit approval.
- [ ] The resulting object was read back and matches the requested action.
- [ ] No secret or browser-session material was copied to logs, Git or chat.
