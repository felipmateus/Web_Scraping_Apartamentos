##  O chromedrive foi importado para o sistema de froma direta nas variaveis do sitema

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from time import sleep


def get_system():

    driver: WebDriver = webdriver.Chrome()
    url = "https://www.zapimoveis.com.br/"
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="app"]/section/section[1]/div/section/form/div/div[1]/div[1]/div/button[2]').click()
    driver.find_element_by_css_selector('#l-select1 > optgroup:nth-child(2) > option:nth-child(1)').click()
    driver.find_element_by_xpath('//*[@id="app"]/section/section[1]/div/section/form/div/div[2]/div/div/div/input').send_keys('Niterói, Icarai')
    driver.find_element_by_xpath('//*[@id="app"]/section/section[1]/div/section/form/div/div[2]/button').send_keys(Keys.ENTER)

    ## a função eleep é necessária devido à demora do website para carregar, causando erro caso não o tenha no código
    sleep(2)

    cont = 5
##  provando para o Guilherme q eu aprendi
    for i in range(5):
        cont = cont + 1
        if cont>7:
            cont = cont - 1

        print(cont)
        sleep(5)
        driver.find_element_by_xpath('//*[@id="app"]/section/div[3]/div[2]/section/ul/li['+str(cont)+']/button').send_keys(Keys.ENTER)

    sleep(10)

get_system()
