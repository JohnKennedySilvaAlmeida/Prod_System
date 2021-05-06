# -*- coding: utf-8 -*-
# Modal dialog window with Progressbar for the bigger project
import time
from tkinter import *
from tkinter import simpledialog
from tkinter.ttk import Progressbar
from tkinter.ttk import Style
from tkinter import messagebox
import pymysql

# Criando Variaveis de Fontes e Cores
Fonte_10 = "Arial, 10"
Fonte_11 = "Arial, 11"
Fonte_12 = "Arial, 12"
Fonte_11B = ("Arial", 11, "bold")
Fonte_12B = ("Arial", 12, "bold")
Fonte_14B = ("Arial", 14, "bold")
Vermelho = "red"
Preto = "black"
Branco = "white"
Gold = "#daa520"
Cinza51 = "gray51"
Verde = "#276955"


def Autenticar_Login():

    Conexao = pymysql.connect(host="localhost", user="root", passwd="P@ssw0rd", db="DB_SYSTEM")
    Cursor_Login = Conexao.cursor()
    Cursor_Login.execute("SELECT ")





# Criando o TK Tela de Login Principal
Windows_Login = Tk()
Windows_Login.geometry("400x460+450+200")  # Tamanho da Janela
Windows_Login.iconbitmap("Imagens\\Logo_SFundo.ico")  # Anexando o Icone na Tela
Windows_Login.resizable(False, False)  # Desativando o Botão Maximizar a Janela
Windows_Login.title("Seja Bem Vindo")  # Criando Titulo na Janela
Windows_Login.config(bg=Verde)  # Determinando cor de fundo da janela, podendo criar outros atributos

#  Variavei de Imagens
Imagem_BarraCinza = PhotoImage(file="Imagens\\Barra_LogoCinza.png")
Imagem_BarraCinza2 = PhotoImage(file="Imagens\\Barra_LogoCinza2.png")

# ---------------------------------------------------------------------------------------------------------------------
# Criando Label para Anexar Imagem
Lbl_Barra_Cinza = Label(Windows_Login, image=Imagem_BarraCinza, bg=Verde)
Lbl_Barra_Cinza.image = Imagem_BarraCinza
Lbl_Barra_Cinza.place(x=3, y=10)
# Criando Label para Anexar Imagem
Lbl_Barra_Cinza2 = Label(Windows_Login, image=Imagem_BarraCinza2, bg=Verde)
Lbl_Barra_Cinza2.image = Imagem_BarraCinza2
Lbl_Barra_Cinza2.place(x=370, y=210)
# Criando Label para Anexar Imagem
Lbl_Barra_Dourada = Label(Windows_Login, image=Imagem_BarraCinza, bg=Verde)
Lbl_Barra_Dourada.image = Imagem_BarraCinza
Lbl_Barra_Dourada.place(x=3, y=260)
# ---------------------------------------------------------------------------------------------------------------------
Lbl_Sauda = Label(Windows_Login, text="BEM VINDO!", bg=Verde, fg=Branco, font=Fonte_14B, anchor=W)
Lbl_Sauda.place(x=140, y=170, width=120)
# ---------------------------------------------------------------------------------------------------------------------
# Criando Variaveis pra receber valor digitado
VarNome_User = StringVar()
VarNome_User.set("")  # Setando Valor Nulo para variavel
VarSenha = StringVar()
VarSenha.set("")  # Setando Valor Nulo para variavel
# ---------------------------------------------------------------------------------------------------------------------
# LabelFrame da tela de Login
FrLogin = LabelFrame(Windows_Login, text="LOGIN", bg=Verde, fg=Preto, font=Fonte_10)
FrLogin.place(x=50, y=200, width=300, height=150)
# Label do Usuario
LblLogin = Label(FrLogin, text="USUÁRIO:", bg=Verde, fg=Branco, font=Fonte_11B)
LblLogin.place(x=5, y=5)
# Entrada do Usuario
EntNome = Entry(FrLogin, textvariable=VarNome_User, font=Fonte_12)
EntNome.place(x=90, y=5)
EntNome.focus()
# Label da Senha
LblSenha = Label(FrLogin, text="SENHA:", bg=Verde, fg=Branco, font=Fonte_11B)
LblSenha.place(x=5, y=45)
# Entrada da Senha
EntSenha = Entry(FrLogin, textvariable=VarSenha, font=Fonte_12, show="*")
EntSenha.place(x=90, y=45)
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ----- Botões -----
# Botão ENTRAR
BtnEntrar = Button(FrLogin, text="ENTRAR", bg=Cinza51, fg=Branco, font=Fonte_12B)
BtnEntrar.place(x=138, y=80)
BtnEntrar.focus_set()
# botão SAIR
BtnCadastro = Button(FrLogin, text="SAIR", bg=Cinza51, fg=Branco, font=Fonte_12B)
BtnCadastro.place(x=221, y=80)
# ---------------------------------------------------------------------------------------------------------------------
# Formando Um LOOP da Tela
Windows_Login.mainloop()
