import requests
from bs4 import BeautifulSoup

def winespiritsQuery(sku):
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 14150.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.114 Safari/537.36',
    }

    params = (
    ('catalogId', '10051'),
    ('storeId', '10051'),
    ('productId', sku),
    )

    response = requests.get('https://www.finewineandgoodspirits.com/webapp/wcs/stores/servlet/ProductDisplay', headers=headers, params=params)
    soup = BeautifulSoup(response.text, 'html.parser') 
    price = soup.select(".productPrice")[0].get_text().replace("$", "")
    return (soup.select("#name_ga")[0]['value'], float(price.strip().split("\n")[0]))

def all_queries():
    return [winespiritsQuery(sku) for sku in [
            "1947430",
            "1950762"
            ]]

if __name__ == "__main__":
        print(all_queries())
