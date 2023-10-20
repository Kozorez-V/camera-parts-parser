from modules import scraper
from modules import converter
from modules import call
from urllib.parse import urljoin
import pandas as pd

url = "https://in-commerce.ru/zapchasty/dlya-zerkalnyh-fotoapparatov/canon-komplectuyuschie.html?start=0"

while True:
    response = call.response(url)

    data = scraper.get_data(response)

    item_list = scraper.get_items(data)

    item_data = converter.get_item_data(item_list)

    next_page_url = scraper.get_next_page(data)

    if next_page_url:
        url = urljoin(url, next_page_url)
    else:
        item_data.to_csv('./camera_parts.csv', index=False)
        item_data.to_excel('./camera_parts.xlsx', index=False)
        break