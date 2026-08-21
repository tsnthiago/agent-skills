---
name: langfuse-stats
description: Setup, troubleshoot, and query local Langfuse observability metrics.
---
# Langfuse Observability

This skill covers setting up the native Hermes Langfuse plugin, troubleshooting silent failures, and querying local stats.

## Setup & Troubleshooting Pitfalls
- **Silent Failure due to missing SDK:** The `observability/langfuse` plugin will fail silently if the `langfuse` Python package is not installed in the agent's virtual environment. 
  *Fix:* `/usr/local/lib/hermes-agent/venv/bin/pip install langfuse`
- **Configuration:** Keys must be set in `~/.hermes/.env`:
  ```ini
  HERMES_LANGFUSE_PUBLIC_KEY="..."
  HERMES_LANGFUSE_SECRET_KEY="..."
  HERMES_LANGFUSE_BASE_URL="http://localhost:3000"
  ```
- **Restart Required:** After installing the pip package or changing `.env`, restart the gateway (`pkill -f "hermes_cli.main gateway run"` or `systemctl restart hermes-gateway`).
- **Port Conflicts:** If self-hosting via Docker Compose, port `3000` is often taken by the Hermes WhatsApp bridge. Map to `3031:3000` in `docker-compose.yml` and set `NEXTAUTH_URL=http://localhost:3031`.

## Querying Stats
Run the included script to get a summary of costs, token usage, and latency from a local Langfuse instance:
`python3 ~/.hermes/skills/langfuse-stats/scripts/langfuse_summary.py`
