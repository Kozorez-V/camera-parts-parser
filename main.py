from modules import scraper
from modules import converter
from modules import call
from urllib.parse import urljoin
import pandas as pd
import os

url = "https://in-commerce.ru/zapchasty/dlya-zerkalnyh-fotoapparatov/canon-komplectuyuschie.html"

while True:
    response = call.response(url)

    data = scraper.get_data(response)

    item_list = scraper.get_items(data)

    item_data = converter.get_item_data(item_list)

    next_page_url = scraper.get_next_page(data)

    if next_page_url:
        url = urljoin(url, next_page_url)
    else:
        if not os.path.isdir('./export'):
            os.makedirs('./export')
        item_data.to_csv('./export/camera_parts.csv', index=False)
        item_data.to_excel('./export/camera_parts.xlsx', index=False)
        break