---
name: meeting-viral-shorts-cuts
description: >-
  Cria cortes virais 9:16 (Shorts/Reels) a partir de gravações de reunião
  (MP4 local): extrai áudio, Gemini lista trechos cortáveis, monta multi-clip
  (hook→setup→tension→payoff→CTA) e render FFmpeg com legendas. Use when the
  user asks for cortes de reunião, meeting shorts, clipes de call/Meet/Zoom,
  ou pipeline de conteúdo a partir de gravação interna.
---

# Meeting Viral Shorts Cuts

**Não reinventar.** Pipeline: `meetings/main.py` (`ingest` → `audio` → `candidates` → `cuts` → `render`).

Gemini **só processa áudio** (nunca o MP4). Devolve `candidates[]`; a 2ª passagem (texto) monta Shorts como a skill YouTube.

Estratégia: [reference-strategy.md](reference-strategy.md) · schema: [reference-schema.md](reference-schema.md)

## Quando aplicar

- Cortes / Shorts / Reels a partir de MP4s de reunião (Meet, Zoom, Teams)
- Re-render / top-N de cortes já gerados
- Conteúdo de marca pessoal extraído de call interna

## Skills relacionadas

| Etapa | Skill |
|-------|--------|
| Shorts a partir de YouTube | `youtube-viral-shorts-cuts` |
| Gemini API | `gemini-interactions-api` |

## Pré-requisitos

```powershell
cd meetings
pip install -r requirements.txt
# GEMINI_API_KEY em meetings/.env ou youtube/.env
# ffmpeg/ffprobe no PATH
```

## Princípio

1. Perfil (opcional): esta skill não embute nem exige um perfil pessoal.
   Perfis reais (voz, nicho, defaults de um criador específico) vivem em
   overlays privados — ex. `braiam-company-private/projects/content-automation/profiles/`
   — e são carregados pelo agente sob demanda, fora deste repositório. Sem
   perfil, use os defaults genéricos abaixo.
2. Primary = MP4 **mais longo** se vários arquivos da mesma reunião
3. Template visual Hormozi até o user pedir outro

## Workflow (obrigatório)

```
Progresso:
- [ ] 1. Declarar: «Usando meeting-viral-shorts-cuts → meetings/main.py»
- [ ] 2. Escopo (smoke | pipeline completo | cuts-only | render-only)
- [ ] 3. Rodar comandos abaixo
- [ ] 4. Confirmar candidates.json + cuts.json + shorts/*.mp4
- [ ] 5. Creditar música se a licença exigir
```

### Comandos canônicos

Working directory: **`meetings/`**.

```powershell
python main.py pipeline --files "PATH1" "PATH2" -o out --max-cuts 5 --min-s 45 --max-s 90 --max-rank 3
python main.py ingest --files "PATH" -o out
python main.py candidates MEETING_ID -o out
python main.py cuts MEETING_ID -o out
python main.py render -o out --meeting-id MEETING_ID --max-rank 3
```

Gemini **nunca** recebe `type: video`. Áudio via Files API (`type: audio`).

## Layout de saída

```
meetings/out/
  cuts_manifest.json
  renders_manifest.json
  meetings/{id}_{slug}/
    source.mp4
    audio.mp3
    audio_chunks/
    meta.json
    candidates.json
    cuts.json
    cuts_overview.md
    gemini_usage.json
    shorts/{cut_id}_{slug}.mp4
```

## Regras

- Montagem 4–7 clips, 45–90s, hook→setup→tension→payoff→CTA
- CTA de plataforma (salva/comenta/segue) — nunca “assista a reunião”
- Timestamps só dentro dos candidates
- Teto de custo ~US$1 sem `--force`; log em `gemini_usage.json`
- Modelo: `gemini-3.7-flash` com fallback `gemini-3.6-flash`

## Decisões rápidas

| Situação | Ação |
|----------|------|
| Pedido de shorts de reunião | `main.py pipeline` |
| Dois arquivos da mesma call | ingest os dois; primary = mais longo |
| Estimativa > US$1 | parar; `--force` só com ok do user |
| Música ausente | render sem BG |
