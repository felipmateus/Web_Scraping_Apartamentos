from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from time import sleep



def raspagem_dados():

    driver: WebDriver = webdriver.Chrome()

    url = "https://www.zapimoveis.com.br/"
    driver.get(url)
    driver.find_element_by_xpath(
        '//*[@id="app"]/section/section[1]/div/section/form/div/div[1]/div[1]/div/button[2]').click()
    driver.find_element_by_css_selector('#l-select1 > optgroup:nth-child(2) > option:nth-child(1)').click()
    driver.find_element_by_xpath(
        '//*[@id="app"]/section/section[1]/div/section/form/div/div[2]/div/div/div/input').send_keys('Niterói, Icarai')
    driver.find_element_by_xpath('//*[@id="app"]/section/section[1]/div/section/form/div/div[2]/button').send_keys(
        Keys.ENTER)
    sleep(2)

    valores_aluguel_text = []
    valores_iptu_text = []
    valores_condominio_text = []
    enderecos_text = []
    tamanho_m2_apartamentos_text = []
    numero_quartos_text = []
    numero_vagas_text = []
    numero_banheiros_text = []




    cont = 1
    for i in range(2):
        try:
            valores_aluguel = driver.find_elements_by_xpath(
                '//p[@class="simple-card__price js-price heading-regular heading-regular__bolder align-left"]')
            for valor_aluguel in valores_aluguel:
                valores_aluguel_text.append(float((valor_aluguel.text.split("R$")[1].split("/mês")[0])))
            #  sleep(1)
        except:
            print("Não foi possível raspar os valores de aluguel da página " + str(cont))

        try:
            valores_iptu = driver.find_elements_by_xpath("//li[@class='card-price__item iptu text-regular']")
            for valor_iptu in valores_iptu:
                valores_iptu_text.append((float(valor_iptu.text.split("IPTU R$")[1])))
            # sleep(1)
        except:
            print("Não foi possível obter os valores de IPTU da página " + str(cont))

        # try:
        #     descricoes_text = []
        #     descricoes_apartamentos = driver.find_elements_by_xpath('//div[@class="collapse simple-card__description"]')
        #     for descricao_apartamento in descricoes_apartamentos:
        #         descricoes_text.append(descricao_apartamento.text)
        # sleep(1)
        #
        # except:
        #     print("Não foi possível obter as descrições dos apartamentos da página " + str(cont))

        try:
            valores_condominio = driver.find_elements_by_xpath(
                '//li[@class="card-price__item condominium text-regular"]')
            for valor_condominio in valores_condominio:
                valores_condominio_text.append((float(valor_condominio.text.split("condomínio R$")[1])))
            # sleep(1)
        except:
            print("Não foi possível obter os valores dos condomínios da página " + str(cont))

        try:
            enderecos = driver.find_elements_by_xpath('//p[@class="color-dark text-regular simple-card__address"]')
            for endereco in enderecos:
                enderecos_text.append(endereco.text)
        except:
            print("Não foi possível obter os endereços da página " + str(cont))

        try:
            tamanho_m2_apartamentos = driver.find_elements_by_xpath(
                '//li[@class="feature__item text-small js-areas"]')
            for tamanho_m2_apartamento in tamanho_m2_apartamentos:
                tamanho_m2_apartamentos_text.append(tamanho_m2_apartamento.text)
        except:
            print("Não foi possível obter as áreas dos apartamentos da página " + str(cont))

        try:
            numero_quartos = driver.find_elements_by_xpath('//li[@class="feature__item text-small js-bedrooms"]')
            for numero_quarto in numero_quartos:
                numero_quartos_text.append(numero_quarto.text)
        except:
            print("Não foi possível obter os números dos quartos da página" + str(cont))

        try:
            numero_vagas = driver.find_elements_by_xpath(
                '//li[@class="feature__item text-small js-parking-spaces"]')
            for numero_vaga in numero_vagas:
                numero_vagas_text.append(numero_vaga.text)
        except:
            print("Não foi possível obter os números das vagas da página" + str(cont))

        try:
            numero_banheiros = driver.find_elements_by_xpath(
                '//li[@class="feature__item text-small js-bathrooms"]')
            for numero_banheiro in numero_banheiros:
                numero_banheiros_text.append(numero_banheiro.text)
        except:
            print("Não foi possível obter os números dos baneheiros da página" + str(cont))

        try:
            cont = cont + 1
            driver.find_element_by_xpath(
                '//button[@class="pagination__button pagination__button--next js-next-page button button-primary button-primary--outline button--regular button--icon"]').send_keys(
                Keys.ENTER)
            print("Próxima página")
            sleep(1)
        except:
            print("Não há mais páginas")


    return (valores_aluguel_text, valores_iptu_text,valores_condominio_text, enderecos_text, tamanho_m2_apartamentos_text,numero_quartos_text,numero_vagas_text,numero_banheiros_text)