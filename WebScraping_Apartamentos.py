## Foi necessário implementar um contador para driblar o site e conseguir localizar o botão da próxima página.

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class scrappy:

    def iniciar(self):
        self.driver: WebDriver = webdriver.Chrome()
        url = "https://www.zapimoveis.com.br/"
        self.driver.get(url)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section[1]/div/section/form/div/div[1]/div[1]/div/button[2]').click()
        self.driver.find_element_by_css_selector('#l-select1 > optgroup:nth-child(2) > option:nth-child(1)').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section[1]/div/section/form/div/div[2]/div/div/div/input').send_keys('Niterói, Icarai')
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section[1]/div/section/form/div/div[2]/button').send_keys(Keys.ENTER)
        sleep(2)

    def raspagem_dados(self):
        cont = 5
        for i in range(20):
            for i in range(20):
                dados = self.driver.find_element_by_xpath('//*[@id="app"]/section/div[3]/div[2]/section/div/div[1]/div/div[2]')
                print(dados.text)




            cont = cont + 1
            if cont>7:
                cont = cont - 1
                print('PRÓXIMA PÁGINA')
                self.driver.find_element_by_xpath('//*[@id="app"]/section/div[3]/div[2]/section/ul/li[' + str(cont) + ']/button').send_keys(Keys.ENTER)
            else:
                self.driver.find_element_by_xpath('//*[@id="app"]/section/div[3]/div[2]/section/ul/li[' + str(cont) + ']/button').send_keys(Keys.ENTER)
            sleep(5)

start = scrappy()
start.iniciar()
start.raspagem_dados()


