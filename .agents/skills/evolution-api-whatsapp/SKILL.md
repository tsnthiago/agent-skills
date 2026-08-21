---
name: evolution-api-whatsapp
description: "Inspect, manage, and troubleshoot self-hosted Evolution API WhatsApp instances, database schemas (PostgreSQL), Redis caches, and webhook delivery."
version: 1.0.1
author: Thiago Nobrega / Hermes Agent
license: MIT
metadata:
  tags: [whatsapp, evolution-api, docker, postgres, baileys, social-media, webhooks]
---

# Evolution API WhatsApp Operations

Manage and troubleshoot self-hosted **Evolution API** instances running in Docker, backed by PostgreSQL and Redis.

---

## When to Use

- Inspecting Evolution API instance connectivity status, QR codes, or active phone numbers.
- Listing connected WhatsApp instances, groups, and message telemetry.
- Querying the backing PostgreSQL database safely for message logs, instance states, or contact maps.
- Debugging webhook delivery failures and Redis pub/sub events.

---

## Safety & Privacy Defaults

1. **Metadata First:** Always prioritize querying instance states, contact counts, and delivery statuses over dumping private message content.
2. **Secret Redaction:** Automatically redact API keys, global tokens, and private session credentials before printing logs.
3. **Read-Only Operations:** Use read-only SQL queries (`SELECT`) unless a state migration or cleanup is explicitly requested.

---

## Essential Diagnostics

### 1. Check Service Health
```bash
docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}' | grep -E "evolution|postgres|redis"
```

### 2. Fetch Active Instances via REST API
```bash
curl -sS -H "apikey: YOUR_API_KEY" http://127.0.0.1:8080/instance/fetchInstances | jq .
```

### 3. Inspect Instance State in PostgreSQL
```bash
docker exec -i evolution_postgres psql -U evolution_user -d evolution -c 'SELECT "name", "connectionStatus", "ownerJid", "updatedAt" FROM "Instance";'
```

### 4. Check Webhook Delivery Logs
```bash
docker logs --tail 100 evolution_api | grep -i "webhook"
```
