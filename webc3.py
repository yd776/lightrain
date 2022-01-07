import requests
from bs4 import BeautifulSoup


def trade_spider():
    url='https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=9d0e9da7-4bfb-42d7-b0f8-215e468153b4&as-backfill=on'
    source_code=requests.get(url)
    plain_text=source_code.text
    soup=BeautifulSoup(plain_text ,features="html.parser")
    #heading_tags = [""]

    print("List of objects:")

    for link in soup.findAll('div', {'class':'_4rR01T'}):
        print(link.text.strip())
        print(" ")

    print("Respective links:")

    for link in soup.findAll('a', {'class':'_1fQZEK'}):
        href='https://www.flipkart.com'+link.get('href')
        #print(link.text.strip())
        print(href)
        print(" ")



trade_spider()