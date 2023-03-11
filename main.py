import requests
from bs4 import BeautifulSoup
import csv

url = "http://ufcstats.com/fight-details/636fd144716a3084"
file_name = 'sample.csv'

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
table = doc.find_all('table')
totals = table[0]
sigstrike = table[2]

total_headers_all = totals.find_all('th')
total_rows = totals.find_all('p')

sig_headers_all = sigstrike.find_all('th')
sig_rows = sigstrike.find_all('p')

total_header = []
total_data = []
sig_header = []
sig_data = []

for th in total_headers_all:
    total_header.append(th.get_text().strip())

for td in total_rows:
    total_data.append(td.get_text().strip())

for th in sig_headers_all:
    sig_header.append(th.get_text().strip())

for td in sig_rows:
    sig_data.append(td.get_text().strip())


def alt_array(input_array):
    result_array = []
    second_result_array = []
    for i in range(len(input_array)):
        if i % 2 == 0:
            result_array.append(input_array[i])
        else:
            second_result_array.append(input_array[i])
    return result_array, second_result_array


finaltotaldata, finaltotaldata2 = alt_array(total_data)

final_sig_data, final_sig_data2 = alt_array(sig_data)


print(total_header)
print(finaltotaldata)
print(finaltotaldata2)

print(sig_header)
print(final_sig_data)
print(final_sig_data2)

