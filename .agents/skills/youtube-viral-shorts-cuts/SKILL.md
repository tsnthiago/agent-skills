---
name: youtube-viral-shorts-cuts
description: >-
  Cria cortes virais 9:16 (Shorts/Reels) a partir de um vídeo YouTube ou de um
  canal: download HQ, seleção editorial de cortes (Gemini), captions, título em
  caixa branca, efeitos, música royalty-free e render FFmpeg. Use when the user
  asks for cortes, shorts, reels, clipes virais, render de cortes, extrair
  trechos de um vídeo/canal, ou pipeline de viral shorts com perfil configurável.
---

# YouTube Viral Shorts Cuts

**Não reinventar.** Pipeline determinístico: `youtube/main.py` (`download` → `cuts` → `render`).

Cuts usam **Gemini** para **montar** Shorts multi-clip (até 90s): hook → setup → tension → payoff → CTA/open-loop, colando trechos não contínuos do long-form — não inventar `cuts.json` na mão salvo edição pontual.

Estratégia: [reference-strategy.md](reference-strategy.md) · schema: [reference-schema.md](reference-schema.md)

## Quando aplicar

- Cortes / Shorts / Reels / clipes virais a partir de URL, `video_id` ou pasta já baixada
- Re-render / top-N de cortes existentes
- Pipeline completo de viral shorts com perfil opcional do canal

## Skills relacionadas

| Etapa | Skill / ferramenta |
|-------|-------------------|
| Só download | `youtube-innertube-download` → mesmo `main.py download` |
| Análise 1 vídeo | `youtube-video-analysis` → `main.py analyze` |
| Outliers de canal | `youtube-channel-outliers` → `main.py outliers` |
| Pesquisa web | `agent-reach` |

## Pré-requisitos

```powershell
cd youtube
pip install -r requirements.txt
# youtube/.env com GEMINI_API_KEY=...
# yt-dlp-sabr + ffmpeg .exe (ver skill de download)
```

## Princípio: mesmo canal vs canal novo

1. **Canal perfilado**: esta skill não embute nem exige um perfil de canal
   específico. Perfis reais de cliente/canal (nicho, tom, música default)
   vivem em overlays privados — ex.
   `braiam-company-private/clients/<client>/profiles/` — e são carregados
   pelo agente sob demanda, fora deste repositório.
2. **Canal novo**: analisar nicho (tema, tom, pacing, idioma) antes de renderizar em massa; ajustar música/hooks
3. **Tema ≠ perfil**: trocar música/tom do hook; manter template visual até o user pedir outro

## Workflow (obrigatório)

```
Progresso:
- [ ] 1. Declarar: «Usando youtube-viral-shorts-cuts → youtube/main.py»
- [ ] 2. Escopo (1 vídeo | cuts-only | render-only | top N)
- [ ] 3. Rodar pipeline ou etapas isoladas (comandos abaixo)
- [ ] 4. Confirmar cuts.json + shorts/*.mp4
- [ ] 5. Creditar música se a licença exigir
```

### Comandos canônicos

Working directory: **`youtube/`**.

Pipeline completo:

```powershell
python main.py pipeline "URL" -o out --max-cuts 5 --min-s 45 --max-s 90 --max-rank 3
```

Só até cuts (sem render):

```powershell
python main.py pipeline "URL" -o out --cuts-only --min-s 45 --max-s 90
```

Etapas isoladas:

```powershell
python main.py download "URL" -o out --max-height 1080
python main.py cuts VIDEO_ID -o out --max-cuts 5 --min-s 45 --max-s 90
python main.py render -o out --video-id VIDEO_ID --max-rank 3
python main.py render -o out --video-id VIDEO_ID --cut-id VIDEOID_c01
python main.py render -o out --video-id VIDEO_ID --all
```

### Layout de saída

```
youtube/out/
  cuts_manifest.json
  renders_manifest.json
  videos/{id}_{slug}/
    {id}.1080p.mp4
    transcript.json | .vtt | .txt
    meta.json
    cuts.json
    cuts_overview.md
    shorts/{cut_id}_{slug}.mp4
    shorts/{cut_id}_{slug}.ass
  assets/fonts/   # Bebas Neue, Montserrat (já no repo youtube/)
  assets/music/   # + CREDIT.txt
```

## Regras editoriais (o script aplica; o agent valida)

- Montagem multi-clip: gancho → setup → tensão → payoff → CTA open-loop (vídeo completo)
- `hook` = título caixa branca (casing natural, não ALL CAPS)
- Duração alvo default **45–90s** (`--min-s` / `--max-s`)
- Não inventar trechos fora do transcript
- Schema / estratégia / estilo: [reference-schema.md](reference-schema.md), [reference-strategy.md](reference-strategy.md), [reference-render.md](reference-render.md)

## Estilo visual (já no `modules/render.py`)

1. Título topo: caixa branca, texto preto, ~4–5s
2. Legendas: amarelo, stroke preto, 1–2 palavras, Bebas Neue
3. 1080×1920 cover-crop sem stretch; zoom lento
4. Frame de referência do usuário > este default

## Decisões rápidas

| Situação | Ação |
|----------|------|
| Pedido de shorts | `main.py pipeline` (não reinventar FFmpeg/Gemini) |
| Só JSON de cortes | `--cuts-only` ou `main.py cuts` |
| Proxy free | transcript ok; vídeo HQ sem proxy se SABR travar |
| Canal com perfil privado | carregar overlay de perfil fora deste repositório |
| Height 360 | parar; corrigir SABR antes de renderizar |
| Música errada | `--music PATH` ou trocar em `assets/music/` |

## Limites

- Não usar scripts legados específicos de clientes nem scripts embutidos antigos da skill.
- Gemini cobra tokens; o pipeline grava `gemini_usage.json`.
- Free proxies na lista `out/proxies/` envelhecem rápido.
