# from bs4 import BeautifulSoup
# import urllib.request

# sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
# soup = BeautifulSoup(sauce, 'lxml')


# # Print all information of table
# table = soup.table
# print(table)

# print()

# # Now we have to print table data with information

# table_rows = table.find_all('tr')

# for tr in table_rows:
# 	td = tr.find_all('td')
# 	row = [i.text for i in td]
# 	print(row)






# XML File


from bs4 import BeautifulSoup
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
soup = BeautifulSoup(sauce, 'xml')
#print(soup)

for url in soup.find_all('loc'):
	print(url.text)