import psutil
import time
from datetime import datetime
from tabulate import tabulate

class SmartGuard:
    def __init__(self):
        self.start_time = datetime.now()

    def get_cpu_usage(self):
        return psutil.cpu_percent(interval=1)

    def get_memory_usage(self):
        memory_info = psutil.virtual_memory()
        return memory_info.percent

    def get_disk_usage(self):
        disk_info = psutil.disk_usage('/')
        return disk_info.percent

    def get_network_io(self):
        net_io = psutil.net_io_counters()
        return net_io.bytes_sent, net_io.bytes_recv

    def display_system_usage(self):
        print("\n=== System Usage Statistics ===")
        print(f"Time Running: {datetime.now() - self.start_time}")
        print(tabulate([
            ["CPU Usage (%)", self.get_cpu_usage()],
            ["Memory Usage (%)", self.get_memory_usage()],
            ["Disk Usage (%)", self.get_disk_usage()],
            ["Network Sent (bytes)", self.get_network_io()[0]],
            ["Network Received (bytes)", self.get_network_io()[1]]
        ], headers=["Metric", "Value"]))

    def run(self):
        print("SmartGuard is now running. Press Ctrl+C to stop.")
        try:
            while True:
                self.display_system_usage()
                time.sleep(5)
        except KeyboardInterrupt:
            print("\nSmartGuard stopped.")

if __name__ == '__main__':
    guard = SmartGuard()
    guard.run()