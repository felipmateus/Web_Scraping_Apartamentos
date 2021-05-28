from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def abrir_chrome():
    driver: WebDriver = webdriver.Chrome()
    url = "https://www.zapimoveis.com.br/"
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="app"]/section/section[1]/div/section/form/div/div[1]/div[1]/div/button[2]').click()
    driver.find_element_by_css_selector('#l-select1 > optgroup:nth-child(2) > option:nth-child(1)').click()
    driver.find_element_by_xpath('//*[@id="app"]/section/section[1]/div/section/form/div/div[2]/div/div/div/input').send_keys('Niterói, Icarai')
    driver.find_element_by_xpath('//*[@id="app"]/section/section[1]/div/section/form/div/div[2]/button').send_keys(Keys.ENTER)
    sleep(2)
