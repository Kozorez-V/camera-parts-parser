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

# get url

url.show_camera_brand_list(camera_brands)

brand_number = url.get_brand_number()

page_url = url.get_page_url(camera_brands, brand_number)

# parse the data

while True:

    # get response
    response = call.response(page_url)

    # scrape the web page
    data = scraper.get_data(response)
    item_list = scraper.get_items(data)

    # convert the data to DataFrame
    item_data = converter.get_item_data(item_list)

    # go to the next page
    next_page_url = scraper.get_next_page(data)

    if next_page_url:
        page_url = urljoin(page_url, next_page_url)
    else:
        # check if a folder exist; if not, then create it
        if not os.path.isdir('./export'):
            os.makedirs('./export')

        # choose the file format
        format_number = export.choose_format()
        result_check_format_number = export.check_format_number(format_number)
        export.show_result_check_format_number(result_check_format_number, format_number)

        # get file name
        file_name = export.get_file_name()
        export.check_file_name(file_name)

        # export
        export.export(item_data, format_number, file_name)
        break
