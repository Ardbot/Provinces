"""Фильтрация для Avito.
Составление URL запроса"""


class Filters(object):
    def __init__(self, region, sity, categories, subcategories, product):
        self.region = region
        self.sity = sity
        # self.sity = "belogorsk"
        self.categories = categories
        self.subcategories = subcategories
        self.product = product

    def stringr_url(self):
        # url = f"https://www.avito.ru/{region}{categories}?q={product}"
        # https: // www.avito.ru / amurskaya_oblast / tovary_dlya_kompyutera?cd = 1
        url = f"https://www.avito.ru/{self.region}_{self.sity}/{self.categories}/{self.subcategories}?q={self.product}"
        print(url)
        return url

    print(stringr_url())


if __name__ == '__main__':
    pass
