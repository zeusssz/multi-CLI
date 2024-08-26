import argparse
import os

def preview_changes(directory, prefix='', suffix='', extension=None):
    files = [f for f in os.listdir(directory) if not extension or f.endswith(extension)]
    for index, filename in enumerate(files):
        name, ext = os.path.splitext(filename)
        new_name = f"{prefix}{name}{suffix}{ext}"
        print(f"{filename} -> {new_name}")

def rename_files(directory, prefix='', suffix='', numbering=False, extension=None):
    files = [f for f in os.listdir(directory) if not extension or f.endswith(extension)]
    for index, filename in enumerate(files):
        name, ext = os.path.splitext(filename)
        new_name = f"{prefix}{name}{suffix}{ext}"
        if numbering:
            new_name = f"{prefix}{index + 1}{suffix}{ext}"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
        print(f"Renamed {filename} to {new_name}")

def main():
    parser = argparse.ArgumentParser(description="Rename files in a directory.")
    parser.add_argument('directory', type=str, help='Directory containing files to rename')
    parser.add_argument('--prefix', type=str, default='', help='Prefix to add to file names')
    parser.add_argument('--suffix', type=str, default='', help='Suffix to add to file names')
    parser.add_argument('--numbering', action='store_true', help='Add numbering to file names')
    parser.add_argument('--extension', type=str, help='File extension to rename (e.g., .txt)')
    parser.add_argument('--preview', action='store_true', help='Preview changes without renaming')
    args = parser.parse_args()

    if args.preview:
        preview_changes(args.directory, args.prefix, args.suffix, args.extension)
    else:
        rename_files(args.directory, args.prefix, args.suffix, args.numbering, args.extension)

if __name__ == "__main__":
    main()
