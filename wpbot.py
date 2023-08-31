from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

with open('messages.txt', 'r', encoding='utf-8') as messages:
    messagelist = list()
    text = messages.read()
    messagelist = text.split('\n')

print(messagelist)


def start():
    flag = False
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)  # if we don't get any response, we will wait 3 seconds
    driver.get('https://web.whatsapp.com/')
    input("Enter any button if your QR is scanned: ")
    message_area = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    while True:
        message_area.click()
        wp_source = driver.page_source  # it includes html source codes
        soup = bs(wp_source, 'lxml')
        search = soup.find_all('div', {'class': ['p357zi0d r15c9g6i g4oj0cdv ovllcyds l0vqccxk pm5hny62']})
        try:
            online = search[0].span.text
            print(online)
            if (online in ['çevrimiçi', 'online']) and flag == False:
                print('ONLINE')
                msgtosend = messagelist[random.randint(0, len(messagelist)-1)]
                message_area.send_keys(msgtosend)
                message_area.send_keys(Keys.ENTER)
                flag = True
            elif online not in ['çevrimiçi', 'online']:
                print("OFFLINE")
                flag = False
        except:
            print("OFFLINE")
            flag = False
        time.sleep(5)


start()





