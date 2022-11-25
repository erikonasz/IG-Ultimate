from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

def login():
    driver.get("https://www.instagram.com/")
    button = driver.find_element(By.XPATH, '//button[text()="Only allow essential cookies"]')
    button.click()
    time.sleep(1)
    username = driver.find_element(By.NAME, 'username')
    password = driver.find_element(By.NAME, 'password')

    username.click()
    username.send_keys('Your username')
    password.click()
    password.send_keys('Your password')
    time.sleep(3)

    login_B = driver.find_element(By.XPATH, '//div[text()="Log in"]')
    login_B.click()
    time.sleep(8)

    saveinfo = driver.find_element(By.XPATH, '//button[text()="Not Now"]')
    saveinfo.click()
    time.sleep(8)

    notifics = driver.find_element(By.XPATH, '//button[text()="Not Now"]')
    notifics.click()
    time.sleep(8)



login()




