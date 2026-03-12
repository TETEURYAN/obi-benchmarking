# Polya - Overview

This project intent to be a evaluator of LLM models in the context of the first two steps of Polya's method for problem solving - Understanding and Planning.

## The problem

LLMs are good at generating code, and exists a large number of benchmarks to evaluate them. However, there are few studies about the first two steps of Polya's method for problem solving - Understanding and Planning. This project aims to check how good are the LLMs in this context.

## The methodology

We will use a set of OBI (Olimpíada Brasileira de Informática) problems to evaluate the LLMs. Providing the problem statement, we will ask the LLM to describe the understanding of the problem and the plan to solve it. 

### Understanding

In this step the LLM should describe the understanding of the problem. This description should include:

- Input of the problem
- Contraints of the problem
- Objective of the problem
- Output of the problem
- The edge cases to consider


### Plan

In this step the LLM should describe the plan to solve the problem. This description should include:

- The algorithm to solve the problem
- The data structures to use
- The time complexity of the algorithm
- The space complexity of the algorithm
- Step by step description of solving the problem in natural language

## The dataset

The dataset will be composed of 10 problems from OBI, with different levels of difficulty. These problems will be available in a JSON file, with the following structure:

{
    "id": "",
    "title": "",
    "statement": "",
    "input": "",
    "output": "",
    "constraints": "",
    "examples": [
        {
            "input": "",
            "output": ""
        }
    ]
}

## The evaluation

We will evaluate the LLM based on the following criteria:

- Step 1: Understanding
    - Input: 0/10
    - Constraints: 0/10
    - Objective: 0/10
    - Output: 0/10
    - Edge cases: 0/10
    - Total: 0/50

- Step 2: Planning
    - Algorithm: 0/10
    - Data structures: 0/10
    - Time complexity: 0/10
    - Space complexity: 0/10
    - Step by step description: 0/10
    - Total: 0/50

## Script

For this evaluation we will use a script that will take the questions from the dataset and ask the LLM to solve them. Then the script will output the evaluation in a CSV file with the following structure:

| question_id | model | understanding_text | plan_text | 

### Technical Requirements

- Language: Python
- Package Manager: `uv`
- Dependencies: `openai` (or similar for LLM access), `pandas` (for CSV handling), `pydantic` (for data validation).



