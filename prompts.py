POLYA_PROMPT_TEMPLATE = """
You are a problem-solving expert. Use Polya's method to solve the following problem.
Focus on the first two steps: Understanding and Planning.

# Problem: {title}

{statement}

## Input Description
{input_description}

## Output Description
{output_description}

## Constraints
{constraints}

## Examples
{examples_text}

# Instructions:
Provide your response in two clear sections: "Understanding" and "Plan".

### Understanding Section:
- Describe the input of the problem.
- List the constraints of the problem.
- State the objective of the problem.
- Describe the output of the problem.
- Identify the edge cases to consider.

### Plan Section:
- Describe the algorithm to solve the problem.
- Specify the data structures to use.
- State the time complexity of the algorithm.
- State the space complexity of the algorithm.
- Provide a step-by-step description of solving the problem in natural language.

Do not write any code. Focus only on understanding and planning.
"""
