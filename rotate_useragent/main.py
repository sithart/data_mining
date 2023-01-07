from urllib.error import URLError


# Reference URL
# https://medium.com/geekculture/rotate-ip-address-and-user-agent-to-scrape-data-a010216c8d0c

import itertools
from openpyxl import Workbook


things = [
    {
        "Fruit": "Orange",
        "Flavour": "Good",
        "Expiration": "21May20"
    },
    {
        "Fruit": "Apple",
        "Flavour": "Good",
        "Junk": "Spam",
        "Expiration": "19May20"
    },
    {
        "Fruit": "Banana",
        "Flavour": "Regular",
        "Expiration": "16May20"
    }
]

def write_xls(filename, data):
    wb = Workbook(write_only=True)
    ws = wb.create_sheet()

    headers = list(set(itertools.chain.from_iterable(data)))
    ws.append(headers)

    for elements in data:
        ws.append([elements.get(h) for h in headers])

    wb.save(filename)

import uuid
filename = str(uuid.uuid4()) + '.xlsx'
print("File Name :", filename)
write_xls(filename, things)
