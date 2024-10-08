import argparse
import requests
import json
# TODO : FIX
def fetch_data(endpoint, params=None, method='GET', data=None, auth=None, pretty=False):
    if method == 'POST':
        response = requests.post(endpoint, params=params, json=data, auth=auth)
    else:
        response = requests.get(endpoint, params=params, auth=auth)
    
    if response.status_code == 200:
        data = response.json()
        if pretty:
            print(json.dumps(data, indent=4))
        else:
            print(data)
    else:
        print(f"Error {response.status_code}: {response.text}")

def main():
    parser = argparse.ArgumentParser(description="Fetch data from an API.")
    parser.add_argument('endpoint', type=str, help='API endpoint URL')
    parser.add_argument('--params', type=str, help='Query parameters in key=value format (comma-separated)')
    parser.add_argument('--method', type=str, choices=['GET', 'POST'], default='GET', help='HTTP method')
    parser.add_argument('--data', type=str, help='Data to send with POST requests (JSON format)')
    parser.add_argument('--auth', type=str, help='Authentication credentials in username:password format')
    parser.add_argument('--pretty', action='store_true', help='Pretty print JSON output')
    args = parser.parse_args()

    params = dict(param.split('=') for param in args.params.split(',')) if args.params else None
    data = json.loads(args.data) if args.data else None
    auth = tuple(args.auth.split(':')) if args.auth else None

    fetch_data(args.endpoint, params, args.method, data, auth, args.pretty)

if __name__ == "__main__":
    main()
