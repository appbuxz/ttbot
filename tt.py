from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

def main():
    driver.get("https://www.tiktok.com/login")
    print("скрипт запущен")
    time.sleep(3)
    print("URL:", driver.current_url,"\nТекущий заголовок:", driver.title)
    driver.execute_script("window.scrollBy(0, 30);")
    time.sleep(3)
    element1 = driver.find_element(By.CSS_SELECTOR,".tiktok-1kd6uhh-DivLastLoginMethodContainer.e1cgu1qo2")
    element1.click()
    print(element1)
main()