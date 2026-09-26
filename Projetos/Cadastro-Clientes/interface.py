import tkinter as tk
from tkinter import messagebox
import json
import main
import re

cliente_editando = None

def formatar_telefone(event):
    telefone = telefone_entry.get()

    numeros = re.sub(r"\D", "", telefone)
    if len(numeros) > 11:
        numeros = numeros[:11]

    if len(numeros) == 0:
        telefone_formatado = ""
    elif len(numeros) <= 2 :
        telefone_formatado = "(" + numeros
    elif len(numeros) <= 7:
        telefone_formatado = "(" + numeros[:2] + ") " + numeros[2:]
    else:
        telefone_formatado = "(" + numeros[:2] + ") " + numeros[2:7] + "-" + numeros[7:]

    telefone_entry.delete(0, tk.END)
    telefone_entry.insert(0, telefone_formatado)
    telefone_entry.icursor(tk.END)

def salvar_edicao():
    global cliente_editando

    if cliente_editando is None:
        return

    cliente = main.clientes[cliente_editando]

    novo_nome = nome_entry.get()
    novo_telefone = telefone_entry.get()

    if len(novo_telefone) !=15:
        messagebox.showwarning(
            "Edição",
            "Digite um telefone válido!"
        )
        return

    if novo_nome == "":
        messagebox.showwarning("Edição", "O nome não pode ficar vazio.")
        return

    if novo_telefone == "":
        messagebox.showwarning("Edição", "O telefone não pode ficar vazio.")
        return

    for i, outro_cliente in enumerate(main.clientes):
        if i != cliente_editando and outro_cliente[0] == novo_nome:
            messagebox.showwarning("Edição", "Já existe um cliente com esse nome.")
            return

    cliente[0] = novo_nome
    cliente[1] = novo_telefone

    with open("clientes.json", "w") as arquivo:
        json.dump(main.clientes, arquivo)

    messagebox.showinfo("Salvar", "Cliente salvo!")

    clientes_lista.delete(0, tk.END)

    for cliente in main.clientes:
        clientes_lista.insert(tk.END, cliente[0] + " - " + cliente[1])

    nome_entry.delete(0, tk.END)
    telefone_entry.delete(0, tk.END)

    cliente_editando = None

def editar():
    global cliente_editando

    selecionado = clientes_lista.curselection()

    if not selecionado:
        return

    indice = selecionado[0]

    cliente_editando = indice

    cliente = main.clientes[indice]

    nome_entry.delete(0, tk.END)
    nome_entry.insert(0, cliente[0])

    telefone_entry.delete(0, tk.END)
    telefone_entry.insert(0, cliente[1])

    print("Cliente", indice, "selecionado")

def excluir():
    selecionado = clientes_lista.curselection()

    if not selecionado:
        return

    item_selecionado = clientes_lista.get(selecionado[0])

    print("selecionado", item_selecionado)

    nome_excluir = item_selecionado.split(" - ")[0]

    print("nome para excluir: ", nome_excluir)

    for cliente in main.clientes:
        if cliente[0] == nome_excluir:
            print("Cliente", cliente ,"encontrado")

            main.clientes.remove(cliente)

            with open("clientes.json", "w") as arquivo:
                json.dump(main.clientes, arquivo)

            clientes_lista.delete(0, tk.END)

            for cliente in main.clientes:
                clientes_lista.insert(tk.END, cliente[0] + " - " + cliente[1])

            print("Cliente excluido")
            messagebox.showinfo("Exclusão", "Cliente excluido!")

            break

def cadastrar():
    nome = nome_entry.get()
    telefone = telefone_entry.get()

    if nome == "":
        messagebox.showinfo("Cadastro", "Digite o nome do cliente!")
        return

    if telefone == "":
        messagebox.showinfo("Cadastro", "Digite o telefone do cliente!")
        return

    if len(telefone) != 15:
        messagebox.showwarning(
            "Cadastro",
            "Digite um número válido"
        )
        return

    if any(cliente[0] == nome for cliente in main.clientes):
        messagebox.showwarning("Cadastro", "Cliente já cadastrado.")
        return

    main.cadastrar_cliente(nome, telefone)

    clientes_lista.insert(tk.END,nome + " - " + telefone)

    messagebox.showinfo("Cadastrado", "Cliente cadastrado")

    nome_entry.delete(0, tk.END)
    telefone_entry.delete(0, tk.END)

def pesquisar():
    nome_pesquisar = pesquisa_entry.get()

    for cliente in main.clientes:
        if cliente[0] == nome_pesquisar:
            resultado_pesquisa.config(
                text="Cliente encontrado: "+ cliente[0] + " - " + cliente[1]
            )
            messagebox.showinfo(
                "pesquisa",
                "Cliente encontrado: " + cliente[0] + " - " + cliente[1]
        )

            print("Cliente encontrado", cliente)
            pesquisa_entry.delete(0, tk.END)
            return

    resultado_pesquisa.config(text="Cliente não encontrado")

    messagebox.showinfo(
        "pesquisa",
        "Cliente não encontrado!"
    )
    pesquisa_entry.delete(0, tk.END)

    print("Cliente não encontrado")

janela = tk.Tk()

janela.title("Cadastro de Clientes")
janela.geometry("500x500")
janela.configure(bg="#050505")

titulo = tk.Label(
    janela,
    text="Cadastro de Clientes",
    font=("Arial", 20,  "bold"),
    fg="#00eaff",
    bg="#050505"

)
titulo.pack(pady=(15, 20))

nome_label = tk.Label(
    janela,
    text="Nome: ",
    fg="white",
    bg="#050505"
)
nome_label.pack(pady=5)

nome_entry = tk.Entry(
    janela,
    width=40,
    fg="white",
    bg="#111111",
    insertbackground="white",
    relief="flat",
    bd=0,
    justify="center"
)
nome_entry.pack(pady=5)

telefone_label = tk.Label(
    janela,
    text="Telefone: ",
    fg="white",
    bg="#050505"
    )
telefone_label.pack(pady=5)

telefone_entry = tk.Entry(
    janela,
    width=40,
    bg="#111111",
    fg="white",
    insertbackground="white",
    relief="flat",
    bd=0,
    justify="center"
)

telefone_entry.bind("<KeyRelease>", formatar_telefone)
telefone_entry.pack(pady=5)


frame_botoes = tk.Frame(
    janela,
    bg="#050505",
)
frame_botoes.pack()

botao_cadastrar = tk.Button(
    frame_botoes,
    text="Cadastrar",
    command=cadastrar,
    width=20,
    bg="#111111",
    fg="#00eaff",
    activebackground="#00eaff",
    activeforeground="#050505",
    relief="flat",
    bd=0
)
botao_cadastrar.pack(side="left", padx=5, pady=5)

botao_editar = tk.Button(
    frame_botoes,
    text="Editar",
    command=editar,
    width=20,
    bg="#111111",
    fg="#00eaff",
    activebackground="#00eaff",
    activeforeground="#050505",
    relief="flat",
    bd=0
)
botao_editar.pack(side="left", padx=5, pady=5)

frame_botoes2 = tk.Frame(
    janela,
    bg="#050505",
)
frame_botoes2.pack()

botao_salvar = tk.Button(
     frame_botoes2,
    text="Salvar Edição",
    command=salvar_edicao,
    width=20,
    bg="#111111",
    fg="#00eaff",
    activebackground="#00eaff",
    activeforeground="#050505",
    relief="flat",
    bd=0
)
botao_salvar.pack(side="left", padx=5, pady=5)

botao_excluir = tk.Button(
    frame_botoes2,
    text="Excluir",
    command=excluir,
    width=20,
    bg="#111111",
    fg="#00eaff",
    activebackground="#00eaff",
    activeforeground="#050505",
    relief="flat",
    bd=0
)
botao_excluir.pack(side="left", padx=5, pady=5)

frame_pesquisar = tk.Frame(
    janela,
    bg="#050505",
)
frame_pesquisar.pack()

botao_pesquisar = tk.Button(
    frame_pesquisar,
    text="Pesquisar",
    command=pesquisar,
    width=20,
    bg="#111111",
    fg="#00eaff",
    activebackground="#00eaff",
    activeforeground="#050505",
    relief="flat",
    bd=0
)
botao_pesquisar.pack(pady=5)

cliente_label = tk.Label(
    janela,
    text="Clientes cadastrados",
    fg="white",
    bg="#050505"
)
cliente_label.pack(pady=5)

clientes_lista = tk.Listbox(
    janela,
    width=50,
    height=4,
    bg="#111111",
    fg="white",
    selectbackground="#00eaff",
    selectforeground="#050505",
    relief="flat",
    bd=0,
    justify="center"

)
clientes_lista.pack(pady=5)

pesquisa_label = tk.Label(
    janela,
    text="Pesquisa cliente",
    fg="white",
    bg="#050505",
    justify="center"
)
pesquisa_label.pack(pady=5)

pesquisa_entry = tk.Entry(
    janela,
    width=40,
    bg="#111111",
    fg="white",
    insertbackground="white",
    relief="flat",
    bd=0,
    justify="center"
)

pesquisa_entry.pack(pady=5)

resultado_pesquisa = tk.Label(
    janela,
    text="",
    fg="white",
    bg="#050505"
)
resultado_pesquisa.pack(pady=5)

for cliente in main.clientes:
    clientes_lista.insert(tk.END, cliente[0] + " - " + cliente[1])

janela.mainloop()