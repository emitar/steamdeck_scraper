from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import telebot

#telebot variables
token = 'YOUR_TOKEN'
chat_id = 'YOUR_CHAT_ID'

#Expected storage, leave blank if you don't care. (ex. 64, 256, 512)
expected_storage=''

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
        now = datetime.datetime.now()
        main_div = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'salepurchaseonlydisplay_Name_2K2zo')))
        sale_section = driver.find_elements(By.ID, 'SaleSection_33131')[0].text
        lines = sale_section.splitlines()
        for i in range(1, len(lines), 3):
            if "Out of stock" not in lines[i]:
                name = lines[i-1].split('-')[0]
                storage = name.split(' ')[2]
                price = lines[i+1]
                if expected_storage !='':
                    if storage == expected_storage:
                        msg = f'{name} in stock {price}'
                        send_msg(msg)
                else:
                    msg = f'{name} in stock  {price}'
                    send_msg(msg)
    except Exception as e:
        msg = f'[Steam Deck] Checking error: {e}'
        send_msg(msg)
    finally:
        driver.quit()


if __name__ == '__main__':
    check_stock()
