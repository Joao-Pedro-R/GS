import random
pix = random.randint(111111111,999999999) #Utilizando da biblioteca random, se cria uma "chave pix" para o programa
cp = random.randint(00000000,99999999) #Para servir de caixa postal
contas = {} #guarda um cpf com a pontuação obtida
csa = [] #contas para serem analisadas
evpart = {} #guarda um cpf com a quantidade de eventos participados
eventos = ["Ubatuba"] #Lista de eventos de coleta de lixo
pc = ["Metrô Vila Mariana"] #pontos de coleta de doações
part = [] #Lista de contas de nível participante
mod = [12345678910] #Lista de contas de nível moderador (adicionado um "cpf" para fácil manuseamento do programa, NÃO USAR A CONTA "12345678910" PARA AS OUTRAS FUNÇÕES, SOMENTE PARA FUNÇÃO ANALISE)
dados = {} #Dicionario que contem os dados dos usuários

def doacao(): #Função para informar o usuário como ajudar a causa através de doações
    print(" ")
    print("=" * 25)
    print(" " * 8, "DOAÇÃO")
    print("=" * 25)
    print("\nAjude a causa através de doações também:")
    print("(1) - Doações monetárias \n(2) - Doações de materiais e equipamentos")
    escolha = int(input())
    if escolha == 1:
        print(f"Chave Pix: {pix}")
    elif escolha == 2:
        print("Pontos de coleta: ")
        for i in pc:
            print(f"- {i}")
        print(f"Caixa postal: {str(cp[0:5])}-{str(cp[5:8])}")
    else:
        print("Número inválido!")

def participarcoleta(x): #Esta função vai servir para mostrar as uniões de coleta de lixo para se inscrever
    print(" ")
    print("=" * 25)
    print(" " * 3, "PARTICIPAR COLETA")
    print("=" * 25)
    print("\nAtuais eventos de coleta de lixo acontecendo para se inscrever:")
    y = 1
    for i in eventos:
        print(f"{y}° - coleta de lixo localização {i}")
        y += 1
    print("Escolha o número do evento que deseja participar: ")
    escolha = int(input()) - 1
    if len(eventos) - 1 < escolha:
        print("Número Inválido!")
    else:
        print(f"Evento escolhido foi: {eventos[escolha]}")
        print("Os pontos serão adicionados a sua conta após o evento de coleta.")
        evpart[x] += 1
        contas[x] += 100


def virarmod(x): #Esta função serve para se uma conta só tiver o nível participante e acima de x participações em coletas poder virar moderador
    print(" ")
    print("=" * 25)
    print(" " * 7, "VIRAR MOD")
    print("=" * 25)
    if evpart[x] >= 10:
        print("\nSua conta será analisada para receber aumento de nível.")
        csa.append(x)
    else:
        print(f"\nA conta deve ter ao menos 10 participações em eventos, a conta possui atualmente {evpart[x]}.")

def pontuacao(x): #Esta função serve para ver a quantidade de pontos e as possibilidades de gastar
    while True:
        print(" ")
        print("=" * 25)
        print(" " * 7, "PONTUAÇÃO")
        print("=" * 25)
        print("\nEscolha a ação: \n(1) - Ver quantidade de pontos \n(2) - Ver Lista de recompensas \n(3) - Gastar pontos \n(4) - sair")
        escolha = int(input())
        if escolha == 1:
            print(f"Você têm {contas[x]} pontos.")
        elif escolha == 2: #Recompensas não definidas
            print("Lista de recompensas: \n@ Recompensa 1 -- 100 pontos \n@ Recompensa 2 -- 200 pontos \n@ Recompensa 3 -- 400 pontos \n@ Recompensa 4 -- 800 pontos \n@ Recompensa 5 -- 1600 pontos \n@ Recompensa 6 -- 3200 pontos \n@ Recompensa 7 -- 6400 pontos \n@ Recompensa 8 -- 12800 pontos")
        elif escolha == 3:
            print("Lista de recompensas: \n(1) Recompensa 1 -- 100 pontos \n(2) Recompensa 2 -- 200 pontos \n(3) Recompensa 3 -- 400 pontos \n(4) Recompensa 4 -- 800 pontos \n(5) Recompensa 5 -- 1600 pontos \n(6) Recompensa 6 -- 3200 pontos \n(7) Recompensa 7 -- 6400 pontos \n(8) Recompensa 8 -- 12800 pontos")
            resgatar = int(input())
            if resgatar == 1:
                if contas[x] - 100 < 0:
                    print("Pontos insuficientes para a troca!")
                else:
                    contas[x] = contas[x] - 100
                    print("Recompensa 1")
            elif resgatar == 2:
                if contas[x] - 200 < 0:
                    print("Pontos insuficientes para a troca!")
                else:
                    contas[x] = contas[x] - 200
                    print("Recompensa 2")
            elif resgatar == 3:
                if contas[x] - 400 < 0:
                    print("Pontos insuficientes para a troca!")
                else:
                    contas[x] = contas[x] - 400
                    print("Recompensa 3")
            elif resgatar == 4:
                if contas[x] - 800 < 0:
                    print("Pontos insuficientes para a troca!")
                else:
                    contas[x] = contas[x] - 800
                    print("Recompensa 4")
            elif resgatar == 5:
                if contas[x] - 1600 < 0:
                    print("Pontos insuficientes para a troca!")
                else:
                    contas[x] = contas[x] - 1600
                    print("Recompensa 5")
            elif resgatar == 6:
                if contas[x] - 3200 < 0:
                    print("Pontos insuficientes para a troca!")
                else:
                    contas[x] = contas[x] - 3200
                    print("Recompensa 6")
            elif resgatar == 7:
                if contas[x] - 6400 < 0:
                    print("Pontos insuficientes para a troca!")
                else:
                    contas[x] = contas[x] - 6400
                    print("Recompensa 7")
            elif resgatar == 8:
                if contas[x] - 12800 < 0:
                    print("Pontos insuficientes para a troca!")
                else:
                    contas[x] = contas[x] - 12800
                    print("Recompensa 8")
            else:
                print("Número inválido!")
        elif escolha == 4:
            break
        else:
            print("Número inválido!")


def criarcoleta(): #Esta função permite um moderador criar uma união de coleta de lixo
    print(" ")
    print("=" * 25)
    print(" " * 6, "CRIAR COLETA")
    print("=" * 25)
    print("\nInsira a localização para um evento de coleta de lixo: ")
    criar = input()
    print(f"Evento de coleta em {criar} criado.")
    eventos.append(criar)

def analisar(): #Esta função deixa um moderador analisar um pedido de uma conta nível participante para se tornar moderador
    print(" ")
    print("=" * 25)
    print(" " * 8, "ANALISE")
    print("=" * 25)
    print(" ")
    for i in csa:
        print(dados[i][0])
        print("(1) - para promover \n(2) - para recusar")
        escolha = int(input())
        if escolha == 1:
            mod.append(i)
        elif escolha == 2:
            csa.remove(i)
        else:
            print("Número inválido!")

def info(cpf): #Esta função mostra as informações da conta
    print(" ")
    print("=" * 25)
    print(" " * 9, "INFO")
    print("=" * 25)
    print("\nNome do Usuário:")
    print(dados[cpf][0])
    print("--" * 25)
    print("CPF do Usuário:")
    print(f"{str(cpf)[0:3]}.{str(cpf)[3:6]}.{str(cpf)[6:9]}-{str(cpf)[9:11]}")
    print("--" * 25)
    print("Idade do Usuário:")
    print(f"{dados[cpf][1]} anos")
    print("--" * 25)
    print("Estado Civil do Usuário:")
    print(dados[cpf][2])
    print("--" * 25)
    print("Profissão do Usuário:")
    print(dados[cpf][3])
    print("--" * 25)
    if cpf in mod:
        print("Nível: \nModerador")
    else:
        print("Nível: \nParticipante")
    
def criarpc(): #Esta função deixa um moderador criar um ponto de coleta de doações
    print(" ")
    print("=" * 25)
    print(" " * 2, "CRIAR PONTO COLETA")
    print("=" * 25)
    print("\nInsira a localização na qual terá um ponto de coleta para doações: ")
    novopc = input()
    pc.append(novopc)

def cadastro(): #Criar uma conta nível participante
    print(" ")
    print("=" * 25)
    print(" " * 7, "CADASTRO")
    print("=" * 25)
    print(" ")
    while True:
        global ldados #lista de dados
        ldados = []
        print("Insira as informações a seguir para criar uma conta")
        print("CPF (Somente números)")
        cpf2 = int(input())
        if cpf2 in part:
            print("CPF já cadastrado")
            break
        else:
            print("--" * 25)
            print("Nome")
            nome = input()
            ldados.append(nome)
            print("--" * 25)
            print("Idade")
            print("Necessário ter acima de 16 anos para criar uma conta")
            idade = int(input())
            if idade >= 16 and idade <= 120:
                ldados.append(idade)
                print("--" * 25)
                print("Estado Civil")
                ec = input()
                ldados.append(ec)
                print("--" * 25)
                print("Profissão")
                prof = input()
                ldados.append(prof)
                part.append(int(cpf2))
                dados[cpf2] = ldados
                evpart[cpf2] = 0
                contas[cpf2] = 0
                print("--" * 25)
                print("Conta criada.")
                break
            else:
                print("/" * 25)
                print("Idade inválida!")
                print("/" * 25)

def menup(): #Entrar em uma conta participante
    while True:

        print(" ")
        print("=" * 25)
        print(" " * 7, "MENU PART")
        print("=" * 25)
        print(f"Bem-vindo ao menu de participante do Costeira Livre, {dados[cpf][0]}")
        print("Escolha a ação a ser realizada")
        print("(1) - Se inscrever em uma coleta \n(2) - Pontuação \n(3) - Informação da conta \n(4) - Se candidatar a se tornar moderador \n(5) - Fazer uma doação \n(6) - Sair")
        escolha = int(input())
        if escolha == 1:
            participarcoleta(cpf)
        elif escolha == 2:
            pontuacao(cpf)
        elif escolha == 3:
            info(cpf)
        elif escolha == 4:
            virarmod(cpf)
        elif escolha == 5:
            doacao()
        elif escolha == 6:
            break
        else:
            print("Número inválido!")

def menum(): #Entrar em uma conta moderador
    while True:

        print(" ")
        print("=" * 25)
        print(" " * 7, "MENU MOD")
        print("=" * 25)
        print(f"Bem-vindo ao menu de moderador do Costeira Livre, {dados[cpf][0]}")
        print("Escolha a ação a ser realizada")
        print("(1) - Se inscrever em uma coleta \n(2) - Pontuação \n(3) - Informação da conta \n(4) - Analisar candidatos a moderador \n(5) - Fazer uma doação \n(6) - Criar uma coleta \n(7) - Criar um ponto de coleta de doações \n(8) - Sair")
        escolha = int(input())
        if escolha == 1:
            participarcoleta(cpf)
        elif escolha == 2:
            pontuacao(cpf)
        elif escolha == 3:
            info(cpf)
        elif escolha == 4:
            analisar()
        elif escolha == 5:
            doacao()
        elif escolha == 6:
            criarcoleta()
        elif escolha == 7:
            criarpc()
        elif escolha == 8:
            break
        else:
            print("Número inválido!")

def acesso(): #Início do programa
    while True:
        global cpf
        print(" ")
        print("=" * 25)
        print(" " * 5, "MENU INICIAL")
        print("=" * 25)
        print("\nBem-vindo a Costeira Livre \nEscolha uma das opções para prosseguir: \n\n(1) - Se quiser criar uma conta \n(2) - Para ir para o menu participante \n(3) - Para ir para o menu moderador \n(4) - Se deseja encerrar o programa")
        escolha = int(input())
        if escolha == 1:
            cadastro()
        elif escolha == 2:
            print("--" * 25)
            print("Insira o CPF (somente número)")
            cpf = int(input())
            if cpf in part:
                menup()
            else:
                print("--" * 25)
                print("Conta não existe")
        elif escolha == 3:
            print("--" * 25)
            print("Insira o CPF (somente número)")
            cpf = int(input())
            if cpf in mod:
                menum()
            else:
                print("Conta não possui nível moderador")
        elif escolha == 4:
            break
        else:
            print("Número inválido!")

acesso()
print("--" * 50)
print(f"Obrigado por utilizar nosso aplicativo, volte denovo.")
