import requests
import logging
from logging import config
import logging_config
import ua_generator

# logging.basicConfig(filename='logs.log',
#                     level=logging.INFO,
#                     filemode='w',
#                     format='{asctime} {levelname} {message}',
#                     style='{')

config.dictConfig(logging_config.LOGGING)

logger = logging.getLogger(__name__)

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
        logger.error('The request timed out')
    except requests.exceptions.RequestException as e:
        logger.error(f'An error occured: {e}')
        exit()
