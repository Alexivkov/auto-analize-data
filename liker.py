import selenium
from selenium import webdriver
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException

import random
random.seed()

like_time = 10
all_likes = 50
all_subscriptions = 50
hour_like = 7
hour_sub = 7

# in that hour
likes = 0
subscriptions = 0

def xpath_existence(url):
    try:
        browser.find_element_by_xpath(url)
        existence = 1
    except NoSuchElementException:
        existence = 0
    return existence

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

# input('Enter for enter')
f = open(r'D:\PycharmProjects\InstaBot\venv\filtered_persons_list.txt', 'r')
file_list = []
for line in f:
    file_list.append(line)
f.close()

# print('file_list', file_list)
# my subscription list
subscription_list = []
f1 = open(r'D:\PycharmProjects\InstaBot\venv\my_subscriptions_list.txt', 'r')
for line1 in f1:
    subscription_list.append(line1)
f1.close()
# print('subscription_list', subscription_list)

j = 0 # input number in terminal
n = 0 # пропущеное число пользователей из-за совпадения subscription_list
next_person = 0  # если тру - след пользователь по циклу
start_time = time.time() # time of cycle stating

# cycle
for person in file_list:
    # условие для паузы цикла
    if likes >= all_likes:
        print('like limit in day')
        break
    if subscriptions >= all_subscriptions:
        print('subscriptions limit in day')
        break
    # # max in an hour
    if ((time.time() - start_time) <= 60*60) and (hour_sub <= subscriptions):
        print('subscriber limit in an hour')
        print('wait', int(60*60 - (time.time() - start_time))/60, 'minutes')

        # удаляем из отфильтрованных пользователей тех, на которых уже подписка
        f = open(r'D:\PycharmProjects\InstaBot\venv\filtered_persons_list.txt', 'w')
        for i in range(j, len(file_list)):
            f.write(file_list[i])
        f.close()

            # обнуляем
        time.sleep(60*60 - (time.time() - start_time))
        start_time = time.time()
        subscriptions = 0
        likes = 0

        # max in an hour
    if ((time.time() - start_time) <= 60 * 60) and (hour_like <= likes):
        print('subscriber limit in an hour')
        print('wait', int(60 * 60 - (time.time() - start_time)) / 60, 'minutes')

        # удаляем из отфильтрованных пользователей тех, на которых уже подписка
        f = open(r'D:\PycharmProjects\InstaBot\venv\filtered_persons_list.txt', 'w')
        for i in range(j, len(file_list)):
            f.write(file_list[i])
            # print(file_list)
        f.close()

        # обнуляем
        time.sleep(60 * 60 - (time.time() - start_time))
        start_time = time.time()
        subscriptions = 0
        likes = 0

    # обнуление часа
    if ( (time.time() - start_time) >= 60*60):
        start_time = time.time()
        subscriptions = 0
        likes = 0

    # сравниваем с массивом подписок
    for line in subscription_list:
        next_person = 0
        if person == line:
            next_person = 1
            print(j + 1, 'subscription exists already')
            j += 1
            n += 1
            break
    if next_person == 1:
        continue
    #выводим в терминал номера
    j += 1
    print('\n' + str(j - n) + ': ')

    # print('open person')
    #open user page
    browser.get(person)
    time.sleep(1.5)

    # открываем публикации и лайки

    #проверяем есть ли подписка на этого пользователя
    element = '//section/main/div/header/section/div[1]/div[1]/span/span[1]/button'
    #print(xpath_existence(element) == 1)
    if xpath_existence(element) == 1:
        try:
            follow_status = browser.find_element_by_xpath(element).text
            # print(follow_status)
        except StaleElementReferenceException:
            print('Error code 1.0')
            continue
        if (follow_status == 'Following') or (follow_status == 'Подписки'):
            print('Already subsribed on this \n')
            continue

        # search publications and open 2 random
        element = "//a[contains(@href, '/p/')]"
        if xpath_existence(element) == 0:


            print(j, 'Error code 1.1')
            continue
        # print(element)
        posts = browser.find_elements_by_xpath(element)
        i = 0
        # print(posts)
        for post in posts:
            posts[i] = post.get_attribute('href')
            # print(posts[i])
            i +=1
        # print(posts)
        rand_post = random.randint(0,5)
        # print(rand_post)
        for i in range(2):
            # print('in rand cycle')
            browser.get(posts[rand_post + i])
            time.sleep(0.3)
            browser.find_element_by_xpath('//section/main/div/div/article/div[2]/section[1]/span[1]/button').click()
            likes += 1
            print('+1 like')
            time.sleep(like_time)

        # 2 подписка на пользователя
        try:
            element = '//section/main/div/div/article/header/div[2]/div[1]/div[2]/button'
            if xpath_existence(element) == 0:
                print(j,' Error code 2.0')
            try:
                browser.find_element_by_xpath(element).click()
            except StaleElementReferenceException:
                print(j, 'Error code 2.1')
                continue
        except ElementClickInterceptedException:
            print(j, 'Error code 2.2')
            continue

        subscriptions += 1
        print('+1 subscription', person[0:len(person) - 1])
        time.sleep(0.5)

        # запись новой подписки в файл подписок
        f = open(r'D:\PycharmProjects\InstaBot\venv\my_subscriptions_list.txt', 'a')
        f.write(person)
        f.close()
    # end of cycle

    f = open(r'D:\PycharmProjects\InstaBot\venv\filtered_persons_list.txt', 'w')
    for i in range(j, len(file_list)):
        f.write(file_list[i])
    f.close()

browser.quit()

