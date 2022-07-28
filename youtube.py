import playsound
from selenium import webdriver
import time

from banner import USER_CHOICE, SOUND
from config import PATH, options


def get_link_file(url):
    driver = webdriver.Chrome(PATH, chrome_options=options)

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
    link_file = download_box.get_attribute('href')

    driver.close()

    return link_file


def get_user_url():
    user_input = input("""Please Enter The Url : 
__   __          _         _          ____  _                       
\ \ / /__  _   _| |_ _   _| |__   ___|  _ \| | __ _ _   _  ___ _ __ 
 \ V / _ \| | | | __| | | | '_ \ / _ \ |_) | |/ _` | | | |/ _ \ '__|
  | | (_) | |_| | |_| |_| | |_) |  __/  __/| | (_| | |_| |  __/ |   
  |_|\___/ \__,_|\__|\__,_|_.__/ \___|_|   |_|\__,_|\__, |\___|_|   
                                                    |___/           
--------------------------------------------------------------------
Created By : AmirhoseinSohrabi & MohsenAzizi 

amirhoseinsohrabi.official@gmail.com
me.mohsen.azizi@gmail.com


            """)
    return user_input


def get_user_choice(link):
    user_input = input(USER_CHOICE)
    if user_input.lower() == "y":
        url = get_user_url()
        new_url = get_link_file(url)
        return get_user_choice(new_url)
    elif user_input.lower() == "x":
        play_sound(link)
    else:
        print("Oops!!, wrong choice, try again please ...")
        return get_user_choice(link)


def play_sound(url):
    user_input = input(SOUND)
    if user_input.lower() == "p":
        playsound.playsound(url)
    elif user_input.lower() == "x":
        exit()
    else:
        print("Oops!!, wrong choice, try again please ...")
        return play_sound(url)
