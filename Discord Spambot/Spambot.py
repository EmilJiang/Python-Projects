from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
chromedriver = "/Users/Emil/Downloads/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.get("https://discord.com/login")
sleep(4)
element = driver.find_element_by_name("email")
element.send_keys(input("username "))
element1 = driver.find_element_by_name("password")
element1.send_keys(input("password "))
element1.send_keys(Keys.RETURN)
sleep(7)
name = input("discord name ")
name1 = driver.find_element_by_xpath('//div[contains(text(), ' + "'" + name + "'" ')]').click()
text = driver.find_element_by_xpath('//*[@id = "app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div[3]/div[2]')
num = input("how many times ")
text1 = input("what to spam ")
for i in range(0, int(num)):
    if text1[0] == "@":
        text.send_keys(text1)
        sleep(.7)
        text.send_keys(Keys.RETURN)
        text.send_keys(Keys.RETURN)
    else:
        text.send_keys(text1)
        sleep(1)
        text.send_keys(Keys.RETURN)
y = input("Again? Y/N ")
sleep(3)
if y == "Y":
    name = input("discord name ")
    name1 = driver.find_element_by_xpath('//div[contains(text(), ' + "'" + name + "'" ')]').click()
    text = driver.find_element_by_xpath(
        '//*[@id = "app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div[3]/div[2]')
    num = input("how many times ")
    text1 = input("what to spam ")
    for i in range(0, int(num)):
        if text1[0] == "@":
            text.send_keys(text1)
            sleep(.7)
            text.send_keys(Keys.RETURN)
            text.send_keys(Keys.RETURN)
        else:
            text.send_keys(text1)
            sleep(.7)
            text.send_keys(Keys.RETURN)
else:
    driver.quit()
