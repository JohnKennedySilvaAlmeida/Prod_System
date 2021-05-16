# -*- coding: utf-8 -*-
# Modal dialog window with Progressbar for the bigger project
from tkinter import *
from tkinter import messagebox
import pymysql

# Criando Variaveis de Fontes e Cores
Fonte_8 = "Arial, 8"
Fonte_11 = "Arial, 11"
Fonte_12 = "Arial, 12"
Fonte_11B = ("Arial", 11, "bold")
Fonte_12B = ("Arial", 12, "bold")
Fonte_14B = ("Arial", 14, "bold")
Fonte12I = ("Courier", 12, "italic")
Branco = "white"
Cinza_Novo = "#262f36"
Amarelo_Novo = "#f99c11"
Cinza40 = "Gray40"
Lista_Users = []


def Autenticar_Login(event=None):

    Conexao = pymysql.connect(host="localhost", user="root", passwd="P@ssw0rd", db="BD_SYSTEM")
    Cursor_Login = Conexao.cursor()
    Curso_Pwrd = Conexao.cursor()
    Id_Login = ""
    Id_Pswd = ""
    Cursor_Login.execute("SELECT ID FROM USERS WHERE LOGIN_USER = '%s';" % VarNome_User.get())
    Curso_Pwrd.execute("SELECT ID FROM USERS WHERE PASSWORD = '%s';" % VarSenha.get())
    for log in Cursor_Login.fetchall():
        Id_Login = log[0]
    for psw in Curso_Pwrd.fetchall():
        Id_Pswd = psw[0]

    if Id_Login == Id_Pswd and Id_Login != "" and Id_Pswd != "":
        Windows_Login.destroy()
        Conexao.close()
        import Tela_Main
    else:
        messagebox.showinfo("ERROR", "DADOS INCORRETOS")
        VarNome_User.set("")
        VarSenha.set("")
        EntNome.focus()


# Criando o TK Tela de Login Principal
Windows_Login = Tk()
Windows_Login.geometry("400x300+450+200")  # Tamanho da Janela
Windows_Login.iconbitmap("Imagens/logo.ico")  # Anexando o Icone na Tela
Windows_Login.resizable(False, False)  # Desativando o Botão Maximizar a Janela
Windows_Login.title("LOGIN")  # Criando Titulo na Janela
Windows_Login.config(bg=Cinza_Novo)  # Determinando cor de fundo da janela, podendo criar outros atributos

#  Variavei de Imagens
Imagem_BarraCinza = PhotoImage(file="Imagens\\Barra_LogoCinza.png")
Imagem_BarraCinza2 = PhotoImage(file="Imagens\\Barra_LogoCinza2.png")

# -----------------------------------------------------------------------------------------------------------------
Lbl_Titulo9 = Label(Windows_Login, text="----" * 8, bg=Cinza_Novo, fg=Amarelo_Novo, font=Fonte12I)
Lbl_Titulo9.place(x=0, y=10)
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
Lbl_Sauda = Label(Windows_Login, text="BEM VINDO!", bg=Cinza_Novo, fg=Amarelo_Novo, font=Fonte_14B, anchor=W)
Lbl_Sauda.place(x=140, y=69, width=120)
# ---------------------------------------------------------------------------------------------------------------------
# Criando Variaveis pra receber valor digitado
VarNome_User = StringVar()
VarNome_User.set("")  # Setando Valor Nulo para variavel
VarSenha = StringVar()
VarSenha.set("")  # Setando Valor Nulo para variavel
# ---------------------------------------------------------------------------------------------------------------------
# LabelFrame da tela de Login
FrLogin = LabelFrame(Windows_Login, text="LOGIN", bg=Cinza_Novo, fg=Amarelo_Novo, font=Fonte_8)
FrLogin.place(x=50, y=100, width=300, height=150)
# Label do Usuario
LblLogin = Label(FrLogin, text="USUÁRIO:", bg=Cinza_Novo, fg=Branco, font=Fonte_11B)
LblLogin.place(x=5, y=5)
# Entrada do Usuario
EntNome = Entry(FrLogin, textvariable=VarNome_User, font=Fonte_12)
EntNome.place(x=90, y=5)
EntNome.focus()
# Label da Senha
LblSenha = Label(FrLogin, text="SENHA:", bg=Cinza_Novo, fg=Branco, font=Fonte_11B)
LblSenha.place(x=5, y=45)
# Entrada da Senha
EntSenha = Entry(FrLogin, textvariable=VarSenha, font=Fonte_12, show="*")
EntSenha.bind("<Return>", Autenticar_Login)
EntSenha.place(x=90, y=45)
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ----- Botões -----
# Botão ENTRAR
BtnEntrar = Button(FrLogin, text="ENTRAR", bg=Cinza40, fg=Branco, font=Fonte_12B, activebackground=Cinza_Novo,
                   activeforeground=Branco, command=Autenticar_Login)
BtnEntrar.place(x=192, y=80)
BtnEntrar.focus_set()
# ---------------------------------------------------------------------------------------------------------------------
# Formando Um LOOP da Tela
Windows_Login.mainloop()
