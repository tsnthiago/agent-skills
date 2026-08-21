---
name: youtube-proxy-mine
description: >-
  Minera proxies HTTP/HTTPS livres validados contra YouTube (InnerTube player),
  com watch contínuo, histórico de commits dos repos e defaults leves (meta-only).
  Use when the user asks to mine proxies, find free proxies, proxy list, valid.txt,
  minerar proxies, buscar proxies, proxy YouTube, or run youtube/mine.ps1.
---

# YouTube Proxy Mine

**Não reinventar.** Usar o pipeline em `youtube/` (repo Braiam).

| Peça | Caminho |
|------|---------|
| Miner (Python) | `youtube/modules/proxy_mine.py` |
| Start | `youtube/mine.ps1` |
| Stop + cleanup | `youtube/stop_mine.ps1` **ou** esta skill `scripts/cleanup.ps1` |
| Bank | `youtube/out/proxies/valid.txt` |

## Quando usar

- Pedido de minerar / achar / validar proxies livres para YouTube
- Encher `valid.txt` / `valid_meta.txt`
- Watch contínuo observando listas públicas (GitHub) + commits antigos quando ocioso

## Hard limits (NÃO violar)

Aprendizado de runs reais: `200 workers + deep/yt-dlp` derrete CPU/RAM e `full+=0`.

| Parâmetro | Default seguro | Proibido sem pedido explícito |
|-----------|----------------|-------------------------------|
| Mode | **meta-only** | `--full` / deep yt-dlp |
| Workers | **64** | \> 96 |
| Deep workers | 0 (meta-only) | \> 2 |
| Timeout meta | 10–20s | \> 30s com muitos workers |
| Clear invalid | TTL 12h | limpar **todo** round |
| Instâncias | **1** | 2+ em paralelo |

- Preferir `http,https` (socks rende pouco e gasta tempo).
- Nunca subir segunda instância se já houver `proxy_mine` rodando.
- Deep/yt-dlp só se o usuário pedir HQ explicitamente (`-Full`).

## Protocolo obrigatório de cleanup

**Sempre** ao parar, trocar parâmetros, ou antes de `-Fresh`:

```powershell
cd youtube
powershell -ExecutionPolicy Bypass -File .\stop_mine.ps1
# cleanup completo (árvore + yt-dlp + temp):
powershell -ExecutionPolicy Bypass -File ..\.agents\skills\youtube-proxy-mine\scripts\cleanup.ps1
```

O agent **DEVE** rodar o cleanup quando:

1. O usuário pedir para parar
2. A sessão/comando for abortado
3. For reiniciar com outros parâmetros
4. O PC estiver lento e houver suspeita de órfãos

Verificar depois:

```powershell
Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -match 'proxy_mine|yt-dlp-sabr' }
# deve retornar vazio
```

## Como rodar (agressivo mas seguro)

```powershell
cd youtube
# 1) cleanup primeiro
powershell -ExecutionPolicy Bypass -File ..\.agents\skills\youtube-proxy-mine\scripts\cleanup.ps1

# 2) uma instância só — do zero
powershell -ExecutionPolicy Bypass -File .\mine.ps1 -Fresh -Workers 64 -Timeout 20

# 3) ou continuar bank existente (sem -Fresh)
powershell -ExecutionPolicy Bypass -File .\mine.ps1 -Workers 64 -Timeout 20
```

Watch padrão: live → mantém invalid → idle busca commits antigos dos repos → refetch.

### GitHub rate limit (history)

Idle history usa `api.github.com` (lista de commits). Sem token = **60 req/h** e o miner ficava spamando WARN + idle vazio.

Agora: cache de SHAs (~45 min), cooldown ao bater 403/429, e `commits_per_source` de verdade (não corta no 3º commit global).

```powershell
# recomendado — PAT classic com repo público (só leitura)
$env:GITHUB_TOKEN = "ghp_..."   # ou GH_TOKEN
powershell -ExecutionPolicy Bypass -File .\mine.ps1 -Workers 64 -Timeout 20
```

### Parar

```powershell
cd youtube
powershell -ExecutionPolicy Bypass -File ..\.agents\skills\youtube-proxy-mine\scripts\cleanup.ps1
```

## Saídas

| Arquivo | Conteúdo |
|---------|----------|
| `out/proxies/valid.txt` | Proxies META+ (player YouTube OK) — **bank principal** |
| `out/proxies/valid_meta.txt` | Mesmo conjunto meta |
| `out/proxies/invalid.txt` | Mortos (não retestar até TTL) |
| `out/proxies/history_shas.txt` | Commits já escavados |
| `out/proxies/results.jsonl` | Log detalhado (pode crescer; não apagar no stop) |

## Checklist do agent

1. [ ] Rodar cleanup se houver miner/yt-dlp residual
2. [ ] Confirmar **0** instâncias antes de start
3. [ ] Subir **1** `mine.ps1` meta-only ≤64 workers
4. [ ] Monitorar `valid.txt` crescendo; se PC ficar lento → cleanup imediato
5. [ ] Ao terminar pedido do usuário → cleanup obrigatório

## Anti-padrões

- ❌ `--full` / deep por default
- ❌ Workers 200+
- ❌ Várias shells `mine.ps1` ao mesmo tempo
- ❌ `-ClearInvalidEachRound` (retesta milhares de mortos)
- ❌ Matar só o PID pai e deixar yt-dlp/node órfãos
- ❌ Reimplementar o miner fora de `youtube/modules/proxy_mine.py`
