from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from time import sleep



class testeob:

    def abrir_chrome(self):
        driver: WebDriver = webdriver.Chrome()
        url = "https://www.zapimoveis.com.br/"
        driver.get(url)
        driver.find_element_by_xpath('//*[@id="app"]/section/section[1]/div/section/form/div/div[1]/div[1]/div/button[2]').click()
        driver.find_element_by_css_selector('#l-select1 > optgroup:nth-child(2) > option:nth-child(1)').click()
        driver.find_element_by_xpath('//*[@id="app"]/section/section[1]/div/section/form/div/div[2]/div/div/div/input').send_keys('Niterói, Icarai')
        driver.find_element_by_xpath('//*[@id="app"]/section/section[1]/div/section/form/div/div[2]/button').send_keys(Keys.ENTER)
        sleep(4)


    def raspagem_dados(self):
        self.valores_aluguel_text = []

        cont = 1
        for i in range(10):
            try:
                valores_aluguel = self.driver.find_elements_by_xpath('//p[@class="simple-card__price js-price heading-regular heading-regular__bolder align-left"]')
                for valor_aluguel in valores_aluguel:
                    self.valores_aluguel_text.append(valor_aluguel.text)
                #  sleep(1)
            except:
                print("Não foi possível raspar os valores de aluguel da página " + str(cont))

start = testeob()
start.abrir_chrome()
start.raspagem_dados()