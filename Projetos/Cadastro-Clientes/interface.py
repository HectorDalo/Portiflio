import re
import tkinter as tk
from tkinter import messagebox

import main


# Índice do cliente que está sendo editado.
cliente_editando = None


def formatar_telefone(event=None):
    """Formata o telefone enquanto o usuário digita."""
    texto = telefone_entry.get()
    numeros = re.sub(r"\D", "", texto)[:11]

    if len(numeros) == 0:
        formatado = ""
    elif len(numeros) <= 2:
        formatado = f"({numeros}"
    elif len(numeros) <= 6:
        formatado = f"({numeros[:2]}) {numeros[2:]}"
    elif len(numeros) <= 10:
        formatado = f"({numeros[:2]}) {numeros[2:6]}-{numeros[6:]}"
    else:
        formatado = f"({numeros[:2]}) {numeros[2:7]}-{numeros[7:]}"

    telefone_entry.delete(0, tk.END)
    telefone_entry.insert(0, formatado)
    telefone_entry.icursor(tk.END)


def atualizar_lista():
    clientes_lista.delete(0, tk.END)

    largura = 48

    for nome, telefone in main.clientes:
        texto = f"{nome} - {telefone}"
        clientes_lista.insert(tk.END, texto.center(largura))


def limpar_campos():
    """Limpa os campos do formulário."""
    nome_entry.delete(0, tk.END)
    telefone_entry.delete(0, tk.END)


def cancelar_edicao():
    """Cancela a edição em andamento."""
    global cliente_editando

    cliente_editando = None
    limpar_campos()
    clientes_lista.selection_clear(0, tk.END)


def cadastrar():
    nome = nome_entry.get().strip()
    telefone = telefone_entry.get().strip()

    if not nome:
        messagebox.showwarning(
            "Cadastro",
            "Digite o nome do cliente."
        )
        nome_entry.focus_set()
        return

    if not main.telefone_valido(telefone):
        messagebox.showwarning(
            "Cadastro",
            "Digite um telefone válido com DDD (10 ou 11 dígitos)."
        )
        telefone_entry.focus_set()
        return

    # Verifica se o nome já existe.
    for cliente in main.clientes:
        if cliente[0].strip().casefold() == nome.casefold():
            messagebox.showerror(
                "Cliente duplicado",
                "Já existe um cliente com esse nome."
            )
            nome_entry.focus_set()
            return

    # Verifica se o telefone já existe.
    telefone_numeros = "".join(
        caractere for caractere in telefone
        if caractere.isdigit()
    )

    for cliente in main.clientes:
        telefone_existente = "".join(
            caractere for caractere in cliente[1]
            if caractere.isdigit()
        )

        if telefone_existente == telefone_numeros:
            messagebox.showerror(
                "Telefone duplicado",
                "Esse telefone já está cadastrado."
            )
            telefone_entry.focus_set()
            return

    if main.cadastrar_cliente(nome, telefone):
        atualizar_lista()
        limpar_campos()

        messagebox.showinfo(
            "Cadastro",
            "Cliente cadastrado com sucesso!"
        )
    else:
        messagebox.showerror(
            "Erro no cadastro",
            "Não foi possível cadastrar o cliente. Verifique os dados e tente novamente."
        )



def editar():
    global cliente_editando

    selecionado = clientes_lista.curselection()

    if not selecionado:
        messagebox.showwarning(
            "Edição", "Selecione um cliente na lista."
        )
        return

    cliente_editando = selecionado[0]
    cliente = main.clientes[cliente_editando]

    limpar_campos()

    nome_entry.insert(0, cliente[0])
    telefone_entry.insert(0, cliente[1])

    nome_entry.focus_set()


def salvar_edicao():
    global cliente_editando

    if cliente_editando is None:
        messagebox.showwarning(
            "Edição",
            "Selecione um cliente para editar."
        )
        return

    if cliente_editando >= len(main.clientes):
        messagebox.showerror(
            "Edição",
            "Não foi possível localizar o cliente selecionado."
        )
        cancelar_edicao()
        atualizar_lista()
        return

    nome_original = main.clientes[cliente_editando][0]
    novo_nome = nome_entry.get().strip()
    novo_telefone = telefone_entry.get().strip()

    if not novo_nome:
        messagebox.showwarning(
            "Edição",
            "Digite o nome do cliente."
        )
        nome_entry.focus_set()
        return

    if not main.telefone_valido(novo_telefone):
        messagebox.showwarning(
            "Edição",
            "Digite um telefone válido com DDD (10 ou 11 dígitos)."
        )
        telefone_entry.focus_set()
        return

    # Verifica duplicidades em outros clientes.
    telefone_numeros = "".join(
        c for c in novo_telefone if c.isdigit()
    )

    for i, cliente in enumerate(main.clientes):
        if i == cliente_editando:
            continue

        if cliente[0].strip().casefold() == novo_nome.casefold():
            messagebox.showerror(
                "Nome duplicado",
                "Outro cliente já possui esse nome."
            )
            nome_entry.focus_set()
            return

        telefone_existente = "".join(
            c for c in cliente[1] if c.isdigit()
        )

        if telefone_existente == telefone_numeros:
            messagebox.showerror(
                "Telefone duplicado",
                "Esse telefone pertence a outro cliente."
            )
            telefone_entry.focus_set()
            return

    if main.editar_cliente(nome_original, novo_nome, novo_telefone):
        atualizar_lista()
        cancelar_edicao()

        messagebox.showinfo(
            "Edição",
            "Cliente atualizado com sucesso!"
        )
    else:
        messagebox.showerror(
            "Erro na edição",
            "Não foi possível atualizar o cliente. Verifique os dados."
        )



def excluir():
    selecionado = clientes_lista.curselection()

    if not selecionado:
        messagebox.showwarning(
            "Exclusão", "Selecione um cliente na lista."
        )
        return

    indice = selecionado[0]
    nome = main.clientes[indice][0]

    confirmar = messagebox.askyesno(
        "Confirmar exclusão",
        f"Deseja realmente excluir o cliente {nome}?",
    )

    if not confirmar:
        return

    if main.excluir_cliente(nome):
        atualizar_lista()
        cancelar_edicao()
        resultado_pesquisa.config(text="")
        messagebox.showinfo(
            "Exclusão", "Cliente excluído com sucesso!"
        )


def pesquisar():
    nome = pesquisa_entry.get().strip()

    if not nome:
        messagebox.showwarning(
            "Pesquisa", "Digite o nome do cliente."
        )
        pesquisa_entry.focus_set()
        return

    cliente = main.pesquisar_cliente(nome)

    if cliente:
        mensagem = f"Cliente encontrado: {cliente[0]} - {cliente[1]}"
        resultado_pesquisa.config(text=mensagem)
    else:
        resultado_pesquisa.config(text="Cliente não encontrado.")

def limpar_pesquisa():
    pesquisa_entry.delete(0, tk.END)
    resultado_pesquisa.config(text="")
    pesquisa_entry.focus_set()


# Configuração da janela principal.
janela = tk.Tk()
janela.title("Sistema de Cadastro de Clientes")
janela.geometry("540x700")
janela.minsize(500, 650)
janela.configure(bg="#050505")


# Estilos reutilizados.
FUNDO = "#050505"
FUNDO_CAMPO = "#111111"
CIANO = "#00eaff"
BRANCO = "#ffffff"


def criar_label(texto):
    return tk.Label(
        janela,
        text=texto,
        fg=BRANCO,
        bg=FUNDO,
        font=("Arial", 10),
    )


def criar_botao(pai, texto, comando):
    return tk.Button(
        pai,
        text=texto,
        command=comando,
        width=17,
        bg=FUNDO_CAMPO,
        fg=CIANO,
        activebackground=CIANO,
        activeforeground=FUNDO,
        relief="flat",
        bd=0,
        cursor="hand2",
        font=("Arial", 9, "bold"),
        pady=7,
    )


def criar_campo():
    return tk.Entry(
        janela,
        width=42,
        bg=FUNDO_CAMPO,
        fg=BRANCO,
        insertbackground=BRANCO,
        relief="flat",
        bd=0,
        justify="center",
        font=("Arial", 10),
    )


# Título.
titulo = tk.Label(
    janela,
    text="Cadastro de Clientes",
    font=("Arial", 20, "bold"),
    fg=CIANO,
    bg=FUNDO,
)
titulo.pack(pady=(20, 18))


# Formulário de cadastro e edição.
criar_label("Nome completo").pack(pady=(3, 5))
nome_entry = criar_campo()
nome_entry.pack(ipady=7, pady=(0, 10))

criar_label("Telefone com DDD").pack(pady=(3, 5))
telefone_entry = criar_campo()
telefone_entry.pack(ipady=7, pady=(0, 12))
telefone_entry.bind("<KeyRelease>", formatar_telefone)


# Botões de cadastro e edição.
frame_botoes = tk.Frame(janela, bg=FUNDO)
frame_botoes.pack(pady=3)

criar_botao(frame_botoes, "Cadastrar", cadastrar).grid(
    row=0, column=0, padx=4, pady=4
)
criar_botao(frame_botoes, "Editar selecionado", editar).grid(
    row=0, column=1, padx=4, pady=4
)

frame_botoes2 = tk.Frame(janela, bg=FUNDO)
frame_botoes2.pack(pady=2)

criar_botao(
    frame_botoes2, "Salvar edição", salvar_edicao
).grid(row=0, column=0, padx=4, pady=4)

criar_botao(
    frame_botoes2, "Excluir selecionado", excluir
).grid(row=0, column=1, padx=4, pady=4)


# Lista de clientes.
criar_label("Clientes cadastrados").pack(pady=(16, 5))

frame_lista = tk.Frame(janela, bg=FUNDO)
frame_lista.pack(padx=20, fill="x")

barra_rolagem = tk.Scrollbar(frame_lista)
barra_rolagem.pack(side="right", fill="y")

clientes_lista = tk.Listbox(
    frame_lista,
    justify= "center",
    height=7,
    bg=FUNDO_CAMPO,
    fg=BRANCO,
    selectbackground=CIANO,
    selectforeground=FUNDO,
    relief="flat",
    bd=0,
    font=("Consolas", 10),
    yscrollcommand=barra_rolagem.set,
    exportselection=False,
)

clientes_lista.pack(side="left", fill="both", expand=True)
barra_rolagem.config(command=clientes_lista.yview)


# Pesquisa de clientes.
criar_label("Pesquisar cliente pelo nome").pack(pady=(15, 5))

pesquisa_entry = criar_campo()
pesquisa_entry.pack(ipady=7, pady=(0, 5))

frame_pesquisa_botoes = tk.Frame(janela, bg=FUNDO)
frame_pesquisa_botoes.pack(pady=5)

criar_botao(
    frame_pesquisa_botoes, "Pesquisar", pesquisar
).grid(row=0, column=0, padx=4)

criar_botao(
    frame_pesquisa_botoes, "Limpar pesquisa", limpar_pesquisa
).grid(row=0, column=1, padx=4)

resultado_pesquisa = tk.Label(
    janela,
    text="",
    fg=CIANO,
    bg=FUNDO,
    font=("Arial", 9),
    wraplength=480,
)
resultado_pesquisa.pack(pady=5)


# Carrega os registros salvos ao abrir a janela.
atualizar_lista()

janela.mainloop()