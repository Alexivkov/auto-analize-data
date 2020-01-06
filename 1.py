from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome(r'D:\PycharmProjects\InstaBot\venv\chromedriver.exe')

    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element_by_id("input_value")
    answer = calc(x.text)
    browser.find_element_by_css_selector('[for="robotCheckbox"]').click()

    browser.find_element_by_tag_name('input').send_keys(answer)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element_by_id('robotsRule').click()
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла