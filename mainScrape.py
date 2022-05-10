from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.secform4.com/insider-trading/1494730.htm')
print(html_text)
