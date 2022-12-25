import requests
from bs4 import BeautifulSoup as bs
url1 = 'https://pogoda.mail.ru/prognoz/'
print('Введите латиницей город, для которого будем смотреть погоду')
#moskva, noyabrsk
city = input()
url = url1 + city
print(url)

response = requests.get(url).text
#print(response)
soup = bs(response, 'html.parser')
weather = soup.find('div', class_="information__content__temperature")
print(weather.text)