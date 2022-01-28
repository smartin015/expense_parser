import requests
import sys

def geagleQuery(sku):
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 14150.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.114 Safari/537.36',
        'content-type': 'application/json;charset=utf-8',
    }

    data = '{"operationName":"ProductDetailQuery","variables":{"sku":"SKUSKUSKU","count":8,"ignoreFulfillmentMethod":true,"storeCode":"40"},"query":"fragment GetProductTileData on Product {\\n  brand\\n  categoryNames\\n  circular {\\n    endDate\\n    startDate\\n    __typename\\n  }\\n  comparedPrice\\n  coupons {\\n    conditions {\\n      minBasketValue\\n      minQty\\n      offerType\\n      __typename\\n    }\\n    description\\n    disclaimer\\n    discountType\\n    expiryDate\\n    externalId\\n    products {\\n      sku\\n      __typename\\n    }\\n    rewards {\\n      offerValue\\n      rewardQuantity\\n      __typename\\n    }\\n    summary\\n    __typename\\n  }\\n  displayItemSize\\n  id\\n  itemFulfillmentMethods\\n  images {\\n    kind\\n    url\\n    __typename\\n  }\\n  name\\n  price\\n  pricingModel\\n  promo {\\n    badgeText\\n    promoType\\n    qty\\n    __typename\\n  }\\n  restrictions {\\n    restrictionType\\n    __typename\\n  }\\n  sizeOfFirstAdd\\n  sizes\\n  sku\\n  __typename\\n}\\n\\nquery ProductDetailQuery($sku: String!, $storeCode: String!, $count: Int!, $ignoreFulfillmentMethod: Boolean!) {\\n  product: fetchProduct(\\n    sku: $sku\\n    storeCode: $storeCode\\n    ignoreFulfillmentMethod: true\\n  ) {\\n    allergens\\n    brand\\n    categoryNames\\n    comparedPrice\\n    coupons {\\n      conditions {\\n        minBasketValue\\n        minQty\\n        offerType\\n        __typename\\n      }\\n      description\\n      disclaimer\\n      externalId\\n      discountType\\n      products {\\n        sku\\n        __typename\\n      }\\n      rewards {\\n        offerValue\\n        rewardQuantity\\n        __typename\\n      }\\n      expiryDate\\n      summary\\n      __typename\\n    }\\n    description\\n    directions\\n    displayItemSize\\n    displayPricePerUnit\\n    healthClaims\\n    id\\n    images {\\n      url\\n      kind\\n      __typename\\n    }\\n    indications\\n    ingredients\\n    itemFulfillmentMethods\\n    name\\n    nutritionFacts {\\n      id\\n      name\\n      dailyValue\\n      quantity\\n      __typename\\n    }\\n    price\\n    pricingModel\\n    promo {\\n      qty\\n      badgeText\\n      promoType\\n      __typename\\n    }\\n    restrictions {\\n      restrictionType\\n      __typename\\n    }\\n    sizeOfFirstAdd\\n    sizes\\n    sku\\n    vendor\\n    warnings\\n    __typename\\n  }\\n  productRecommendations: productRecommendations(\\n    first: $count\\n    sku: $sku\\n    storeCode: $storeCode\\n    ignoreFulfillmentMethod: $ignoreFulfillmentMethod\\n  ) {\\n    edges {\\n      node {\\n        ...GetProductTileData\\n        __typename\\n      }\\n      __typename\\n    }\\n    queryId\\n    __typename\\n  }\\n}\\n"}'.replace("SKUSKUSKU", sku)

    response = requests.post('https://adapter.shop.gianteagle.com/api', headers=headers, data=data)
    if response.status_code != requests.codes.ok:
        sys.stderr.write("ERROR fetching geagle query - code ", response.status_code)
        return ("ERROR", 0)
    j = response.json()
    if j is None:
        sys.stderr.write("Failed to convert geagle query to json")
        return ("ERROR", 0)
    product = j["data"]["product"]
    if product is None:
        sys.stderr.write("No product result for sku ", sku)
        return ("NOPRODUCT " + sku, 0.0)
    return (product["name"], float(product["price"]))

def all_queries():
    return [geagleQuery(sku) for sku in [
        "00030034000523", # eggs
        "00030034000608", # whole milk
        "00030034027476", # black beans
        "00000000046084", # bulk garlic
        "00030034935023", # white rice
        ]]


if __name__ == "__main__":
    print(all_queries())
