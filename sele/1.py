import selenium
from selenium import webdriver
import time

link = "http://suninjuly.github.io/alert_accept.html"
try:
    browser = webdriver.Chrome(r'D:\PycharmProjects\InstaBot\venv\chromedriver.exe')
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла