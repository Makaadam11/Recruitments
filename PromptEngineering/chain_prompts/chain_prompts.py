# Step 1: Meta Prompting - Setting the context for the task
PROMPT_META = """
You are a marketing compliance specialist at [Company] Fintech Ltd. Your task is to evaluate the compliance of promotional materials with FCA regulations and company standards while balancing creativity and effectiveness. Note that you are only responsible for compliance evaluation, not financial advice.
"""

# Step 2: Prompt Chaining - Evaluation of primary categories using Tree of Thoughts
PROMPT_CATEGORIES = [
    # Clarity Evaluation - Tree of Thoughts (parallel exploration for deeper analysis)
    """ Evaluate the clarity of the communication: Is the language simple and understandable? Are technical terms explained? List suggestions to make the content more accessible.""",
    
    # Fairness Evaluation - Tree of Thoughts
    """ Evaluate the fairness of the message: Does it reflect both the benefits and risks of the financial product? Recommend adjustments to maintain balance.""",
    
    # Accuracy Evaluation - Tree of Thoughts
    """ Evaluate accuracy and verifiability: Are all data and statements reliable, verifiable, and adequately supported by sources? Provide recommendations for corrections as needed.
    """
]

# Step 3: Step-by-step evaluation of specific guidelines (Prompt Chaining + CoT Prompting)
SPECIFIC_GUIDELINES_PROMPTS = [
    # Example for evaluating specific terms - Chain-of-Thought Prompting
    """ Evaluate the use of terms such as "best," "safest." Ensure that each term is supported by sources, and the context is clear.""",

    # Example for guidelines on referencing competitors
    """ Check references to competitors: Are they compliant with the guidelines? Avoid aggressive language. Report any suggested corrections.""",
    
    # Trademark and logo compliance
    """ Evaluate the use of trademarks and logos per guidelines. Ensure permission is granted for their usage.""",
    
    # Evaluating sources, graphs, and data dates
    """ Verify statistics and graphs: Are they properly referenced and dated? Suggest updates for any outdated information.""",
    
    # Guidelines on terminology related to savings accounts
    """ Review the use of the term "savings account" according to FCA guidelines. Suggest changes if necessary.""",
    
    # Tone, language, and wording evaluation
    """ Review tone and language: Avoid misleading or trivializing investment terminology. Formulate recommendations for corrections as needed.""",
]

# Step 4: Aggregating results and creating final output sections
def aggregate_suggestions(category_results, specific_guidelines_results):
    """Function to aggregate suggestions into final output sections"""
    # Section 1: Other Suggested Modifications (brief, numbered list)
    other_suggestions = "\n**Other Suggested Modifications:**\n" + "\n".join([f"{i+1}. {suggestion[:25]}" for i, suggestion in enumerate(category_results + specific_guidelines_results)])

    # Section 2: Suggested Modifications Explanation (numbered, structured explanation)
    explanation = "\n**Suggested Modifications Explanation:**\n" + "\n".join([f"{i+1}. {explanation}" for i, explanation in enumerate(category_results + specific_guidelines_results)])

    # Limit to required 200 words in Section 2
    if len(explanation.split()) > 200:
        explanation = " ".join(explanation.split()[:200]) + "..."

    combined_report = "Final Compliance Report:\n" + other_suggestions + "\n" + explanation
    return combined_report

# Step 5: Implementing Self-Consistency on each section's results
# Assume we have a `guardrails_check` function that validates the output for contextual compliance
def guardrails_check(output):
    """
    Function that applies Guardrails AI to validate the output for compliance with context requirements.
    Returns True if output is compliant, otherwise False.
    """
    # Placeholder for Guardrails AI API validation
    return True  # Assuming the output is compliant for illustration

def apply_self_consistency_with_guardrails(prompt, retries=3):
    """Run the prompt multiple times, apply Guardrails AI validation, and select the most frequent compliant answer."""
    results = []
    for _ in range(retries):
        result = run_prompt(prompt)
        if guardrails_check(result):  # Validate result with Guardrails AI
            results.append(result)
    
    if results:  # Select the most common result among compliant ones
        most_common_result = Counter(results).most_common(1)[0][0]
        return most_common_result
    else:
        return "No compliant answer found."

# Step 6: Generating the Final Report with specified outputs
def generate_compliance_report():
    # Processing main categories (ToT)
    category_results = [apply_self_consistency_with_guardrails(prompt) for prompt in PROMPT_CATEGORIES]

    # Processing specific guidelines (Prompt Chaining + CoT)
    specific_guidelines_results = [apply_self_consistency_with_guardrails(prompt) for prompt in SPECIFIC_GUIDELINES_PROMPTS]

    # Aggregating results into the structured report with specified conditions
    return aggregate_suggestions(category_results, specific_guidelines_results)

# Run the full analysis
compliance_report = generate_compliance_report()
print(compliance_report)
