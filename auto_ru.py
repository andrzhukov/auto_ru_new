import requests
from bs4 import BeautifulSoup
import csv

HOST = 'https://auto.ru/'
URL = 'https://auto.ru/moskva/cars/kia/all/'
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'suid=9e294e963ebcfa27236cf412eeb3df51.21ef21a8ba994c7441c755a2d733a071; yandexuid=6388443431621378173; my=YwA%3D; credit_filter_promo_popup_closed=true; gdpr=0; _ym_uid=1622588957472292933; yandex_login=mr.bichirovich; i=dQvQwE0HSwpVUm4pE02YPtDH4+tJ1KdqQknIqR/2g6Mm5chm7sUlgjrbF/wMVDSwZTmiyOUtVeSMtm7ZHnSP8URCNJo=; credit_modal_autoshow_closed=true; autoru_sid=a%3Ag622a86692cr4ulcjbgevrv0s6odkpju.8bdabf0e621dca76d8f14e4fd7f92386%7C1648163689540.604800.ek9uBwhmgUyQbttzI5uucw.yQs_GzknDk4khAPbWubhTJFWDrW4GBKADUA_y38BBH0; gradius=0; gids=213; autoru-visits-count=1; yuidlt=1; autoruuid=g622a86692cr4ulcjbgevrv0s6odkpju.8bdabf0e621dca76d8f14e4fd7f92386; _csrf_token=abd676202bcbdfcbaaeeaf47efcb67b16190e1d898fb83fd; from=direct; X-Vertis-DC=vla; Session_id=3:1648409780.5.0.1629930556092:X7nZPg:c.1.2:1|292394208.7427060.402.2:7427060|61:3302.683628.GXf779V5Rv505-2dDt01cY_wlrQ; ys=c_chck.886450874; mda2_beacon=1648409780921; sso_status=sso.passport.yandex.ru:synchronized; _ym_isad=2; _yasc=tnQHOhLYzKXBHmuEOvWmejxPDEuG3wZYSK+6YNcnzbFNFHoZ; from_lifetime=1648409987799; _ym_d=1648409987; cycada=nqH7+oUJczCSw/SzGMoOECKCXlp5wIMqb89bi8TJjIo=',
    'Host': 'auto.ru',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36'
}


# мб сделать парсинг через класс??

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='ListingItem')
    #print(items)
    cars = []

    for item in items:
        car_title = str(item.find('a', class_='Link ListingItemTitle__link').get_text)
       # car_title = car_title.split('>')[1].rstrip('<div')
        cars.append(
            {
                'title': car_title,
                'car_link': item.find('a', class_='Link ListingItemTitle__link').get('href')
            }
        )
    return cars
    #print(items)

html = get_html(URL)
print(html.text)
#print(get_content(html.text))
