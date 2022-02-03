from bs4 import BeautifulSoup
import requests
from av_filters import Filters


def test():
    # filter = Filters("amurskaya_oblast", "tovary_dlya_kompyutera", "komplektuyuschie", "videokarty", "rtx 3050")
    # url = filter.stringr_url()
    # print(url)
    url = "https://www.avito.ru/amurskaya_oblast/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw?p=1"
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "html.parser")
    all_content = bs.find_all('div', class_="iva-item-content-rejJg")


    # for link in all_content:
    #     print(link)
    #     print("https://www.avito.ru" + link["href"])


    # print(all_links)

    for content in all_content:
        name = content.find('h3', class_="title-root-zZCwT")
        print(name.text)

        price = content.find(class_="price-text-_YGDY")
        print(price.text)

        sity = content.find(class_="geo-georeferences-SEtee")
        print(sity.text)

        url_product = content.find(class_="iva-item-titleStep-pdebR")
        for link in url_product:
            print("https://www.avito.ru" + link["href"])

        print("#" * 20)


if __name__ == '__main__':
    test()
