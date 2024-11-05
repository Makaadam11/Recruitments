import unittest
from src.frameworks.custom_metrics_framework import CustomMetrics, ModelMetrics
import json

class TestCustomMetrics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('config/config.json', 'r') as file:
            cls.config = json.load(file)
        cls.framework = CustomMetrics(config_path='config/config.json')

    def test_evaluate_model(self):
        for model_name, model_config in self.config['models'].items():
            metrics = self.framework.evaluate_model(model_name, model_config)
            self.assertIsInstance(metrics, ModelMetrics)
            self.assertIn('mmlu', metrics.performance_scores)

    def test_calculate_model_score(self):
        metrics = ModelMetrics(
            name='test_model',
            performance_scores={'mmlu': 0.8, 'hellaswag': 0.7},
            cost_per_1k_tokens=0.02,
            avg_latency_ms=100,
            max_context_length=2048,
            supported_features=['feature1', 'feature2'],
            license_type='open',
            hosting_options=['cloud', 'on-prem']
        )
        score = self.framework.calculate_model_score(metrics)
        self.assertIsInstance(score, float)

    def test_generate_recommendation(self):
        recommendation = self.framework.generate_recommendation()
        self.assertIsInstance(recommendation, dict)
        self.assertIn('recommended_model', recommendation)

if __name__ == '__main__':
    unittest.main()