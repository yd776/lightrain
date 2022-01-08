from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3029.110 Safari/537.3'}

source = requests.get('https://www.amazon.in/s?k=iphone&crid=1PU805VI4PBGB&sprefix=iphone%2Caps%2C240&ref=nb_sb_noss', headers = headers).text
soup = BeautifulSoup(source, 'lxml')

#print(soup.prettify())

Names = []
Prices = []
Rating = []
Links = []

for i in soup.find_all('span', {'class':'a-size-medium a-color-base a-text-normal'}):
    string=i.text
    Names.append(string.strip())

for j in soup.find_all('span', {'class':'a-price-whole'}):
    Prices.append(j.text)

for k in soup.find_all('span', {'class':'a-icon-alt'}):
    Rating.append(k.text)

for l in soup.find_all('a', {'class':'a-link-normal s-link-style a-text-normal'}):
    Links.append(l.get('href'))

for each in Names:
    print(each)

for every in Prices:
    print(every)

for stars in Rating:
    print(stars)

for link in Links:
    print("https://www.amazon.in"+link)

