import time
globalLista = []
arq = open('Informações.txt', 'w')

class client:
    nome = str()
    cpf  = str()
    data_nascimento = str()
    plano           = str()
    endereco = []

def cadastrar():
    person = client() #classe 
    person.nome = str(input("Digite seu nome:"))
    person.cpf = str(input('cpf:'))
    person.data_nascimento = str(input('Data de nascimento:'))
    globalLista.append(person)

def listar():
   for i in range(len(globalLista)):
    print(f'Nome:{globalLista[i].nome}')
    print(f'CPF:{globalLista[i].cpf}')
    print(f'Data de nascimento:{globalLista[i].data_nascimento}')
    if len(globalLista[i].plano) > 0:
        print('Plano: ' + globalLista[i].plano)

def pesquisar(): #dentro da função editar
    cpf = str(input('Pesquise pelo CPF:'))
    for i in range(len(globalLista)):
        if cpf == globalLista[i].cpf:
            return i 

def editar():
    idx = pesquisar()
    print('''
    [1] Nome
    [2] CPF
    [3] Data de nasciemento ''')

    pergunta = int(input('Opção que será editada:'))
    
    if pergunta == 1:
        globalLista[idx].nome = input('Reescreva aqui:')
    elif pergunta == 2:
        globalLista[idx].cpf = input('Reescreva aqui:')
    elif pergunta == 3:
        globalLista[idx].data_nascimento = input('Reescreva aqui:')

 #PARTE LETÍCIA 
def remover_pessoa():
    print("### Remover cliente ###")
    idx = pesquisar()
    del globalLista[idx]

def salvar():
    globalLista.append()
    salvar()

#PARTE YLANA

def sugestao(): 

    #ESQUEMA CONTADOR
    pacote1 = []
    pacote2 = []
    pacote3 = []
    resultado1 = ('O MELHOR PACOTE PARA VOCÊ É O: CompNet Residencia')
    resultado2 = ('O MELHOR PACOTE PARA VOCÊ É O:  CompNet Residencial Plus')
    resultado3 = ('O MELHOR PACOTE PARA VOCÊ É O: CompNet Gamer')   
    #PARTE INICIAL: INSTRUÇÕES 
    print('='*100)
    print("\033[1;33mOlá, vamos ajudar você na escolha da melhor oferta\033[m")
    print('='*100)
    print("""
            PAINEL DE INSTRUÇÕES!
            Olá, seja bem-vindo(a) aos serviços da CompNet.
            Responda as seguintes perguntas para analisarmos qual o melhor serviço para você.

            OBS:
            RESPONDA USANDO AS OPÇÕES: 'a', 'b' , 'c' ou 'd'
            """)
    print('='*100)
    print('\033[;7mINICIANDO PESQUISA...\033[m')
    time.sleep(2)

    #PERGUNTAS PARA O USUARIO
    def question1 ():
        print(''' 
    \033[1;33m === Como você pretende usar sua internet? === \033[m 
        [A] Navegar em redes sociais  
        [B] Jogar on-line
        [C] Assistir séries/filmes ou ouvir música
        [D] Carregar e baixar arquivos
        ''')
        resp = str(input('escolha uma alternativa: '))
        print(resp)
        if resp == 'a':
            pacote1.append(resp)
        elif resp == 'b':
            pacote3.append(resp)
        elif resp == 'c':
            pacote2.append(resp)
        elif resp == 'd':
            pacote2.append(resp)
        

    def question2 ():
        print(''' 
    \033[1;33m === Quantos dispositivos estariam conectados na internet ao mesmo tempo?  === \033[m 
        [A] 1 a 5  
        [B] 5 a 10
        [C] Mais de 10
        ''')
        resp = str(input('escolha uma alternativa: '))
        if resp == 'a':
            pacote1.append(resp)
        elif resp == 'b':
            pacote1.append(resp)
        elif resp == 'c':
            pacote2.append(resp)


    def question3 ():
        print(''' 
    \033[1;33m === Você também procura um plano celular?  === \033[m 
        [A] Sim 
        [B] Não
        ''')
        resp = str(input('escolha uma alternativa: '))
        if resp == 'a':
            pacote2.append(resp)
        elif resp == 'b':
            pacote1.append(resp)

    def question4 ():
        print(''' 
    \033[1;33m === Qual média de valor você gastaria de gastar?  === \033[m 
        [A] Até 100 reais 
        [B] 100 a 200 reais
        [C] Acima de 200 reais
        ''')
        resp = str(input('escolha uma alternativa: '))
        if resp == 'a':
            pacote1.append(resp)
        elif resp == 'b':
            pacote2.append(resp)
        elif resp == 'c':
            pacote3.append(resp)

        #SISTEMA DE PONTOS PARA SABER QUAL O MAIS INDICADO 
        print(pacote1)
        print(pacote2)
        print(pacote3)

        quantidade_lista1 = pacote1
        print(f'quantidade de elementos 1: ', len(quantidade_lista1))
        quantidade_lista2 = pacote2
        print(f'quantidade de elementos 2: ', len(quantidade_lista2))
        quantidade_lista3 = pacote3
        print(f'quantidade de elementos 3: ', len(quantidade_lista3))

        print('='*100)
        print('COMPNET SERVIÇOS ')
        print('Analisando respostas...')
        time.sleep(0.50)
        print('='*100)

        #CONDIÇÕES
        if quantidade_lista1 > quantidade_lista2 and quantidade_lista1 > quantidade_lista3:
            print(resultado1)
        elif quantidade_lista2 > quantidade_lista1 and quantidade_lista2 > quantidade_lista3:
            print(resultado2)
        elif quantidade_lista3 > quantidade_lista1 and quantidade_lista3 > quantidade_lista2:
            print(resultado3)

        
        time.sleep(2)
        print('=== \033[1mOBRIGADA PELA PREFERÊNCIA \033[m ===')
        
    question1()
    question2()
    question3()
    question4()

#MENU

def menuPrincipal():
    while True:
        print(''' 
                * MENU PRINCIPAL *

                    [1] Cadastrar  
                    [2] Listar Dados
                    [3] Editar
                    [4] Sugestão de Pacote   
                    [5] Escolher Plano 
                    [6] Cancelar compra 
                    ''') #[7] Salvar -> função que deve ser chamada automaticamente no final do código 

        m = int(input('Opção:'))
        if m == 1:
            cadastrar()
        elif m == 2:
            listar()
        elif m == 3:
            editar()
        elif m == 4:
            sugestao()
        elif m == 5:
            pass
        elif m == 6:
            remover_pessoa()

menuPrincipal()