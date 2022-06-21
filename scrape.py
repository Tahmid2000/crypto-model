import requests
from bs4 import BeautifulSoup
from pprint import pprint
from openpyxl import Workbook


def getRows():
    rows = html.select('.cmc-table-row')
    data = []
    for row in rows[0:20]:
        name = row.select(
            ".cmc-table__cell--sort-by__name")[0].get_text()
        ticker = row.select(
            ".cmc-table__cell--sort-by__symbol")[0].get_text()
        price = row.select(
            ".cmc-table__cell--sort-by__price")[0].get_text()
        data.append({'name': name, 'ticker': ticker, 'price': price})
        print(f'({ticker}) price: {price}')
    return data


def dataToExcel(data, date):

    sheet['A1'] = 'name'
    sheet['B1'] = 'ticker'
    sheet['C1'] = 'price'
    count = 2
    for d in data:
        sheet[f'A{count}'] = d['name']
        sheet[f'B{count}'] = d['ticker']
        sheet[f'C{count}'] = d['price']
        count += 1
        print(d)
    workbook.save(filename=f'{date}.xlsx')


if __name__ == "__main__":
    date = input("Please enter a date in the format yyyymmdd: ")
    url = f'https://coinmarketcap.com/historical/{date}/'
    data = requests.get(url)
    html = BeautifulSoup(data.text, 'html.parser')
    workbook = Workbook()
    sheet = workbook.active
    dataToExcel(getRows(), date)
