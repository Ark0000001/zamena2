import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import csv
import re
#
#
# def refine_ang(ang):
#     intab = 'А, В, С, Е, Н, К, М, О, Р, Т, Х, а, с, е, о, р, х, к'
#     outtab = 'A, B, C, E, H, K, M, O, P, T, X, a, c, e, o, p, x, k'
#     trantab = ang.maketrans(intab,outtab)
#     return ang.translate(trantab)
#
# with open ('modif.csv', 'r') as f:
#   old_data = f.read()
#
# new_data = refine_ang(old_data)
#
# with open ('prom.txt', 'w') as f:
#   f.write(new_data)

def get_html(url):
    ua = UserAgent()
    headers = {'User-Agent': ua.chrome}
    r = requests.get(url, headers=headers)
    if r.ok:
        return r.text

soup = BeautifulSoup(get_html('http://surgut.snert.ru/category/metallicheskie-shkafy/'), 'lxml')
# url1 = soup.find('div', class_='lazyloading-paging').find('li').find('a').text.strip()



lis = soup.find('ul', class_='prd-list-pagination').find_all('li')

for li in lis:
    ang = li.find('a')


    e = []
    e.append(ang)
    e += e

print(e)