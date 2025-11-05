from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tableBody = doc.tbody  
trows = tableBody.contents

# traversing on the same row
# print(trows[0].next_sibling)
# traversing up and down the tree
# print(list(trows[0].parent))

prices = {}
for trow in trows[:10]:
    # name, price = trow.contents[2:4]
    # coinName = name.p.string
    # print(price)
    try:
        # Assuming name and price are in specific table columns
        name = trow.find('p', {'class': 'coin-item-symbol'}).text.strip()
        
        # Extract the price from the td with class 'td-price'
        price_div = trow.find('td', {'class': 'td-price'})
        if price_div:
            price = price_div.find('span').text.strip()
        else:
            price = "N/A"
        
        # Store the coin name and price in the dictionary
        prices[name] = price
    except AttributeError:
        # In case of any missing or malformed elements
        continue
print(prices)