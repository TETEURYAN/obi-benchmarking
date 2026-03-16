# Polya - Overview

This project intent to be a evaluator of LLM models in the context of the first two steps of Polya's method for problem solving - Understanding and Planning.

## The problem

LLMs are good at generating code, and exists a large number of benchmarks to evaluate them. However, there are few studies about the first two steps of Polya's method for problem solving - Understanding and Planning. This project aims to check how good are the LLMs in this context.

## Architecture

The solver is composed of a multi-agent system, where each agent is responsible for a specific step of Polya's method. The agents are:
- Comprehension Agent: Responsible for understanding the problem
- Planning Agent: Responsible for planning the solution
- Evaluation Agent: Responsible for evaluating the solution

## The methodology

We will use a set of OBI (Olimpíada Brasileira de Informática) problems to evaluate the LLMs. Providing the problem statement, we will ask the LLM to describe the understanding of the problem, the plan to solve it, and the solution.

### Comprehension Agent

In this step the LLM should describe the understanding of the problem. This description should include:

- Input of the problem
- Contraints of the problem
- Objective of the problem
- Output of the problem
- The edge cases to consider

### Planning Agent

In this step the LLM should describe the plan to solve the problem. This description should include:

- The algorithm to solve the problem
- The data structures to use
- The time complexity of the algorithm
- The space complexity of the algorithm
- Step by step description of solving the problem in natural language

### Implementation Agent

In this step the LLM should implement the solution based on the plan provided by the Planning Agent. This implementation should include:

The implementation should be in Python and should be able to solve the problem.

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

We will evaluate the LLM based on the judge's evaluation. The judge will evaluate the solution based on the following criteria:

- Correctness: The solution should produce the correct output for the given input.
- Test cases: The solution should pass all the test cases.
- Time complexity: The solution should have a time complexity less than or equal to the problem constraints.
- Space complexity: The solution should have a space complexity less than or equal to the problem constraints.


## Script

For this evaluation we will use a script that will take the questions from the dataset and ask the LLM to solve them. Then the script will output the evaluation in a CSV file with the following structure:

| question_id | model | understanding_text | plan_text | code_text | judge_correctness | judge_test_cases | judge_time_complexity | judge_space_complexity | 

### Technical Requirements

- Language: Python
- Package Manager: `uv`
- Dependencies: `openai` (or similar for LLM access), `pandas` (for CSV handling), `pydantic` (for data validation).



