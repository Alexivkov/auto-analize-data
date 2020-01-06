from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome(r'D:\PycharmProjects\InstaBot\venv\chromedriver.exe')
    browser.get(link)
    x = browser.find_element_by_id('treasure')
    answer = x.get_attribute('valuex')
    # print(answer)
    browser.find_element_by_id('answer').send_keys(calc(answer))
    browser.find_element_by_css_selector('input[type=checkbox]').click()
    browser.find_element_by_css_selector('[value = "robots"]').click()
    browser.find_element_by_tag_name('button').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()