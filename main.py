from selenium import webdriver
import random
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.set_window_size(1920, 1080)

uname = input("Enter your IG email: ")
paswo = input("Enter IG password: ")


def login():
    driver.get("https://www.instagram.com/")
    time.sleep(6)
    button = driver.find_element(
        By.XPATH, '//button[text()="Only allow essential cookies"]'
    )
    button.click()
    time.sleep(6)
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")

    username.click()
    username.send_keys(uname)
    password.click()
    password.send_keys(paswo)
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
        print("Button not found. Wrong Username/Password?")
        quit()
    try:
        notifics = driver.find_element(By.XPATH, '//button[text()="Not Now"]')
        notifics.click()
        time.sleep(6)
        print("Clicking on Notifications button")
    except:
        print("Button not found. Skipping notifications button.")
        pass


def Randomsleep():
    _sleep = random.randint(60, 120)
    time.sleep(_sleep)


def SelectAutof():
    print("Please select the function: ")
    print("1. AutoFollow people who followed particular page")
    print("2. AutoFollow everyone who liked the particular post")
    print("3. UnFollow everyone from your page")
    selectf = input()
    if selectf == "1":
        igpagef = input("Please enter the IG page username: ")
        driver.get(f"https://www.instagram.com/{igpagef}/followers")
        time.sleep(8)
        Follow()
    if selectf == "2":
        postcode = input(
            "Please enter the IG post code https://www.instagram.com/p/xxxxxxxx/: "
        )
        driver.get(f"https://www.instagram.com/p/{postcode}/liked_by")
        time.sleep(8)
        FollowP()
    if selectf == "3":
        myig = input("Enter your IG username")
        driver.get(f"https://www.instagram.com/{myig}/following/")
        time.sleep(5)
        UnFollow()


def Follow():
    scroll = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]",
    )
    while True:
        for _ in range(2):
            time.sleep(5)
            driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", scroll
            )
        fbuttons = driver.find_elements(By.CSS_SELECTOR, "._aano div div button")
        try:
            for button in fbuttons:
                if button.text == "Follow":
                    button.click()
                    print("Followed!")
                    Randomsleep()
        except:
            print("Can't find follow button, all people already followed?")
            time.sleep(3)
            SelectAutof()


def FollowP():
    scroll1 = driver.find_element(By.XPATH, "/html")
    while True:
        for _ in range(2):
            time.sleep(5)
            driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", scroll1
            )
        fbuttonsp = driver.find_elements(By.XPATH, '//div[text()="Follow"]')
        try:
            for button in fbuttonsp:
                if button.text == "Follow":
                    button.click()
                    print("Followed!")
                    Randomsleep()
        except:
            print("Can't find follow button, all people already followed?")
            time.sleep(3)
            SelectAutof()


def UnFollow():
    scroll3 = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]",
    )
    while True:
        for _ in range(2):
            time.sleep(5)
            driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", scroll3
            )
        ubuttons = driver.find_elements(By.CSS_SELECTOR, "._aano div div button")
        try:
            for button in ubuttons:
                if button.text == "Following":
                    button.click()
                    time.sleep(3)
                    s = driver.find_element(By.XPATH, '//button[text()="Unfollow"]')
                    s.click()
                    print("UnFollowed!")
                    Randomsleep()
        except:
            print("Can't find unfollow button, all people already followed?")
            time.sleep(3)
            SelectAutof()


login()
SelectAutof()
