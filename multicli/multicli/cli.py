import argparse
from multicli import log_analyzer, bulk_renamer, api_data_fetcher, system_monitor, backup_utility, env_setup, data_converter

def main():
    parser = argparse.ArgumentParser(prog='multicli', description='MultiCLI: A multi-purpose command-line tool.')
    subparsers = parser.add_subparsers(dest='command', help='Sub-command help')

    # Log Analyzer Command
    parser_analyze = subparsers.add_parser('analyze_log', help='Analyze log files')
    parser_analyze.add_argument('--file', type=str, required=True, help='Log file to analyze')

    # File Renamer Command
    parser_rename = subparsers.add_parser('rename_files', help='Rename files in a directory')
    parser_rename.add_argument('directory', type=str, help='Directory containing files to rename')
    parser_rename.add_argument('--prefix', type=str, default='', help='Prefix to add to file names')
    parser_rename.add_argument('--suffix', type=str, default='', help='Suffix to add to file names')

    # API Data Fetcher Command
    parser_fetch = subparsers.add_parser('fetch_api', help='Fetch data from an API')
    parser_fetch.add_argument('url', type=str, help='URL of the API to fetch data from')

    # System Monitor Command
    parser_monitor = subparsers.add_parser('monitor_system', help='Monitor system resources')

    # Backup Utility Command
    parser_backup = subparsers.add_parser('backup', help='Backup files or directories')
    parser_backup.add_argument('source', type=str, help='Source directory to backup')
    parser_backup.add_argument('destination', type=str, help='Destination for the backup')

    # Environment Setup Command
    parser_setup = subparsers.add_parser('setup_env', help='Set up the development environment')
    parser_setup.add_argument('config_file', type=str, help='Configuration file for the environment setup')

    # Data Converter Command
    parser_convert = subparsers.add_parser('convert_data', help='Convert data between formats')
    parser_convert.add_argument('input_file', type=str, help='Input file path')
    parser_convert.add_argument('output_file', type=str, help='Output file path')
    parser_convert.add_argument('--format', type=str, choices=['json', 'csv', 'xml'], help='Output format')

    args = parser.parse_args()

    if args.command == 'analyze_log':
        log_analyzer.analyze(args.file)
    elif args.command == 'rename_files':
        bulk_renamer.rename(args.directory, args.prefix, args.suffix)
    elif args.command == 'fetch_api':
        api_data_fetcher.fetch(args.url)
    elif args.command == 'monitor_system':
        system_monitor.monitor()
    elif args.command == 'backup':
        backup_utility.backup(args.source, args.destination)
    elif args.command == 'setup_env':
        env_setup.setup(args.config_file)
    elif args.command == 'convert_data':
        data_converter.convert(args.input_file, args.output_file, args.format)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()