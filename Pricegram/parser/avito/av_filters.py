"""Фильтрация для Avito.
Составление URL запроса"""


class Filters(object):
    def __init__(self, region, sity, categories, subcategories, product):
        self.region = region
        self.sity = sity
        self.categories = categories
        self.subcategories = subcategories
        self.product = product

    def stringr_url(self):
        url = f"https://www.avito.ru/{self.region}/{self.sity}/{self.categories}/{self.subcategories}?q={self.product}"
        return url


if __name__ == '__main__':
    run = Filters("rossiya", "tovary_dlya_kompyutera", "komplektuyuschie", "videokarty", "Видеокарта")
    print(run.sity)
    print(run.stringr_url())