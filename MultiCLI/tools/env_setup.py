import argparse
import subprocess
import os

def setup_environment(requirements_file, env_vars_file=None):
    print("Installing Python dependencies...")
    subprocess.check_call(['pip', 'install', '-r', requirements_file])
    
    if env_vars_file:
        with open(env_vars_file, 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                os.environ[key] = value
                print(f"Set environment variable: {key}")

    print("Environment setup complete.")

def main():
    parser = argparse.ArgumentParser(description="Setup development environment.")
    parser.add_argument('requirements_file', type=str, help='Path to the requirements.txt file')
    parser.add_argument('--env-vars-file', type=str, help='Path to the environment variables file (key=value format)')
    args = parser.parse_args()

    setup_environment(args.requirements_file, args.env_vars_file)

if __name__ == "__main__":
    main()
