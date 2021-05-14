import csv
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

        cont = 1
        for i in range(2):
            try:
                valores_aluguel = self.driver.find_elements_by_xpath('//p[@class="simple-card__price js-price heading-regular heading-regular__bolder align-left"]')
                for valor_aluguel in valores_aluguel:
                    self.valores_aluguel_corrigido = valor_aluguel.text
                # sleep(1)
            except:
                print("Não foi possível raspar os valores de aluguel da página " + str(cont))

            # try:
            #     valores_iptu = self.driver.find_elements_by_xpath("//li[@class='card-price__item iptu text-regular']")
            #     for valor_iptu in valores_iptu:
            #         self.valores_iptu_corrigido = valor_iptu.text
            #     # sleep(1)
            # except:
            #     print("Não foi possível obter os valores de IPTU da página " + str(cont))
            #
            # try:
            #     descricoes_apartamentos = self.driver.find_elements_by_xpath('//div[@class="collapse simple-card__description"]')
            #     for descricao_apartamento in descricoes_apartamentos:
            #         self.descricoes = descricao_apartamento.text
            #     # sleep(1)
            # except:
            #     print("Não foi possível obter as descrições dos apartamentos da página " + str(cont))
            #
            # try:
            #     valores_condominio = self.driver.find_elements_by_xpath('//li[@class="card-price__item condominium text-regular"]')
            #     for valor_condominio in valores_condominio:
            #         self.valores_condominio_corrigidos = valor_condominio.text
            #     # sleep(1)
            # except:
            #     print("Não foi possível obter os valores dos condomínios da página " + str(cont))
            #
            # try:
            #     enderecos = self.driver.find_elements_by_xpath('//p[@class="color-dark text-regular simple-card__address"]')
            #     for endereco in enderecos:
            #         self.enderecos_corrigidos = endereco.text
            #     # sleep(1)
            # except:
            #     print("Não foi possível obter os endereços da página " + str(cont))
            #
            # try:
            #     area_apartamentos = self.driver.find_elements_by_xpath('//li[@class="feature__item text-small js-areas"]')
            #     for area_apartamento in area_apartamentos:
            #         self.area_apartamentos_corrigidos = area_apartamento.text
            #     # sleep(1)
            # except:
            #     print("Não foi possível obter as áreas dos apartamentos da página " + str(cont))
            #
            # try:
            #     numero_quartos = self.driver.find_elements_by_xpath('//li[@class="feature__item text-small js-bedrooms"]')
            #     for numero_quarto in numero_quartos:
            #         self.numero_quartos_corrigidos = numero_quarto.text
            #     # sleep(1)
            # except:
            #     print("Não foi possível obter os números dos quartos da página" + str(cont))
            #
            # try:
            #     numero_vagas = self.driver.find_elements_by_xpath('//li[@class="feature__item text-small js-parking-spaces"]')
            #     for numero_vaga in numero_vagas:
            #         self.numero_vagas_corrigidas = numero_vaga.text
            #     # sleep(1)
            # except:
            #     print("Não foi possível obter os números das vagas da página" + str(cont))
            #
            # try:
            #     numero_banheiros = self.driver.find_elements_by_xpath('//li[@class="feature__item text-small js-bathrooms"]')
            #     for numero_banheiro in numero_banheiros:
            #         self.numero_banheiros_corrigidos = numero_banheiro.text
            #     # sleep(1)
            # except:
            #     print("Não foi possível obter os números dos baneheiros da página" + str(cont))
            #
            try:
                cont = cont + 1
                self.driver.find_element_by_xpath('//button[@class="pagination__button pagination__button--next js-next-page button button-primary button-primary--outline button--regular button--icon"]').send_keys(Keys.ENTER)
                print("Próxima página")
                sleep(1)
            except:
                print("Não há mais páginas")

    def criar_planilha(self):
        with open(r'C:\Users\Felipe\PycharmProjects\webscraping_apartamento\teste.csv', 'w', newline='') as result_file:
            wr = csv.writer(result_file, dialect='excel')
            wr.writerow(self.valores_aluguel_corrigido)
            # wr.writerow(self.descricao)
            # wr.writerow(self.valores_condominio_corrigidos)
            # wr.writerow(self.valores_iptu_corrigido)
            # wr.writerow(self.enderecos_corrigidos)
            # wr.writerow(self.area_apartamentos_corrigidos)
            # wr.writerow(self.numero_quartos_corrigidos)
            # wr.writerow(self.numero_vagas_corrigidas)
            # wr.writerow(self.numero_banheiros_corrigidos)






start = scrappy()
start.iniciar()
start.raspagem_dados()
start.criar_planilha()
