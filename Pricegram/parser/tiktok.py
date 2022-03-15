import webbrowser

from bs4 import BeautifulSoup
import requests
import time

import pyautogui

def main():
    authoriz_err()

def authoriz_err():
    url = "https://1tok.ru/"
    r = requests.get(url)
    print(r.text)
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
    url = "https://1tok.ru/"

    payload = {'login_username': '@ardbot',
               'login_password': 'admin'}
    files = [

    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)

def coord():
    old_time = 0
    while True:
        if time.time() - old_time > 1:
            # print(old_time)
            # print(time.time())
            # print(time.time() - old_time)
            old_time = time.time()
            print(pyautogui.position())


# https://1tok.ru/user.php
def scrin():
    time.sleep(5)
    while True:
        print(pyautogui.position())
        pyautogui.moveTo(100, 200, 2)
        # Клик Выполнить
        pyautogui.click(x=787, y=378)
        time.sleep(5)
        # Лайк
        pyautogui.doubleClick(x=1010, y=657)
        print("like")
        time.sleep(1)

        # Закрыть окно
        pyautogui.click(x=470, y=14)
        print("like")
        # time.sleep(1)

        # # Вкладка
        # pyautogui.click(x=50, y=20)
        time.sleep(5)
        # print("Вкладка")


if __name__ == '__main__':
    # main()
    # authorization()
    scrin()
    # coord()