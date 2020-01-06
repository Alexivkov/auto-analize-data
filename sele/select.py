from selenium import webdriver
import time

browser = webdriver.Chrome(r'D:\PycharmProjects\InstaBot\venv\chromedriver.exe')
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser.get(link)
    number1 = browser.find_element_by_id('num1')
    number2 = browser.find_element_by_id('num1')
    sum = number1 + number2
    print(sum)
    select = browser.find_element_by_tag_name('select')
    select.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
