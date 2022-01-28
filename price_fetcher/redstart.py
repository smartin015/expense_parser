import requests
from bs4 import BeautifulSoup

def redstartQuery(typ):
    resp = requests.get("https://redstartroasters.com/shop/%s/" % typ)
    soup = BeautifulSoup(resp.text, 'html.parser')
    return (soup.select("#main h1")[0].get_text(), float(soup.select("p.price")[0].get_text().replace("$", "")))

def all_queries():
    return [redstartQuery("espresso-finca-buena-vista")]

if __name__ == "__main__":
    print(all_queries())
