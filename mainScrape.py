from bs4 import BeautifulSoup
import requests

# printing html source code from secform4.com in a BS4 instance
html_text = requests.get('https://www.secform4.com/insider-trading/1494730.htm').text
soup = BeautifulSoup(html_text, 'lxml')
transaction_date = soup.find_all('td', class_='transactionHead')
shares_traded = soup.find_all('td', class_='sTraded')
average_price = soup.find_all('td', class_='priceHead')
total_amount = soup.find_all('td', class_='headAmt')

company = soup.find_all_next('td', class_='company')
insider_relationship = soup.find_all_next('td', class_='irTxt')

data_element = soup.find_all('tb', class_='card')

'''
for data in data_element:
    data_int = data.a.text
    data_str = data.td.text
'''

# print(data_str, data_str)
print(transaction_date, shares_traded, average_price, total_amount)
