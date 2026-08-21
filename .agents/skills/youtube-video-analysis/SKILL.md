---
name: youtube-video-analysis
description: >-
  Análise completa e detalhada de vídeos (YouTube e similares) com base no
  transcript completo da legenda auto-gerada (qualquer idioma), metadados e
  comentários, produzindo uma análise holística. Use when the user sends a
  video URL to analyze, asks for análise de vídeo, video breakdown, transcript
  analysis, comment analysis, or holistic review of a YouTube video.
---

# YouTube Video Analysis

**Não reinventar.** Coleta + síntese via `youtube/main.py analyze` (Gemini + transcript/meta/comentários do pipeline).

## Quando aplicar

- URL de YouTube / pedido de análise completa, breakdown, insights, comentários + transcript
- Não usar para inventário de canal inteiro → `youtube-channel-outliers`
- Não usar para Shorts/cortes → `youtube-viral-shorts-cuts`

## Pré-requisitos

```powershell
cd youtube
pip install -r requirements.txt
# youtube/.env → GEMINI_API_KEY=...
```

## Workflow (obrigatório)

```
Progresso:
- [ ] 1. Declarar: «Usando youtube-video-analysis → youtube/main.py analyze»
- [ ] 2. Rodar o comando (não yt-dlp manual / agent-reach para a coleta principal)
- [ ] 3. Ler o artefato gerado + entregar relatório no idioma do pedido
- [ ] 4. Se o user pedir só o texto: resumir o output do script sem reinventar coleta
```

### Comando canônico

Working directory: **`youtube/`**.

```powershell
python main.py analyze "URL_OR_ID" -o out
python main.py analyze "URL" -o out --skip-comments
python main.py analyze "URL" -o out --model gemini-3.5-flash-lite
```

Equivalente: `python -m modules.analyze ...`

O módulo baixa/usa transcript ASR (InnerTube), metadados e (salvo `--skip-comments`) comentários top; sintetiza com Gemini.

### Saída

Artefatos sob `out/` (pasta do vídeo / analysis) — seguir o path impresso no JSON do comando. Template editorial de referência: [analysis-template.md](analysis-template.md).

## Regras

- **Sempre** `main.py analyze` primeiro. Só cair para yt-dlp/agent-reach se o script falhar de forma bloqueante e o usuário aceitar fallback.
- Não inventar trechos fora do transcript; citar timestamps quando o artefato tiver.
- Idioma do relatório = idioma do pedido do usuário (default PT-BR se o pedido for em PT).
- Não baixar o mp4 salvo pedido explícito de download (usar skill de download / `main.py download`).
- Não expor cookies/tokens / `GEMINI_API_KEY`.

## Limites

- Comentários são amostragem best-effort, não 100% do YouTube.
- ASR pode errar; assinalar incerteza quando o sentido depender disso.
