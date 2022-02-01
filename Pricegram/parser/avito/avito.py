from bs4 import BeautifulSoup
import requests
from av_filters import Filters

def test(requests=None):

    url = Filters.stringr_url()
    print(url)
    requests = requests.get(url)
    bs = BeautifulSoup(requests.text, "html.parser")

    all_links = bs.find_all('a', class_="iva-item-title-py3i_")
    for link in all_links:
        print("https://www.avito.ru" + link["href"])


