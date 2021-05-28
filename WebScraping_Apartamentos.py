from scraping import raspagem_dados
from criar_planilha import criar_planilha_excel
from Abrir_Chrome import abrir_chrome
from enviar_email import enviar_email


abrir_chrome()
raspagem_dados()
criar_planilha_excel()
enviar_email()
