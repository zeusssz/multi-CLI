import argparse
import shutil
import os
import datetime
import schedule
import time

def backup_files(source, destination):
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    backup_name = f"backup_{timestamp}.zip"
    shutil.make_archive(os.path.join(destination, backup_name), 'zip', source)
    print(f"Backup created: {backup_name}")

def job(source, destination):
    backup_files(source, destination)

def main():
    parser = argparse.ArgumentParser(description="Backup files or directories.")
    parser.add_argument('source', type=str, help='Source directory or file to backup')
    parser.add_argument('destination', type=str, help='Destination directory to store backup')
    parser.add_argument('--schedule', type=str, help='Backup schedule in the format of a cron-like string (e.g., "daily", "hourly")')
    args = parser.parse_args()

    if args.schedule:
        if args.schedule == 'daily':
            schedule.every().day.at("00:00").do(job, args.source, args.destination)
        elif args.schedule == 'hourly':
            schedule.every().hour.do(job, args.source, args.destination)
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        backup_files(args.source, args.destination)

if __name__ == "__main__":
    main()
