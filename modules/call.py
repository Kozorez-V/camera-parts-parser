import requests
import ua_generator

user_agent = ua_generator.generate()

headers = {
    'Accept': 'text/hmtl',
    'User-Agent': str(user_agent)
}


def response(url):
    try:
        session = requests.Session()
        response = session.get(url=url, headers=headers, timeout=5)
        response.raise_for_status()
        return response
    except requests.exceptions.Timeout:
        print('The request timed out')
    except requests.exceptions.RequestException as e:
        print(f'An error occured: {e}')
        exit()
