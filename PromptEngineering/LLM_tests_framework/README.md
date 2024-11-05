# Project README

## Overview

This skeleton project is designed to automate evaluation and selection of the best LLM based on various metrics. It integrates multiple evaluation frameworks and provides a comprehensive analysis of model performance, cost, and latency.

## Project Structure

- .github/workflows/ci.yml: Configuration for Continuous Integration (CI) pipeline.
- config/config.json: Configuration file containing model details and evaluation criteria.
- README.md: This documentation file.
- requirements.txt: List of dependencies required for the project.
- src/: Source code directory.
  - __init__.py: Initialization file for the `src` package.
  - main.py: Main script to run the evaluation and select the best model.
  - frameworks/: Directory containing different evaluation frameworks.
    - custom_metrics.py: Framework for evaluating models using custom metrics.
    - deepeval_metrics.py: Framework for evaluating models using DeepEval metrics.
    - integration_tracker.py: Framework for integrating and summarizing results from different evaluations.
    - performance_tracker.py: Framework for tracking and analyzing performance metrics.
- tests/: Directory containing unit tests.
  - __init__.py: Initialization file for the `tests` package.
  - test_custom_metrics.py: Unit tests for the custom metrics framework.
  - test_deepeval_metrics.py: Unit tests for the DeepEval metrics framework.
  - test_integration_tracker.py: Unit tests for the integration tracker framework.
  - test_performance_tracker.py: Unit tests for the performance tracker framework.

## How It Works

### Configuration

The configuration file `config/config.json` contains details about the models to be evaluated and the criteria for evaluation. This file is loaded at the beginning of the evaluation process.

### Evaluation Frameworks

1. Custom Metrics Framework (`custom_metrics.py`):
   - Purpose: Evaluates models based on custom-defined metrics.
   - Functionality:
     - Model Evaluation: Evaluates models on various benchmark datasets (e.g., MMLU, HellaSwag, TruthfulQA, HumanEval, custom benchmarks).
     - Performance Metrics: Calculates performance scores, cost per 1k tokens, average latency, and other metrics.
     - Score Calculation: Provides methods to calculate a final score for each model based on weighted performance, cost, latency, and feature scores.
     - Recommendations: Generates recommendations for model selection based on trade-offs between performance, cost, and latency.

2. DeepEval Metrics Framework (`deepeval_metrics.py`):
   - Purpose: Uses the DeepEval library to evaluate models.
   - Functionality:
     - Metric Initialization: Initializes various metrics such as hallucination, relevancy, contextual precision, contextual recall, faithfulness, bias, toxicity, and RAGAS.
     - Model Evaluation: Evaluates models using the DeepEval library and the initialized metrics.
     - Continuous Evaluation: Supports continuous evaluation at specified intervals, logging results and analyzing trends.
     - Report Generation: Generates comprehensive evaluation reports, including summaries, detailed results, historical trends, and recommendations.

3. Integration Tracker (`integration_tracker.py`):
   - Purpose: Integrates results from different evaluation frameworks.
   - Functionality:
     - Comprehensive Testing: Runs comprehensive tests across base models, RAG implementations, prompt variations, and integration scenarios.
     - Result Aggregation: Aggregates results from different tests and frameworks.
     - Summary Generation: Generates summaries of results, including best-performing combinations, performance metrics, cost analysis, and latency analysis.
     - Recommendations: Provides recommendations based on the aggregated results and trade-offs between performance, cost, and latency.

4. Performance Tracker (`performance_tracker.py`):
   - Purpose: Tracks and analyzes performance metrics.
   - Functionality:
     - Request Tracking: Tracks individual requests, including model used, tokens consumed, latency, cost, and success rate.
     - Cost Analysis: Analyzes costs over specified periods, including total cost, cost by model, cost trends, and cost projections.
     - Resource Optimization: Provides methods to optimize resource allocation based on current usage and performance metrics.
     - Threshold Checking: Checks cost and performance thresholds, triggering alerts if thresholds are exceeded.


### Main Script

The main script (`main.py`) orchestrates the entire evaluation process:

1. Load Configuration: Reads the configuration file to get model details and evaluation criteria.
2. Initialize Testers: Initializes instances of the evaluation frameworks.
3. Run Evaluations: Runs evaluations using both the custom metrics and DeepEval frameworks.
4. Combine Results: Combines results from both frameworks.
5. Calculate Scores: Calculates a final score for each model based on the combined results.
6. Select Best Model: Selects the best model based on the highest score.
7. Save Best Model: Saves the name of the best model to a file for deployment.

### Continuous Integration

The CI pipeline (`.github/workflows/ci.yml`) ensures that the project passes all tests before deployment:

1. Checkout Code: Checks out the code from the repository.
2. Set Up Python: Sets up the Python environment.
3. Install Dependencies: Installs the required dependencies.
4. Run Tests: Runs the unit tests to ensure the code is working correctly.
5. Select and Save Best Model: Runs the main script to select and save the best model.
6. Deploy: Deploys the application using the best model if all tests pass.

## Running the Project

1. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

2. Run the Main Script
   ```sh
   python src/main.py
   ```

3. Run Tests
   ```sh
   python -m unittest discover -s tests
   ```

## License
This project is licensed under the MIT License.