---
name: youtube-innertube-download
description: >-
  Downloads YouTube videos in high quality (SABR yt-dlp primary) and full
  auto-generated transcripts via InnerTube. Use when the user asks to download
  YouTube videos, obtain HQ mp4, fetch auto captions / transcripts regardless of
  language, or when stable yt-dlp / InnerTube HTTPS only returns 360p under SABR.
---

# YouTube HQ Download + Transcript

**Não reinventar.** Rodar o pipeline determinístico em `youtube/` (repo Braiam).

| Asset | Implementação |
|-------|----------------|
| Vídeo HQ | `modules/download.py` → yt-dlp SABR (`android_vr` + `tv`) |
| Transcript ASR | InnerTube `player` → timedtext `json3` |

## Quando usar

- Pedido explícito de download de vídeo YouTube
- Precisa de qualidade > 360p e/ou transcript ASR
- Outras skills YouTube pedem download como pré-requisito

Não substitui `youtube-video-analysis` / `youtube-channel-outliers` / `youtube-viral-shorts-cuts` (essas orquestram etapas próprias via o mesmo `youtube/`).

## Pré-requisitos

```powershell
cd youtube
pip install -r requirements.txt
# GEMINI não é necessário para download
# ffmpeg .exe real no PATH (não só ffmpeg.cmd quebrado)
# yt-dlp SABR:
#   %USERPROFILE%\.agent-reach\bin\yt-dlp-sabr.exe
```

Instalar SABR se faltar:

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.agent-reach\bin" | Out-Null
Invoke-WebRequest `
  "https://github.com/bashonly/yt-dlp/releases/download/sabr/yt-dlp.exe" `
  -OutFile "$env:USERPROFILE\.agent-reach\bin\yt-dlp-sabr.exe"
```

## Workflow (obrigatório)

```
Progresso:
- [ ] 1. Declarar: «Usando youtube-innertube-download → youtube/main.py download»
- [ ] 2. cd para a pasta youtube/ do workspace (Braiam)
- [ ] 3. Rodar main.py download (não scripts antigos da skill)
- [ ] 4. Confirmar height (meta/ffprobe) e transcript ASR
```

### Comandos canônicos

Working directory: **`youtube/`** (ou path absoluto do repo).

```powershell
python main.py download "URL_OR_ID" -o out --max-height 1080
python main.py download "URL" -o out --transcript-only --lang pt
python main.py download "URL" -o out --video-only --max-height 1080
python main.py download "URL" -o out --proxy "http://host:port"
```

Equivalente módulo:

```powershell
python -m modules.download "URL" -o out --max-height 1080
```

### Saídas (layout canônico)

`out/videos/{id}_{slug}/`

| Arquivo | Conteúdo |
|---------|----------|
| `{id}.1080p.mp4` | vídeo+áudio merge |
| `transcript.json` / `.txt` / `.vtt` | ASR com timestamps |
| `meta.json` | título, paths, proxy usado |

## Regras

- **Sempre** chamar `youtube/main.py` (ou `python -m modules.download`). Não reimplementar InnerTube/yt-dlp na mão; não usar `scripts/download.py` antigo da skill.
- Proxy free costuma bastar para meta/transcript; SABR HQ via free proxy muitas vezes trava — preferir IP direto ou proxy residencial para o mp4.
- Se height ≈ 360 / `progressive`: atualizar `yt-dlp-sabr.exe` e repetir; não fingir HQ.
- Preferir pasta do projeto (`youtube/out` ou `-o` do cliente), não tmp genérico.
- Não expor cookies/tokens.

## Limites

- Members-only / age-gate / bot wall podem exigir cookies.
- Client `tv` pode cair em DRM experiment — o script já prioriza `android_vr`.
- Detalhe técnico legado: [reference.md](reference.md) (só contexto; a execução é o pipeline).
