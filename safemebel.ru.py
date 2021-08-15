import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import csv
import re
# отличие с ценой

def get_html(url):
    ua = UserAgent()
    headers = {'User-Agent': ua.chrome}
    r = requests.get(url, headers=headers)
    if r.ok:
        return r.text

def refine_ang(ang1):
    ang = str.upper(ang1)
    intab = 'А, В, С, Е, Н, К, М, О, Р, Т, Х'
    outtab = 'A, B, C, E, H, K, M, O, P, T, X'
    trantab = ang.maketrans(intab,outtab)
    return ang.translate(trantab)

def refine_p(p):
    return p.replace(' ','')

def write_csv(data):
    with open('ufa_safemebel.csv', 'a',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'], data['price']))

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    lis = soup.find_all('div', class_='item_info')

    for li in lis:
        try:
            ang = li.find('div', class_='item-title').find('a').text.strip()

            name = refine_ang(ang)
        except:
            name = ''

        try:
            p = li.find('div', class_='price').find('span', class_='price_value').text.strip()
            price = refine_p(p)
        except:
            price = ''
        data = {'name': name,
                'price': price}

        write_csv(data)

def konec(url):

    soup = BeautifulSoup(get_html(url), 'lxml')
    url1 = soup.find('div', class_='nums').find_all('a', class_="dark_link")
    for elem in url1:
        e = []
        e.append(elem)

    k = str(e[-1])
    c = re.compile('\d+')

    return int(c.findall(k)[-1])+1


def main():



    pattern = 'https://ufa.safemebel.ru/catalog/shkafy_metallicheskie/?PAGEN_1={}'

    for i in range(1, konec(pattern)):
        url = pattern.format(str(i))
        get_page_data(get_html(url))

    pattern = 'https://ufa.safemebel.ru/catalog/seyfy/?PAGEN_1={}'

    for i in range(0, konec(pattern)):
        url = pattern.format(str(i))
        get_page_data(get_html(url))


if __name__ == '__main__':
    main()