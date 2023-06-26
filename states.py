from aiogram.dispatcher.filters.state import State, StatesGroup


class DownloadExel(StatesGroup):
    download_exel = State()
    dollar_exchange_rate = State()


class FindProduct(StatesGroup):
    find_product = State()
