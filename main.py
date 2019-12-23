from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path=r"C:\REPLOCATION\Osu-Message-Sender\chromedriver.exe")

# don't forget to remove the top 6 people in users after using this script
with open("users.txt") as file:
    users = [next(file) for i in range(6)]

with open("message.txt") as file:
    message = file.readlines()
message = [line[:-1] for line in message]

browser.get('https://osu.ppy.sh/forum/ucp.php?i=pm&mode=compose')
elem = browser.find_element_by_name('username')
elem.clear()
elem.send_keys('YOURUSERNAME')
elem = browser.find_element_by_name('password')
elem.clear()
elem.send_keys('YOURPASSWORD')
elem.send_keys(Keys.RETURN)

elem = browser.find_element_by_name('subject')
elem.send_keys('YOURSUBJECT')

# the number might vary from which icon you want
elem = browser.find_element_by_xpath('//input[@id="17"]')
elem.click()

elem = browser.find_element_by_name('message')
for line in message:
    elem.send_keys(line)
    elem.send_keys(Keys.RETURN)

elem = browser.find_element_by_name('username_list')
for user in users:
    elem.send_keys(user)
    elem.send_keys(Keys.RETURN)

elem = browser.find_element_by_name('add_to')
elem.click()

elem = browser.execute_script('return submitForm("post");')
