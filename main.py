from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def search_wikipedia(query):
    browser = webdriver.Chrome()
    browser.get("https://ru.wikipedia.org/")

    search_box = browser.find_element(By.ID, "searchInput")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    return browser

def list_paragraphs(browser):
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for idx, para in enumerate(paragraphs):
        print(f"Параграф {idx + 1}:")
        print(para.text)
        print("\n")

def list_internal_links(browser):
    links = browser.find_elements(By.XPATH, "//div[@id='bodyContent']//a[@href and not(contains(@href, ':'))]")
    internal_links = [link for link in links if link.get_attribute("href").startswith("https://ru.wikipedia.org/wiki/")]
    for idx, link in enumerate(internal_links):
        print(f"{idx + 1}: {link.text} - {link.get_attribute('href')}")
    return internal_links

def main():
    query = input("Введите ваш запрос: ")
    browser = search_wikipedia(query)

    while True:
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на внутреннюю ссылку")
        print("3. Выйти")

        choice = input("Введите номер вашего выбора: ")

        if choice == "1":
            list_paragraphs(browser)
        elif choice == "2":
            internal_links = list_internal_links(browser)
            link_choice = int(input("Введите номер ссылки, которую хотите открыть: ")) - 1
            if 0 <= link_choice < len(internal_links):
                browser.get(internal_links[link_choice].get_attribute("href"))
        elif choice == "3":
            browser.quit()
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
