# Reference — Schemas

## `cuts.json` (por vídeo) — schema 2.0 multi-clip

```json
{
  "schema_version": "2.0",
  "generated_at": "ISO-8601Z",
  "target": {
    "platform": "shorts_reels",
    "aspect_ratio": "9:16",
    "duration_range_s": [45, 90],
    "edit_mode": "assembled_multi_clip",
    "strategy": "hook_setup_tension_payoff_cta_open_loop",
    "beats": ["hook", "setup", "tension", "payoff", "cta"]
  },
  "source": { "video_id": "...", "folder": "videos/{id}_{slug}", "path": "..." },
  "cuts": [
    {
      "cut_id": "{video_id}_c01",
      "rank": 1,
      "slug": "snake_case",
      "edit_mode": "assembled_multi_clip",
      "duration_ms": 72000,
      "hook": "Título caixa branca",
      "narrative_arc": "mito → reframe → prova → CTA",
      "open_loop": "o que fica em aberto no long-form",
      "full_video_cta": "intenção do CTA",
      "summary": "...",
      "why_it_works": "...",
      "clip_count": 5,
      "clips": [
        {
          "index": 1,
          "role": "hook",
          "start_ms": 0,
          "end_ms": 0,
          "duration_ms": 0,
          "timeline_start_ms": 0,
          "timeline_end_ms": 0,
          "reason": "...",
          "transcript": "..."
        }
      ],
      "transcript": "texto colado com …",
      "captions": [
        { "start_ms": 0, "end_ms": 0, "text": "cue no clock do short", "clip_index": 1 }
      ]
    }
  ]
}
```

Notas:

- `start_ms`/`end_ms` no nível do cut = primeiro/último clip (legado overview)
- `duration_ms` = soma dos clips (duração real do short)
- `captions` já remapeadas para o timeline montado
- Ver [reference-strategy.md](reference-strategy.md)

## `cuts_manifest.json` / `renders_manifest.json`

Mantêm lista de vídeos/renders; `edit_mode` e `clip_count` aparecem nos entries quando multi-clip.
