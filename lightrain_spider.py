from bs4 import BeautifulSoup
import requests
import pyshorteners

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3029.110 Safari/537.3'}

source = requests.get('https://www.amazon.in/s?k=laptops&crid=1AMUSK00JZMXU&sprefix=laptop%2Caps%2C239&ref=nb_sb_noss', headers = headers).text
soup = BeautifulSoup(source, 'lxml')

results = soup.find_all('div', {'data-component-type':'s-search-result'})
records = []

s = pyshorteners.Shortener().tinyurl


def get_info(items):
    atag=items.h2.a
    name=atag.text.strip()
    url = s.short("https://www.amazon.in"+atag.get('href'))
    
    try:
        price_parent = items.find('span', 'a-offscreen').text
    except AttributeError:
        return

    try:
        rating = items.i.text
        review_count = items.find('span', {'class': 'a-size-base'}).text
    except AttributeError:
        rating = ''
        review_count = ''

    result = (name,url,price_parent,rating,review_count)

    return result


for item in results:
    record = get_info(item)
    if record:
        records.append(record)

def get_more_infor(url):
    source_1 = requests.get(url, headers = headers).text
    soup_1 = BeautifulSoup(source_1, 'lxml')
    results_0 = soup_1.find_all('td', {'class':'a-span3'})
    results_1 = soup_1.find_all('td', {'class':'a-span9'})

    for i in range(len(results_0)):
        print(results_0[i].text + ':' + results_1[i].text)


for i in range(len(records)):
    print('name :' + records[i][0])
    print('url :' + records[i][1])
    print('price :' + records[i][2])
    print('rating :' + records[i][3])
    print('review_count :' + records[i][4])
    print(' ')
    get_more_infor(records[i][1])
    print(" ")
 
