from bs4 import BeautifulSoup
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

soup = BeautifulSoup(sauce, 'lxml')

#print(soup)

# Print Title
print(soup.title)

print()

# Print String or Text of Title
print(soup.title.text)

print()

# Print all paragraph tags
print(soup.find_all('p'))

print()

# Print all paragraph with text(also sub text or string)
for paragrapgh in soup.find_all('p'):
	print(paragrapgh.text)

print()

# Print all text
print(soup.get_text())

print()

# Print all ancher tags
for url in soup.find_all('a'):
	print(url.text)
	# Get Actually Links
	print(url.get('href'))