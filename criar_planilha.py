import openpyxl
import WebScraping_Apartamentos as ws


def criar_planilha_excel():
    wb = openpyxl.Workbook()

    wb['Sheet'].title = "Report Automation"

    sh1 = wb.active

    index1 = 1
    for i in ws.self.valores_aluguel_text:
        sh1.cell(column=1, row=index1, value=i)
        index1 = index1 + 1

    index2 = 1
    for valor_iptu in ws.self.valores_iptu_text:
        sh1.cell(column=2, row=index2, value=valor_iptu)
        index2 = index2 + 1

    index3 = 1
    for valor_condomio in ws.self.valores_condominio_text:
        sh1.cell(column=3, row=index3, value=valor_condomio)
        index3 = index3 + 1

    index4 = 1
    for endereco in ws.self.enderecos_text:
        sh1.cell(column=4, row=index4, value=endereco)
        index4 = index4 + 1

    index5 = 1
    for tamanho_m2_apartamento in ws.self.tamanho_m2_apartamentos_text:
        sh1.cell(column=5, row=index5, value=tamanho_m2_apartamento)
        index5 = index5 + 1

    index6 = 1
    for numero_quarto in ws.self.numero_quartos_text:
        sh1.cell(column=6, row=index6, value=numero_quarto)
        index6 = index6 + 1

    index7 = 1
    for numero_vaga in ws.self.numero_vagas_text:
        sh1.cell(column=7, row=index7, value=numero_vaga)
        index7 = index7 + 1

    index8 = 1
    for numero_banheiro in ws.self.numero_banheiros_text:
        sh1.cell(column=8, row=index8, value=numero_banheiro)
        index8 = index8 + 1

    wb.save("C:\\Users\\Felipe\\PycharmProjects\\webscraping_apartamento\\treinando_excel2.xlsx")