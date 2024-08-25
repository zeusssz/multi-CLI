import argparse
import psutil
import time

def display_system_info(export_file=None, interval=5):
    while True:
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        network_stats = psutil.net_if_stats()

        info = (
            f"CPU Usage: {cpu_usage}%\n"
            f"Memory Usage: {memory_usage}%\n"
            f"Disk Usage: {disk_usage}%\n"
            f"Network Stats: {network_stats}\n"
        )
        
        print(info)
        if export_file:
            with open(export_file, 'a') as file:
                file.write(info + '\n')

        time.sleep(interval)

def main():
    parser = argparse.ArgumentParser(description="Monitor system resources.")
    parser.add_argument('--export', type=str, help='File to export stats')
    parser.add_argument('--interval', type=int, default=5, help='Interval in seconds between updates')
    args = parser.parse_args()

    display_system_info(args.export, args.interval)

if __name__ == "__main__":
    main()
