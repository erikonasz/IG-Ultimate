from selenium import webdriver
import random
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.set_window_size(1920,1080)




def login():
    driver.get("https://www.instagram.com/")
    time.sleep(6)
    button = driver.find_element(By.XPATH, '//button[text()="Only allow essential cookies"]')
    button.click()
    time.sleep(6)
    username = driver.find_element(By.NAME, 'username')
    password = driver.find_element(By.NAME, 'password')

    username.click()
    username.send_keys('username')
    password.click()
    password.send_keys('pass')
    time.sleep(3)

    login_B = driver.find_element(By.XPATH, '//div[text()="Log in"]')
    login_B.click()
    time.sleep(6)
    print("Logging in!")
    try:
        saveinfo = driver.find_element(By.XPATH, '//button[text()="Not Now"]')
        saveinfo.click()
        time.sleep(6)
    except:
        print('Button not found. Skipping save info button.')
        pass
    try:
        notifics = driver.find_element(By.XPATH, '//button[text()="Not Now"]')
        notifics.click()
        time.sleep(6)
        print("Clicking on Notifications button")
    except:
        print('Button not found. Skipping notifications button.')
        pass
    pplinput = int(input("How many people would you like to follow?"))

def Randomsleep():
    _sleep = random.randint(3,7)
    time.sleep(_sleep)

def SelectAutof():
    selectf = input('Press 1 to Autofollow from a page. Press 2 to AutoFollow from the post(liked post people):  ')
    if selectf == '1':
        igpagef = input("Please enter the IG page username: ")
        driver.get(f"https://www.instagram.com/{igpagef}/followers")
        time.sleep(8)
        Follow()

def Follow():
    scroll = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
    while True:
        for _ in range(2):
            time.sleep(5)
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
        fbuttons = driver.find_elements(By.CSS_SELECTOR, "._aano div div button")
        try:
            for button in fbuttons:
                if button.text == 'Follow':
                    button.click()
                    Randomsleep()
                    time.sleep(3)
            #if FC == pplinput:
                #print("Reached the desired follow amount!")
                #SelectAutof()
        except:
            print("Can't find follow button, all people already followed?")
            time.sleep(3)
        try:
            cancelfolw = driver.find_element(By.XPATH, '//button[text()="Cancel"]')
            cancelfolw.click()
        finally:
            time.sleep(5)
            Follow()

login()
SelectAutof()

