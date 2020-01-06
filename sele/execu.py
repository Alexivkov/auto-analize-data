from selenium import webdriver
import time
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome(r'C:\chromedriver\chromedriver.exe')
    browser.get(link)
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()