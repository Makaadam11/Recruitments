from frameworks.deepeval_metrics import DeepEvalMetrics
from frameworks.custom_metrics import CustomMetrics
from frameworks.integration_tracker import IntegrationTracker
from frameworks.performance_tracker import PerformanceTracker
import json

# Load configuration
config_path = 'config/config.json'
with open(config_path, 'r') as file:
    config = json.load(file)

# Initialize testers
deepeval_tester = DeepEvalMetrics(config_path)
custom_metrics_tester = CustomMetrics(config_path)
integration_tracker = IntegrationTracker(config)
performance_tracker = PerformanceTracker(config)

# Run evaluations
deepeval_results = deepeval_tester.run_full_evaluation()
custom_metrics_results = {
    model_name: custom_metrics_tester.evaluate_model(model_name, model_config)
    for model_name, model_config in config['models'].items()
}

# Combine results
combined_results = {**deepeval_results, **custom_metrics_results}

# Calculate scores for each model
model_scores = {
    model_name: custom_metrics_tester.calculate_model_score(metrics)
    for model_name, metrics in combined_results.items()
}

# Select the best model
best_model = max(model_scores.items(), key=lambda x: x[1])[0]

print(f"The best model is: {best_model}")

# Save the best model to a file for deployment
with open('best_model.txt', 'w') as file:
    file.write(best_model)