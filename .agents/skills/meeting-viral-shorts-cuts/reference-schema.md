# Reference — Schemas

## `candidates.json`

```json
{
  "schema_version": "1.0",
  "candidates": [
    {
      "id": "c00_00",
      "start_ms": 0,
      "end_ms": 0,
      "transcript": "...",
      "why_cuttable": "...",
      "topic": "produtividade|ia|empreender|outro",
      "energy": "high|medium"
    }
  ]
}
```

## `cuts.json` 2.0

Igual à skill YouTube (`clips[]` + `captions` no clock do short), com:

```json
{
  "source": {
    "kind": "meeting",
    "meeting_id": "...",
    "path": "meetings/{id}_{slug}/source.mp4"
  }
}
```

`full_video_cta` = CTA de plataforma, não “assista a reunião”.
