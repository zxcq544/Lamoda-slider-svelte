import shutil
import requests
import lxml.html
import os
from pprint import pprint
import json
from decimal import *


html_string = ""

with open('product_list_catalog.html', 'r') as file:
    html_string = file.read().replace('\n', '')

doc = lxml.html.fromstring(html_string)


def clean_url(url):
    image_url = url.split("/")[-4:]
    image_url = "/".join(image_url)
    image_url = "./" + image_url
    return image_url


elems = doc.find_class("products-list-item")
all_products = []
print(len(elems))
for el in elems:
    product = {}
    if "data-gallery" in el.attrib:
        product["data-gallery"] = []
        product["data-src"] = ""
        # product["price"] = 0
        # print(el.attrib["data-gallery"])
        image_urls = el.attrib["data-gallery"][1:-1].split(",")
        product["data-src"] = clean_url(el.attrib["data-src"])
        product["data-sku"] = el.attrib["data-sku"]
        # product["price"] = Decimal(el.attrib["data-price"])

        child_div = el.find_class("to-favorites")
        if "data-sku" in child_div[0].attrib:
            product["data-name"] = child_div[0].attrib["data-name"]
            product["data-price-origin"] = child_div[0].attrib["data-price-origin"]
            product["data-gender"] = child_div[0].attrib["data-gender"]
            product["data-color-family"] = child_div[0].attrib["data-color-family"]
            product["data-brand"] = child_div[0].attrib["data-brand"]
            product["data-is-sport"] = child_div[0].attrib["data-is-sport"]
            product["data-is-premium"] = child_div[0].attrib["data-is-premium"]
            product["data-season"] = child_div[0].attrib["data-season"]
            product["data-is-new"] = child_div[0].attrib["data-is-new"]
            product["data-category"] = child_div[0].attrib["data-category"]
            if "data-discount" in child_div[0].attrib:
                product["data-price"] = child_div[0].attrib["data-price"]
                product["data-discount"] = child_div[0].attrib["data-discount"]
                product["data-discount-percent"] = child_div[0].attrib["data-discount-percent"]
            # else:
            #     print("No discount")
        else:
            print("child not found")

        image_url = ""
        for img in image_urls:
            image_url = clean_url(img)
            product["data-gallery"].append(image_url)
        # print(image_urls)
        all_products.append(product)
pprint(all_products)


product_file = open("products.json", "w")
# magic happens here to make it pretty-printed
product_file.write(json.dumps(all_products, indent=4, sort_keys=True))
product_file.close()
