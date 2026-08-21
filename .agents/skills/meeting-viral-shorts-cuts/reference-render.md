# Reference — Render

Template visual idêntico ao YouTube Hormozi (`modules/render.py`):

1. Título topo: caixa branca, texto preto, ~4–5s, casing natural
2. Legendas: amarelo, stroke preto, 1–2 palavras, Bebas Neue (fallback Impact)
3. 1080×1920 cover-crop; Meet landscape pode cortar tiles — aceito no v1
4. Extração no **MP4 local** via FFmpeg — Gemini não entra no render
5. Legendas: **Whisper `large-v3` na GPU** (word-level no áudio já montado)

Fonte 720p ok. Sem música se `assets/music/bg_motivational.mp3` não existir.

Crédito default (se a faixa Inspired for usada): Kevin MacLeod / CC BY 4.0 — ver `assets/music/CREDIT.txt`.
