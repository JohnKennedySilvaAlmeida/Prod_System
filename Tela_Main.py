# ------------- TELA PRINCIPAL ----------------------------------------------------------------------------------------
from tkinter import *
from tkinter import font

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
Fonte_teste = ("Palatino Linotype", 12, "bold")

Windows = Tk()
Windows.geometry("1300x725+10+10")
Windows.title("SOFTWARE DE GERENCIAMENTO")
# Windows.minsize(1300, 750)
# Windows.maxsize(1300, 750)
# Ajusta tela conforme tamnho munitor
Windows.winfo_screenwidth() 
Windows.winfo_screenheight()
Windows.resizable(True, True)
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
    Row_Lancamento.config(bg=Branco)

def Row_Down_Button_4(event=None):
    Row_Lancamento.config(bg=Amarelo_Novo)

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

def Register_Note(event=None):
    import Entry_Note

def Register_Store(event=None):
    import Register_Store

def Register_Industry(event=None):
    import Register_Ind

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
Lbl_Titulo = Label(Windows, text="SISTEMA DE GERENCIAMENTO", bg=Cinza_Novo, fg=Amarelo_Novo, font=Fonte_teste)
Lbl_Titulo.place(x=1100, y=20)#Ajusta tamnho dimanico - nao fixo
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Lbl_Titulo2 = Label(Windows, text="----"*15, bg=Cinza_Novo, fg=Amarelo_Novo, font=Fonte12I)
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
Row_Arquivo.place(x=67, y=91, width=90, height=4)
# ---------------------------------------------------------------------------------------------------------------------
Row_Consultas = Label(Windows, bg=Amarelo_Novo)
Row_Consultas.place(x=177, y=91, width=90, height=4)
# ---------------------------------------------------------------------------------------------------------------------
Row_Relatorios = Label(Windows, bg=Amarelo_Novo)
Row_Relatorios.place(x=282, y=91, width=105, height=4)
# ---------------------------------------------------------------------------------------------------------------------
Row_Lancamento = Label(Windows, bg=Amarelo_Novo)
Row_Lancamento.place(x=407, y=91, width=120, height=4)
# ---------------------------------------------------------------------------------------------------------------------
Row_Suporte = Label(Windows, bg=Amarelo_Novo)
Row_Suporte.place(x=548, y=91, width=76, height=4)
# ---------------------------------------------------------------------------------------------------------------------
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Criando MENU Arquivo
Arquivo = Menubutton(Windows, text="CADASTRO", background=Cinza_Novo, foreground=Branco, font=Fonte_teste,
                     activebackground=Cinza_Novo, activeforeground=Branco)
Arquivo.place(x=60, y=68, height=20)
Arquivo.bind("<Enter>", Row_Up_Button_1)  # Ação Para Aparecer a linha embaixo da Label
Arquivo.bind("<Leave>", Row_Down_Button_1)  # Ação Para Desaparecer a linha embaixo da Label
Arquivo.menu = Menu(Arquivo, background=Cinza60, fg=Branco, tearoff=0, activebackground=Cinza_Novo)
Arquivo["menu"] = Arquivo.menu  # Criando Atributo menu pro MENU Arquivo
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Consultas = Menubutton(Windows, text="CONSULTA", background=Cinza_Novo, foreground=Branco, font=Fonte_teste,
                     activebackground=Cinza_Novo, activeforeground=Branco)
Consultas.place(x=170, y=68, height=20)
Consultas.bind("<Enter>", Row_Up_Button_2)  # Ação Para Aparecer a linha embaixo da Label
Consultas.bind("<Leave>", Row_Down_Button_2)  # Ação Para Desaparecer a linha embaixo da Label
Consultas.menu = Menu(Consultas, background=Cinza60, fg=Branco, tearoff=0, activebackground=Cinza_Novo)
Consultas["menu"] = Consultas.menu  # Criando Atributo menu pro MENU Consultas
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Relatorios = Menubutton(Windows, text="RELATÓRIOS", background=Cinza_Novo, foreground=Branco, font=Fonte_teste,
                     activebackground=Cinza_Novo, activeforeground=Branco)
Relatorios.place(x=276, y=68, height=20)
Relatorios.bind("<Enter>", Row_Up_Button_3)  # Ação Para Aparecer a linha embaixo da Label
Relatorios.bind("<Leave>", Row_Down_Button_3)  # Ação Para Desaparecer a linha embaixo da Label
Relatorios.menu = Menu(Relatorios, background=Cinza60, fg=Branco, tearoff=0, activebackground=Cinza_Novo)
Relatorios["menu"] = Relatorios.menu  # Criando Atributo menu pro MENU Relatorios
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Lancamento = Menubutton(Windows, text="LANÇAMENTO", background=Cinza_Novo, foreground=Branco, font=Fonte_teste,
                     activebackground=Cinza_Novo, activeforeground=Branco)
Lancamento.place(x=400, y=68, height=20)
Lancamento.bind("<Enter>", Row_Up_Button_4)  # Ação Para Aparecer a linha embaixo da Label
Lancamento.bind("<Leave>", Row_Down_Button_4)  # Ação Para Desaparecer a linha embaixo da Label
Lancamento.menu = Menu(Lancamento, background=Cinza_Novo, fg=Branco, tearoff=0, activebackground=Cinza40)
Lancamento["menu"] = Lancamento.menu  # Criando Atributo menu pro MENU Relatorios
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Suporte = Menubutton(Windows, text="SUPORTE", background=Cinza_Novo, foreground=Branco, font=Fonte_teste,
                     activebackground=Cinza_Novo, activeforeground=Branco)
Suporte.place(x=542, y=68, height=20)
Suporte.bind("<Enter>", Row_Up_Button_5)  # Ação Para Aparecer a linha embaixo da Label
Suporte.bind("<Leave>", Row_Down_Button_5)  # Ação Para Desaparecer a linha embaixo da Label
Suporte.menu = Menu(Suporte, background=Cinza_Novo, fg=Branco, tearoff=0, activebackground=Cinza40)
Suporte["menu"] = Suporte.menu  # Criando Atributo menu pro MENU Historicos
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Criando Clientes Menu com funções NOVO e EXCLUIR e EDITAR
ClientesMenu = Menu(Arquivo, background=Cinza_Novo, fg=Branco, tearoff=False, activebackground=Cinza40)
ClientesMenu.add_command(label='NOVO', font=Fonte_teste)
ClientesMenu.add_command(label='EXCLUIR', font=Fonte_teste)
ClientesMenu.add_command(label='EDITAR', font=Fonte_teste)
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# Criando Usuario Menu com funções NOVO e EXCLUIR
UsuarioMenu = Menu(Arquivo, background=Cinza_Novo, fg=Branco, tearoff=False, activebackground=Cinza40)
UsuarioMenu.add_command(label='NOVO', font=Fonte_teste, command=Register_Users)
UsuarioMenu.add_command(label='EXCLUIR', font=Fonte_teste)
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# Criando Grupo Menu com funções NOVO e EXCLUIR
GrupoMenu = Menu(Arquivo, background=Cinza_Novo, fg=Branco, tearoff=False, activebackground=Cinza40)
GrupoMenu.add_command(label='NOVO', font=Fonte_teste, command=Register_Group)
GrupoMenu.add_command(label='EXCLUIR', font=Fonte_teste, command=Delete_Group)
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# Criando Inserir Nota
Lancamento.menu.add_command(label='NOTA', font=Fonte_teste, command=Register_Note, activebackground=Cinza40)
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# Criando Produtos Menu com funções NOVO e EXCLUIR
ProdutosMenu = Menu(Arquivo, background=Cinza_Novo, fg=Branco, tearoff=False, activebackground=Cinza40)
ProdutosMenu.add_command(label='NOVO', font=Fonte_teste, command=Register_Prod)
ProdutosMenu.add_command(label='EXCLUIR', font=Fonte_teste, command=Excluir_Produtos)
# ---------------------------------------------------------------------------------------------------------------------
# Criando Consultas Menu com funções ESTOQUE, VENDAS, PRODUTO
Consultas.menu.add_command(label='ESTOQUE', font=Fonte_teste, background=Cinza_Novo, activebackground=Cinza40)
Consultas.menu.add_command(label='VENDAS', font=Fonte_teste, background=Cinza_Novo, activebackground=Cinza40)
Consultas.menu.add_command(label='PRODUTO', font=Fonte_teste, background=Cinza_Novo, activebackground=Cinza40,
                           command=Consulta_Prod)
# ---------------------------------------------------------------------------------------------------------------------
# Criando Relatorios Menu com função VENDAS
Relatorios.menu.add_command(label='VENDAS', font=Fonte_teste, background=Cinza_Novo, activebackground=Cinza40)
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
Arquivo.menu.add_cascade(label='CLIENTES', menu=ClientesMenu, font=Fonte_teste, background=Cinza_Novo,
                         activebackground=Cinza40)
Arquivo.menu.add_cascade(label="USUÁRIOS", menu=UsuarioMenu, font=Fonte_teste, background=Cinza_Novo,
                         activebackground=Cinza40)
Arquivo.menu.add_cascade(label="GRUPO", menu=GrupoMenu, font=Fonte_teste, background=Cinza_Novo,
                         activebackground=Cinza40)
Arquivo.menu.add_cascade(label="PRODUTOS", font=Fonte_teste, menu=ProdutosMenu, background=Cinza_Novo,
                         activebackground=Cinza40)
Arquivo.menu.add_command(label="FORNECEDOR", font=Fonte_teste, background=Cinza_Novo, activebackground=Cinza40,
                         command=Register_Industry)
Arquivo.menu.add_command(label="LOJA", font=Fonte_teste, background=Cinza_Novo, activebackground=Cinza40,
                         command=Register_Store)
Arquivo.menu.add_command(label="SAIR", font=Fonte_teste, background=Cinza_Novo, activebackground=Vermelho,
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
