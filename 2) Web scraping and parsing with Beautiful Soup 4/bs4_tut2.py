from bs4 import BeautifulSoup
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = BeautifulSoup(sauce, 'lxml')
#print(soup)


# print all nav

nav = soup.nav
for url in nav.find_all('a'):
	print(url.get('href'))

print()

# Print all body with p tag
body = soup.body
for paragrapgh in body.find_all('p'):
	print(paragrapgh.text)

print()

# Print all the div text
for div in soup.find_all('div'):
	print(div.text)

print()

# Print all the div text with specific class 
for div in soup.find_all('div', class_ = 'body'):
	print(div.text)