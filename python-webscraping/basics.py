import selenium 
from bs4 import BeautifulSoup

with open("index.html", "r") as file:
    doc = BeautifulSoup(file, "html.parser") 

tag = doc.title
print(tag)

tag2 = doc.find("a")
tag3 = doc.findAll("p")[0]

# print(doc.prettify())
print(tag3)

