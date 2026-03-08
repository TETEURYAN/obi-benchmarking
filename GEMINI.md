# Pólya - Project Overview

Pólya is a system that helps freshman programming students to solve programming problems. Based on the Pólya's four-step method for problem solving, Pólya focus on each step as a separate task, and provides immediate feedback to the student. 

## Pólya's four-step method

1. Understand the problem (Comprehension)
2. Devise a plan (Planning)
3. Carry out the plan (Implementation)
4. Look back (Testing)

## System Architecture

![System Architecture](assets/arch.png)

```mermaid
graph TD
    Student([Student])

    subgraph Polya ["Polya [Software]"]
        Interface(["Interface<br>&lt;container&gt;<br>Streamlit"])
        Orchestrator(["Orchestrator"])
        QuestionManager(["Question Manager"])
        Judge(["Judge"])

        subgraph Agents ["Agents"]
            Comprehension(["Comprehension Agent<br>&lt;container&gt;"])
            Planning(["Planning Agent<br>&lt;container&gt;"])
            Implementation(["Implementation (Code)<br>Agent<br>&lt;container&gt;"])
        end
    end

    Database(["Question Database<br>&lt;container&gt;<br>JSON"])

    %% Connections
    Student -- "Select a question to<br>study" --> Interface
    Interface -- "User I/O" --> Orchestrator
    Orchestrator -- "Retrieves the<br>available programming<br>questions to solve" --> QuestionManager
    QuestionManager -- "Loads the data from<br>JSON file" --> Database
    Orchestrator -- "Send the user code to<br>test on test cases" --> Judge
    Orchestrator --> Comprehension
    Orchestrator --> Planning
    Orchestrator --> Implementation
```

## System Main Flow

![System Main Flow](assets/flow.png)

```mermaid
sequenceDiagram
    participant S as Student
    participant I as Interface
    participant O as Orchestrator
    participant CA as Comprehension Agent
    participant PA as Plan Agent
    participant IA as Implementation Agent
    participant J as Judge

    S->>I: Selects the question to solve
    Note over I: List questions
    Note over I: Show question information

    %% Comprehension Phase
    S->>I: Starts the comp. and chat with agent
    Note over I: Start a conversation for comprehension process
    I->>O: Starts the comp ->
    Note over O: Start the Comprehension Agent and store conversation context
    O->>CA: Starts the comp ->
    Note over CA: Guide the student to understand the problem and constraints

    CA->>O: When it's confident that student understood the problem
    Note over O: Stop the comprehension agent
    O->>I: notify the student ->
    Note over I: Shows to student that they understood the problem with a summary
    I-->>S: verify the student ->

    %% Planning Phase
    S->>I: Checks to proceed, and chat with agent
    Note over I: Proceed to planning step
    I->>O: Starts the planning ->
    Note over O: Start the Plan Agent and store conversation context
    O->>PA: Starts the planning ->
    Note over PA: Guide the student to plan a solution to the problem

    PA->>O: When it is confident that student planned a good solution
    Note over O: Stop the plan agent
    O->>I: notify the student ->
    Note over I: Shows to student that they planned a feasible solution with a summary

    %% Implementation Phase
    S->>I: Checks to proceed
    Note over I: Proceed to implementation step and shows the code interface
    I->>O: Starts the implementation ->
    Note over O: Start the Implementation Agent
    O->>IA: Starts the implementation ->
    Note over IA: Guide the student to code they proposed as planned, executing the tests and code

    %% Implementation Loop
    loop Implementation Loop
        S->>I: Run the submit
        Note over I: Shows a processing interface
        I->>O: Send the code ->
        Note over O: Sends to the judge to run test cases
        O->>J: Send the code and question information ->
        Note over J: Evaluate the code against execution test cases
        J->>O: Return the evaluation results ->
        Note over O: Checks the evaluation results

        alt If is not correct
            O->>IA: If is not correct, send to implementation agent ->
            Note over IA: Checks the user code, the evaluation results, planning, and question info
            IA->>I: Output the processing results with tips to user solve correctly ->
            Note over I: Output the processing results with tips to user solve correctly
        else If is correct
            O->>I: If is correct, stop the process ->
            Note over I: Shows that student completed successful
        end
    end
```

# Tech Stack

| Component | Technology |
|-----------|------------|
| Package Manager | uv |
| Interface | Streamlit |
| Orchestrator | Python |
| Question Manager | Python |
| Judge | Judge0 Python SDK |
| Comprehension Agent | Python, Haystack |
| Planning Agent | Python, Haystack |
| Implementation Agent | Python, Haystack |
| Question Database | JSON |