---
name: rtk-token-efficient-terminal
description: "Use when an agent runs noisy terminal commands and needs smaller, actionable output without hiding errors."
version: 1.0.0
author: BRAIAM / Thiago Nobrega
license: MIT
metadata:
  tags: [tokens, terminal, rtk, cli, observability, efficiency]
  source: https://github.com/rtk-ai/rtk
  upstream_license: Apache-2.0
---

# Terminal eficiente com RTK

## Objetivo

Use o RTK para reduzir **saída de comandos de terminal** que entraria no contexto do agente: logs repetitivos, listagens extensas, status de Git, resultados de testes e builds. Ele não reduz automaticamente o tamanho do prompt do usuário, das skills carregadas, do histórico da conversa ou da resposta do modelo.

A economia de tokens exibida pelo RTK é uma estimativa baseada no volume de bytes. Trate percentuais como indicador operacional, não como fatura do provedor.

## Quando usar

- O agente executa `git`, testes, builds, linters, Docker, buscas ou logs ruidosos.
- A informação necessária é status, falhas, arquivos alterados ou resumo de execução.
- A saída bruta não é necessária para diagnosticar o problema.

## Quando não usar

- Ao investigar bug em que contexto completo, linhas longas ou logs integrais são a evidência principal.
- Para copiar dados exatos, gerar artefatos, validar conteúdo completo ou depurar filtros do próprio RTK.
- Para comandos compostos/heredocs que o rewriter deixou intactos; não reescreva manualmente sem confirmar equivalência.

## Configuração segura no Hermes

1. Instale uma versão verificada do RTK e confirme `rtk --version`.
2. Desative telemetria se o ambiente exigir operação local:
   ```bash
   rtk telemetry disable
   rtk telemetry status
   ```
3. Ative o plugin Hermes:
   ```bash
   rtk init --agent hermes
   hermes plugins list --plain --no-bundled
   ```
4. Reinicie a sessão/gateway do Hermes. O plugin atua antes de chamadas ao `terminal` e falha aberto: se não conseguir reescrever, o comando original deve continuar.

## Uso direto

Prefira o plugin para comandos simples. Use RTK explicitamente quando quiser controlar o filtro:

```bash
rtk git status
rtk git diff
rtk pytest
rtk docker compose ps
rtk docker logs <container>
rtk grep "padrão" .
rtk read caminho/do/arquivo
```

Para saída arbitrária, mantenha evidência de erro sem despejar progresso:

```bash
rtk err <comando>
rtk test <comando-de-teste>
```

## Protocolo de investigação

1. Comece com saída compacta para localizar arquivo, teste ou erro relevante.
2. Se o diagnóstico depender de detalhe removido, recupere somente a fonte necessária com o comando original ou leitura paginada.
3. Nunca conclua que não há erro só porque um filtro omitiu detalhe; valide o exit code e a prova mais próxima.
4. Para builds/testes, execute sem filtros quando for necessário preservar o código de saída e o output integral de uma falha.

## Limites e riscos

- Filtros podem truncar contexto útil; RTK é uma camada de eficiência, não uma fonte de verdade.
- `rtk rewrite` retorna códigos específicos para rewrite/passthrough. Plugins devem preservar o comando original em qualquer incerteza.
- Não use wrappers que mascarem exit code, como pipes para `tail`, em gates de build/teste.
- Nunca habilite telemetria sem decisão explícita do operador.

## Verificação

- [ ] `rtk --version` responde.
- [ ] `rtk telemetry status` confirma a política desejada.
- [ ] `rtk rewrite 'git status'` produz `rtk git status` ou o plugin está habilitado.
- [ ] Um comando suportado mantém o mesmo exit code e produz saída menor.
- [ ] Uma falha real continua exibindo erro suficiente para correção.

## Referências

- Upstream: https://github.com/rtk-ai/rtk
- Integração Hermes: `hooks/hermes/` no repositório upstream
- Licença upstream: Apache-2.0
