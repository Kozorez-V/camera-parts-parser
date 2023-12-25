import os


def choose_format():
    format_number = int(input("Please, select a format to export the data by entering its number:"
                              "\n1. CSV"
                              "\n2. XLSX"
                              "\n3. Both\n"))

    return format_number


def check_format_number(format_number):
    if format_number == 1 or format_number == 2 or format_number == 3:
        return True

    return False


def show_result_check_format_number(result_check_format_number, format_number):
    if result_check_format_number is True:
        print(f"You choosed {format_number}")
    else:
        print("This choise doesn't exist. Please, try again.")
        exit()


def get_file_name():
    file_name = str(input("Please, enter the file name: "))

    return file_name


def check_file_name(file_name):
    if file_name.isspace():
        print("The file name is empty.")
        exit()
    if os.path.exists(f"./export/{file_name}.csv") or os.path.exists(f"./export/{file_name}.xlsx"):
        print("The file with that name already exists.")
        exit()


def export(item_data, format_number, file_name):
    if format_number == 1:
        item_data.to_csv(f"./export/{file_name}.csv", index=False)
    if format_number == 2:
        item_data.to_excel(f"./export/{file_name}.xlsx", index=False)
    if format_number == 3:
        item_data.to_csv(f"./export/{file_name}.csv", index=False)
        item_data.to_excel(f"./export/{file_name}.xlsx", index=False)

    print("The data has been successfully exported")
