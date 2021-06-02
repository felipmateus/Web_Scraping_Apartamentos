
def f_apartamento_ideal(valores_aluguel_text, valores_iptu_text, valores_condominio_text):


    # valor_aluguel_inteiro = []
    # valor_iptu_inteiro = []
    #
    # for valor_aluguel_text in valores_aluguel_text:
    #     valor_aluguel_inteiro.append(float(valor_aluguel_text))
    # for valor_iptu in valores_iptu_text:
    #     valor_iptu_inteiro.append(float(valor_iptu))

    # zipped_lists = zip(valores_aluguel_text, valores_iptu_text, valores_condominio_text)
    #
    # sum = [x + y + z for (x, y, z) in zipped_lists]
    #
    # valor_maximo = max(sum)
    # valor_minimo = min(sum)
    #
    # print(valor_minimo, valor_maximo)

    list3 = []

    for i in range(len(valores_aluguel_text)):
        if type(valores_aluguel_text[i]) == float and type(valores_iptu_text[i]) == float and type(valores_condominio_text[i]) == float:
            list3.append(valores_aluguel_text[i] + valores_iptu_text[i] + valores_condominio_text[i])
        else:
            print('nao foi possivel somar')

    valor_maximo = max(list3)
    valor_minimo = min(list3)

    print("Custo total minimo e: ", valor_minimo,  "O valor total maximo e : ",  valor_maximo)
    print(valores_aluguel_text)
    print(valores_condominio_text)
    print(valores_iptu_text)
    print(list3)
