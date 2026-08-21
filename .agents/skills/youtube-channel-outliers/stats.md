# Método estatístico

## Baseline

Calcular sobre vídeos públicos com `view_count` não nulo:

- mediana e média de views
- média/mediana **excluindo o #1 de views** (mostra o “canal real”)
- mediana de `engagement`

## Outlier (IQR + z)

Para cada métrica:

1. Q1, Q3, IQR = Q3−Q1
2. Fence alto = Q3 + 1.5×IQR; fence baixo = Q1 − 1.5×IQR
3. z = (x − mean) / stdev

Marcar HIGH se `x > fence_alto` **ou** `z ≥ 2`.
Marcar LOW (rates/engagement/views) se `x < fence_baixo` **ou** `z ≤ −2`.

## Score composto (priorizar dissecção)

Ordenar candidatos por:

1. Nº de flags HIGH em métricas de performance
2. `max(z)` em views/likes/comments
3. views absolutas

Sempre dissecar o mega-outlier (z ≫ 2 em views) se existir.
