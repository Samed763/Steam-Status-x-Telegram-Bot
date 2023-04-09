from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import telebot

TOKEN = 'Your Token'
tb = telebot.TeleBot(TOKEN)
user = tb.get_me()

driver = webdriver.Chrome()
driver.get("https://steamstat.us/")

degisken_1=None

while True:

    Durum = driver.find_element(By.XPATH ,'//*[@id="csgo_community"]')

    element_text = Durum.text
    print('1.Sunucun Durumu:'+element_text)

    if(degisken_1==None):
        tb.send_message(chat_id=, "----BOT BAŞLATILDI----")

    if(degisken_1 != element_text):
        tb.send_message(chat_id=, "Sunucu Durumu:"+" "+element_text)
        print("*------DURUMLAR DEĞİŞTİ------*")
        time.sleep(5)
        degisken_1=element_text

    else:
        time.sleep(5) 
        print("*------------ ELSE ÇALIŞTI ------------*")
