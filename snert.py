import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import csv
import re


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
    f=p.replace('Р','')
    return f.replace(' ','')

def write_csv(data):
    with open('snert.csv', 'a',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'], data['price']))

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    lis = soup.find_all('div', class_='other')

    for li in lis:
        try:
            ang = li.find('div', class_='name').find('h5', class_='no-rating').text.strip()

            name = refine_ang(ang)
        except:
            name = ''

        try:
            p = li.find('div', class_='product-price').find('span', class_='price').text.strip()
            price = refine_p(p)
        except:
            price = ''
        data = {'name': name,
                'price': price}

        write_csv(data)

def konec(url):

    soup = BeautifulSoup(get_html(url), 'lxml')
    url1 = soup.find('div', class_='lazyloading-paging').find_all('a').text.strip()
    for elem in url1:
        e = []
        e.append(elem)

    k = str(e[-1])
    c = re.compile('\d+')

    return int(c.findall(k)[-1])+1


def main():



    pattern = 'http://surgut.snert.ru/category/metallicheskie-shkafy/?page={}'

    for i in range(1, konec(pattern)):
        url = pattern.format(str(i))
        get_page_data(get_html(url))

    pattern = 'http://surgut.snert.ru/category/seyfy/?page={}'

    for i in range(0, konec(pattern)):
        url = pattern.format(str(i))
        get_page_data(get_html(url))


if __name__ == '__main__':
    main()