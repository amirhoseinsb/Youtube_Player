#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 17:17:31 2022
@author: amir
"""

import playsound
from selenium import webdriver
import time

while True:
    url = input('Please Enter The Url : ')
    driver_path = './chromedriver'
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')

    driver = webdriver.Chrome(
                driver_path,
                chrome_options = options
            )

    driver.get('https://yt1s.com/en331/youtube-to-mp3')
    time.sleep(10)
    box = driver.find_element_by_css_selector('input#s_input')
    box.send_keys(url)
    time.sleep(10)
    convert_mp3 = driver.find_element_by_css_selector('button#btn-convert')
    convert_mp3.click()
    time.sleep(5)
    get_link = driver.find_element_by_css_selector('button#btn-action')
    get_link.click()

    time.sleep(2)


    download_box = driver.find_element_by_css_selector('a#asuccess')
    download_link = download_box.get_attribute('href')
    print(download_link)

    z = input('''
              Y == continue for get the next link
              X == Exit To Play Music ''')

    if z == 'Y':
        continue
    else :
        break

select_play = input('''
           Enter The Play Type:
           P = Play Music
           X = Exit
           ''')
if select_play =='P' or 'p':
    playsound.playsound(download_link)

elif select_play == 'X' or 'x':
    exit() 
