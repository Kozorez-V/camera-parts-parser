def show_camera_brand_list(camera_brands):
    for brand in camera_brands.keys():
        print(brand)


def get_brand_number():
    brand_number = int(input("Please, select a brand by entering its number: "))

    return brand_number


def get_page_url(camera_brands, brand_number):
    for brand, url in camera_brands.items():
        if str(brand_number) == brand[:1]:
            return url
