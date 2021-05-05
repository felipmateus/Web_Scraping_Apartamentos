##  O chromedrive foi importado para o sistema de froma direta nas variaveis do sitema

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from time import sleep


def get_system():
##   Nessa parte eu entro com os parâmetros de pesquisa do apartamento
    driver: WebDriver = webdriver.Chrome()
    url = "https://www.zapimoveis.com.br/"
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="app"]/section/section[1]/div/section/form/div/div[1]/div[1]/div/button[2]').click()
    driver.find_element_by_css_selector('#l-select1 > optgroup:nth-child(2) > option:nth-child(1)').click()
    driver.find_element_by_xpath('//*[@id="app"]/section/section[1]/div/section/form/div/div[2]/div/div/div/input').send_keys('Niterói, Icarai')
    driver.find_element_by_xpath('//*[@id="app"]/section/section[1]/div/section/form/div/div[2]/button').send_keys(Keys.ENTER)

##  a função eleep é necessária devido à demora para carregar o website, causando erro caso não o tenha no código
    sleep(2)

##  foi necessário implementar um contador para driblar o site para conseguir localizar o botão de próxima página
    cont = 5

## o primeiro laço de repetição é para direcionar para próxima página
    for i in range(20):
##  o sengundo laço é para raspar todas as informações essenciais da página
        for i in range(20):
            dados = driver.find_element_by_xpath('//*[@id="app"]/section/div[3]/div[2]/section/div/div[1]/div/div[2]')
            print(dados.text)
        cont = cont + 1
##  foi necessário colocar uma condição para driblar o site e localizar o botão próxima página
        if cont>7:
            cont = cont - 1
            print('PRÓXIMA PÁGINA')
            driver.find_element_by_xpath('//*[@id="app"]/section/div[3]/div[2]/section/ul/li['+str(cont)+']/button').send_keys(Keys.ENTER)
        else:
            driver.find_element_by_xpath('//*[@id="app"]/section/div[3]/div[2]/section/ul/li[' + str(cont) + ']/button').send_keys(Keys.ENTER)
        sleep(5)

get_system()
