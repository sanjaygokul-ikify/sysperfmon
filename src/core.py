import psutil
import pandas as pd
import numpy as np

class SystemPerformanceMonitor:
    def __init__(self):
        self.metrics = {}

    def run(self):
        # Collect system metrics
        self.metrics['cpu_usage'] = psutil.cpu_percent()
        self.metrics['memory_usage'] = psutil.virtual_memory().percent
        # Analyze metrics and provide recommendations
        recommendations = self.analyze_metrics()
        # Optimize system performance
        self.optimize_performance(recommendations)

    def analyze_metrics(self):
        # Analyze metrics and provide recommendations
        recommendations = {}
        if self.metrics['cpu_usage'] > 80:
            recommendations['cpu'] = 'Reduce CPU usage'
        if self.metrics['memory_usage'] > 80:
            recommendations['memory'] = 'Reduce memory usage'
        return recommendations

    def optimize_performance(self, recommendations):
        # Optimize system performance based on recommendations
        for resource, recommendation in recommendations.items():
            if resource == 'cpu':
                # Reduce CPU usage
                print('Reducing CPU usage')
            elif resource == 'memory':
                # Reduce memory usage
                print('Reducing memory usage')