from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie_id = "bigCookie"
cookie_count_id = "cookies"

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]")))

language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, cookie_id)))

cookie = driver.find_element(By.ID, cookie_id)

while True:
    time.sleep(0.0000001)
    cookie.click()
    cookie_count = driver.find_element(By.ID, cookie_count_id).text.split(" ")[0]
    cookie_count = int(cookie_count.replace(",", ""))
    print(cookie_count)

time.sleep(10)

driver.quit()
