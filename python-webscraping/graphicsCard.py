from bs4 import BeautifulSoup
import requests
import re 

# ! Main Info
product = input("Enter product that you are looking for: ")
url = f"https://www.newegg.ca/p/pl?d={product}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

# Nitty Gritty
page_text = doc.find(class_="list-tool-pagination-text").strong
pages = int(str(page_text).split("/")[-2].split('>')[-1][:-1])
# print(pages)

items_found = {}


for page in range(1, pages+1):
    url = f"https://www.newegg.ca/p/pl?d={product}&N=4131&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    div = doc.find(class_="list-wrap")
    items = div.find_all(string=re.compile(product))

    
    for item in items:
        parent = item.parent
        if parent.name != 'a':
            continue
        link = parent['href']
        next_parent = item.find_parent("div", class_=re.compile("item-cell"))
        try:
            price = next_parent.find(class_="price-current").strong.string
            items_found[item] = {"price": int(price.replace(",","")), "link": link}
        except:
            pass

# print(items_found)

sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])

for item in sorted_items:
    print(item[0]) # name
    print(f"{item[1]['price']}") # price 
    print(item[1]['link']) # link of item
    print(' _______________________________________')

