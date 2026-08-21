---
name: youtube-channel-outliers
description: >-
  Analisa canais do YouTube: lista vídeos com métricas, calcula baseline
  estatística e identifica outliers de views/likes/comentários/engajamento.
  Depois disseca os principais outliers (transcript, metadados, comentários
  top por likes) e extrai a fórmula do sucesso. Use when the user asks to
  analyze a channel, list channel videos, find outlier videos, compare
  channel performance, or discover what made top videos work.
---

# YouTube Channel Outliers

**Não reinventar.** Inventário + outliers (+ síntese Gemini) via `youtube/main.py outliers`.

Para **um** vídeo genérico → `youtube-video-analysis`. Para Shorts → `youtube-viral-shorts-cuts`.

## Quando aplicar

- Listar vídeos do canal com métricas
- Achar outliers / hits / flops / fórmula do sucesso
- Comparar engajamento relativo vs alcance

## Pré-requisitos

```powershell
cd youtube
pip install -r requirements.txt
# youtube/.env → GEMINI_API_KEY=...  (omitir síntese: --no-gemini)
```

## Workflow (obrigatório)

```
Progresso:
- [ ] 1. Declarar: «Usando youtube-channel-outliers → youtube/main.py outliers»
- [ ] 2. Rodar o comando com a URL do canal
- [ ] 3. Ler artefatos (JSON/relatório) e entregar síntese ao usuário
- [ ] 4. Se pedirem dissecção extra de 1 hit: youtube-video-analysis / main.py analyze
```

### Comando canônico

Working directory: **`youtube/`**.

```powershell
python main.py outliers "https://www.youtube.com/@canal" -o out
python main.py outliers "CHANNEL_URL" -o out --limit 50
python main.py outliers "CHANNEL_URL" -o out --no-gemini
python main.py outliers "CHANNEL_URL" -o out --model gemini-3.5-flash-lite
```

Equivalente: `python -m modules.outliers ...`

### Métricas (o script calcula; o agent interpreta)

| Métrica | Uso |
|---------|-----|
| `view_count` | alcance |
| `like_count` / `comment_count` | afinidade / conversa |
| `like_rate`, `comment_rate`, `engagement` | qualidade relativa |
| `views_per_min` | eficiência de duração |

Outlier típico: > Q3+1.5×IQR ou \|z\| ≥ 2 (detalhe: [stats.md](stats.md)).
Classes: volume, engajamento alto, engajamento baixo (SEO frio), formato extremo.

Relatório humano de referência: [report-template.md](report-template.md).

## Regras

- **Sempre** `main.py outliers` — não montar `yt-dlp --flat-playlist` + stats na mão salvo falha do script.
- Não baixar mp4s do canal inteiro salvo pedido.
- Não inventar likes/comentários; citar só o que veio nos artefatos.
- Members-only: listar se possível; métricas podem faltar.
- Não expor secrets.

## Limites

- Comentários / flat playlist são best-effort (anti-bot YouTube).
- `--limit` controla profundidade; canais enormes não precisam de scrape total sem o usuário pedir.
