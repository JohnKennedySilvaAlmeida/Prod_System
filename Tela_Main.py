# ------------- TELA PRINCIPAL ----------------------------------------------------------------------------------------
from tkinter import *

# Variaveis de Cor
Branco = "White"
Preto = "Black"
Vermelho = "Red4"
Cinza60 = "Gray60"
Cinza40 = "Gray40"
Cinza90 = "Gray90"
Cinza_Novo = "#262f36"
Amarelo_Novo = "#f99c11"

# Variavéis de Fonte
Fonte8 = "Arial, 8"
Fonte8B = ("Arial", 8, "bold")
Fonte10 = "Arial, 10"
Fonte10B = ("Arial", 10, "bold")
Fonte11 = "Arial, 11"
Fonte11B = ("Arial", 11, "bold")
Fonte12 = "Arial, 12"
Fonte12B = ("Arial", 12, "bold")
Fonte13B = ("Arial", 13, "bold")
Fonte12I = ("Courier", 12, "italic")

Windows = Tk()
Windows.geometry("1500x750+10+10")
Windows.title("TK8 - SOFTWARE DE GERENCIAMENTO")
Windows.minsize(1500, 750)
Windows.maxsize(1500, 750)
Windows.resizable(False, False)
Windows["bg"] = Branco


def Row_Up_Button_1(event=None):
    Row_Arquivo.config(bg=Branco)

def Row_Down_Button_1(event=None):
    Row_Arquivo.config(bg=Amarelo_Novo)

def Row_Up_Button_2(event=None):
    Row_Consultas.config(bg=Branco)

def Row_Down_Button_2(event=None):
    Row_Consultas.config(bg=Amarelo_Novo)

def Row_Up_Button_3(event=None):
    Row_Relatorios.config(bg=Branco)

def Row_Down_Button_3(event=None):
    Row_Relatorios.config(bg=Amarelo_Novo)

def Row_Up_Button_4(event=None):
    Row_Agenda.config(bg=Branco)

def Row_Down_Button_4(event=None):
    Row_Agenda.config(bg=Amarelo_Novo)

def Row_Up_Button_5(event=None):
    Row_Suporte.config(bg=Branco)

def Row_Down_Button_5(event=None):
    Row_Suporte.config(bg=Amarelo_Novo)

def Register_Group(event=None):
    import Register_Group

def Delete_Group(event=None):
    import Drop_Group

def Desativar_Max(event=None):
    pass

def Sair_Tela_Inicial(event=None):
    Windows.destroy()

def Register_Prod(event=None):
    import Register_Prod

def Excluir_Produtos(event=None):
    import Drop_Prod

def Register_Users(event=None):
    import Register_Users

def Consulta_Prod(event=None):
    import Consulta_Prod

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# ---------------------------------------------------------------------------------------------------------------------
Lbl_Linha_1 = Label(Windows, bg=Cinza_Novo)
Lbl_Linha_1.place(x=0, y=0, width=1500, height=100)
# ---------------------------------------------------------------------------------------------------------------------
Lbl_Linha_2 = Label(Windows, bg=Branco)
Lbl_Linha_2.place(x=0, y=5, width=1500, height=4)
# ---------------------------------------------------------------------------------------------------------------------
Lbl_Linha_3 = Label(Windows, bg=Amarelo_Novo)
Lbl_Linha_3.place(x=0, y=91, width=1500, height=4)
# ---------------------------------------------------------------------------------------------------------------------
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Lbl_Titulo = Label(Windows, text="SISTEMA DE GERENCIAMENTO", bg=Cinza_Novo, fg=Amarelo_Novo, font=Fonte12I)
Lbl_Titulo.place(x=1220, y=20)
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Lbl_Titulo2 = Label(Windows, text="----"*27, bg=Cinza_Novo, fg=Amarelo_Novo, font=Fonte12I)
Lbl_Titulo2.place(x=0, y=20)
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Logo = PhotoImage(file="Imagens\\Work.png")
Lbl_Logo = Label(Windows, bg=Amarelo_Novo, image=Logo, borderwidth=9)
Lbl_Logo.image= Logo
Lbl_Logo.place(x=15, y=50)
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Fundo_Tela = PhotoImage(file="Imagens\\Fundo.png")
Lbl_Logo2 = Label(Windows, bg=Cinza_Novo, image=Fundo_Tela, borderwidth=9)
Lbl_Logo2.image = Fundo_Tela
Lbl_Logo2.place(x=0, y=100, width=1500, height=750)
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Row_Arquivo = Label(Windows, bg=Amarelo_Novo)
Row_Arquivo.place(x=65, y=91, width=74, height=4)
# ---------------------------------------------------------------------------------------------------------------------
Row_Consultas = Label(Windows, bg=Amarelo_Novo)
Row_Consultas.place(x=156, y=91, width=90, height=4)
# ---------------------------------------------------------------------------------------------------------------------
Row_Relatorios = Label(Windows, bg=Amarelo_Novo)
Row_Relatorios.place(x=274, y=91, width=103, height=4)
# ---------------------------------------------------------------------------------------------------------------------
Row_Agenda = Label(Windows, bg=Amarelo_Novo)
Row_Agenda.place(x=396, y=91, width=68, height=4)
# ---------------------------------------------------------------------------------------------------------------------
Row_Suporte = Label(Windows, bg=Amarelo_Novo)
Row_Suporte.place(x=486, y=91, width=80, height=4)
# ---------------------------------------------------------------------------------------------------------------------
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Criando MENU Arquivo
Arquivo = Menubutton(Windows, text="ARQUIVO", background=Cinza_Novo, foreground=Branco, font=Fonte12B,
                     activebackground=Cinza_Novo, activeforeground=Branco)
Arquivo.place(x=60, y=68, height=20)
Arquivo.bind("<Enter>", Row_Up_Button_1)  # Ação Para Aparecer a linha embaixo da Label
Arquivo.bind("<Leave>", Row_Down_Button_1)  # Ação Para Desaparecer a linha embaixo da Label
Arquivo.menu = Menu(Arquivo, background=Cinza60, fg=Branco, tearoff=0, activebackground=Cinza_Novo)
Arquivo["menu"] = Arquivo.menu  # Criando Atributo menu pro MENU Arquivo
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Consultas = Menubutton(Windows, text="CONSULTA", background=Cinza_Novo, foreground=Branco, font=Fonte12B,
                     activebackground=Cinza_Novo, activeforeground=Branco)
Consultas.place(x=153, y=68, height=20)
Consultas.bind("<Enter>", Row_Up_Button_2)  # Ação Para Aparecer a linha embaixo da Label
Consultas.bind("<Leave>", Row_Down_Button_2)  # Ação Para Desaparecer a linha embaixo da Label
Consultas.menu = Menu(Consultas, background=Cinza60, fg=Branco, tearoff=0, activebackground=Cinza_Novo)
Consultas["menu"] = Consultas.menu  # Criando Atributo menu pro MENU Consultas
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Relatorios = Menubutton(Windows, text="RELATÓRIOS", background=Cinza_Novo, foreground=Branco, font=Fonte12B,
                     activebackground=Cinza_Novo, activeforeground=Branco)
Relatorios.place(x=266, y=68, height=20)
Relatorios.bind("<Enter>", Row_Up_Button_3)  # Ação Para Aparecer a linha embaixo da Label
Relatorios.bind("<Leave>", Row_Down_Button_3)  # Ação Para Desaparecer a linha embaixo da Label
Relatorios.menu = Menu(Relatorios, background=Cinza60, fg=Branco, tearoff=0, activebackground=Cinza_Novo)
Relatorios["menu"] = Relatorios.menu  # Criando Atributo menu pro MENU Relatorios
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Agenda = Menubutton(Windows, text="AGENDA", background=Cinza_Novo, foreground=Branco, font=Fonte12B,
                     activebackground=Cinza_Novo, activeforeground=Branco)
Agenda.place(x=390, y=68, height=20)
Agenda.bind("<Enter>", Row_Up_Button_4)  # Ação Para Aparecer a linha embaixo da Label
Agenda.bind("<Leave>", Row_Down_Button_4)  # Ação Para Desaparecer a linha embaixo da Label
Agenda.menu = Menu(Agenda, background=Cinza60, fg=Branco, tearoff=0, activebackground=Cinza_Novo)
Agenda["menu"] = Agenda.menu  # Criando Atributo menu pro MENU Agenda
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Suporte = Menubutton(Windows, text="SUPORTE", background=Cinza_Novo, foreground=Branco, font=Fonte12B,
                     activebackground=Cinza_Novo, activeforeground=Branco)
Suporte.place(x=480, y=68, height=20)
Suporte.bind("<Enter>", Row_Up_Button_5)  # Ação Para Aparecer a linha embaixo da Label
Suporte.bind("<Leave>", Row_Down_Button_5)  # Ação Para Desaparecer a linha embaixo da Label
Suporte.menu = Menu(Suporte, background=Cinza_Novo, fg=Branco, tearoff=0, activebackground=Cinza40)
Suporte["menu"] = Suporte.menu  # Criando Atributo menu pro MENU Historicos
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Criando Clientes Menu com funções NOVO e EXCLUIR e EDITAR
ClientesMenu = Menu(Arquivo, background=Cinza_Novo, fg=Branco, tearoff=False, activebackground=Cinza40)
ClientesMenu.add_command(label='NOVO', font=Fonte12B)
ClientesMenu.add_command(label='EXCLUIR', font=Fonte12B)
ClientesMenu.add_command(label='EDITAR', font=Fonte12B)
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# Criando Usuario Menu com funções NOVO e EXCLUIR
UsuarioMenu = Menu(Arquivo, background=Cinza_Novo, fg=Branco, tearoff=False, activebackground=Cinza40)
UsuarioMenu.add_command(label='NOVO', font=Fonte12B, command=Register_Users)
UsuarioMenu.add_command(label='EXCLUIR', font=Fonte12B)
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# Criando Grupo Menu com funções NOVO e EXCLUIR
GrupoMenu = Menu(Arquivo, background=Cinza_Novo, fg=Branco, tearoff=False, activebackground=Cinza40)
GrupoMenu.add_command(label='NOVO', font=Fonte12B, command=Register_Group)
GrupoMenu.add_command(label='EXCLUIR', font=Fonte12B, command=Delete_Group)
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# Criando Produtos Menu com funções NOVO e EXCLUIR
ProdutosMenu = Menu(Arquivo, background=Cinza_Novo, fg=Branco, tearoff=False, activebackground=Cinza40)
ProdutosMenu.add_command(label='NOVO', font=Fonte12B, command=Register_Prod)
ProdutosMenu.add_command(label='EXCLUIR', font=Fonte12B, command=Excluir_Produtos)
# ---------------------------------------------------------------------------------------------------------------------
# Criando Consultas Menu com funções ESTOQUE, VENDAS, PRODUTO
Consultas.menu.add_command(label='ESTOQUE', font=Fonte12B, background=Cinza_Novo, activebackground=Cinza40)
Consultas.menu.add_command(label='VENDAS', font=Fonte12B, background=Cinza_Novo, activebackground=Cinza40)
Consultas.menu.add_command(label='PRODUTO', font=Fonte12B, background=Cinza_Novo, activebackground=Cinza40,
                           command=Consulta_Prod)
# ---------------------------------------------------------------------------------------------------------------------
# Criando Relatorios Menu com função VENDAS
Relatorios.menu.add_command(label='VENDAS', font=Fonte12B, background=Cinza_Novo, activebackground=Cinza40)
# ---------------------------------------------------------------------------------------------------------------------
# Criando Agenda Menu com função Telefonica
Agenda.menu.add_command(label='TELEFÔNICA', font=Fonte12B, background=Cinza_Novo, activebackground=Cinza40)
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
Arquivo.menu.add_cascade(label='CLIENTES', menu=ClientesMenu, font=Fonte12B, background=Cinza_Novo,
                         activebackground=Cinza40)
Arquivo.menu.add_cascade(label="USUÁRIOS", menu=UsuarioMenu, font=Fonte12B, background=Cinza_Novo,
                         activebackground=Cinza40)
Arquivo.menu.add_cascade(label="GRUPO", menu=GrupoMenu, font=Fonte12B, background=Cinza_Novo,
                         activebackground=Cinza40)
Arquivo.menu.add_cascade(label="PRODUTOS", font=Fonte12B, menu=ProdutosMenu, background=Cinza_Novo,
                         activebackground=Cinza40)
Arquivo.menu.add_command(label="SAIR", font=Fonte12, background=Cinza_Novo, activebackground=Vermelho,
                         command=Sair_Tela_Inicial)
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Cadastro de Tecla Atalho
Windows.bind_all("<Control-u>", Register_Users)
Windows.bind_all("<Control-s>", Sair_Tela_Inicial)
Windows.bind_all("<Control-p>", Register_Prod)
Windows.bind_all("<Control-m>", Register_Group)

# Desativando o Botão X da Tela
Windows.protocol("WM_DELETE_WINDOW", Desativar_Max)
Windows.iconbitmap("Imagens/Logo_SFundo.ico")
Windows.mainloop()
