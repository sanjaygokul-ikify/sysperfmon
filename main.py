import psutil
import pandas as pd
import numpy as np
from src.core import SystemPerformanceMonitor

if __name__ == '__main__':
    monitor = SystemPerformanceMonitor()
    monitor.run()