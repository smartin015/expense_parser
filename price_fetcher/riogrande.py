import requests
from bs4 import BeautifulSoup

def riograndeQuery():
    headers = {
            'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 14150.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.114 Safari/537.36',
                
            }
    resp = requests.get("https://www.riogrande.com/", headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    silver = soup.select("body > div.container-fluid > header > nav > div:nth-child(1) > div > div:nth-child(1) > div.col-xs-4.col-sm-8.col-sm-pull-0.col-sm-10.col-md-pull-6.col-md-6.text-sm-right.text-md-left.text-lg-left.metal-markets-block.hidden-xs.hidden-print > a > span:nth-child(1)")[0]
    return (silver.find("strong").get_text().strip(), float(silver.select("span")[-1].get_text().replace("$","")))

def all_queries():
    return [riograndeQuery()]

if __name__ == "__main__":
    print(all_queries())
