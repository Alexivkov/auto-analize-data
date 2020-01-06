from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def browser_get_link_and_wait(link):
    browser.get(link)
    browser.implicitly_wait(10)

links = [
    "https://beru.ru/",
    "http://iphone-ekb.ru/",
    "http://www.uralapple.ru/",
    "https://a66.ru/"
]
phone = 'iPhone 11 Pro 64'

browser = webdriver.Chrome(r'D:\PycharmProjects\InstaBot\venv\chromedriver.exe')
for link in links:
    browser_get_link_and_wait(link)
        # price = WebDriverWait(browser, 14).until(
        #     EC.presence_of_element_located((By.TAG_NAME, "input"))
        # )
    try:
        if link == "https://beru.ru/":
            browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div/div/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div/div/form/div[1]/div/span/span/input").send_keys(phone)
        else:
            browser.find_element_by_tag_name("input")
        browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        browser.implicitly_wait(10)
        print(link.split("//")[-1].split("/")[0], browser.find_element(By.CSS_SELECTOR, "[data-auto='price']").text)
    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(7)
        # закрываем браузер после всех манипуляций
        browser.quit()
