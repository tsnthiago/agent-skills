---
name: ai-trend-monitor
description: "Curadoria de notícias e tendências sobre Inteligência Artificial, evitando duplicações usando um script Python stateful."
tags: [ai, tech, news, briefing, python]
---

# AI Trend Monitor (BRAIAM)

Esta skill orienta o agente na execução do Curador Automático de IA.

## Execução
O monitoramento é feito primariamente pelo script `scripts/fetch_ai_trends.py` embutido nesta skill. Esse script:
1. Faz o fetch via RSS dos principais portais de tecnologia e IA (TechCrunch, Hacker News, Google News Global, Google News BR).
2. Compara os títulos com um arquivo de cache local `~/.hermes/cache/seen_ai_news.json`.
3. Retorna um JSON apenas com as notícias *INÉDITAS* (limitado a 3 por categoria para evitar spam).

## Como processar no Cronjob
- Execute o script Python usando a tool `execute_code` com o código lido do arquivo `scripts/fetch_ai_trends.py` ou via `terminal` chamando `/root/.hermes/skills/ai-trend-monitor/scripts/fetch_ai_trends.py`.
- Se o script retornar `{"status": "no_new_articles"}`, responda ao usuário de forma bem curta dizendo que não houve atualizações relevantes na última hora.
- Se retornar os dados, crie o "📡 CURADORIA BRAIAM: TECNOLOGIA E I.A." formatando de maneira enxuta, traduzindo para português o que for necessário, mantendo uma pegada curadora e estratégica. Use bullets com emojis no lugar de markdown.