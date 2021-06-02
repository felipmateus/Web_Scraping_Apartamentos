
def f_apartamento_ideal(valores_aluguel_text, valores_iptu_text, valores_condominio_text):

    zipped_lists = zip(valores_aluguel_text, valores_iptu_text)

    sum = [x + y for (x, y) in zipped_lists]
    print(sum)

    # list3 = []
    #
    # for i in range(len(valores_aluguel_text)):
    #     if type(valores_aluguel_text[i]) == int and type(valores_iptu_text[i]) == int and type(valores_condominio_text[i]) == int:
    #         list3.append(valores_aluguel_text[i] + valores_iptu_text[i] + valores_condominio_text[i])
    #     else:
    #         print('nao foi possivel somar')

    # valor_maximo = max(list3)
    # valor_minimo = min(list3)
    # print(list3)
