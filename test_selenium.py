from seleniumwire.webdriver import Chrome
from selenium.webdriver.common.by import By
import sqlite3
import time
import random

# driver for Google Chrome pipiska
webdriver = '/Users/andrejzukov/PycharmProjects/pythonProject4/chromedriver/chromedriver'
driver = Chrome(webdriver)

# Creating database and cursor
dbase = sqlite3.connect('auto_ru_cars.db')
cur = dbase.cursor()

# TEST - test url
test_url = 'https://auto.ru/moskva/cars/bmw/3er/all/?top_days=1&year_from=2018&year_to=2019'

# TEST - Creating test table
dbase.execute('CREATE TABLE IF NOT EXISTS {}(Name, Link, Engine_Power, Year, Mileage, Price, Photo, Owner)'.format('test_cars'))
dbase.commit()

# Creating headers for request to auto.ru
def interceptor(request):
    del request.headers['Accept']
    del request.headers['Accept-Encoding']
    del request.headers['Accept-Language']
    del request.headers['Cache-Control']
    del request.headers['Connection']
    del request.headers['Host']
    del request.headers['User-Agent']
   
    request.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    request.headers['Accept-Encoding'] = 'gzip, deflate, br'
    request.headers['Accept-Language'] = 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
    request.headers['Cache-Control'] = 'max-age=0'
    request.headers['Connection'] = 'keep-alive'
    request.headers['Cookie'] = 'suid=9e294e963ebcfa27236cf412eeb3df51.21ef21a8ba994c7441c755a2d733a071; \
                yandexuid=6388443431621378173; \
                my=YwA%3D; \
                credit_filter_promo_popup_closed=true; \
                gdpr=0; \
                _ym_uid=1622588957472292933; \
                i=dQvQwE0HSwpVUm4pE02YPtDH4+tJ1KdqQknIqR/2g6Mm5chm7sUlgjrbF/wMVDSwZTmiyOUtVeSMtm7ZHnSP8URCNJo=; \
                credit_modal_autoshow_closed=true; \
                autoru_sid=a%3Ag622a86692cr4ulcjbgevrv0s6odkpju.8bdabf0e621dca76d8f14e4fd7f92386%7C1648163689540.604800.ek9uBwhmgUyQbttzI5uucw.yQs_GzknDk4khAPbWubhTJFWDrW4GBKADUA_y38BBH0; \
                gradius=0; \
                gids=213; \
                autoru-visits-count=1; \
                yuidlt=1; \
                autoruuid=g622a86692cr4ulcjbgevrv0s6odkpju.8bdabf0e621dca76d8f14e4fd7f92386; \
                _csrf_token=abd676202bcbdfcbaaeeaf47efcb67b16190e1d898fb83fd; \
                from=direct; \
                X-Vertis-DC=vla; \
                Session_id=3:1648409780.5.0.1629930556092:X7nZPg:c.1.2:1|292394208.7427060.402.2:7427060|61:3302.683628.GXf779V5Rv505-2dDt01cY_wlrQ; ys=c_chck.886450874; \
                mda2_beacon=1648409780921; \
                sso_status=sso.passport.yandex.ru:synchronized; \
                _ym_isad=2; \
                _yasc=tnQHOhLYzKXBHmuEOvWmejxPDEuG3wZYSK+6YNcnzbFNFHoZ; \
                from_lifetime=1648409987799; \
                _ym_d=1648409987; \
                cycada=nqH7+oUJczCSw/SzGMoOECKCXlp5wIMqb89bi8TJjIo='
    request.headers['Host'] = 'auto.ru'
    request.headers['User-Agent'] = 'Googlebot/2.1 (+http://www.google.com/bot.html)'
    # request.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'

driver.request_interceptor = interceptor
# driver.get(url)

# This function for getting total number of pages for current search
def get_page_number(first_url):
    driver.get(first_url)
    pages = driver.find_elements(by=By.XPATH,
                                 value='//*[@class="Button Button_color_whiteHoverBlue Button_size_s Button_type_link Button_width_default ListingPagination__page"]')
    try:
        numbers_of_pages = int(pages[-1].get_attribute('href').split('page=')[1])
    except IndexError:
        numbers_of_pages = 1
    driver.close()
    return numbers_of_pages

# print(get_page_number())

# This function for creating the overall list of page links
def create_page_link_list(global_url, page_number):
    if page_number > 1:
        page_list = []
        if '?' in global_url:
            attr = '&page='
        else:
            attr = '?page='
        for num in range(2, page_number + 1):
            page_link = global_url + attr + str(num)
            page_list.append(page_link)
        return page_list
    else:
        return None

# This function create list that include information about cars from the page
def get_car_info_from_page(page_url):
    time.sleep(random.random())
    driver.get(page_url)
    cars_from_page = []
    car_names = driver.find_elements(by=By.XPATH,
                                           value='//div[@class = "ListingCars ListingCars_outputType_list"]//a[@class="Link ListingItemTitle__link"]')
    car_links = driver.find_elements(by=By.XPATH,
                                           value='//div[@class = "ListingCars ListingCars_outputType_list"]//*[@class="Link ListingItemTitle__link"]')
    car_engines = driver.find_elements(by=By.XPATH,
                                           value='//div[@class = "ListingCars ListingCars_outputType_list"]//*[@class="ListingItemTechSummaryDesktop__cell"]')
    car_years = driver.find_elements(by=By.XPATH,
                                           value='//div[@class = "ListingCars ListingCars_outputType_list"]//*[@class="ListingItem__year"]')
    car_mileages = driver.find_elements(by=By.XPATH,
                                     value='//div[@class = "ListingCars ListingCars_outputType_list"]//*[@class="ListingItem__kmAge"]')
    car_prices = driver.find_elements(by=By.XPATH,
                                      value='//div[@class = "ListingCars ListingCars_outputType_list"]//*[@class="ListingItemPrice__content"]')
    car_engines_clear = []
    for engine in car_engines:
        if "л.с." in engine.text:
            car_engines_clear.append(engine.text)
        else:
            continue
    for idx in range(len(car_engines_clear)):
        car_engines_clear[idx] = car_engines_clear[idx].replace('\u2009/\u2009', ' | ')
    for i in range(len(car_names)):
        cars_from_page.append([car_names[i].text, car_links[i].get_attribute('href'), car_engines_clear[i],
                               car_years[i].text, car_mileages[i].text, car_prices[i].text, 'No Photo', 'No Owner'])
    driver.close()
    return cars_from_page

# This function create list that include information about cars from all pages
def get_car_info_from_all_pages(url):
    page_num = get_page_number(test_url)
    if create_page_link_list(url, page_num) == None:
        page_list = [url]
    else:
        page_list = [url] + create_page_link_list(url, page_num)
    print(page_list)
    total_cars_info = []
    for page_url in page_list:
        total_cars_info += get_car_info_from_page(page_url)
    return total_cars_info

# This function write information about cars from list to database
def write_info_to_db(car_lst, tablename):
    cur.executemany('INSERT INTO {} VALUES(?, ?, ?, ?, ?, ?, ?, ?)'.format(tablename), car_lst)
    dbase.commit()
    return

# This function gets ads on the url and compares it with ads from table in database.
# It returns new ads as a result of comparison,
def check_new_ads(url, tablename):
    req = cur.execute('SELECT * FROM {}'.format(tablename)).fetchall()
    last_ads = get_car_info_from_all_pages(url)
    new_ads = []
    for ad in last_ads:
        ad_match = False
        for r in req:
            if ad[0] == r[0] and ad[1] == r[1] and ad[2] == r[2] and ad[3] == r[3] and ad[4] == r[4]:
                ad_match = True
                # print('Машина найдена в БД: ' + ad[0] + '. Ссылка: ' + ad[1])
            else:
                continue
        if ad_match == False:
            # print('Найдена новая машина: ' + ad[0] + '. Ссылка: ' + ad[1])
            new_ads.append(ad)
    return new_ads

# This function gets photo and owner information from the ads in the list
def get_photo_owner(car_lst):
    for item in car_lst:
        driver.get(item[1])
        photo_links = driver.find_elements(by=By.XPATH,
                                            value='//div[@class = "ImageGalleryDesktop__itemContainer"]//img[@class="ImageGalleryDesktop__image"]')
        owner_quantity = driver.find_elements(by=By.XPATH,
                                           value='//li[@class = "CardInfoRow CardInfoRow_ownersCount"]//span[@class="CardInfoRow__cell"]')
        item[6] = photo_links[0].get_attribute('src')
        item[7] = owner_quantity[1].text
    driver.close()
    return car_lst

print(get_car_info_from_all_pages(test_url))


# driver.close()
