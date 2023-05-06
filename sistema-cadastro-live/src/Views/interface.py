from Controller.requisicoes import ReqController
import os

loja = ReqController()
def root():
    while True:
        print("""
                SISTEMA DE REGISTRO EM POO | LIVECODE INFINITY SCHOOL!
                --------------- INFORME UMA OPERAÇÃO -----------------
                1 - Cadastrar Clientes
                2 - Consultar Clientes por Nome
                3 - Consultar Todos os Clientes
                4 - Alterar dados
                5 - Deletar Clientes
                0 - EXIT
                """)
        
        options = ["1","2","3","4","5","0"]
        print("Informe um numero para Operação desejada: ")
        choice = input('>> ')

        while choice not in options:
            print("Erro, Informe apenas opções de acordo ao menu!")
            choice = input('>> ')
        os.system('cls')
        if choice == "1":
            while True:
                print("------Registro de Clientes------")
                print("informe o nome do cliente: ")
                name = input(">> ")
                print("informe a idade: ")
                idade = input(">> ")
                print("informe o cpf: ")
                cpf = input(">> ")
                os.system('cls')
                loja.insertDados(name,idade,cpf)
                print("deseja continuar Cadastrando ? [Y/N]")
                choice = input('>> ')
                os.system('cls')
                if choice == "n":
                    break
        elif choice == "2":
            while True:
                print("------Consultar Clientes por Nome------")
                print("informe o nome do cliente para consulta: ")
                name_consulta = input(">> ")
                print(loja.selectForName(name_consulta))
                print("deseja continuar Consultando ? [Y/N]")
                choice = input('>> ')
                os.system('cls')
                if choice == "n":
                    break
        elif choice == "3":
            while True:
                print("------Consultar todos os Clientes------")
                loja.selectAll()
                print("deseja voltar para o menu principal [Y/N]: ")
                choice = input('>> ')
                os.system('cls')
                if choice == "y":
                    break  
        elif choice == "4":
            while True:
                print("------Alterar dados dos Clientes------")
                print("informe o nome do cliente que deseja alterar: ")
                search = input(">> ")
                print("informe um novo nome: ")
                new_name = input(">> ")
                print("informe uma nova idade: ")
                new_idade = input(">> ")
                print("informe um novo cpf: ")
                new_cpf = input(">> ")
                loja.updatedados(search,new_name,new_idade,new_cpf)
                print(loja.selectForName(new_name))
                print("deseja consultar outro Cliente ? [Y/N]: ")
                choice = input('>> ')
                os.system('cls')
                if choice == "n":
                    break  
        elif choice == "5":
            while True:
                print("------Deletar Clientes------")
                loja.selectAll()
                print("informe o id do cliente que deseja Deletar: ")
                search_id = int(input(">> "))
                os.system('cls')
                print(f"tem certeza que deseja deletar o cliente com id:{search_id}? [Y/N]")
                question = input(">> ")
                if question == "y":
                    loja.deleteForId(search_id)
                    loja.selectAll()
                    print("deseja deletar mais algum cliente ? [Y/N]: ")
                    choice = input(">> ")
                    os.system('cls')
                    if choice == "n":
                        break
                else:
                        break
                    
        elif choice == "0":
            print("Sistema Encerrado.")
            exit()
                