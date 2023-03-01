# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 11:49:42 2023

@author: LENOVO
"""

from requests_html import HTMLSession

session = HTMLSession()
response = session.get('https://coreyms.com/')

articles = response.html.find('article')

for article in articles:
    headline = article.find('.entry-title-link', first=True).text
    print(headline)

    summary = article.find('.entry-content p', first=True).text
    print(summary)

    try:
        vid_src = article.find('iframe', first=True).attrs['src']
        vid_id = vid_src.split('/')[4].split('?')[0]
        yt_link = f'https://youtube.com/watch?v={vid_id}'
        print(yt_link)
    except Exception as e:
        print(e)
    print()

    
    