# import requests      # Библиотека для отправки запросов
# import numpy as np   # Библиотека для матриц, векторов и линала
# import pandas as pd  # Библиотека для табличек
# import time          # Библиотека для тайм-менеджмента
#
# import socks
# import socket
#
# page_link = 'https://86safe.ru/'
# response = requests.get(page_link)
# print(response)
#
# for key, value in response.request.headers.items():
#     print(key+": "+value)

# name1 = 'шкаф ПРАКТИК LS-11-40D,5030'
# name2 = 'Сейф оружейный Aiko Чирок 1320,6530'
#
# def dict1(s):
#     d = dict()
#     a = ''
#     i = 0
#     while i < len(s):
#         a = s[i].split(',')
#         d[a[i]] = a[i + 1]
#         i + 2
#     return d
#
# print(h=dict1(name1))
import re

from bs4 import BeautifulSoup
import requests


def konec(url):

    soup = BeautifulSoup(url, 'lxml')
    url1 = soup.find('div', class_='nums').find_all('a', class_="dark_link").text
    for elem in url1:
        e = []
        e.append(elem)
    print(e)
    k = str(e[-1])
    c = re.compile('\d+')
    print(int(c.findall(k)[-1])+1)
    return int(c.findall(k)[-1])+1


def mmm():



    pattern = 'https://xn--c1azcgcc.xn----7sbenacbbl2bhik1tlb.xn--p1ai/catalog/metallicheskie-shkafy/?PAGEN_1={}'

    for i in range(1, konec(pattern)):
        url = pattern.format(str(i))
        get_page_data(get_html(url))
