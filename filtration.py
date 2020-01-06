import selenium
from selenium import webdriver
import time

from datetime import timedelta,datetime
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import re

days = 20 # days from last publication
acc_subscription = 1500 #  podpisok
publication = 10
today = datetime.now()

def xpath_existence(url):
    try:
        browser.find_element_by_xpath(url)
        existence = 1
    except NoSuchElementException:
        existence = 0
    return existence

# read all links
f = open(r'D:\PycharmProjects\InstaBot\venv\persons_list.txt', 'r')
file_list = []
for line in f:
    file_list.append(line)
f.close()

#link processing

filtered_list = []
i = 0 # suitable users count
j = 0 # output terminal

browser = webdriver.Chrome() #executable_path='D:\PycharmProjects\InstaBot\venv')
# browser.get('https://www.instagram.com/')
# #Enter Account
# login = 'remtel66'
# password = 'torser'
# browser.get('https://www.instagram.com/accounts/login')
# browser.find_element_by_xpath('//section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(login)
# browser.find_element_by_xpath('//section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(password)
# browser.find_element_by_xpath('//section/main/div/article/div/div[1]/div/form/div[4]').click()
# time.sleep(5)

for person in file_list:
    j +=1
    print(str(person))
    browser.get(str(person))
    # 1 public account
    element = '//section/main/div/div/article[2]/div[1]/div/h2'
    if xpath_existence((element)) == 1:
        try:
            if browser.find_element_by_xpath(element).text == "This Account is Private" or "Это закрытый аккаунт":
                print(j, 'Private account')
                continue
        except StaleElementReferenceException:
            print('ErroR, number 1')

    # 2 <= podpisok
    # element = '//section/main/div/header/section/ul/li[3]/a/span'
    # if xpath_existence(element) == 0:
    #     print(j, 'Error, number 2')
    #     continue
    # status = browser.find_element_by_xpath(element).text
    # status = re.sub(r'\s', '', status)  # delete spaces from subscribers numbers
    # if int(status) > acc_subscription:
    #     print(j, 'more subscriptions')
    #     continue

    # 3 there should not be a link to the site
    element = '//section/main/div/header/section/div[2]/a'
    if xpath_existence(element) == 1:
        print(j, ' site link !!!')
        continue

    # 4 minimum quantity of publications
    element = '//section/main/div/header/section/ul/li[1]/a/span'
    if xpath_existence(element) == 0:
        print(j, 'error, number 4')
        continue
    status = browser.find_element_by_xpath(element).text
    status = re.sub(r'\s', '', status).replace(',', '')
    if int(status) < publication:
        print(j, 'more publications')
        continue

    # 5 photo avatar
    element = '//section/main/div/header/div/div/span/img'
    if xpath_existence(element) ==0:
        print(j, 'Error code 5')
        continue
    status = browser.find_element_by_xpath(element).get_attribute('src')
    if status.find('s150x150') == -1:
        print(j, 'without avatar')
        continue

    #6 check on the date of the last publication
    element = '//a[contains(@href, "/p/")]'
    if xpath_existence(element) == 0:
        print(j, 'Error code 6')
        continue
    status = browser.find_element_by_xpath(element).get_attribute('href')
    browser.get(status)
    post_date = browser.find_element_by_xpath('//time').get_attribute('datetime')
    year = int(post_date[0:4])
    month = int(post_date[5:7])
    day = int(post_date[8:10])
    post_date = datetime(year, month, day)
    period = today - post_date
    if period.days > days:
        print(j, 'publication was too long')
        continue

    # Add user to filtered list
    filtered_list.append(person)
    print(j, 'add new user', person)
    i+=1
    if i >10:
        break
#out of cycle

# write to file
f = open(r'D:\PycharmProjects\InstaBot\venv\filtered_persons_list.txt', 'w')
for line in filtered_list:
    f.write(line)
f.close()
print('\n')
browser.quit()