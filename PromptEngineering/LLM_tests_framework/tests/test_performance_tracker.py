import unittest
from src.frameworks.performance_tracker import PerformanceTracker
from datetime import datetime

class TestPerformanceTracker(unittest.TestCase):
    def setUp(self):
        self.framework = PerformanceTracker()

    def test_track_request(self):
        """Test tracking a single request"""
        request_data = {
            'model': 'test_model',
            'tokens': 100,
            'latency': 200,
            'success': True
        }
        self.framework.track_request(request_data)
        self.assertEqual(len(self.framework.usage_data), 1)
        self.assertEqual(self.framework.usage_data.iloc[0]['model'], 'test_model')

    def test_analyze_costs(self):
        """Test analyzing costs over a given period"""
        # Add some dummy data
        for i in range(10):
            self.framework.track_request({
                'model': 'test_model',
                'tokens': 100,
                'latency': 200,
                'success': True
            })
        costs = self.framework.analyze_costs('day')
        self.assertIn('total_cost', costs)
        self.assertIn('cost_by_model', costs)
        self.assertIn('cost_trends', costs)
        self.assertIn('cost_projections', costs)

    def test_optimize_resource_allocation(self):
        """Test optimizing resource allocation"""
        # Add some dummy data
        for i in range(10):
            self.framework.track_request({
                'model': 'test_model',
                'tokens': 100,
                'latency': 200,
                'success': True
            })
        optimization = self.framework.optimize_resource_allocation()
        self.assertIn('recommendations', optimization)
        self.assertIn('expected_savings', optimization)
        self.assertIn('performance_impact', optimization)

    def test_check_thresholds(self):
        """Test checking cost and performance thresholds"""
        # Add some dummy data
        for i in range(1000):
            self.framework.track_request({
                'model': 'test_model',
                'tokens': 100,
                'latency': 200,
                'success': True
            })
        self.framework._check_thresholds()
        # Assuming the thresholds are set, you can add assertions here

if __name__ == '__main__':
    unittest.main()