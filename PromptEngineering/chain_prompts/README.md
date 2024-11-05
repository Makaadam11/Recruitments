# Chain Prompts
    This module automates the evaluation of promotional materials for compliance with FCA regulations and company standards. It uses a combination of meta prompting, prompt chaining, and self-consistency techniques to generate a comprehensive compliance report.

## Key Steps
### 1. Meta Prompting: 
    Sets the context for the compliance evaluation task.
### 2. Prompt Chaining: 
    Evaluates primary categories using the Tree of Thoughts (ToT) method.
### 3. Step-by-step Evaluation: 
    Uses Chain-of-Thought (CoT) prompting to evaluate specific guidelines.
### 4. Aggregating Results: 
    Combines suggestions into final output sections.
### 5. Self-Consistency: 
    Runs prompts multiple times to select the most frequent answer.
### 6. Guidance AI: 
    Applies Guardrails AI to validate the output for compliance with context requirements.
### 7. Generating the Final Report: 
    Processes main categories and specific guidelines to create a structured compliance report.