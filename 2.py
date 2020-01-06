from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome(r'D:\PycharmProjects\InstaBot\venv\chromedriver.exe')
    browser.get(link)
    elements = browser.find_elements_by_class_name("form-control")
    for element in elements:
       element.send_keys("Мо")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '1.txt')# добавляем к этому пути имя файла
    browser.find_element_by_css_selector('[type="file"]').send_keys(file_path)
    button = browser.find_element_by_css_selector("button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()