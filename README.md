# Repositório Universal de Skills para Agentes de IA (`agent-skills`) 🚀

Bem-vindo ao **agent-skills**, uma coleção pública, portátil e pronta para produção de **55 skills** no padrão universal `.agents/skills/`.

Projetado para funcionar de forma nativa e intercambiável com **Anthropic Claude Code**, **OpenAI Codex**, **Google Antigravity (`agy`)**, **Cursor IDE**, **Windsurf**, **Nous Hermes Agent**, **Cline** e **Roo Code**.

O repositório combina as meta-skills de orquestração do **BRAIAM OS**, o padrão de engenharia **Spec-Driven Development (SDD)**, ferramentas avançadas de mineração de conteúdo/mídia e a suíte completa sincronizada automaticamente com o **[mattpocock/skills](https://github.com/mattpocock/skills)**.

---

## 🔄 Sincronização Automática Diária

Este repositório possui uma rotina automatizada via GitHub Actions (`.github/workflows/sync-upstream-skills.yml`) que roda diariamente às **04:00 UTC** para buscar, integrar e atualizar qualquer novidade ou melhoria publicada no repositório de Matt Pocock.

Você também pode disparar uma sincronização manual a qualquer momento via terminal:
```bash
python3 scripts/sync-upstream.py
```

---

## 🧭 Como Usar as Skills com Qualquer Agente

### Método Padrão (Padrão Aberto `.agents`)
Basta clonar ou linkar este repositório no seu projeto:
* **Claude Code:** Reconhece `.agents/skills/` nativamente.
* **Codex / Antigravity (`agy`):** Aponte para o arquivo `.agents/skills/<nome-da-skill>/SKILL.md`.
* **Cursor / Windsurf:** Adicione no prompt ou no seu `.cursorrules`:
  > *"Utilize a skill `.agents/skills/spec-driven-development/SKILL.md` para planejar e executar esta funcionalidade."*
* **Hermes Agent:** Copie ou crie symlink para `~/.hermes/skills/`.

---

## 📚 Guia Completo do Catálogo de Skills (50 Skills)

Abaixo está o guia detalhado explicando **o que é**, **para que serve** e **quando acionar** cada skill:

---

### 🧠 1. Arquitetura, Governança & Orquestração (BRAIAM OS)

| Skill | Para que serve (Humano) | Quando a IA deve acionar (Gatilho) |
|---|---|---|
| **[`braiam-orchestrator`](.agents/skills/braiam-orchestrator/SKILL.md)** | Transforma qualquer agente em um Sistema Operacional pessoal ou corporativo. Controla contexto em 4 camadas e isola dados privados. | Ao orquestrar múltiplos agentes, organizar bases de conhecimento (Obsidian/Notion) ou estruturar fluxos de trabalho complexos. |
| **[`spec-driven-development`](.agents/skills/spec-driven-development/SKILL.md)** | Engenharia Spec-First (SDD). Proíbe código sem especificação prévia (`SPEC.md`), forçando contratos de dados e testes antes da implementação. | Ao iniciar qualquer nova funcionalidade, refatoração de múltiplos arquivos ou arquitetura de APIs/ferramentas. |
| **[`braiam-hybrid-worker`](.agents/skills/braiam-hybrid-worker/SKILL.md)** | Delegação para workers CLI locais ou remotos (Claude Code, Codex, Antigravity via SSH) economizando tokens e quotas. | Ao terceirizar tarefas pesadas de compilação, testes ou refatoração para um terminal dedicado. |

---

### 🛠️ 2. Engenharia de Software, Design & Qualidade (Matt Pocock)

| Skill | Para que serve (Humano) | Quando a IA deve acionar (Gatilho) |
|---|---|---|
| **[`to-spec`](.agents/skills/to-spec/SKILL.md)** | Transforma ideias vagas, conversas ou requisitos soltos em um documento de especificação técnica formal (`SPEC.md`). | Quando o usuário pedir para planejar uma funcionalidade ou quando os requisitos estiverem soltos/ambíguos. |
| **[`implement-spec`](.agents/skills/implement-spec/SKILL.md)** | Lê uma especificação pronta e gera a estratégia de implementação em passos bite-sized e testáveis. | Imediatamente após a aprovação de uma `SPEC.md` para quebrar a execução em etapas. |
| **[`implement`](.agents/skills/implement/SKILL.md)** | Executa o plano de código com precisão cirúrgica, focando no código mínimo necessário e sem escopo extra. | Na fase de escrita de código de uma tarefa planejada. |
| **[`tdd`](.agents/skills/tdd/SKILL.md)** | Prática de Test-Driven Development (Red-Green-Refactor). Define testes que falham antes de escrever código de produção. | Ao criar módulos com lógica de negócio complexa, transformações de dados ou algoritmos críticos. |
| **[`diagnosing-bugs`](.agents/skills/diagnosing-bugs/SKILL.md)** | Diagnóstico metódico de bugs em 4 fases. Proíbe palpites ou chutes antes de isolar a causa-raiz com evidências. | Ao receber relatos de erros, testes quebrados ou comportamentos anômalos no sistema. |
| **[`code-review`](.agents/skills/code-review/SKILL.md)** | Revisão de código profunda pré-commit buscando vulnerabilidades, regressões, falta de testes e problemas de tipagem. | Antes de abrir PRs ou após finalizar alterações significativas em arquivos. |
| **[`codebase-design`](.agents/skills/codebase-design/SKILL.md)** | Padrão *Design it Twice*. Força o desenho de duas abordagens arquiteturais distintas antes da decisão final. | Ao projetar novos módulos, abstrações centrais ou integrações estruturais. |
| **[`improve-codebase-architecture`](.agents/skills/improve-codebase-architecture/SKILL.md)** | Analisa o acoplamento e dependências de um projeto, gerando relatórios de melhoria contínua. | Ao refatorar projetos legados ou quando a arquitetura estiver desorganizada. |
| **[`domain-modeling`](.agents/skills/domain-modeling/SKILL.md)** | Modela domínios de negócio complexos em código, gerando ADRs (Architecture Decision Records) e entidades limpas. | Ao definir novos modelos de negócio, tabelas de banco de dados ou regras de domínio. |
| **[`resolving-merge-conflicts`](.agents/skills/resolving-merge-conflicts/SKILL.md)** | Resolução neutra e inteligente de conflitos de merge no Git, preservando a intenção de ambos os lados. | Ao encontrar conflitos de merge ou rebase no Git. |
| **[`prototype`](.agents/skills/prototype/SKILL.md)** | Desenvolvimento rápido de protótipos e provas de conceito descartáveis (UI ou lógica). | Ao validar rapidamente uma ideia ou viabilidade técnica antes da implementação definitiva. |
| **[`research`](.agents/skills/research/SKILL.md)** | Pesquisa técnica estruturada em documentações, papers e web para fundamentar decisões. | Quando faltar informação técnica sobre uma biblioteca, API externa ou padrão. |
| **[`grill-with-docs`](.agents/skills/grill-with-docs/SKILL.md)** | Estuda a documentação de uma tecnologia e faz perguntas para testar a compreensão e arquitetura. | Ao integrar uma nova biblioteca ou SDK desconhecido. |
| **[`wayfinder`](.agents/skills/wayfinder/SKILL.md)** | Bússola para navegar em codebases complexas e decidir qual o próximo passo de engenharia. | Quando o agente ou usuário estiver incerto sobre qual caminho seguir no projeto. |
| **[`wizard`](.agents/skills/wizard/SKILL.md)** | Executa passos interativos e assistentes de configuração no terminal. | Durante setups e bootstraps guiados. |
| **[`ask-matt`](.agents/skills/ask-matt/SKILL.md)** | Consulta decisões de engenharia opinativas baseadas no modelo mental de Matt Pocock. | Ao buscar opiniões fortes sobre TypeScript, arquitetura de software e boas práticas. |
| **[`setup-ts-deep-modules`](.agents/skills/setup-ts-deep-modules/SKILL.md)** | Configura regras de módulos profundos em TypeScript com dependency-cruiser. | Ao estruturar projetos TypeScript em monorepos ou arquiteturas limpas. |
| **[`setup-pre-commit`](.agents/skills/setup-pre-commit/SKILL.md)** | Configura hooks automáticos de git pre-commit no repositório. | Ao preparar um repositório para boas práticas de CI e qualidade. |
| **[`git-guardrails-claude-code`](.agents/skills/git-guardrails-claude-code/SKILL.md)** | Bloqueia comandos destrutivos do Git (ex: `push --force`) executados por agentes autônomos. | Em ambientes onde agentes executam comandos de terminal com autonomia. |
| **[`scaffold-exercises`](.agents/skills/scaffold-exercises/SKILL.md)** | Cria esqueletos de exercícios práticos com testes para aprendizado. | Ao criar materiais didáticos ou desafios técnicos. |
| **[`migrate-to-shoehorn`](.agents/skills/migrate-to-shoehorn/SKILL.md)** | Automatiza migração de dependências legadas em pacotes. | Em processos de modernização de dependências. |
| **[`loop-me`](.agents/skills/loop-me/SKILL.md)** | Loop iterativo de melhoria contínua com feedback em tempo real. | Em tarefas que exigem múltiplas rodadas de refinamento. |

---

### 💬 3. Comunicação, Entrevistas, Escrita & Ensino (Matt Pocock)

| Skill | Para que serve (Humano) | Quando a IA deve acionar (Gatilho) |
|---|---|---|
| **[`grill-me`](.agents/skills/grill-me/SKILL.md)** | Faz o agente entrevistar o humano com perguntas desafiadoras para desvendar requisitos ocultos. | Quando a solicitação do usuário estiver vaga ou antes de planejar grandes projetos. |
| **[`grilling`](.agents/skills/grilling/SKILL.md)** | Protocolo de perguntas sucessivas e profundas para extrair clareza técnica. | Em sessões de discovery, refinamento de escopo e ideação. |
| **[`to-questionnaire`](.agents/skills/to-questionnaire/SKILL.md)** | Converte discussões abertas em formulários estruturados de tomada de decisão. | Para colher respostas padronizadas de stakeholders ou usuários. |
| **[`teach`](.agents/skills/teach/SKILL.md)** | Ensina tópicos complexos estruturando glossários, missões práticas e registros de evolução. | Quando o usuário pede para aprender ou entender a fundo uma tecnologia ou conceito. |
| **[`writing-for-agents`](.agents/skills/writing-for-agents/SKILL.md)** | Padrões de redação de instruções e prompts para outros agentes de IA operarem sem ambiguidades. | Ao redigir arquivos `AGENTS.md`, `CLAUDE.md`, `.cursorrules` ou novas skills. |
| **[`writing-beats`](.agents/skills/writing-beats/SKILL.md)** | Estruturação de redação técnica e artigos em blocos de ritmo (*beats* narrativos). | Ao produzir artigos, newsletters ou documentações extensas. |
| **[`writing-fragments`](.agents/skills/writing-fragments/SKILL.md)** | Captura de pensamentos e ideias em fragmentos para posterior síntese. | Em sessões de brainstorming e notas rápidas. |
| **[`writing-shape`](.agents/skills/writing-shape/SKILL.md)** | Dá formato e tom correto a textos técnicos e informativos. | Na revisão e polimento final de textos. |
| **[`handoff`](.agents/skills/handoff/SKILL.md)** | Transição limpa de contexto entre sessões de trabalho para evitar perda de memória. | Ao encerrar uma sessão de trabalho longa ou trocar de agente. |
| **[`claude-handoff`](.agents/skills/claude-handoff/SKILL.md)** | Empacotamento de estado específico para o Claude Code continuar tarefas perfeitamente. | Ao passar tarefas do orquestrador para o Claude Code CLI. |
| **[`wait-what`](.agents/skills/wait-what/SKILL.md)** | Momento de pausa reflexiva do agente quando ele detecta contradições ou inconsistências. | Sempre que os requisitos forem contraditórios ou violarem premissas anteriores. |
| **[`triage`](.agents/skills/triage/SKILL.md)** | Triagem metódica de issues, bugs e solicitações pendentes. | Na gestão de backlog e triagem de chamados. |
| **[`to-tickets`](.agents/skills/to-tickets/SKILL.md)** | Converte especificações ou discussões em tickets/issues acionáveis para o time. | Após a especificação, para popular Jira, Linear ou GitHub Issues. |
| **[`setup-matt-pocock-skills`](.agents/skills/setup-matt-pocock-skills/SKILL.md)** | Configura o ambiente de trabalho e labels de issues do ecossistema. | Na inicialização de novos projetos que utilizam a suíte de skills. |

---

### 🎥 4. Inteligência de Mídia, YouTube & Mineração de Dados (BRAIAM)

| Skill | Para que serve (Humano) | Quando a IA deve acionar (Gatilho) |
|---|---|---|
| **[`youtube-channel-outliers`](.agents/skills/youtube-channel-outliers/SKILL.md)** | Analisa canais do YouTube, calcula médias de views/likes/comentários e encontra os vídeos virais *outliers*. | Quando o usuário quiser mapear canais concorrentes ou descobrir o que dá audiência em um nicho. |
| **[`youtube-video-analysis`](.agents/skills/youtube-video-analysis/SKILL.md)** | Dissecação profunda de um vídeo específico (transcrição, pontos de retenção, hooks e análise de sentimento). | Para dissecar o roteiro e estrutura de um vídeo de alta performance. |
| **[`youtube-viral-shorts-cuts`](.agents/skills/youtube-viral-shorts-cuts/SKILL.md)** | Mineração de cortes virais para Shorts/Reels a partir de vídeos longos (com timestamps, hooks e framing 9:16). | Ao criar conteúdo curto derivado de vídeos longos do YouTube. |
| **[`meeting-viral-shorts-cuts`](.agents/skills/meeting-viral-shorts-cuts/SKILL.md)** | Mineração de momentos de alto impacto e insights em reuniões, webinars e podcasts gravados. | Para extrair cortes de reuniões internas, aulas ou palestras. |
| **[`youtube-innertube-download`](.agents/skills/youtube-innertube-download/SKILL.md)** | Extração ultra-rápida de metadados e transcrições de vídeos via API interna do YouTube sem bloqueios. | Sempre que precisar baixar metadados ou transcrições de vídeos sem passar por restrições de bot. |
| **[`youtube-proxy-mine`](.agents/skills/youtube-proxy-mine/SKILL.md)** | Rotação automática de proxies para mineração massiva de dados do YouTube sem sofrer rate limit. | Em tarefas de scraping e mineração em larga escala de milhares de vídeos. |

---

### 📡 5. Tendências, Notícias & Social (BRAIAM)

| Skill | Para que serve (Humano) | Quando a IA deve acionar (Gatilho) |
|---|---|---|
| **[`ai-trend-monitor`](.agents/skills/ai-trend-monitor/SKILL.md)** | Curador stateful que monitora TechCrunch, Hacker News e Google News, alertando apenas sobre notícias 100% inéditas. | Em rotinas diárias/horárias de briefing e curadoria de novidades de IA. |
| **[`twitter-trends`](.agents/skills/twitter-trends/SKILL.md)** | Extrai em tempo real os Trending Topics do X/Twitter (Brasil e Global) sem necessidade de login ou API Key. | Ao monitorar assuntos em alta, notícias quentes ou tópicos virais do momento. |
| **[`agent-reach`](.agents/skills/agent-reach/SKILL.md)** | Roteador universal de busca e extração de conteúdo na internet em 15 plataformas (Twitter, Reddit, YouTube, Bilibili, GitHub, LinkedIn, XiaoHongShu, Exa, V2EX, etc.). | Ao fazer pesquisas profundas na web, buscar menções sociais ou raspar links/artigos de múltiplas plataformas. |
| **[`evolution-api-whatsapp`](.agents/skills/evolution-api-whatsapp/SKILL.md)** | Diagnóstico, status de instâncias, inspeção de banco PostgreSQL/Redis e webhooks da Evolution API. | Ao gerenciar ou solucionar problemas em gateways de WhatsApp self-hosted. |
| **[`opencli-x-browser-bridge`](.agents/skills/opencli-x-browser-bridge/SKILL.md)** | Conecta agentes ao X via OpenCLI e sessão Chrome controlada pelo operador, com leitura delimitada e escrita aprovada. | Ao integrar ou diagnosticar uma conta X sem mover cookies para um servidor. |

---

### 🎨 6. Grafos de Conhecimento, Visualização & Observabilidade (BRAIAM & Open Source)

| Skill | Para que serve (Humano) | Quando a IA deve acionar (Gatilho) |
|---|---|---|
| **[`codegraph`](.agents/skills/codegraph/SKILL.md)** | Grafo semântico de código via AST (Tree-Sitter). Permite consultar definições, hierarquias de chamadas, blast radius e navegação estrutural instantânea sem usar grep. | Ao entender o funcionamento estrutural de uma codebase, rastrear quem chama o quê ou mapear o impacto de refatorações. |
| **[`graphify`](.agents/skills/graphify/SKILL.md)** | Converte qualquer pasta de arquivos (código, docs, PDFs, imagens, áudios) em um grafo de conhecimento navegável, com `graph.html`, comunidades e relatório `GRAPH_REPORT.md`. | Quando o usuário pedir para mapear ou fazer perguntas contextuais sobre múltiplos documentos, repositórios ou conteúdos multimídia (`/graphify`). |
| **[`excalidraw`](.agents/skills/excalidraw/SKILL.md)** | Gera diagramas arquiteturais em JSON nativo com upload automático (AES-GCM client-side) no [excalidraw.com](https://excalidraw.com). | Ao desenhar arquiteturas de sistemas, fluxogramas, sequências ou diagramas explicativos. |
| **[`langfuse-stats`](.agents/skills/langfuse-stats/SKILL.md)** | Consulta telemetria, custos de tokens, traces e latência em instâncias locais do Langfuse. | Para auditar consumo de API, custos de LLMs e desempenho de agentes. |

---

### ⚡ 7. Eficiência de Tokens & Contexto

| Skill | Para que serve (Humano) | Quando a IA deve acionar (Gatilho) |
|---|---|---|
| **[`rtk-token-efficient-terminal`](.agents/skills/rtk-token-efficient-terminal/SKILL.md)** | Reduz ruído de saída de comandos de terminal com RTK, preservando exit codes e uma rota para recuperar detalhes quando necessários. | Ao executar Git, testes, builds, logs, Docker ou buscas que geram saída extensa para um agente. |
| **[`caveman-local-token-efficiency`](.agents/skills/caveman-local-token-efficiency/SKILL.md)** | Audita e reduz fluxo de tokens com Caveman local, com privacidade, recuperação de contexto e limites de licença explícitos. | Antes de configurar compressão de prompt/contexto, proxy local ou resposta mais concisa em agentes. |

---

## 📄 Licença
Distribuído sob licença MIT. Criado e mantido por [Thiago Nobrega](https://github.com/tsnthiago).  
Upstream skills copyright [Matt Pocock](https://github.com/mattpocock/skills).
