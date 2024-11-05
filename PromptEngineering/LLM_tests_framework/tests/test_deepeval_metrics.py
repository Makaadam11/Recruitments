import unittest
from src.frameworks.deepeval_metrics import DeepEvalMetrics
import json

class TestDeepEvalMetrics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('config/config.json', 'r') as file:
            cls.config = json.load(file)
        cls.framework = DeepEvalMetrics(config_path='config/config.json')

    def test_initialize_metrics(self):
        self.framework.initialize_metrics()
        self.assertIn('hallucination', self.framework.metrics)
        self.assertIn('relevancy', self.framework.metrics)

    def test_run_full_evaluation(self):
        results = self.framework.run_full_evaluation()
        self.assertIsInstance(results, dict)
        for model_name in self.config['models']:
            self.assertIn(model_name, results)

    def test_generate_report(self):
        report = self.framework.generate_report()
        self.assertIsInstance(report, dict)
        self.assertIn('timestamp', report)

    def test_evaluate_model_all_metrics(self):
        for model_name, model_config in self.config['models'].items():
            results = self.framework.evaluate_model_all_metrics(model_name, model_config)
            self.assertIsInstance(results, dict)
            for metric in self.framework.metrics.keys():
                self.assertIn(metric, results)

if __name__ == '__main__':
    unittest.main()