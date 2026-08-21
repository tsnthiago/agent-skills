# YouTube HQ download — referência

## Ordem de tentativa (script)

1. **SABR yt-dlp** (`download_video_sabr`) — preferido
2. **InnerTube adaptive** HTTPS Range (`download_video_innertube`)
3. **Progressive** itag 18 (~360p) — último recurso + `fallback_reason`

## SABR yt-dlp (vídeo HQ)

| Item | Valor |
|------|--------|
| Binary | `%USERPROFILE%\.agent-reach\bin\yt-dlp-sabr.exe` |
| Release | https://github.com/bashonly/yt-dlp/releases/tag/sabr |
| Upstream PR | https://github.com/yt-dlp/yt-dlp/pull/13515 |
| Issue contexto | https://github.com/yt-dlp/yt-dlp/issues/12482 |
| Clients | `tv,android_vr` |
| Extractor args | `youtube:formats=duplicate;player-client=tv,android_vr` |
| Format | `bv*[height<=H][protocol=sabr][vcodec^=avc1]+ba[protocol=sabr]/…` |
| JS runtime | Node (`--js-runtimes node`) |

Sem o build SABR, o CDN costuma listar 1080p adaptive mas **bloquear Range** alto → só 360p.

Instalação rápida:

```powershell
Invoke-WebRequest `
  "https://github.com/bashonly/yt-dlp/releases/download/sabr/yt-dlp.exe" `
  -OutFile "$env:USERPROFILE\.agent-reach\bin\yt-dlp-sabr.exe"
```

Pip (venv isolado):

```bash
pip install "yt-dlp[default] @ git+https://github.com/coletdjnz/yt-dlp-dev@feat/youtube/sabr"
```

## InnerTube (transcript + fallback vídeo)

### Clients (teste 2026-08)

| Client | Version override | Uso |
|--------|------------------|-----|
| ANDROID | 20.10.38 | Captions ASR + listagem de streams |
| IOS | 20.10.4 | Fallback player |
| WEB stock | — | Bot / UNPLAYABLE |

Fonte da lib: https://github.com/tombulled/innertube

### Transcript ASR

1. Ler `captionTracks` do `player`
2. Preferir `kind == "asr"`
3. GET `baseUrl` com `fmt=json3`
4. Concatenar `events[].segs[].utf8`, dedupe rolling captions
5. Gravar `.txt` / `.json` / `.vtt`

### Download CDN (InnerTube HTTPS)

- Full GET em `googlevideo.com` → frequentemente **403** → usar **Range**.
- Sob experimento SABR, offsets altos (~2.5–15 MB+) → 403 mesmo com URL nova.
- Progressive (itag 18) costuma completar, mas fica em **360p**.

## Dependências

```
innertube>=2.1.19
httpx>=0.23
ffmpeg no PATH
yt-dlp-sabr.exe (ou venv feat/youtube/sabr)
Node.js (JS challenges do yt-dlp)
```

## Verificação

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 FILE.mp4
```

Esperado para HQ: `1920,1080` (ou resolução pedida em `--max-height`).
