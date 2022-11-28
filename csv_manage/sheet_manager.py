import pandas as pd


class SheetManager:

    def __init__(self):
        self.csv = pd.read_csv('data/sheets/weather.csv', index_col=0, delimiter=';', encoding='Windows-1251')
        self.df = pd.DataFrame(self.csv)

    def get_value(self, row_value: int, col_value: int):
        value = self.df.loc[row_value][col_value]
        if isinstance(value, float):
            return False
        return value
