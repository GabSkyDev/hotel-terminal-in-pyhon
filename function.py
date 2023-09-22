# Variáveis globais
nome = []
cpf = []
dias = []
indice = []
despesa = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0

# Função que apresenta os textos do menu
def menu ():
    print('Bem Vindo! Digite uma opção para continuar!')
    print("Digite 1 para Registrar Hóspedes")
    print("Digite 2 para Pesquisar Hóspedes")
    print("Digite 3 para Reservar Área de Lazer")
    print("Digite 4 para Calcular o Total")
    print("Digite 0 para Sair")

# Função que monta a estrutura principal do Hotel, na qual executa uma série de funções de acordo com a opção escolhida
def escolhaMenu ():
    global i, nome, cpf, dias, indice, despesa
    menu()
    choose = int(input('Sua opção escolhida é: '))
    if choose == 1:
        registrarHospedes()
        voltaMenu()
    elif choose == 2:
        exibirHospedes()
        voltaMenu()
    elif choose == 3:
        exibirHospedes()
        areaLazer()
        voltaMenu()
    elif choose == 4:
        exibirHospedes()
        exibirTotal()
        voltaMenu()
    elif choose == 0:
        print('Obrigado por utilizar nossos serviços!')
        voltaMenu()
    else:
        print('Opção Inválida!')
        voltaMenu()

# Essa função abaixo questiona se o usuário deseja voltar ao menu após realizar o procedimento
def voltaMenu ():
    global i, nome, cpf, dias, indice, despesa
    while True:
        back = str(input('Gostaria de voltar ao menu? (S/N): '))
        if back == 'S' or back == 's' or back == 'Sim' or back == 'sim':
            escolhaMenu()
            break
        else:
            print('Tente Novamente!')

# Essa função realiza uma série de perguntas para registrar os hóspedes no hotel
def registrarHospedes ():
    global i, nome, cpf, dias, indice, despesa
    if i == 10:
        print('O registro de hóspedes está cheio! ')
        voltaMenu()
    else:
        while True:
            n = str(input("Você selecionou a opção 'Registro de Hóspedes'\nDigite o nome do hóspede: "))
            nome.append(n)
            c = str(input(f"Digite o CPF de {n}: "))
            cpf.append(c)
            d = int(input(f"Digite quantos dias {n} vai reservar: "))
            dias.append(d)
            indice.append(i)
            print(f"=== INFORMAÇÕES ===\nÍndice: {i}\nNome: {n}\nCPF: {c}\nDias: {d}\n===================")
            confirm = str(input(f"Você confirma as informações de {n}? (S/N): "))
            if confirm == "S" or confirm == "Sim" or confirm == "s" or confirm == "sim":
                i += 1
                print('Cadastro realizado com sucesso!')
                voltaMenu()

# A função abaixo faz uma exibição das informações essenciais dos hóspedes cadastrados
def exibirHospedes():
    global i, nome, cpf, dias, indice, despesa
    print("Os hóspedes cadastrados são: \n")

    for i in range(len(nome)):
        if dias[i] >= 0:
            print(f"Índice: {indice[i]}")
            print(f"Nome: {nome[i]}")
            print(f"CPF: {cpf[i]}")
            print(f"Quantidade de dias: {dias[i]} \n")
            i += 1

# A função logo abaixo permite que o usuário possa usufruir dos componentes do hotel e ter o valor adicionado a despesa
def areaLazer ():
    global i, nome, cpf, dias, indice, despesa
    pesquisa = int(input('Digite o índice do hóspede desejado: '))
    print("Para utilizar a 'Academia' digite 'A'")
    print("Para utilizar o 'Salão de Festas' digite 'S'")
    print("Para utilizar o 'Restaurante' digite 'R'")
    lazer = str(input("Digite a área de lazer desejada (A/S/R): "))

    if lazer == "A" or lazer == "a":
        despesa[pesquisa] += 20
        print('O valor foi adicionado a sua conta!')
    elif lazer == "S" or lazer == "s":
        despesa[pesquisa] += 50
        print('O valor foi adicionado a sua conta!')
    elif lazer == "R" or lazer == "r":
        despesa[pesquisa] += 35
        print('O valor foi adicionado a sua conta!')
    else:
        print("Àrea Inválida! Tente Novamente!")
        voltaMenu()

# Essa função abaixo exibe o total que cada usuário deve pagar de acordo com sua diária e atividades no hotel
def exibirTotal ():
    global i, nome, cpf, dias, indice, despesa
    while True:
        pesquisa = int(input('Digite o índice do hóspede desejado: '))
        if pesquisa < 0:
            print('"posição inexiste e/ou posição não ocupada por um hóspede!\nTente Novamente!')
        if pesquisa >= 0:
            total = despesa[pesquisa] + 100 * dias[pesquisa]
            print(f"O hóspede {nome[pesquisa]} tem um gasto total de {total}  Reais!")
            voltaMenu()
