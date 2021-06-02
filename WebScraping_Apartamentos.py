from scraping import raspagem_dados
from criar_planilha import criar_planilha_excel
from enviar_email import enviar_email
from apartamento_ideal import f_apartamento_ideal

tupla_valores_texts = raspagem_dados()

criar_planilha_excel(tupla_valores_texts[0],tupla_valores_texts[1],tupla_valores_texts[2],tupla_valores_texts[3],tupla_valores_texts[4],tupla_valores_texts[5],tupla_valores_texts[6],tupla_valores_texts[7])

print(tupla_valores_texts[0],tupla_valores_texts[1],tupla_valores_texts[2])
# enviar_email()

f_apartamento_ideal(tupla_valores_texts[0],tupla_valores_texts[1], tupla_valores_texts[2])
