import argparse
import csv
import json

def convert_csv_to_json(csv_file, json_file):
    with open(csv_file, mode='r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    with open(json_file, mode='w') as f:
        json.dump(rows, f, indent=4)
    print(f"CSV converted to JSON: {json_file}")

def convert_json_to_csv(json_file, csv_file):
    with open(json_file, mode='r') as f:
        data = json.load(f)
    
    with open(csv_file, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"JSON converted to CSV: {csv_file}")

def main():
    parser = argparse.ArgumentParser(description="Convert between different data formats.")
    parser.add_argument('input_file', type=str, help='Input file path')
    parser.add_argument('output_file', type=str, help='Output file path')
    parser.add_argument('--format', type=str, choices=['csv-to-json', 'json-to-csv'], required=True, help='Conversion format')
    args = parser.parse_args()

    if args.format == 'csv-to-json':
        convert_csv_to_json(args.input_file, args.output_file)
    elif args.format == 'json-to-csv':
        convert_json_to_csv(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
