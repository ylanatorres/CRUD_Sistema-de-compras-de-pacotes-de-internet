'''
arquivo = open("listar.txt", "a")

frases = list()
frases.append("TreinaWeb \n")
frases.append("Python \n")
frases.append("Arquivos \n")
frases.append("Django \n")

arquivo.writelines(frases)
'''
globalLista = []

arq = open('Informações.txt', 'w')
def salvar():
globalLista.append(arq)
def listar():
   for i in range(len(globalLista)):
    print(f'Nome:{globalLista[i].nome}')
    print(f'CPF:{globalLista[i].cpf}')
    print(f'Data de nascimento:{globalLista[i].data_nascimento}')
    if len(globalLista[i].plano) > 0:
        print('Plano: ' + globalLista[i].plano)
        salvar()