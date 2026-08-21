---
name: twitter-trends
description: "Scrape Twitter trending topics (Brazil and Worldwide) usando browser_navigate via trends24.in sem necessidade de API Keys."
tags: [twitter, trends, scraping, browser, automation]
---

# Twitter Trends Scraper

Esta skill orienta o agente a extrair os tópicos mais comentados (Trending Topics) do X/Twitter usando o navegador interno, burlando a exigência de login ao acessar o agregador público Trends24.

## Passos para Execução

1. Use o tool `browser_navigate` para acessar a URL da região desejada:
   - Brasil: `https://trends24.in/brazil/`
   - Global (Worldwide): `https://trends24.in/`
2. Analise o snapshot retornado pela navegação. Caso a navegação dê timeout (Operation timed out), isso é comum no carregamento. Chame `browser_snapshot` logo em seguida para ler o DOM da página.
3. Busque na árvore do snapshot pela seção correspondente a "1 hour ago" ou as primeiras listas de `listitem`.
4. Extraia os Top 10 primeiros itens (textos/links).
5. Se o objetivo for obter Brasil e Global, repita o passo a passo para as duas URLs.
6. Consolide os resultados formatando como uma lista limpa e legível e inclua uma brevíssima análise do que está em alta.

## Pitfalls (Armadilhas)
- **Bloqueio de Login:** NUNCA tente acessar `x.com/explore/tabs/trending` diretamente, o X fará um redirecionamento forçado para a tela de login. Sempre use `trends24.in`.
- **Timeouts:** O `browser_navigate` pode acusar timeout se a página tiver muitos anúncios (iframes). O DOM principal geralmente já está carregado, então basta um `browser_snapshot` para capturar os dados.
- **Truncação do Snapshot:** O snapshot pode ser grande. Os dados de "1 hour ago" estão logo no topo do `tabpanel`, não é necessário tentar ler o final do documento.