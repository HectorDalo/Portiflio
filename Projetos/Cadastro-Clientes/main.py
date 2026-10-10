import json
import os

# Mantém o arquivo JSON na mesma pasta deste arquivo Python.
PASTA_PROJETO = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_CLIENTES = os.path.join(PASTA_PROJETO, "clientes.json")


def carregar_clientes():
    """Carrega os clientes salvos no arquivo JSON."""
    if not os.path.exists(ARQUIVO_CLIENTES):
        return []

    try:
        with open(ARQUIVO_CLIENTES, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        if not isinstance(dados, list):
            raise ValueError("O arquivo JSON não contém uma lista de clientes.")

        for cliente in dados:
            if (
                not isinstance(cliente, list)
                or len(cliente) != 2
                or not all(isinstance(campo, str) for campo in cliente)
            ):
                raise ValueError("O arquivo JSON contém um cadastro inválido.")

        return dados

    except json.JSONDecodeError as erro:
        raise ValueError(
            "O arquivo clientes.json está inválido. "
            "Verifique o conteúdo antes de continuar."
        ) from erro


def salvar_dados():
    """Salva os clientes no JSON e informa se a operação funcionou."""
    try:
        with open(ARQUIVO_CLIENTES, "w", encoding="utf-8") as arquivo:
            json.dump(clientes, arquivo, ensure_ascii=False, indent=4)
        return True

    except OSError as erro:
        print(f"Erro ao salvar os clientes: {erro}")
        return False


# Lista compartilhada pela interface e pelo modo de terminal.
clientes = carregar_clientes()


def telefone_valido(telefone):
    """Aceita telefones brasileiros com 10 ou 11 dígitos."""
    numeros = "".join(caractere for caractere in telefone if caractere.isdigit())
    return len(numeros) in (10, 11)


def cadastrar_cliente(nome=None, telefone=None):
    """Cadastra um cliente e retorna True se for salvo."""

    if nome is None:
        nome = input("Digite o nome do cliente: ")

    nome = nome.strip()

    if not nome:
        print("O nome não pode ficar vazio.")
        return False

    # Impede nomes repetidos.
    for cliente in clientes:
        if cliente[0].strip().casefold() == nome.casefold():
            print("Já existe um cliente com esse nome.")
            return False

    if telefone is None:
        telefone = input("Digite o telefone do cliente: ")

    telefone = telefone.strip()

    if not telefone_valido(telefone):
        print("Digite um telefone válido com DDD.")
        return False

    # Compara apenas os números, ignorando parênteses, espaços e hífens.
    telefone_numeros = "".join(
        caractere for caractere in telefone
        if caractere.isdigit()
    )

    for cliente in clientes:
        telefone_existente = "".join(
            caractere for caractere in cliente[1]
            if caractere.isdigit()
        )

        if telefone_existente == telefone_numeros:
            print("Esse telefone já está cadastrado.")
            return False

    clientes.append([nome, telefone])

    if not salvar_dados():
        clientes.pop()
        return False

    print(f"Cliente {nome} cadastrado com sucesso!")
    return True



def listar_clientes():
    """Exibe todos os clientes no terminal."""
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    print("\nClientes cadastrados:")

    for indice, cliente in enumerate(clientes, start=1):
        print(f"{indice}. Nome: {cliente[0]} | Telefone: {cliente[1]}")


def excluir_cliente(nome=None):
    """Exclui um cliente pelo nome."""
    if nome is None:
        nome = input("Digite o nome do cliente que deseja excluir: ")

    nome = nome.strip()

    for indice, cliente in enumerate(clientes):
        if cliente[0].casefold() == nome.casefold():
            removido = clientes.pop(indice)

            if not salvar_dados():
                clientes.insert(indice, removido)
                return False

            print(f"Cliente {removido[0]} excluído com sucesso!")
            return True

    print("Cliente não encontrado.")
    return False


def editar_cliente(nome=None, novo_nome=None, novo_telefone=None):
    """Edita um cliente sem permitir nomes ou telefones duplicados."""

    if nome is None:
        nome = input("Digite o nome do cliente que deseja editar: ")

    nome = nome.strip()

    indice = next(
        (
            i for i, cliente in enumerate(clientes)
            if cliente[0].strip().casefold() == nome.casefold()
        ),
        None
    )

    if indice is None:
        print("Cliente não encontrado.")
        return False

    cliente_original = clientes[indice]

    if novo_nome is None:
        novo_nome = input("Digite o novo nome: ")

    if novo_telefone is None:
        novo_telefone = input("Digite o novo telefone: ")

    novo_nome = novo_nome.strip()
    novo_telefone = novo_telefone.strip()

    if not novo_nome:
        print("O nome não pode ficar vazio.")
        return False

    if not telefone_valido(novo_telefone):
        print("Digite um telefone válido com DDD.")
        return False

    telefone_numeros = "".join(
        c for c in novo_telefone if c.isdigit()
    )

    for i, cliente in enumerate(clientes):
        if i == indice:
            continue

        if cliente[0].strip().casefold() == novo_nome.casefold():
            print("Já existe outro cliente com esse nome.")
            return False

        telefone_existente = "".join(
            c for c in cliente[1] if c.isdigit()
        )

        if telefone_existente == telefone_numeros:
            print("Esse telefone já está cadastrado para outro cliente.")
            return False

    dados_antigos = cliente_original.copy()
    clientes[indice] = [novo_nome, novo_telefone]

    if not salvar_dados():
        clientes[indice] = dados_antigos
        return False

    print(f"Cliente {novo_nome} editado com sucesso!")
    return True



def pesquisar_cliente(nome=None):
    """Busca um cliente pelo nome, sem diferenciar maiúsculas."""
    if nome is None:
        nome = input("Digite o nome do cliente: ")

    nome = nome.strip()

    for cliente in clientes:
        if cliente[0].casefold() == nome.casefold():
            print(f"Nome: {cliente[0]} | Telefone: {cliente[1]}")
            return cliente

    print("Cliente não encontrado.")
    return None


def executar_terminal():
    """Executa o sistema pelo terminal."""
    while True:
        print("\n=== Sistema de Cadastro de Clientes ===")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Excluir cliente")
        print("4 - Editar cliente")
        print("5 - Pesquisar cliente")
        print("6 - Sair")

        opcao = input("Digite a opção: ").strip()

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
        else:
            print("Opção inválida. Escolha de 1 a 6.")


if __name__ == "__main__":
    executar_terminal()