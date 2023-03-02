from bs4 import BeautifulSoup
import re


with open("index2.html", "r") as f:
	doc = BeautifulSoup(f, "html.parser")

# Searching for tags
result = doc.find("option")
print(result)

# Find tag/multiple tag
tags = doc.find_all(["div", "p", "li"])
print(tags)

# If you want to specific tag
tags = doc.find_all(["option"], string="Undergraduate")
print(tags)

# Find Class name
tags = doc.find_all(class_= "btn-item")
print(tags)

# Find Regular Expression
tags = doc.find_all(text=re.compile("\$.*"))
for tag in tags:
	print(tag.strip())