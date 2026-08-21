# Recursos Portáteis de Agentes (`.agents/`) 🚀

Este diretório é o lar canônico de skills reutilizáveis que seguem o padrão aberto `.agents/`.

## Estrutura de Diretórios

```text
.agents/
  README.md
  skills/
    <nome-da-skill>/
      SKILL.md
      references/
      scripts/
      templates/
      assets/
```

## Compatibilidade Universal

As skills localizadas em `.agents/skills/` são 100% interoperáveis com:
- **Anthropic Claude Code**
- **OpenAI Codex CLI**
- **Google Antigravity (`agy`)**
- **Cursor IDE / Windsurf**
- **Nous Hermes Agent**
- **Cline / Roo Code**
- Qualquer orquestrador de IA que suporte injeção de contexto ou ferramentas dinâmicas.

## Regras de Engenharia para Skills
1. **Contrato Estrito:** Toda skill deve ter um `SKILL.md` com YAML frontmatter válido, gatilhos de ativação explícitos (*Quando usar* / *Quando não usar*), fluxo passo a passo e critérios de verificação.
2. **Autonomia:** Scripts auxiliares (`scripts/`) e referências (`references/`) devem ser autocontidos na pasta da skill.
3. **Privacidade e Segurança:** Nunca incluir credenciais, chaves de API, dados privados ou caminhos absolutos de máquinas específicas.

Consulte o [`README.md`](../README.md) na raiz do repositório para o catálogo completo e detalhado das 50 skills disponíveis.
