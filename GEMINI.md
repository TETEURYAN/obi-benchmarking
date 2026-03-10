# Pólya - Visão Geral do Projeto

Pólya é um sistema que ajuda estudantes de programação iniciantes a resolver problemas de programação. Baseado no método de quatro etapas de Pólya para resolução de problemas, Pólya foca em cada etapa como uma tarefa separada e fornece feedback imediato ao estudante.

## Método de quatro etapas de Pólya

1. Entender o problema (Compreensão)
2. Elaborar um plano (Planejamento)
3. Executar o plano (Implementação)
4. Revisar (Teste)

## Arquitetura do Sistema

![Arquitetura do Sistema](assets/arch.png)

```mermaid
graph TD
    Student([Estudante])

    subgraph Polya ["Polya [Software]"]
        Interface(["Interface<br>&lt;container&gt;<br>Streamlit"])
        Orchestrator(["Orchestrator"])
        QuestionManager(["Gerenciador de Questões"])
        Judge(["Juiz"])

        subgraph Agents ["Agentes"]
            Comprehension(["Agente de Compreensão<br>&lt;container&gt;"])
            Planning(["Agente de Planejamento<br>&lt;container&gt;"])
            Implementation(["Agente de Implementação (Código)<br>&lt;container&gt;"])
        end
    end

    Database(["Banco de Dados de Questões<br>&lt;container&gt;<br>JSON"])

    %% Conexões
    Student -- "Seleciona uma questão para<br>estudar" --> Interface
    Interface -- "E/S do Usuário" --> Orchestrator
    Orchestrator -- "Recupera as<br>questões de programação<br>disponíveis para resolver" --> QuestionManager
    QuestionManager -- "Carrega os dados do<br>arquivo JSON" --> Database
    Orchestrator -- "Envia o código do usuário para<br>testar nos casos de teste" --> Judge
    Orchestrator --> Comprehension
    Orchestrator --> Planning
    Orchestrator --> Implementation
```

## Fluxo Principal do Sistema

![Fluxo Principal do Sistema](assets/flow.png)

```mermaid
sequenceDiagram
    participant S as Estudante
    participant I as Interface
    participant O as Orchestrator
    participant CA as Agente de Compreensão
    participant PA as Agente de Plano
    participant IA as Agente de Implementação
    participant J as Juiz

    S->>I: Seleciona a questão para resolver
    Note over I: Listar questões
    Note over I: Mostrar informações da questão

    %% Fase de Compreensão
    S->>I: Inicia a comp. e conversa com o agente
    Note over I: Iniciar uma conversa para o processo de compreensão
    I->>O: Inicia a comp ->
    Note over O: Iniciar o Agente de Compreensão e armazenar contexto da conversa
    O->>CA: Inicia a comp ->
    Note over CA: Guiar o estudante a entender o problema e restrições

    CA->>O: Quando confiante de que o estudante entendeu o problema
    Note over O: Parar o agente de compreensão
    O->>I: notificar o estudante ->
    Note over I: Mostra ao estudante que eles entenderam o problema com um resumo
    I-->>S: verificar o estudante ->

    %% Fase de Planejamento
    S->>I: Verifica para prosseguir, e conversa com o agente
    Note over I: Prosseguir para a etapa de planejamento
    I->>O: Inicia o planejamento ->
    Note over O: Iniciar o Agente de Plano e armazenar contexto da conversa
    O->>PA: Inicia o planejamento ->
    Note over PA: Guiar o estudante a planejar uma solução para o problema

    PA->>O: Quando confiante de que o estudante planejou uma boa solução
    Note over O: Parar o agente de plano
    O->>I: notificar o estudante ->
    Note over I: Mostra ao estudante que eles planejaram uma solução viável com um resumo

    %% Fase de Implementação
    S->>I: Verifica para prosseguir
    Note over I: Prosseguir para a etapa de implementação e mostra a interface de código
    I->>O: Inicia a implementação ->
    Note over O: Iniciar o Agente de Implementação
    O->>IA: Inicia a implementação ->
    Note over IA: Guiar o estudante a codificar o que propôs como planejado, executando os testes e código

    %% Loop de Implementação
    loop Loop de Implementação
        S->>I: Executar o envio
        Note over I: Mostra uma interface de processamento
        I->>O: Enviar o código ->
        Note over O: Envia ao juiz para executar casos de teste
        O->>J: Enviar o código e informações da questão ->
        Note over J: Avaliar o código contra casos de teste de execução
        J->>O: Retornar os resultados da avaliação ->
        Note over O: Verifica os resultados da avaliação

        alt Se não estiver correto
            O->>IA: Se não estiver correto, enviar ao agente de implementação ->
            Note over IA: Verifica o código do usuário, os resultados da avaliação, planejamento e informações da questão
            IA->>I: Saída dos resultados de processamento com dicas para o usuário resolver corretamente ->
            Note over I: Saída dos resultados de processamento com dicas para o usuário resolver corretamente
        else Se estiver correto
            O->>I: Se estiver correto, parar o processo ->
            Note over I: Mostra que o estudante completou com sucesso
        end
    end
```

# Pilha de Tecnologia

| Componente | Tecnologia |
|------------|------------|
| Gerenciador de Pacotes | uv |
| Interface | Streamlit |
| Orchestrator | Python |
| Gerenciador de Questões | Python |
| Juiz | Piston (Auto-hospedado via Docker) |
| Agente de Compreensão | Python, Haystack |
| Agente de Planejamento | Python, Haystack |
| Agente de Implementação | Python, Haystack |
| Banco de Dados de Questões | JSON |