import requests
from bs4 import BeautifulSoup
import csv

URL = "http://ufcstats.com/fight-details/636fd144716a3084"
FILENAME = 'sample.csv'

result = requests.get(URL)
doc = BeautifulSoup(result.text, "html.parser")
table = doc.find_all('table')
totals = table[0]
sig_strike = table[2]

# Grabbing headers / data for both tables within page
total_headers_all = totals.find_all('th')
total_rows = totals.find_all('p')
sig_headers_all = sig_strike.find_all('th')
sig_rows = sig_strike.find_all('p')

# Cleaning the data up
total_header = []
total_data = []


for th in total_headers_all:
    total_header.append(th.get_text().strip())
for td in total_rows:
    total_data.append(td.get_text().strip())
for th in sig_headers_all:
    total_header.append(th.get_text().strip())
for td in sig_rows:
    total_data.append(td.get_text().strip())


def alt_array(input_array):
    result_array = []
    second_result_array = []
    for i in range(len(input_array)):
        if i % 2 == 0:
            result_array.append(input_array[i])
        else:
            second_result_array.append(input_array[i])
    return result_array, second_result_array


final_total_data, final_total_data2 = alt_array(total_data)

all_data = [total_header, final_total_data, final_total_data2]



with open(FILENAME, 'a') as f:
    writer = csv.writer(f)
    writer.writerows(all_data)

