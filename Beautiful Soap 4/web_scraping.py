from bs4 import BeautifulSoup

with open("index.html", "r") as f:
	doc =  BeautifulSoup(f, "html.parser")

# Print HTML file on local machine
#print(doc.prettify())

# Find By tag Name
tag = doc.title
print(tag)
# We have to access what inside in this title
print(tag.string)

# Find all by tag name
tags = doc.find_all('p')
print(tags)

