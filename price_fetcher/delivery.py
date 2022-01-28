import requests
from bs4 import BeautifulSoup

def peoplesIndianQuery():
    resp = requests.get("https://www.beyondmenu.com/29721/pittsburgh/people-s-indian-restaurant-pittsburgh-15224.aspx")
    soup = BeautifulSoup(resp.text, 'html.parser')
    pmasala = soup.find("a", {"data-item-id": "33083324"})
    return (pmasala.select(".menu-item-link-itemname")[0].get_text().strip(), float(pmasala.select(".menu-item-link-price")[0].get_text().replace("$","")))

def mtEverestSushiQuery():
    resp = requests.get("https://www.mteverestsushi.com/order/main/standard-maki-roll-hand-roll/california-roll")
    soup = BeautifulSoup(resp.text, 'html.parser')
    return (soup.select("#item_name")[0].get_text().strip(), float(soup.select("td.price")[0].get_text().replace("$","")))

def ramenBarQuery():
    resp = requests.get("http://ramenbarpittsburgh.com/menu/")
    soup = BeautifulSoup(resp.text, 'html.parser')

    for item in soup.select("table p"):
        if item.get_text().startswith("Ajo"):
            return (item.find("strong").get_text().strip(),float(list(item.children)[2]))

def all_queries():
    return [
            peoplesIndianQuery(),
            mtEverestSushiQuery(),
            ramenBarQuery()
            ]

if __name__ == "__main__":
    print(all_queries())
