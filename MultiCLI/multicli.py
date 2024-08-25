import argparse
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'tools')))

# Import tools modules
from tools import log_analyzer, bulk_renamer, api_data_fetcher, system_monitor, backup_utility, env_setup, data_converter  # type: ignore

def main():
    parser = argparse.ArgumentParser(description="Multicli: A multi-functional CLI tool.")
    subparsers = parser.add_subparsers(dest='command')
    
    # Log Analyzer
    log_parser = subparsers.add_parser('analyze', help='Analyze log files')
    log_parser.add_argument('file', type=str, help='Path to the log file')
    log_parser.add_argument('--pattern', type=str, help='Pattern to search for in log lines')
    log_parser.add_argument('--start-date', type=str, help='Start date for filtering (YYYY-MM-DD)')
    log_parser.add_argument('--end-date', type=str, help='End date for filtering (YYYY-MM-DD)')
    
    # File Renamer
    rename_parser = subparsers.add_parser('rename', help='Rename files in a directory')
    rename_parser.add_argument('directory', type=str, help='Directory containing files to rename')
    rename_parser.add_argument('--prefix', type=str, default='', help='Prefix to add to file names')
    rename_parser.add_argument('--suffix', type=str, default='', help='Suffix to add to file names')
    rename_parser.add_argument('--numbering', action='store_true', help='Add numbering to file names')
    rename_parser.add_argument('--extension', type=str, help='File extension to rename (e.g., .txt)')
    rename_parser.add_argument('--preview', action='store_true', help='Preview changes without renaming')
    
    # API Data Fetcher
    api_parser = subparsers.add_parser('fetch', help='Fetch data from an API')
    api_parser.add_argument('endpoint', type=str, help='API endpoint URL')
    api_parser.add_argument('--params', type=str, help='Query parameters in key=value format (comma-separated)')
    api_parser.add_argument('--method', type=str, choices=['GET', 'POST'], default='GET', help='HTTP method')
    api_parser.add_argument('--data', type=str, help='Data to send with POST requests (JSON format)')
    api_parser.add_argument('--auth', type=str, help='Authentication credentials in username:password format')
    api_parser.add_argument('--pretty', action='store_true', help='Pretty print JSON output')
    
    # System Monitor
    system_parser = subparsers.add_parser('monitor', help='Monitor system resources')
    system_parser.add_argument('--export', type=str, help='File to export stats')
    system_parser.add_argument('--interval', type=int, default=5, help='Interval in seconds between updates')
    
    # Backup Utility
    backup_parser = subparsers.add_parser('backup', help='Backup files or directories')
    backup_parser.add_argument('source', type=str, help='Source directory or file to backup')
    backup_parser.add_argument('destination', type=str, help='Destination directory to store backup')
    backup_parser.add_argument('--schedule', type=str, help='Backup schedule in the format of a cron-like string (e.g., "daily", "hourly")')
    
    # Data Converter
    data_parser = subparsers.add_parser('convert', help='Convert between different data formats')
    data_parser.add_argument('input_file', type=str, help='Input file path')
    data_parser.add_argument('output_file', type=str, help='Output file path')
    data_parser.add_argument('--format', type=str, choices=['csv-to-json', 'json-to-csv'], required=True, help='Conversion format')
    
    # Environment Setup
    env_parser = subparsers.add_parser('setup', help='Setup development environment')
    env_parser.add_argument('requirements_file', type=str, help='Path to the requirements.txt file')
    env_parser.add_argument('--env-vars-file', type=str, help='Path to the environment variables file (key=value format)')
    
    args = parser.parse_args()
    
    if args.command == 'analyze':
        log_analyzer.analyze_log(args.file, args.pattern, args.start_date, args.end_date)
    elif args.command == 'rename':
        if args.preview:
            bulk_renamer.preview_changes(args.directory, args.prefix, args.suffix, args.extension)
        else:
            bulk_renamer.rename_files(args.directory, args.prefix, args.suffix, args.numbering, args.extension)
    elif args.command == 'fetch':
        api_data_fetcher.fetch_data(args.endpoint, args.params, args.method, args.data, args.auth, args.pretty)
    elif args.command == 'monitor':
        system_monitor.display_system_info(args.export, args.interval)
    elif args.command == 'backup':
        if args.schedule:
            backup_utility.schedule_backup(args.source, args.destination, args.schedule)
        else:
            backup_utility.backup_files(args.source, args.destination)
    elif args.command == 'setup':
        env_setup.setup_environment(args.requirements_file, args.env_vars_file)
    elif args.command == 'convert':
        if args.format == 'csv-to-json':
            data_converter.convert_csv_to_json(args.input_file, args.output_file)
        elif args.format == 'json-to-csv':
            data_converter.convert_json_to_csv(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
