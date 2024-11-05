import unittest
import asyncio
from src.frameworks.integration_tracker import IntegrationTracker, TestConfig
from src.frameworks.deepeval_metrics import DeepEvalMetrics
from src.frameworks.custom_metrics import CustomMetrics, ModelMetrics
from src.frameworks.performance_tracker import PerformanceTracker

class TestIntegrationTracker(unittest.TestCase):
    def setUp(self):
        self.config = TestConfig(
            model_configs={
                'test_model': {
                    'max_context_length': 2048,
                    'features': ['feature1', 'feature2'],
                    'license': 'open',
                    'hosting': ['cloud', 'on-prem']
                }
            },
            rag_configs={},
            prompt_templates={},
            test_scenarios=[]
        )
        self.tracker = IntegrationTracker(self.config)
        self.deepeval_framework = DeepEvalMetrics(config_path='config/config.json')
        self.custom_framework = CustomMetrics()
        self.performance_tracker = PerformanceTracker()

    def test_combined_evaluation(self):
        deepeval_results = self.deepeval_framework.run_full_evaluation()
        custom_metrics = self.custom_framework.evaluate_model('test_model', {
            'max_context_length': 2048,
            'features': ['feature1', 'feature2'],
            'license': 'open',
            'hosting': ['cloud', 'on-prem']
        })
        self.assertIsInstance(deepeval_results, dict)
        self.assertIsInstance(custom_metrics, dict)

    def test_run_comprehensive_tests(self):
        results = asyncio.run(self.tracker.run_comprehensive_tests())
        self.assertIn('base_models', results)
        self.assertIn('rag_implementations', results)
        self.assertIn('prompt_variations', results)
        self.assertIn('integration_scenarios', results)

if __name__ == '__main__':
    unittest.main()