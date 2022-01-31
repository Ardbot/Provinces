from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    region = "/amurskaya_oblast"
    categories = "/tovary_dlya_kompyutera/"
    product = "Видеокарты"

    # url = f"https://www.avito.ru/{region}{categories}?q={product}"
    url = f"https://www.avito.ru/{region}?q={product}"
    print(url)

    requests = requests.get(url)
    bs = BeautifulSoup(requests.text, "html.parser")

    all_links = bs.find_all('a', class_="iva-item-title-py3i_")
    for link in all_links:
        print("https://www.avito.ru" + link["href"])

