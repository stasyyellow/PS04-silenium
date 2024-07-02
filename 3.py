from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time


def search_wikipedia(query):
    browser = webdriver.Chrome()
    browser.get(
        "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

    # Проверяем по заголовку, тот ли сайт открылся
    assert "Википедия" in browser.title
    time.sleep(2)

    # Находим окно поиска
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    return browser


def list_paragraphs(browser):
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
        user_input = input("Нажмите Enter, чтобы продолжить или 'q', чтобы выйти: ")
        if user_input.lower() == 'q':
            break


def list_internal_links(browser):
    links = browser.find_elements(By.XPATH,
                                  "//div[@id='bodyContent']//a[not(contains(@href, 'redlink')) and contains(@href, '/wiki/')]")
    link_texts = [link.text for link in links if link.text]

    for i, text in enumerate(link_texts):
        print(f"{i + 1}: {text}")

    while True:
        choice = input("Введите номер ссылки для перехода или 'q', чтобы выйти: ")
        if choice.lower() == 'q':
            break
        if choice.isdigit() and 1 <= int(choice) <= len(link_texts):
            links[int(choice) - 1].click()
            time.sleep(2)
            return True
        else:
            print("Неверный ввод. Попробуйте снова.")

    return False


def main():
    user_request = input("Введите запрос: ")
    browser = search_wikipedia(user_request)

    while True:
        action = input(
            "Выберите действие: \n1. Листать параграфы текущей статьи\n2. Перейти на одну из связанных страниц\n3. Выйти\nВаш выбор: ")

        if action == '1':
            list_paragraphs(browser)
        elif action == '2':
            if not list_internal_links(browser):
                break
        elif action == '3':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

    browser.quit()


if __name__ == "__main__":
    main()
