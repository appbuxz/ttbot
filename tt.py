from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import keyboard
import json

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

# загрузка json
with open('output.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

def main():
    driver.get("https://www.tiktok.com/login/phone-or-email/email")
    print("скрипт запущен")
    time.sleep(3)
    print("URL:", driver.current_url,"\nТекущий заголовок:", driver.title)
    login = driver.find_element(By.CSS_SELECTOR,".etcs7ny0")
    passw1 = driver.find_element(By.CSS_SELECTOR,".e1bi0g3c0")
    time.sleep(2)

    for user in data["users"]:
        login.click()
        time.sleep(1)
        keyboard.write(user["login"])
        time.sleep(1)
        passw1.click()
        time.sleep(2)
        keyboard.write(user["passwd"])
    loginsys = driver.find_element(By.CSS_SELECTOR,".ehk74z00")
    time.sleep(1)
    loginsys.click()



main()