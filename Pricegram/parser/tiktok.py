import webbrowser

from bs4 import BeautifulSoup
import requests


def main():
    authoriz_err()

def authoriz_err():
    url = "https://1tok.ru/user.php"
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "html.parser")
    all_content = bs.find_all("div", class_="class_err_content")

    if all_content == "":
        print("Ошибка авторизации")
    else:
        print("ok")
        print(all_content)
        # print(all_content)
    # webbrowser.open('https://1tok.ru/user.php', new=2)

    for link in all_content:
        pass
        # print(link["href"])

def authorization():
    pass

if __name__ == '__main__':
    main()