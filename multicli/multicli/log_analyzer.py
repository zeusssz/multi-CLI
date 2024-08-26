import argparse
import re
from datetime import datetime

def analyze_log(file_path, pattern=None, start_date=None, end_date=None):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if pattern:
        pattern = re.compile(pattern)
        lines = [line for line in lines if pattern.search(line)]

    if start_date or end_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d') if start_date else None
        end_date = datetime.strptime(end_date, '%Y-%m-%d') if end_date else None
        lines = [line for line in lines if filter_by_date(line, start_date, end_date)]

    print(f"Total lines: {len(lines)}")
    for line in lines:
        print(line, end='')

def filter_by_date(line, start_date, end_date):
    date_str = line.split(' ')[0]  # please be the first part of the line
    line_date = datetime.strptime(date_str, '%Y-%m-%d')
    if start_date and line_date < start_date:
        return False
    if end_date and line_date > end_date:
        return False
    return True

def main():
    parser = argparse.ArgumentParser(description="Analyze log files.")
    parser.add_argument('file', type=str, help='Path to the log file')
    parser.add_argument('--pattern', type=str, help='Pattern to search for in log lines')
    parser.add_argument('--start-date', type=str, help='Start date for filtering (YYYY-MM-DD)')
    parser.add_argument('--end-date', type=str, help='End date for filtering (YYYY-MM-DD)')
    args = parser.parse_args()

    analyze_log(args.file, args.pattern, args.start_date, args.end_date)

if __name__ == "__main__":
    main()
