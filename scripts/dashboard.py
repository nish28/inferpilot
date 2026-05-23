import requests

BASE_URL = 'http://localhost:8000'


def main():
    response = requests.get(f'{BASE_URL}/v1/usage', timeout=30)
    print(response.json())


if __name__ == '__main__':
    main()
