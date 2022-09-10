import requests
import bs4

def getTrendyolprice(producturl):
    res = requests.get(producturl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#product-detail-app > div > div.flex-container > div.product-container > div:nth-child(2) > div.container-right-content > div.pr-in-w > div > div > div.product-price-container > div > div > span')
    return elems[0].text.strip()





price = getTrendyolprice('https://www.trendyol.com/anisah-coffee/bolivar-espresso-kavrulmus-cekirdek-kahve-1000-g-p-38807877?boutiqueId=611090&merchantId=155873')
print('The price is ' + price)
