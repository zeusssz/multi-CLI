# 🖥 📁 MultiCLI

MultiCLI is a versatile command-line interface (CLI) tool designed to perform various functions. This project includes multiple tools for tasks such as log analysis, file renaming, API data fetching, system monitoring, backup utilities, environment setup, and data conversion.
<br>
![image](https://github.com/user-attachments/assets/7187bd7e-5c22-404e-b737-5f62214325f8)


## Features

- **Log Analyzer**: Analyze and search through log files.
- **File Renamer**: Rename files with customizable options.
- **API Data Fetcher**: Fetch and process data from APIs.
- **System Monitor**: Monitor system resources and export stats.
- **Backup Utility**: Backup files or directories with optional scheduling.
- **Environment Setup**: Setup a development environment with dependencies and environment variables.
- **Data Converter**: Convert data between different formats (e.g., CSV to JSON).

## Installation

To install MultiCLI, you can download the wheel file from the [releases](https://github.com/zeusssz/multi-CLI/releases) page and install it using pip.
(Or compile the binary directly by using the source code, and running `python setup.py bdist_wheel`)

1. **Download the wheel file** from the [Releases page](https://github.com/zeusssz/multi-CLI/releases/latest/download/multicli-1.0-py3-none-any.whl).

2. **Install the wheel file** using pip:

   ```bash
   pip install path/to/multicli-1.0-py3-none-any.whl
   ```

## Usage

After installation, you can use the `multicli` command to execute various tasks. Here are the available commands:

### Analyze Logs

Analyze log files for specific patterns.

```bash
multicli analyze --file example.log --pattern "error" [--start-date YYYY-MM-DD] [--end-date YYYY-MM-DD]
```

- `--file`: Path to the log file.
- `--pattern`: Pattern to search for in log lines.
- `--start-date` (optional): Start date for filtering (YYYY-MM-DD).
- `--end-date` (optional): End date for filtering (YYYY-MM-DD).

### Rename Files

Rename files in a directory with various options.

```bash
multicli rename --directory /path/to/files [--prefix PREFIX] [--suffix SUFFIX] [--numbering] [--extension EXT] [--preview]
```

- `--directory`: Directory containing files to rename.
- `--prefix` (optional): Prefix to add to file names.
- `--suffix` (optional): Suffix to add to file names.
- `--numbering` (optional): Add numbering to file names.
- `--extension` (optional): File extension to rename (e.g., `.txt`).
- `--preview` (optional): Preview changes without renaming.

### Fetch API Data

Fetch data from an API endpoint.

```bash
multicli fetch --endpoint URL [--params PARAMS] [--method METHOD] [--data DATA] [--auth AUTH] [--pretty]
```

- `--endpoint`: API endpoint URL.
- `--params` (optional): Query parameters in key=value format (comma-separated).
- `--method` (optional): HTTP method (GET or POST, default is GET).
- `--data` (optional): Data to send with POST requests (JSON format).
- `--auth` (optional): Authentication credentials in username:password format.
- `--pretty` (optional): Pretty print JSON output.

### Monitor System

Monitor system resources and export stats.

```bash
multicli monitor [--export FILE] [--interval SECONDS]
```

- `--export` (optional): File to export stats.
- `--interval` (optional): Interval in seconds between updates (default is 5).

### Backup Files

Backup files or directories with optional scheduling.

```bash
multicli backup --source /path/to/source --destination /path/to/destination [--schedule SCHEDULE]
```

- `--source`: Source directory or file to backup.
- `--destination`: Destination directory to store the backup.
- `--schedule` (optional): Backup schedule in a cron-like format (e.g., "daily", "hourly").

### Setup Environment

Setup development environment with dependencies and environment variables.

```bash
multicli setup --requirements-file path/to/requirements.txt [--env-vars-file path/to/env_vars_file]
```

- `--requirements-file`: Path to the `requirements.txt` file.
- `--env-vars-file` (optional): Path to the environment variables file (key=value format).

### Convert Data

Convert data between different formats.

```bash
multicli convert --input-file path/to/input_file --output-file path/to/output_file --format FORMAT
```

- `--input-file`: Input file path.
- `--output-file`: Output file path.
- `--format`: Conversion format (e.g., `csv-to-json`, `json-to-csv`).

## Development

If you wish to contribute or modify MultiCLI, clone the repository and install dependencies:

```bash
git clone https://github.com/zeusssz/multi-CLI.git
cd multi-CLI
pip install -e .
```

## Contact

For any questions or issues, please contact [@roboxer_](https://discord.com/users/roboxer_).
