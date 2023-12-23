from modules import scraper
from modules import converter
from modules import call
from modules import url
from modules import export
from urllib.parse import urljoin
import pandas as pd
import os

camera_brands = {
    "1. Canon":
        "https://in-commerce.ru/zapchasty/dlya-zerkalnyh-fotoapparatov/canon-komplectuyuschie.html",
    "2. Nikon":
        "https://in-commerce.ru/zapchasty/dlya-zerkalnyh-fotoapparatov/nikon-komplectuyuschie.html",
    "3. Sony":
        "https://in-commerce.ru/zapchasty/dlya-zerkalnyh-fotoapparatov/sony-komplectuyuschie.html",
    "4. Panasonic, Samsung, Olympus, Pentax, Fujifilm":
        "https://in-commerce.ru/zapchasty/dlya-zerkalnyh-fotoapparatov/spare-parts-pana-penta-fuji.html"
}

url.show_camera_brand_list(camera_brands)

brand_number = url.get_brand_number()

page_url = url.get_page_url(camera_brands, brand_number)

while True:
    response = call.response(page_url)

    data = scraper.get_data(response)

    item_list = scraper.get_items(data)

    item_data = converter.get_item_data(item_list)

    next_page_url = scraper.get_next_page(data)

    if next_page_url:
        page_url = urljoin(page_url, next_page_url)
    else:
        if not os.path.isdir('./export'):
            os.makedirs('./export')
        format_number = export.choose_format()
        export.export(item_data, format_number)
        break
