# Reference — Estratégia editorial (multi-clip)

Fontes (2025–2026): retenção Shorts (hook 1–2s, open loops, loop narrativo, beats a cada ~2s),
estrutura 5 beats (hook → context/setup → problem/tension → reveal → CTA).

## O que mudou

| Antes | Agora |
|-------|--------|
| 1 trecho contínuo 20–55s | Montagem de **3–7 clips** até **90s** |
| Só `start_ms`/`end_ms` | `clips[]` com `role` + timeline relativa |
| Payoff fechado | Payoff parcial + **open loop** → vídeo completo |

## Beats

1. **hook** — pattern interrupt / mito / consequência (primeiros segundos falados)
2. **setup** — contexto mínimo
3. **tension** — problema / reframe / curiosidade
4. **payoff** — insight que paga o hook (sem esgotar o long-form)
5. **cta** — open loop: vontade de assistir o vídeo completo

## Schema `clips[]`

```json
{
  "role": "hook|setup|tension|payoff|cta|bridge",
  "start_ms": 0,
  "end_ms": 0,
  "reason": "por que este pedaço nesta ordem"
}
```

No `cuts.json` enriquecido cada clip ganha `timeline_start_ms` / `timeline_end_ms`.
`captions` já estão no clock do short montado (0 → duration_ms).

## Render

`modules/render.py` extrai cada clip e concatena (hard cuts), depois aplica o template 9:16.
