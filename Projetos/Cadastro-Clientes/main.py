import json
import os

def cadastrar_cliente(nome=None, telefone=None):
    print("Cadastro de Clientes")
    if nome is None:
        nome = input("Digite o nome do cliente: ")

    encontrado = False
    for cliente in clientes:
        if cliente[0] == nome:
            encontrado = True
    if encontrado:
        print("Cliente ja cadastrado")
    else:
        if telefone is None:
            telefone = input("Digite o telefone do cliente: ")
        if telefone == "":
            print("Telefone não pode ficar vazio!!")
        else:
            clientes.append([nome, telefone])
            with open("clientes.json", "w") as arquivo:
                json.dump(clientes, arquivo)

            print("Cliente", nome ,"cadastrado")

def listar_clientes():
    print("Clientes cadastrados: ")
    for cliente in clientes:
        print("nome", cliente[0])
        print("telefone", cliente[1])

def excluir_cliente():
    print("Excluir um cliente")
    nome_excluir = input("Digite o nome do cliente: ")
    encontrado = False
    for cliente in clientes:
        if cliente[0] == nome_excluir:
            encontrado = True
            clientes.remove(cliente)
            print(clientes)
            with open("clientes.json", "w") as arquivo:
                json.dump(clientes, arquivo)

            print("Cliente", nome_excluir , "Excluido" )
            break
    if not encontrado:
        print("Cliente nao encontrado")

def editar_cliente():
    print("Editar um Cliente")
    nome_editar = input("Digite o nome do cliente que deseja editar: ")
    encontrado = False
    for cliente in clientes:
        if cliente[0] == nome_editar:
            print("Cliente encontrado!")
            encontrado = True
            novo_telefone = input("Digite o novo numero de telefone: ")
            cliente[1] = novo_telefone

            with open("clientes.json", "w") as arquivo:
                json.dump(clientes, arquivo)
            break
    if not encontrado:
        print("Cliente não encontrado.")

def pesquisar_cliente():
    print("Pesquisar Cliente")
    nome_pesquisar = input("Digite o nome do cliente:")
    encontrado = False
    for cliente in clientes:
        if cliente[0] == nome_pesquisar:
            encontrado = True
            print("Cliente Encontrado!")
            print("Nome: ", cliente[0])
            print("telefone: ", cliente[1])
    if not encontrado:
        print("Cliente nao encontrado")


print(os.path.abspath("clientes.json"))

with open("clientes.json", "r") as arquivo:
    clientes = json.load(arquivo)

if __name__ == "__main__":
    print("Sistema de Cadastro de Clientes")

    while True:
        print("1 - Cadastro de Cliente")
        print("2 - Listar Cliente")
        print("3 - Excluir um cliente")
        print("4 - Editar um cliente")
        print("5 - Pesquisar Cliente")
        print("6 - sair")

        opcao = input("Digite a opção: ")

        if opcao == "1":
            cadastrar_cliente()

        elif opcao == "2":
            listar_clientes()

        elif opcao == "3":
            excluir_cliente()

        elif opcao == "4":
            editar_cliente()

        elif opcao == "5":
            pesquisar_cliente()

        elif opcao == "6":
            print("Saindo do sistema...")
            break
