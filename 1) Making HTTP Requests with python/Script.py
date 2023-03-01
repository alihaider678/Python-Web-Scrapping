# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:22:52 2023

@author: LENOVO
"""

import requests

url = 'https://api.github.com'
response = requests.get(url)

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found')