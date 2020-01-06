from  selenium import webdriver
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

# time between unsibscribing
unsub_time = 3
# unsubscribing quantity
max = 20

#check elem exist
def xpath_existence(url):
    try:
        browser.find_element_by_xpath(url)
        existence = 1
    except NoSuchElementException:
        existence = 0
    return existence
try:
    browser = webdriver.Chrome(r'D:\PycharmProjects\InstaBot\venv\chromedriver.exe')
    browser.get('https://www.instagram.com/')

    #Enter Account
    login = 'remtel66'
    password = 'torser'
    browser.get('https://www.instagram.com/accounts/login')
    browser.find_element_by_xpath('//section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(login)
    browser.find_element_by_xpath('//section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(password)
    browser.find_element_by_xpath('//section/main/div/article/div/div[1]/div/form/div[4]').click()
    time.sleep(5)

    # read subscribtions file
    file_list =[]
    f = open(r'D:\PycharmProjects\InstaBot\venv\my_subscriptions_list.txt')
    for line in f:
        file_list.append(line)
    f.close()

    #unsub process
    i = 0
    for line in file_list:
        i += 1
        if i == max + 1:
            break
        browser.get(line)
        # element = 'button'
        element = ('//section / main / div / header / section / div[1] / div[1] / span / span[1] / button')

        if xpath_existence(element) == 0:
            print('Error 1: finding unsub button')
            continue
        try:
            button = browser.find_element_by_xpath(element)
        except StaleElementReferenceException:
            print('Error 2: finding unsub button ')
            continue
        if button.text == "Подписки":
            try:
                button.click()
            except StaleElementReferenceException:
                 print('Error 3: finding unsub button')
        time.sleep(0.5)
        element = '/html/body/div[3]/div/div/div[3]/button[1]'
        if xpath_existence(element) == 0:
            print('Error 4: finding unsub button ')
            continue
        button =browser.find_element_by_xpath(element)
        try:
            button.click()
        except StaleElementReferenceException:
            print('Error 5: push button')
            continue
        print('Unsubscribe from' , line)
        time.sleep(unsub_time)

    # clearing sub_list
    f = open(r'D:\PycharmProjects\InstaBot\venv\my_subscriptions_list.txt')
    i = 0
    for i in range(max, len(file_list)):
        f.write(file_list[i])
        i +=1
    f.close()
finally:
    browser.quit()

