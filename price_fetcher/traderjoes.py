import requests

def tjQuery(sku):
    headers = {
    'authority': 'www.traderjoes.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'accept': '*/*',
    'content-type': 'application/json',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 14150.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.114 Safari/537.36',
    'sec-ch-ua-platform': '"Chrome OS"',
    'origin': 'https://www.traderjoes.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.traderjoes.com/home/products/pdp/092463',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'affinity="ece063aa8b007bdb"',
    }

    data = '{"operationName":"SearchProduct","variables":{"storeCode":"678","published":"1","sku":"SKUSKUSKU"},"query":"query SearchProduct($sku: String, $storeCode: String = \\"678\\", $published: String = \\"1\\") {\\n  products(\\n    filter: {sku: {eq: $sku}, store_code: {eq: $storeCode}, published: {eq: $published}}\\n  ) {\\n    items {\\n      category_hierarchy {\\n        id\\n        url_key\\n        description\\n        name\\n        position\\n        level\\n        created_at\\n        updated_at\\n        product_count\\n        __typename\\n      }\\n      item_story_marketing\\n      product_label\\n      fun_tags\\n      primary_image\\n      primary_image_meta {\\n        url\\n        metadata\\n        __typename\\n      }\\n      other_images\\n      other_images_meta {\\n        url\\n        metadata\\n        __typename\\n      }\\n      context_image\\n      context_image_meta {\\n        url\\n        metadata\\n        __typename\\n      }\\n      published\\n      sku\\n      url_key\\n      name\\n      item_description\\n      item_title\\n      item_characteristics\\n      item_story_qil\\n      use_and_demo\\n      sales_size\\n      sales_uom_code\\n      sales_uom_description\\n      country_of_origin\\n      availability\\n      new_product\\n      promotion\\n      price_range {\\n        minimum_price {\\n          final_price {\\n            currency\\n            value\\n            __typename\\n          }\\n          __typename\\n        }\\n        __typename\\n      }\\n      retail_price\\n      nutrition {\\n        display_sequence\\n        panel_id\\n        panel_title\\n        serving_size\\n        calories_per_serving\\n        servings_per_container\\n        details {\\n          display_seq\\n          nutritional_item\\n          amount\\n          percent_dv\\n          __typename\\n        }\\n        __typename\\n      }\\n      ingredients {\\n        display_sequence\\n        ingredient\\n        __typename\\n      }\\n      allergens {\\n        display_sequence\\n        ingredient\\n        __typename\\n      }\\n      created_at\\n      first_published_date\\n      last_published_date\\n      updated_at\\n      related_products {\\n        sku\\n        item_title\\n        primary_image\\n        primary_image_meta {\\n          url\\n          metadata\\n          __typename\\n        }\\n        price_range {\\n          minimum_price {\\n            final_price {\\n              currency\\n              value\\n              __typename\\n            }\\n            __typename\\n          }\\n          __typename\\n        }\\n        retail_price\\n        sales_size\\n        sales_uom_description\\n        category_hierarchy {\\n          id\\n          name\\n          __typename\\n        }\\n        __typename\\n      }\\n      __typename\\n    }\\n    total_count\\n    page_info {\\n      current_page\\n      page_size\\n      total_pages\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n"}'.replace("SKUSKUSKU", sku)

    response = requests.post('https://www.traderjoes.com/api/graphql', headers=headers, data=data)
    return (
        response.json()['data']['products']['items'][0]['item_title'], 
        float(response.json()['data']['products']['items'][0]['retail_price'])
    )


def all_queries():
    return [tjQuery("092463")]

if __name__ == "__main__":
    print(all_queries())
