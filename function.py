async def get_products(listbook: any = None, text: str = None) -> dict:
    """
    Description: This function returns the entire "products" string of the Excel file as a dictionary.
        Эта функция возвращает всю строку "значений" Excel-файла в виде словаря.

    Example: dict -> {row_1: [column_1, column_2, column_3, ...]}

    :param listbook:
    :param text:
    :return:
    """
    dict_row: dict = {}
    list_value: list = []
    max_row: int = listbook.max_row
    max_column: int = listbook.max_column

    for i in range(1, max_row + 1):
        for j in range(1, max_column + 1):
            text_value = str(listbook.cell(row=i, column=j).value).lower()
            if text_value.find(text.lower()) >= 0:
                for col in range(1, max_column + 1):
                    if col == max_column:
                        dict_row[i] = list_value
                    list_value.append(listbook.cell(row=i, column=col).value)
            list_value = []
    return dict_row


async def get_categories(listbook: any = None) -> list:
    """
    Description: This function returns the entire "categories" start_row of the Excel file as a list.
        Эта функция возвращает всю строку "категорий" Excel-файла в виде списка.

    Example: list -> [column_1, column_2, column_3, ...]

    :param listbook:
    :return:
    """
    list_category: list = []
    start_row: int = 5

    for i in range(1, listbook.max_column + 1):
        list_category.append(listbook.cell(row=start_row, column=i).value)
    return list_category


async def get_profits(listbook: any = None) -> dict:
    """
    Description: This function returns a dictionary of vendors with product markups.
        Эта функция возвращает словарь поставщиков с наценками.

    Example: dict -> {"Поставщик": [10, 15, 20, 25], ...}

    :param listbook:
    :return:
    """
    list_profit: list = []
    dict_profit: dict = {}
    start_row: int = 11

    for i in range(start_row, listbook.max_row + 1):
        for j in range(1, listbook.max_column + 1):
            list_profit.append(listbook.cell(row=i, column=j).value)
            dict_profit[list_profit[0]] = [x for x in list_profit if isinstance(x, int)]
        list_profit = []
    return dict_profit


async def get_minimal_price(providers: dict = None, profits: dict = None) -> int:
    """
    Description: This function returns the minimum price of markup suppliers.
        Эта функция возвращает минимальную цену поставщиков с наценкой.

    Example: int -> 235

    :param providers:
    :param profits:
    :return:
    """
    minimal_price_list: list = []

    for name1, price in providers.items():
        for name2, profit in profits.items():
            if bool(price) and name1 == name2:
                total: int = 0
                if price <= 200:
                    total += price + profit[0]
                elif 200 < price <= 400:
                    total += price + profit[1]
                elif 400 < price < 700:
                    total += price + profit[2]
                elif price >= 700:
                    total += price + profit[3]
                minimal_price_list.append(total)
    minimal_price: int = min(minimal_price_list) if bool(minimal_price_list) else 0
    return minimal_price
