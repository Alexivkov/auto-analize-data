from selenium import webdriver
import time

#python create_persons_list.py & python filtration.py & python liker.py

link = 'https://www.instagram.com/mega_ekb/?hl=ru'
browser = webdriver.Chrome(r'C:\chromedriver\chromedriver.exe')
allpersons = 900
browser.get('https://www.instagram.com/')
browser.implicitly_wait(5)
try:
    browser.get('https://www.instagram.com/accounts/login/')
    # Enter Account
    # input('Enter login and password')
    login = 'remtel66'
    password = 'torser'
    browser.find_element_by_xpath('//section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(login)
    browser.find_element_by_xpath('//section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(password)
    browser.find_element_by_xpath('//section/main/div/article/div/div[1]/div/form/div[4]').click()
    time.sleep(5)

    browser.get(link)
    time.sleep(3)
    browser.find_element_by_xpath('//section/main/div/header/section/ul/li[2]/a').click() #open subscriber list
    time.sleep(2)
    # browser.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()
    element = browser.find_element_by_xpath('/html/body/div[4]/div/div[2]')
    # /html/body/div[4]/div/div[2]/ul/div/li[1]/div/div[1]/div[2]/div[1]/a
    #scrolling

    browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight/%s' %6, element)
    time.sleep(0.8)
    browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight/%s' %4, element)
    time.sleep(0.8)
    browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight/%s' %3, element)
    time.sleep(0.8)
    browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight/%s' %2, element)
    time.sleep(0.8)
    browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight/%s' %1.4, element)
    time.sleep(0.8)
    pers = []  #list of linkes <a> of users
    t = 0.7   #pause for next scroll
    num_scroll = 0   #number of scrolls
    p = 0  # koefficient for waiting  2000, 4000...users

    # for i in range(5):
    #     browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight/%s' % 2, element)
    #     time.sleep(0.8)

    while len(pers) < allpersons:
        num_scroll += 1
        browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', element)

        if num_scroll % 10 == 0:
            print('!')
            # save users in list
            persons = browser.find_elements_by_xpath('//div[@role="dialog"]/div[2]/ul/div/li/div/div/div/div/a[@title]')
            for i in range(len(persons)):
                pers.append(str(persons[i].get_attribute('href')))

            time.sleep(t)
            #waiting
            if (len(pers) > (2000 + 1000 * p) ):
                print('wait 10 min')
                time.sleep(60*10)
                p+=1
    # make file of users list
    f = open(r'D:\PycharmProjects\InstaBot\venv\persons_list.txt', 'w')
    for person in pers:
        f.write(person)
        f.write('\n')

    f.close()
finally:
    browser.quit()
