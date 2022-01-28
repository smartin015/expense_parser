import requests
from bs4 import BeautifulSoup

def onlineMetalsQuery():
    headers = {
            'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 14150.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.114 Safari/537.36',
                
            }
    resp = requests.get("https://www.onlinemetals.com/en/buy/aluminum/1-aluminum-round-bar-6061-t6511-extruded/pid/1090", headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    return (soup.select("h1")[0].get_text().strip(), float(soup.select("span.price")[0].get_text().replace("$","")))

def all_queries():
    return [onlineMetalsQuery()]

if __name__ == "__main__":
    print(all_queries())
