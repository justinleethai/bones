import requests
from bs4 import BeautifulSoup

url = "http://ufcstats.com/fight-details/c5e0e4ee11903076"
output_filename = ''

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
table = doc.find_all('table')
totals = table[0]
sigstrike = table[2]

table_headers = totals.find_all('th')
table_rows = totals.find_all('p')

totalheader = []
totaldata = []
sigdata = []

for th in table_headers:
    totalheader.append(th.get_text().strip())

for td in table_rows:
    totaldata.append(td.get_text().strip())

#print(totaldata)

def alt_array(input_array):
    result_array = []
    second_result_array = []
    for i in range(len(input_array)):
        if i % 2 == 0:
            result_array.append(input_array[i])
        else:
            second_result_array.append(input_array[i])
    return result_array, second_result_array


finaltotaldata, finaltotaldata2 = alt_array(totaldata)


print(totalheader)
print(finaltotaldata)
print(finaltotaldata2)



