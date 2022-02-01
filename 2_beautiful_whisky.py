# Learning bs4 from https://www.youtube.com/watch?v=UClHOT_7hok
# Extends whiskyspider

import requests
from bs4 import BeautifulSoup 

def get_page_links(url):
    baseurl = 'https://www.thewhiskyexchange.com'
    r = requests.get(url)
    sp = BeautifulSoup(r.text, 'lxml')
    links = sp.select('li.product-grid__item a')
    return [baseurl + link.attrs['href'] for link in links]

def product_data(url):
    r = requests.get(url)
    sp = BeautifulSoup(r.text, 'lxml')

    product = {
        'title': sp.select_one('h1.product-main__name').text.strip().replace('\n', ' '),
        'price': sp.select_one('p.product-action__price').text.strip().replace('\n', ''),
        'stock': sp.select_one('p.product-action__stock-flag').text.strip().replace('\n', ''),
        'desc': sp.select_one('div.product-main__description p').text.strip().replace('\n', '')
    }
    print(product)

product_data('https://www.thewhiskyexchange.com/p/34572/omar-sherry-single-malt')

# print(get_page_links('https://www.thewhiskyexchange.com/c/305/world-whisky?pg=1&psize=120&sort=pasc'))