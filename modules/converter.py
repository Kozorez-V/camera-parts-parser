from bs4 import BeautifulSoup
import re
import pandas as pd

item_data = pd.DataFrame({
    "Название": [],
    "Стоимость": [],
    "Наличие": []
})


def get_item_data(item_list):
    for item in item_list:
        try:
            product_name = item.find(class_="product-name b1c-name").text
            price = item.find(class_="PricesalesPrice").text
            stock = item.find("span", class_=re.compile("stock")).text
            item_data.loc[len(item_data.index)] = [product_name, price, stock]
        except AttributeError:
            print("Ошибка")
            exit()

    return item_data
