# Reference — Render & estilo

## Download da fonte (antes do render)

O mp4 1080p **não** vem do yt-dlp estável. Usar skill `youtube-innertube-download`
(SABR yt-dlp + InnerTube transcript). Ver `SKILL.md` §3 e a skill de download.

## Template visual (ASS)

### Título (`Hook`)

- Font: Montserrat (Black/ExtraBold)
- Primary: preto `&H00000000`
- BorderStyle: **3** (caixa opaca)
- OutlineColour / Back: branco `&H00FFFFFF`
- Outline (padding da caixa): ~16–20
- Alignment: 8 (topo centro)
- MarginV: ~70–90
- Texto: **casing natural** (não forçar uppercase)
- Duração: ~4–5s no início do Short

### Legendas (`Hormozi`)

- Font: **Bebas Neue**
- Primary: amarelo `&H0000FFFF`
- Outline: preto, width ~5
- BorderStyle: 1
- Alignment: 2 (bottom centro)
- MarginV: ~500–540 (lower third / peito)
- **1–2 palavras** por frame; palavra ativa com pop `\t` de escala
- Sempre UPPERCASE no texto das legendas

## Sync de captions

YouTube ASR (VTT/json3) usa janelas **sobrepostas**. Timing correto da fala ≈ **início de cada cue até o início da próxima**.

1. Ordenar por `start_ms`
2. Deduplicar mesmo start (ficar com texto mais completo)
3. `end = next.start` (não usar o `end` longo do ASR)
4. Descartar lead-in &lt; ~250ms no começo do corte
5. Expandir em palavras (Whisper preferencialmente)

## FFmpeg (essencial)

### Extract (pass 1)

```text
ffmpeg -i SRC -ss START -t DUR
  -vf setpts=PTS-STARTPTS -af asetpts=PTS-STARTPTS
  → tmp_extract.mp4
```

### Burn (pass 2) — sem distorção

```text
split → bg: scale+crop 1080x1920 + gblur
      → fg: scale+crop 1080x1920 + scale UNIFORME para ~92% (mesmo aspect 9:16)
overlay centro
eq + unsharp + vignette + fade
subtitles=ASS:fontsdir=...
(+ amix voz + música ducked)
```

**Proibido:** `scale=1080:1766` (só altura) — distorce.

Sharp sugerido com aspect exato: largura múltipla de 18 → `SHARP_H = SHARP_W * 1920 / 1080` (ex.: 990×1760).

## render_cuts.py — flags

| Flag | Uso |
|------|-----|
| `--all` | Todos os cortes do manifest |
| `--max-rank N` | Ranks 1..N |
| `--cut-id ID` | Um corte |
| `--whisper` | Retimar palavras (recomendado) |
| `--caption-offset-ms` | Ajuste fino (+ atrasa legenda) |
| `--music` / `--no-music` | Trilha |
| `--music-volume` | Default ~0.13 |
| `--style` | `hormozi` (default visual referência) |

## Música — critérios

| Nicho | Mood sugerido |
|-------|----------------|
| Desenvolvimento pessoal / motivação | Inspirational, cinematic leve |
| Ansiedade / sombra | Ambient, deliberado, sem batida agressiva |
| Energia / hábito / esporte | Upbeat leve, sem vocal |
| Finanças / business | Corporate minimal / pulse suave |
| Humor | Não usar trailer épico; preferir leve/quirky |

Fontes usuais: Incompetech (CC BY), Pixabay Content License, Mixkit — sempre gravar `CREDIT.txt`.

Exemplo Tomás (default histórico):

```text
Inspired by Kevin MacLeod (incompetech.com) — CC BY 4.0
```

## Dependências

- ffmpeg / ffprobe (build completo com libass)
- Python 3.10+
- `faster-whisper` para `--whisper` (modelo `small` CPU int8 ok)
- Fontes em `assets/fonts/`
