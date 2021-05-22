import enviar_email
from scraping import raspagem_dados
from criar_planilha import criar_planilha


class scrappy:
    raspagem_dados()
    criar_planilha()
    enviar_email()


start = scrappy()