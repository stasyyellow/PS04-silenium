from selenium import webdriver
from selenium.webdriver import Keys
#Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.by import By
import time

#запрос пользователя
a = input('Введите запрос для Википедии: ')

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

#проверка того на каком сайте находимся
assert "Википедия" in browser.title
time.sleep(5)
#Находим окно поиска
search_box = browser.find_element(By.ID, "searchInput")
#Прописываем ввод текста в поисковую строку. В кавычках тот текст, который нужно ввести (переменная "a")
search_box.send_keys(a)
#Добавляем не только введение текста, но и его отправку
search_box.send_keys(Keys.RETURN)
time.sleep(5)

#варианты дальнейшей работы программы
# 1 листать параграфы текущей статьи;
# 2 перейти на одну из связанных страниц

b = int(input("Выберите один пункт \n листать параграфы текущей статьи - 1, перейти на одну из связанных страниц - 2"))

if b == 1:
    c = browser.find_element(By.LINK_TEXT, a)
    c.click()

    variants = int(input("Листать параграфы статьи - 1, перейти на одну из внутренних статей - 2"))
    # try / except

    if variants == 1:
        paragraphs = browser.find_elements(By.TAG_NAME, value="p")
        for paragraph in paragraphs:
            print(paragraph.text)
            input()

elif b == 2:
    browser.find_element()