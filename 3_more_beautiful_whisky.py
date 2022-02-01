# From https://www.youtube.com/watch?v=nCuPv3tf2Hg
import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.thewhiskyexchange.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}

r = requests.get('https://www.thewhiskyexchange.com/c/35/japanese-whisky')
soup = BeautifulSoup(r.content, 'lxml')