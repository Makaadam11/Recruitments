from typing import Dict, List
import pandas as pd
from datetime import datetime, timedelta

class PerformanceTracker:
    def __init__(self):
        self.usage_data = pd.DataFrame(columns=['timestamp', 'model', 'tokens_used', 'latency_ms', 'cost', 'success'])
        self.cost_thresholds = self._load_cost_thresholds()
        self.performance_targets = self._load_performance_targets()
        
    def track_request(self, request_data: Dict):
        """Track a single request"""
        self.usage_data = self.usage_data.append({
            'timestamp': datetime.now(),
            'model': request_data['model'],
            'tokens_used': request_data['tokens'],
            'latency_ms': request_data['latency'],
            'cost': self._calculate_cost(request_data),
            'success': request_data['success']
        }, ignore_index=True)
        
        self._check_thresholds()
    
    def analyze_costs(self, period: str = 'day') -> Dict:
        """Analyze costs over a given period"""
        grouped = self.usage_data.groupby(
            pd.Grouper(key='timestamp', freq=period)
        )
        
        return {
            'total_cost': grouped['cost'].sum(),
            'cost_by_model': self._analyze_cost_by_model(grouped),
            'cost_trends': self._analyze_cost_trends(grouped),
            'cost_projections': self._project_costs(grouped)
        }
    
    def optimize_resource_allocation(self) -> Dict:
        """Optimize resource allocation"""
        current_usage = self._analyze_current_usage()
        performance_metrics = self._calculate_performance_metrics()
        
        return {
            'recommendations': self._generate_optimization_recommendations(
                current_usage, performance_metrics
            ),
            'expected_savings': self._calculate_potential_savings(),
            'performance_impact': self._estimate_performance_impact()
        }
    
    def _check_thresholds(self):
        """Check cost and performance thresholds"""
        recent_data = self.usage_data.tail(1000)  # Last 1000 requests
        
        cost_rate = recent_data['cost'].sum() / len(recent_data)
        avg_latency = recent_data['latency_ms'].mean()
        success_rate = recent_data['success'].mean()
        
        if cost_rate > self.cost_thresholds['cost_per_request']:
            self._trigger_cost_alert(cost_rate)
        
        if avg_latency > self.performance_targets['max_latency']:
            self._trigger_performance_alert(avg_latency)
        
        if success_rate < self.performance_targets['min_success_rate']:
            self._trigger_reliability_alert(success_rate)
    
    def _project_costs(self, grouped) -> Dict:
        """Project future costs"""
        historical_trend = self._calculate_historical_trend(grouped)
        
        return {
            'next_day': self._project_for_period(historical_trend, 'day'),
            'next_week': self._project_for_period(historical_trend, 'week'),
            'next_month': self._project_for_period(historical_trend, 'month'),
            'confidence_intervals': self._calculate_confidence_intervals()
        }

    def _calculate_cost(self, request_data: Dict) -> float:
        """Calculate cost of a request"""
        return request_data['tokens'] * 0.01  # Example cost calculation

    def _load_cost_thresholds(self) -> Dict:
        """Load cost thresholds"""
        return {
            'cost_per_request': 1.0  # Example threshold
        }

    def _load_performance_targets(self) -> Dict:
        """Load performance targets"""
        return {
            'max_latency': 500,  # Example target in ms
            'min_success_rate': 0.95  # Example success rate
        }

    def _analyze_cost_by_model(self, grouped) -> Dict:
        """Analyze cost by model"""
        return grouped['cost'].sum().to_dict()

    def _analyze_cost_trends(self, grouped) -> Dict:
        """Analyze cost trends"""
        return grouped['cost'].mean().to_dict()

    def _analyze_current_usage(self) -> Dict:
        """Analyze current usage"""
        return self.usage_data.groupby('model').sum().to_dict()

    def _calculate_performance_metrics(self) -> Dict:
        """Calculate performance metrics"""
        return {
            'avg_latency': self.usage_data['latency_ms'].mean(),
            'success_rate': self.usage_data['success'].mean()
        }

    def _generate_optimization_recommendations(self, current_usage: Dict, performance_metrics: Dict) -> List[str]:
        """Generate optimization recommendations"""
        return ['Optimize model usage based on cost and performance']

    def _calculate_potential_savings(self) -> float:
        """Calculate potential savings"""
        return 100.0  # Example savings calculation

    def _estimate_performance_impact(self) -> Dict:
        """Estimate performance impact"""
        return {
            'latency_impact': -10,  # Example impact in ms
            'success_rate_impact': 0.01  # Example impact in success rate
        }

    def _trigger_cost_alert(self, cost_rate: float):
        """Trigger cost alert"""
        print(f"Cost alert: {cost_rate}")

    def _trigger_performance_alert(self, avg_latency: float):
        """Trigger performance alert"""
        print(f"Performance alert: {avg_latency}")

    def _trigger_reliability_alert(self, success_rate: float):
        """Trigger reliability alert"""
        print(f"Reliability alert: {success_rate}")

    def _calculate_historical_trend(self, grouped) -> Dict:
        """Calculate historical trend"""
        return grouped['cost'].mean().to_dict()

    def _project_for_period(self, historical_trend: Dict, period: str) -> float:
        """Project cost for a period"""
        return historical_trend.get(period, 0.0)

    def _calculate_confidence_intervals(self) -> Dict:
        """Calculate confidence intervals"""
        return {
            'lower': 0.9,
            'upper': 1.1
        }