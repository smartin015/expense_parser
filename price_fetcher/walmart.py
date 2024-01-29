import requests
import sys
from bs4 import BeautifulSoup

def walmartQuery():
    headers = {
        'authority': 'www.walmart.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Chrome OS"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 14150.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.114 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.google.com/',
        'accept-language': 'en-US,en;q=0.9',
        # 'cookie': 'AID=wmlspartner%253D0%253Areflectorid%253D0000000000000000000000%253Alastupd%253D1637963081999; auth=MTAyOTYyMDE4equ%2Fa25otSHvvLZ3JQpkKc7ywF73LUY7tN7p5kRgWDeej8R4Io4i5bjBz0qO6i%2F0SeUWLwT3RUXRtBdtr5LjXzKNqwXykYecAV7o5gTWvpNb77X5jEsdemq9jtgXp3Il767wuZloTfhm7Wk2Kcjygv3M5Jnvc7ePkiG6%2BkglNABRFx0CyoqEAVojEbCUpiznMJ2k%2Fi8bMeVpYWV2lGWYFKdoi9Zo64uTQzyYsQfmB7IUMk70P8glgOEpLOprhDfMywI05adPtwc9%2Fm5r1ONHR6SnEQhsHZ79pMSVgpkedpbbNsTi9I83zz4sCePzFJi0Zyjrl3Xn%2FHqu6RsaPeBV2lTXnRiOIsl2xUmZl17oUaBZA6c9R81JHzoTHwr%2BLnirCR0NZ3BHZKeydlMdPjplQkjyrOXbKKhH072NS%2FW0j%2FU%3D; ACID=e863612b-847c-4d1e-b46c-2049b7151a4f; hasACID=true; locDataV3=eyJpbnRlbnQiOiJTSElQUElORyIsInBpY2t1cCI6W3siYnVJZCI6IjAiLCJub2RlSWQiOiIxNzkwIiwiZGlzcGxheU5hbWUiOiJNb25yb2UgU3VwZXJjZW50ZXIiLCJub2RlVHlwZSI6IlNUT1JFIiwiYWRkcmVzcyI6eyJwb3N0YWxDb2RlIjoiNDgxNjIiLCJhZGRyZXNzTGluZTEiOiIyMTUwIE4gVGVsZWdyYXBoIFJkIiwiY2l0eSI6Ik1vbnJvZSIsInN0YXRlIjoiTUkiLCJjb3VudHJ5IjoiVVMiLCJwb3N0YWxDb2RlOSI6IjQ4MTYyLTg5MDEifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjQxLjk1MTYyNywibG9uZ2l0dWRlIjotODMuMzk1ODI0fSwiaXNHbGFzc0VuYWJsZWQiOnRydWUsInNjaGVkdWxlZEVuYWJsZWQiOnRydWUsInVuU2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZX1dLCJkZWxpdmVyeSI6eyJidUlkIjoiMCIsIm5vZGVJZCI6IjE3OTAiLCJkaXNwbGF5TmFtZSI6Ik1vbnJvZSBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiI0ODE2MiIsImFkZHJlc3NMaW5lMSI6IjIxNTAgTiBUZWxlZ3JhcGggUmQiLCJjaXR5IjoiTW9ucm9lIiwic3RhdGUiOiJNSSIsImNvdW50cnkiOiJVUyIsInBvc3RhbENvZGU5IjoiNDgxNjItODkwMSJ9LCJnZW9Qb2ludCI6eyJsYXRpdHVkZSI6NDEuOTUxNjI3LCJsb25naXR1ZGUiOi04My4zOTU4MjR9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJhY2Nlc3NQb2ludHMiOlt7ImFjY2Vzc1R5cGUiOiJERUxJVkVSWV9BRERSRVNTIn1dfSwic2hpcHBpbmdBZGRyZXNzIjp7ImxhdGl0dWRlIjo0MS45NDIyLCJsb25naXR1ZGUiOi04My4zOSwicG9zdGFsQ29kZSI6IjQ4MTYyIiwiY2l0eSI6Ik1vbnJvZSIsInN0YXRlIjoiTUkiLCJjb3VudHJ5Q29kZSI6IlVTQSIsImdpZnRBZGRyZXNzIjpmYWxzZX0sImFzc29ydG1lbnQiOnsibm9kZUlkIjoiMTc5MCIsImRpc3BsYXlOYW1lIjoiTW9ucm9lIFN1cGVyY2VudGVyIiwiYWNjZXNzUG9pbnRzIjpudWxsLCJpbnRlbnQiOiJQSUNLVVAiLCJzY2hlZHVsZUVuYWJsZWQiOmZhbHNlfSwiaW5zdG9yZSI6ZmFsc2UsInJlZnJlc2hBdCI6MTYzNzk4NDY4MjA2NiwidmFsaWRhdGVLZXkiOiJwcm9kOnYyOmU4NjM2MTJiLTg0N2MtNGQxZS1iNDZjLTIwNDliNzE1MWE0ZiJ9; assortmentStoreId=1790; hasLocData=1; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsInN0b3JlSW50ZW50IjoiUElDS1VQIiwibWVyZ2VGbGFnIjpmYWxzZSwicGlja3VwIjp7Im5vZGVJZCI6IjE3OTAiLCJ0aW1lc3RhbXAiOjE2Mzc5NjMwODIwNTh9LCJwb3N0YWxDb2RlIjp7InRpbWVzdGFtcCI6MTYzNzk2MzA4MjA1OCwiYmFzZSI6IjQ4MTYyIn0sInZhbGlkYXRlS2V5IjoicHJvZDp2MjplODYzNjEyYi04NDdjLTRkMWUtYjQ2Yy0yMDQ5YjcxNTFhNGYifQ%3D%3D; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; TB_SFOU-100=; TB_DC_Flap_Test=1; vtc=bS0ZbNvCgl69joI86GOZDI; bstc=bS0ZbNvCgl69joI86GOZDI; mobileweb=0; xpa=; xpm=3%2B1637963081%2BbS0ZbNvCgl69joI86GOZDI~%2B0; _pxhd=2lxnrQT5oN/eFHSd3dY9DkrZH1hNNXbZPK0ncr1pHUEMiz2rLqyLCT5rmuvVdIpkMn3aOFag/l5zBJjLcC4flQ==:HGFbdEBzwLShFGIFZwVO2P2J4-oOa2yt/Z6RLVAh-szuR1a3TZv5tvCUrXAnA8fo-SX12fWozU6aa5wASGVAcE9Z0T4bbKKXsKK7eTYNnMM=; TBWL-94-glassItemSRL=cg01gbvzd3b3:0:2ryt4rdhzg3fy:1m8zapz4sp798; TS01b0be75=01538efd7c82b76d5ea3a9c4edb1544117d339c8a5d9e47fbee943ef45b70184112d48b2c00bbbaccdcb8ed70e21ac24059001e0de; TS013ed49a=01538efd7c82b76d5ea3a9c4edb1544117d339c8a5d9e47fbee943ef45b70184112d48b2c00bbbaccdcb8ed70e21ac24059001e0de; akavpau_p2=1637963682~id=ae23b30a4727da279109980770207e7a; ak_bmsc=25E990EA9AB199D1BFD3CDA554073C3C~000000000000000000000000000000~YAAQpNbOF4G2vSV9AQAARCs1Xg1bqSex548xi8bcCtN+KVIhguY2vYLHp0mUE42KR2pFU/dKmQdmt7E4U7vsb3kQS+RdbPbe9lZGgoJBBvqPfXUecAaMuw1CBeXkn5ry/oHa8VVZZOFDoB6SJftCg+WGnMggqEm629Qten461BrYPgSJsJAVPeAuyW3RVGcvnWppHaT5+pMzRoWyq2N+a12gIStR1cV4q6BBlNLCEIXUokEf/R1QCkz6XfRgbiG762h9p83a+4juAHueUjsh0e9vFzfjuA64v17H/3tUFhnrPT6IfkL2VS+cpppfSCpb38A828rj2A2xSxXAbNusWRQv41aosiQwzjZCoVFhnoykFXBjj4q3fOQwMzqE48ILgbKH7+HBp1Q3rCY=; TBV=7; adblocked=true; tb-c30=scus-t1; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1637963085000@firstcreate:1637963081999"; TBWL-94-cartGQLSRL=cg01gdc0et7v:0:1cj7fc3f3raiy:1eaadqd5qm6hc; xptwg=233687375:E7E6AE97460540:26013B5:B1661295:E1F9138B:D50754BB:; bm_sv=B65C67375ED4368C337D958F36ED507A~VCZ23fRxDueEOZP1FnT11U/09+ifFZWvevZg8IqnAuoBk2E2WmPYkJ7vWMmVu8tjSFQFXAPcki25V0jIJDvBn5gd41XfbtyBCcd/XhpBs5ibEbz1+8pfaM2Cbh/Suj+fQegj3D2akageLq/QlDc+QlW7Z9P6nXqIlSVZIppytkU=; wm_client_ip=24.127.206.56; tb_sw_supported=true',
    }

    params = (
        ('wl13', '2281'),
        ('selectedSellerId', '0'),
    )

    response = requests.get('https://www.walmart.com/ip/Scott-Professional-Multi-Purpose-Shop-Towels-55-Sheets-per-Roll-6-Ct/54946622', headers=headers, params=params)

    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.select("h1")[0]
    if title is None:
        sys.stderr.write("Could not lookup title for walmart item")
        return ("INVALID_WALMART", -1)
    price = soup.find("span", {"itemprop": "price"})
    if price is None:
        sys.stderr.write("Could not lookup price for walmart item")
        return ("INVALID_WALMART", -1)
    return (title.get_text().strip(), float(price.get_text().replace("$","")))

def all_queries():
    return [walmartQuery()]

if __name__ == "__main__":
    print(all_queries())
