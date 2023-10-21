from bs4 import BeautifulSoup


def get_data(response):
    return BeautifulSoup(response.text, 'html.parser')


def get_items(data):
    return data.find_all("div", class_='spacer panel panel-default product-container')


def get_next_page(data):
    try:
        next_page = data.find('a', {'title': 'Вперёд'})['href']
        return next_page
    except TypeError:
        return False
