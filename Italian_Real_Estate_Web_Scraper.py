from bs4 import BeautifulSoup
import requests
import datetime
import csv


def check_price():
    URL = 'https://www.immobiliare.it/affitto-stanze/trieste/?criterio=prezzo&ordine=asc&gclid=CjwKCAjwtuOlBhBREiwA7agf1rcqnSXEi5oqKPF2pGZntommzrmljxB_KlTI2o-2vsNIY3dZc_a2uxoCX8UQAvD_BwE'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    all_ads = soup2.find_all(class_='in-card__title')
    all_prices = soup2.find_all(class_='in-realEstateListCard__priceOnTop')
    
    #List every ad and every price
    ads = []
    prices = []
    
    today = datetime.date.today()

    for ad in all_ads:
        ads.append(ad.get_text())

    for price in all_prices:
        prices.append(price.get_text())
    
    header = ['Title', 'Price', 'Last Update']

    #-----Rewriting the ads and prices obtained-----
    with open('ImmobiliareWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for i in range(len(ads)):
            data = [ads[i].strip(), prices[i].strip(), today]
            writer.writerow(data)


    
    
    


