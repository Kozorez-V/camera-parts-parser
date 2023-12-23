def choose_format():
    format_number = int(input("Please, select a format to export the data by entering its number:"
                              "\n1. CSV"
                              "\n2. XLSX"
                              "\n3. Both\n"))

    return format_number


def export(item_data, format_number):
    if format_number == 1:
        item_data.to_csv('./export/data.csv', index=False)
    if format_number == 2:
        item_data.to_excel('./export/data.xlsx', index=False)
    else:
        item_data.to_csv('./export/data.csv', index=False)
        item_data.to_excel('./export/data.xlsx', index=False)

    print("The data has been successfully exported")
