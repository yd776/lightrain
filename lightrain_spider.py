from bs4 import BeautifulSoup
import requests
import pyshorteners

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3029.110 Safari/537.3'}

source = requests.get('https://www.amazon.in/s?k=grocery&dc&crid=1LI9XOOBAFX0&sprefix=grocer%2Caps%2C273&ref=a9_sc_1', headers = headers).text
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

for i in range(len(records)):
    print('name :' + records[i][0])
    print('url :' + records[i][1])
    print('price :' + records[i][2])
    print('rating :' + records[i][3])
    print('review_count :' + records[i][4])
    print(" ")
 
ur_l = 'https://www.amazon.in/Lifelong-LLBC1401-%E2%80%8ETraining-Mudguard-Assembled/dp/B0976WNS2V/ref=sr_1_1_sspa?keywords=cycle&qid=1641710519&sprefix=cyc%2Caps%2C340&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExMUpNWERYM0g5VkVRJmVuY3J5cHRlZElkPUEwOTUyODk5SkFZRVYzNUZWMlBUJmVuY3J5cHRlZEFkSWQ9QTAzMDU4OTQzQ0NJQUYxSlE1SjdZJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

def get_more_infor(url):
    source_1 = requests.get(url, headers = headers).text
    soup_1 = BeautifulSoup(source_1, 'lxml')
    results_0 = soup_1.find_all('td', {'class':'a-span3'})
    results_1 = soup_1.find_all('td', {'class':'a-span9'})

    for i in range(len(results_0)):
        print(results_0[i].text + ':' + results_1[i].text)


#get_more_infor(ur_l)