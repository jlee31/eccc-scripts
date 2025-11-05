from bs4 import BeautifulSoup
import re # regular expression

with open("public/index2.html", 'r') as file:
    doc = BeautifulSoup(file, "html.parser")

# Changing the filtering tag
tag = doc.find("option")
#changing tag attributes
tag['value'] = "newvalue"
print(tag.attrs)

# Finding multiple tags
tag2 = doc.find_all(["p", "div", "h2"])
tag3 = doc.find_all(["option"], text="Undergraduate", value="undergraduate")

# Looking for class names
tag4 = doc.find_all(class_="btn-item")
tag5 = doc.find_all(text=re.compile("\$.*"))
# print('\n'.join(tag.strip() for tag in tag5))

tag6 = doc.find_all("input", type="text")
for tag in tag6:
    tag['placeholder'] = "NEWVALUE"

with open("changed.html", "w") as file2:
    file2.write(str(doc))