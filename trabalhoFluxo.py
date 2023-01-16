from os import system

class Staff:
    cargo = str()

    def __init__(self, identificacao:str, usuario:str, senha:str) -> None:
        self.id = identificacao
        self.__usuario = usuario
        self.__senha = senha

    def __repr__(self) -> str:
        return f"Nome: {type(self).__name__} - ID: {self.id}\n"

    def getUsuario(self):
        return self.__usuario

    def getSenha(self):
        return self.__senha
    
    def setUsuario(self, novoUsuario):
        self.__usuario = novoUsuario

    def setSenha(self, novaSenha):
        self.__senha = novaSenha

class Consultor(Staff):     
    def __init__(self, identification:str, username:str, password:str) -> None:
        super.__init__(identification, username, password)
        self.cargo = "consultor"

class Gerente(Staff):
    def __init__(self, identification:str, username:str, password:str) -> None:
        super.__init__(identification, username, password)
        self.cargo = "gerente"

class Projeto:
    def __init__(self, nome:str, equipe:list, desenvolvimento:int, concepcao:int, idVisual:int) -> None:
        self.nome = nome
        self.equipe = equipe
        self.d = desenvolvimento
        self.c = concepcao
        self.i = idVisual
    def __repr__(self) -> str:
        return f"Nome: {type(self).__name__} - Gerente: {self.equipe[-1]}\n"

class Sistema:
    gerentes = list()
    consultores = list()
    projetos = list()
    staff = gerentes + consultores
    projetosAnalise = list()    # [[consultor, etapa, projeto]]

    def criarProjeto(self):
        print("Criando projeto...\n")
        try:
            nome = input("  Insira o nome do projeto: ")
            gerente = input("  Insira a identificacao do gerente da equipe: ")
            numEquipe = input("  Insira a quantidade de consultores envolvidos no projeto: ")
            equipe = list()     # equipe = [IDconsultor1, IDconsultor2, ..., IDconsultorN, IDgerente]
            print("  Insira a identificacao dos consultores envolvidos no projeto: ")
            for i in range(int(numEquipe)):
                consultor = input()
                equipe.append(consultor)
            equipe.append(gerente)
            etapasD = int(input("  Insira quantas etapas de desenvolvimento: "))
            etapasC = int(input("  Insira quantas etapas de concepcao: "))
            etapasI = int(input("  Insira quantas etapas de identidade visual: "))
            self.projetos.append(Projeto(nome, equipe, etapasD, etapasC, etapasI))
            print("\nPROJETO CRIADO COM SUCESSO!")
        except:
            print("HOUVE UM ERRO NA CRIACAO DO PROJETO, POR FAVOR TENTE DE NOVO")
            return

    def removerProjeto(self):
        print("Removendo projeto...\n")
        try:
            nome = input("  Insira o nome do projeto: ")
            for i in range(len(self.projetos)):
                if self.projetos[i].nome == nome:
                    self.projetos.pop(i)
                    print("\nPROJETO REMOVIDO COM SUCESSO!")
                    return
            print("\nPROJETO NAO ENCONTRADO")
        except:
            print("HOUVE UM ERRO NA REMOCAO DO PROJETO, POR FAVOR TENTE DE NOVO")
            return

    def criarConsultor(self):
        print("Criando consultor...\n")
        try:
            identificador = input("  Insira sua ID ")
            usuario = input("  Insira seu usuario de acesso ")
            senha = input("  Insira sua senha de acesso ")
            self.consultores.append(Consultor(identificador, usuario, senha))
            print("\CONSULTOR CRIADO COM SUCESSO!")
        except:
            print("HOUVE UM ERRO NA CRIACAO DO CONSULTOR, POR FAVOR TENTE DE NOVO")
            return

    def removerConsultor(self):
        print("Removendo consultor...\n")
        try:
            id = input("  Insira o ID do consultor: ")
            for i in range(len(self.consultores)):
                if self.consultores[i].id == id:
                    self.consultores.pop(i)
                    print("\CONSULTOR REMOVIDO COM SUCESSO!")
                    return
            print("\CONSULTOR NAO ENCONTRADO")
        except:
            print("HOUVE UM ERRO NA REMOCAO DO CONSULTOR, POR FAVOR TENTE DE NOVO")
            return

    def criarGerente(self):
        print("Criando gerente...\n")
        try:
            identificador = input("  Insira sua ID ")
            usuario = input("  Insira seu usuario de acesso ")
            senha = input("  Insira sua senha de acesso ")
            self.consultores.append(Gerente(identificador, usuario, senha))
            print("\GERENTE CRIADO COM SUCESSO!")
        except:
            print("HOUVE UM ERRO NA CRIACAO DO GERENTE, POR FAVOR TENTE DE NOVO")
            return

    def removerGerente(self):
        print("Removendo gerente...\n")
        try:
            id = input("  Insira o ID do gerente: ")
            for i in range(len(self.gerentes)):
                if self.gerentes[i].id == id:
                    self.gerentes.pop(i)
                    print("\GERENTE REMOVIDO COM SUCESSO!")
                    return
            print("\GERENTE NAO ENCONTRADO")
        except:
            print("HOUVE UM ERRO NA REMOCAO DO GERENTE, POR FAVOR TENTE DE NOVO")
            return

    def listarGCP(self):
        print("\n---GERENTES---\n")
        for g,  in self.gerentes:
            print(g)
        print("\n---CONSULTORES---\n")
        for c,  in self.consultores:
            print(c)
        print("\n---PROJETOS---\n")
        for p,  in self.projetos:
            print(p)

    def logar(self):
        print("Login...")
        try:
            usuario = input("  Insira seu nome: ")
            senha = input("  Insira sua senha: ")
        except:
            print("HOUVE UM ERRO NO LOGIN, POR FAVOR TENTE DE NOVO")
            return
        cargo = str()
        id = str()
        for s in self.staff:
            if s.getUsuario() == usuario and s.getSenha() == senha:
                cargo = s.cargo
                id = s.id
                break
        if cargo == "gerente":
            self.gerenteMenu(id, cargo)
        elif cargo == "consultor":
            self.consultorMenu(id, cargo)
        else:
            print("MEMBRO NAO CADASTRADO")

    def verDados(self, id, cargo):
        print("DADOS: ")
        if cargo == "gerente":
            for g in self.gerentes:
                if g.id == id:
                    print("ID: " + g.id)
                    print("Usuario: " + g.getUsuario())
                    print("Senha: " + g.getSenha())
                    break
        elif cargo == "consultor":
            for c in self.consultores:
                if c.id == id:
                    print("ID: " + c.id)
                    print("Usuario: " + c.getUsuario())
                    print("Senha: " + c.getSenha())
                    break

    def modificarDados(self, id, cargo):
        print("Modificando dados...")
        try:
            novoId = input("  Insira sua nova ID ")
            novoUsuario = input("  Insira seu novo usuario de acesso ")
            novaSenha = input("  Insira sua nova senha de acesso ")
            if cargo == "gerente":
                for g in self.gerentes:
                    if g.id == id:
                        g.id = novoId
                        g.setUsuario(novoUsuario)
                        g.setSenha(novaSenha)
                        print("\DADOS ALTERADOS COM SUCESSO!")
                        break
            elif cargo == "consultor":
                for c in self.consultores:
                    if c.id == id:
                        print("  ID: " + c.id)
                        print("  Usuario: " + c.getUsuario())
                        print("  Senha: " + c.getSenha())
                        print("\DADOS ALTERADOS COM SUCESSO!")
                        break
        except:
            print("HOUVE UM ERRO NA ALTERACAO DOS DADOS, POR FAVOR TENTE DE NOVO")
            return

    def projetosAlocado(self, id):
        print("PROJETOS ALOCADO: ")
        for p in self.projetos:
            if id in p.equipe:
                print(p.nome)

    def avancarProjeto(self, id, cargo):
        if cargo == "gerente":
            pass
        elif cargo == "consultor":
            system("cls")
            print("Pedido de Avanco de Projeto... ")
            print("PROJETOS ALOCADO: ")
            projetos = list()
            for p in self.projetos:
                if id in p.equipe:
                    projetos.append(p)
            print()
            # continuar aqui <------------------------------------------------------
            '''while True:
                nome = input("  Insira o nome do projeto que voce deseja avancar: ")
                etapa = input("  Insira a etapa do projeto que voce deseja avancar: ")
                if id not in p.equipe'''

    def logOffMenu(self):
        print("1. Criar Projeto")
        print("2. Remover Projeto")
        print("3. Criar Consultor")
        print("4. Remover Consultor")
        print("5. Criar Gerente")
        print("6. Remover Gerente")
        print("7. Listar Gerentes / Consultores / Projetos")
        print("8. Sair do Programa")
        print("9. Fazer Login")
        run = True
        while run:
            try:
                choice = input("\nEscolha sua opcao: ")
            except:
                print("POR FAVOR, INSIRA UMA OPCAO VALIDA")
                continue
            if choice == "1":
                self.criarProjeto()
            elif choice == "2":
                self.removerProjeto()
            elif choice == "3":
                self.criarConsultor()
            elif choice == "4":
                self.removerConsultor()
            elif choice == "5":
                self.criarGerente()
            elif choice == "6":
                self.removerGerente()
            elif choice == "7":
                self.listarGCP()
            elif choice == "8":
                run = False
            elif choice == "9":
                self.logar()
            else:
                print("POR FAVOR, INSIRA UMA OPCAO EXISTENTE\n")
    
    def consultorMenu(self, id, cargo):
        print("1. Ver seus dados")
        print("2. Modificar seus dados")
        print("3. Verificar projetos em que está alocando")
        print("4. Avançar com um projeto")
        print("5. Pedir retirada de um projeto")
        print("6. Fazer logout")
        run = True
        while run:
            try:
                choice = input("\nEscolha sua opcao: ")
            except:
                print("POR FAVOR, INSIRA UMA OPCAO VALIDA\n")
                continue
            if choice == "1":
                self.verDados(id, cargo)
            elif choice == "2":
                self.modificarDados(id, cargo)
            elif choice == "3":
                self.projetosAlocado(id)
            elif choice == "4":
                self.AvancarProjeto(id, cargo)
            elif choice == "5":
                self.pedirRetirada()
            elif choice == "6":
                run = False
            else:
                print("POR FAVOR, INSIRA UMA OPCAO EXISTENTE\n")

    def gerenteMenu(self, id, cargo):
        print("1. Ver seus dados")
        print("2. Modificar seus dados")
        print("3. Verificar projetos em que esta alocando")
        print("4. Avançar com um projeto")
        print("5. Dar aval sobre a retirada de um consultor")
        print("6. Passar o projeto a outro gerente")
        print("7. Entregar um projeto")
        print("8. Fazer logout")
        run = True
        while run:
            try:
                choice = input("\nEscolha sua opcao: ")
            except:
                print("POR FAVOR, INSIRA UMA OPCAO VALIDA\n")
                continue
            if choice == "1":
                self.verDados(id, cargo)
            elif choice == "2":
                self.modificarDados(id, cargo)
            elif choice == "3":
                print(choice)
            elif choice == "4":
                print(choice)
            elif choice == "5":
                print(choice)
            elif choice == "6":
                print(choice)
            elif choice == "7":
                print(choice)
            elif choice == "8":
                rue = False
            else:
                print("POR FAVOR, INSIRA UMA OPCAO EXISTENTE\n")

    def ligar(self):
        self.logOffMenu()

meuSistema = Sistema()
meuSistema.ligar()