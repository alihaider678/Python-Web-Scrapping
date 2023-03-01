# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:59:20 2023

@author: LENOVO
"""

from requests_html import HTML

with open('simple.html') as html_file:
    source = html_file.read()
    html = HTML(html = source)
#print(html.html)

#Print Text

#print(html.text)

#article = html.find('div.article', first = True)
#headline = html.find('h2', first = True).text
#summary = html.find('p', first = True).text

#print(headline)
#print(summary)

# If we want to print all articles
articles = html.find('div.article')
for article in articles:
    headline = html.find('h2', first = True).text
    summary = html.find('p', first = True).text
    print(headline)
    print(summary)
    print()
    



