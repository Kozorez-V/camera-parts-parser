import requests
import logging
import ua_generator

logging.basicConfig(filename="error.log", level=logging.ERROR)

user_agent = ua_generator.generate()

headers = {
    "Accept": "text/hmtl",
    "User-Agent": str(user_agent)
}


def response(url):
    try:
        session = requests.Session()
        response = session.get(url=url, headers=headers, timeout=5)
        response.raise_for_status()
        return response
    except requests.exceptions.Timeout:
        logging.error("The request timed out")
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occured: {e}")
        exit()
