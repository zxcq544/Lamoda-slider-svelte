import re
import shutil
import requests
import lxml.html
import os

html_string = ""

with open('product_list_catalog.html', 'r') as file:
    html_string = file.read().replace('\n', '')

doc = lxml.html.fromstring(html_string)

elems = doc.find_class("products-list-item")
print(len(elems))

all_image_urls = []
for el in elems:
    if "data-gallery" in el.attrib:
        # print(el.attrib["data-gallery"])
        image_urls = el.attrib["data-gallery"][1:-1].split(",")
        # print(image_urls)
        all_image_urls += image_urls
# print(all_image_urls)
request_urls = []
for url in all_image_urls:
    #     print(url)
    request_url = "http:" + url
    # print(request_url)
    request_urls.append(request_url)


def download_image_by_url(url):
    remote_url = url
    local_url = remote_url.split("/")
    try:
        os.makedirs("/".join(local_url[3:-1]))
    except FileExistsError as err:
        print(err)
    print(local_url)
    response = requests.get(remote_url, stream=True)
    with open("/".join(local_url[3:]), 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
        print(f"{url} done")
    del response


print(f"{len(request_urls)} images to get")


# uncomment this 2 lines to get images
# for url in request_urls:
# download_image_by_url(url)
