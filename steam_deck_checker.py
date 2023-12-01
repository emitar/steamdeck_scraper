from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import telebot

#telbot variables
token = 'YOUR_TOKEN'
chat_id = 'YOUR_CHAT_ID'

#options settings
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

#def webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#def url
url = 'https://store.steampowered.com/sale/steamdeckrefurbished/'

#init driver
driver.get(url)


def send_msg(msg):
    bot = telebot.TeleBot(token)
    bot.send_message(chat_id, msg)

def check_stock():
    try:
        main_div = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'salepurchaseonlydisplay_Name_2K2zo')))
        names  = driver.find_elements(By.CLASS_NAME, 'salepurchaseonlydisplay_Name_2K2zo')
        prices = driver.find_elements(By.CLASS_NAME, 'salepreviewwidgets_StoreSalePriceBox_Wh0L8')
        statuses = driver.find_elements(By.CLASS_NAME, 'addtocartbutton_ActionOutOfStock_I_6Pn.CartBtn')
        for name, price, status in zip(names, prices, statuses):
            if status.text != 'Out of stock':
                msg = f"{name.text.split('-')[0]}- {price.text} - {status.text}"
                send_msg(msg)
    except Exception as e:
        msg = f'[Steam Deck] Checking error: {e}'
        send_msg(msg)
    finally:
        driver.quit()

if __name__ == '__main__':
    check_stock()
