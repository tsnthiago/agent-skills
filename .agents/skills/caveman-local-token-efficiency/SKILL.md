---
name: caveman-local-token-efficiency
description: "Use when auditing or reducing agent token flow with Caveman local tools while preserving privacy, recovery, and correctness."
version: 1.0.0
author: BRAIAM / Thiago Nobrega
license: MIT
metadata:
  tags: [tokens, caveman, compression, proxy, privacy, context]
  source: https://github.com/JuliusBrussee/caveman
  upstream_licenses: [MIT, BSL-1.1]
---

# Eficiência de tokens local com Caveman

## Objetivo

Caveman oferece duas superfícies diferentes:

1. **Skills de resposta**: removem filler e repetição de respostas do agente.
2. **Runtime local**: comprime conteúdo antes de chegar ao provedor e guarda originais recuperáveis localmente.

Use apenas depois de medir. O resultado local é uma estimativa de tokens processados/economizados, não uma confirmação de cobrança do provedor.

## Quando usar

- Há histórico de sessões, ferramentas ou contexto grande consumindo entrada desnecessária.
- É preciso auditar onde os tokens entram antes de ativar um proxy.
- Uma equipe quer reduzir conteúdo repetitivo sem perder a capacidade de recuperar o original.

## Não use por padrão quando

- A integração do agente é mais nova que a versão oficialmente testada pelo Caveman.
- O fluxo usa OAuth/streaming e o MCP de recuperação ainda não está configurado.
- O ambiente não pode armazenar conteúdo potencialmente sensível em disco local.
- O produto será hospedado para tráfego de terceiros: o runtime Engine/Proxy/MCP é BSL-1.1; valide licença comercial antes desse uso.

## Privacidade primeiro

A telemetria anônima do CLI é opt-out upstream. Antes do primeiro uso operacional:

```bash
caveman telemetry off
caveman telemetry status
```

O runtime pode gravar originais recuperáveis em banco local. Trate o diretório de estado como sensível, com permissões restritas, retenção definida e sem sincronização pública.

## Adoção progressiva

1. **Instalar e verificar binários**
   ```bash
   npm install -g @caveman-ai/cli
   caveman setup --install
   caveman setup --json
   ```
2. **Medir antes de transformar**
   ```bash
   caveman learn
   caveman status
   ```
   Revise os maiores sinks. Não aplique uma economia teórica sem uma hipótese de onde ela vem.
3. **Usar ferramentas locais isoladas**
   ```bash
   printf '%s' '<json>' | caveman compress
   caveman shrink -- <comando-ruidoso>
   caveman toon encode < arquivo.json
   ```
4. **Somente então avaliar proxy/wrap**
   - Rode `caveman doctor <agente>`.
   - Confirme versão e compatibilidade do host.
   - Verifique MCP recovery antes de comprimir streaming/OAuth.
   - Faça uma sessão de teste e compare qualidade, erros e `caveman stats`.
   - Mantenha rollback simples: desabilitar integração e reiniciar o agente.

## Regras de qualidade

- Compressão não pode ocultar um erro, uma exigência de segurança, uma mudança de escopo ou uma confirmação irreversível.
- Recupere o material exato ao tomar decisão baseada em conteúdo comprimido.
- Preserve comandos, IDs, números, código e mensagens de erro literalmente.
- Use linguagem concisa, mas escrita clara para documentos, commits, instruções a humanos e alertas críticos.
- Nunca alegue percentual de economia como redução equivalente da fatura; prompts, histórico e tokens de saída continuam contando.

## Licença e distribuição

Esta skill é uma orientação original e não inclui código upstream. A skill e CLI upstream são MIT, mas o Engine, Proxy, Browser, MCP e componentes de runtime são BSL-1.1. Não copie nem incorpore esses componentes em um serviço de terceiros sem revisar a licença aplicável.

## Verificação

- [ ] `caveman telemetry status` indica `off` quando privacidade local é exigida.
- [ ] `caveman setup --json` mostra binários verificados.
- [ ] O diagnóstico do agente confirma compatibilidade antes de habilitar wrap/proxy.
- [ ] Uma avaliação compara qualidade e não apenas tamanho de entrada.
- [ ] O estado local sensível tem permissões e retenção conhecidas.
- [ ] Existe caminho de rollback documentado e testado.

## Referências

- Upstream: https://github.com/JuliusBrussee/caveman
- Segurança e armazenamento: `SECURITY.md` no repositório upstream
- Licenciamento: `LICENSE`, `LICENSE.BSL` e `LICENSING.md` no repositório upstream
