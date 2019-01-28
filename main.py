 # -*- coding: Shift-JIS -*-
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome("chromedriver.exe")
driver.get('https://www.itpassportsiken.com/ipkakomon.php')

driver.find_element_by_class_name('submit').click()

for i in range(150):
    driver.find_element_by_class_name('selectBtn').click()
    sleep(3)
    driver.find_element_by_class_name('submit').click()
    sleep(3)

#まあ自動で解いてくれるっつっても結局はランダムにボタンを押すのを自動化しただけなんだけどねテヘペロ
