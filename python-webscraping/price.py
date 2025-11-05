from bs4 import BeautifulSoup
import requests

# Turning a URL into a scrapable thing
url = "https://www.newegg.ca/msi-mpg-341cqpx-qd-oled-34-uwqhd-240-hz-metallic-black/p/N82E16824475392?Item=N82E16824475392&cm_sp=Homepage_SS-_-P1_24-475-392-_-07222025"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

# Finding a certain element from a website 

prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)

# Searching and Filtering
