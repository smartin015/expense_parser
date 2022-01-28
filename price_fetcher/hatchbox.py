import requests
from bs4 import BeautifulSoup

def hatchboxQuery():
    headers = {
            'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 14150.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.114 Safari/537.36',
                
            }
    resp = requests.get("https://www.hatchbox3d.com/collections/pla-1-75mm/products/3d-pla-1kg1-75-blk", headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    return (soup.select("h1.product-single__title")[0].get_text().strip(), float(soup.select(".product__price")[0].get_text().replace("$","")))

def all_queries():
    return [hatchboxQuery()]

if __name__ == "__main__":
    print(all_queries())
