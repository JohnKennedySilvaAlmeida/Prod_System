# ---------- TELA DE CADASTRO DE USUÁRIOS -----------------------------------------------------------------------------

from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import pymysql
import datetime


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

tempo = datetime.date.today()  # Variavel recebendo o dia atual
List_Ano_Nasc = []
Primeiro_Ano = int(tempo.year) - 70  # Variavel recebendo Ano atual menos 70 Anos
Contador = 0
for i in range(71):
    List_Ano_Nasc.append(int(Primeiro_Ano) + Contador)
    Contador = Contador + 1

# Função Criado para Calcular Idade
def Calcula_Idade(event=None):

    try:
        mes_idade = int(Mes_Nasc_User.get()) + 1
        n = datetime.date.today() - datetime.date(int(Ano_Nasc_User.get()), mes_idade, int(Dia_Nasc_User.get()))
        idade_User.set(str(n.days / 365)[:2])
    except:
        idade_User.set('0')

# Função Criada para Limitar Tamanho de caracteres de Login
def limitar_Size_Login(login):
    if len(login) > 8:
        return False
    return True

# Função Criada para Limitar Tamanho de caracteres de Senha
def limitar_Size_Senha(Senha):
    if len(Senha) > 6:
        return False
    return True

# Função Criada para Limitar Tamanho de caracteres do CPF
def limitar_Size_Cpf(CPF):
    if len(CPF) > 14:
        return False
    return True

# Função criada para Apagar dados Digitados
def Limpar_Dados():
    Var_Nome_User.set("")
    Var_Cpf_User.set("")
    Var_Cod_Tel.set("")
    Var_Tel.set("")
    Var_Email_User.set("")
    Var_Senha_User.set("")
    Var_Senha_2_User.set("")
    Var_Login_User.set("")
    CMBDia_Nasc_User.set("DIA")
    CMBMes_Nasc_User.set("MÊS")
    CMBAno_Nasc_User.set("ANO")
    EntNome_User.focus()

# Função criada para O Nome do Usuário fique em Letras Maiusculas
def Nome_Maisc(event=None):
    Var_Nome_User.set(EntNome_User.get().upper())

def Up_Salvar(event=None):
    Lbl_txt_Salvar.config(fg=Branco)

def Dawn_Salvar(event=None):
    Lbl_txt_Salvar.config(fg=Cinza_Novo)

# Função criada para Mostra Senha quando CheckButton acionado
def Show_Senha(event=None):

    if Var_Show_Senha.get() == "0":
        EntSenha_User.config(show="")
        EntSenha2_User.config(show="")
        Var_Senha_User.set(EntSenha_User.get())
        Var_Senha_2_User.set(EntSenha2_User.get())
    else:
        EntSenha_User.config(show="*")
        EntSenha2_User.config(show="*")

def Cod_Area(event=None):
    if len(Var_Cod_Tel.get()) == 2:
        ETelCel.focus()

# Função Criada para limitar a 11 caracteres no Login e também somente Números
def validate(action, index, value_if_allowed,
             prior_value, text, validation_type, widget_name, possible_new_value, login):

    if text in '0123456789':
        try:
            float(value_if_allowed)
            if len(login) > 11:
                return False
            return True
        except ValueError:
            return False
    else:
        return False

# Função Criada para limitar a 11 caracteres no Fone e também somente Números
def validate_2(action, index, value_if_allowed,
             prior_value, text, validation_type, widget_name, possible_new_value, fone):

    if text in '0123456789':
        try:
            float(value_if_allowed)
            if len(fone) > 9:
                return False
            return True
        except ValueError:
            return False
    else:
        return False

# Função Criada para Acrescentar Ponto e traço no CPF digitado pra ficar formatado
def format_cpf(event=None):

    text = Var_Cpf_User.get().replace(".", "").replace("-", "")[:11]
    new_text = ""

    if event.keysym.lower() == "backspace": return

    for index in range(len(text)):

        if not text[index] in "0123456789": continue
        if index in [2, 5]:
            new_text += text[index] + "."
        elif index == 8:
            new_text += text[index] + "-"
        else:
            new_text += text[index]

    EntCpf_User.delete(0, "end")
    EntCpf_User.insert(0, new_text)

def Salvar_User(event=None):

    Conexao = ""
    Cursor_Ja_Cadastrado = ""
    btSalvar_User.config(state=DISABLED)
    # Tratando o erro de Entry vazio
    # Condição da Variavel da Entry USUÁRIO vazia
    if Var_Nome_User.get() == "" or Var_Cpf_User.get() == "" or Dia_Nasc_User.get() == "" or \
        Mes_Nasc_User.get() == "" or Ano_Nasc_User.get() == "" or Var_Cod_Tel.get() == "" or \
            Var_Tel.get() == "" or EntEmail_User.get() == "" or EntLogin_User.get() == "" or \
             Var_Senha_User.get() == "" or Var_Senha_2_User.get() == "":
        messagebox.showinfo('ERROR', 'HÁ CAMPO(S) SEM DADOS!', parent=Windows_User)
        btSalvar_User.config(state=NORMAL)
        EntNome_User.focus()
    else:
        CPF = Var_Cpf_User.get()
        try:
            Conexao = pymysql.connect(host="localhost", user="root", passwd="P@ssw0rd", db="BD_SYSTEM")
            Cursor_Ja_Cadastrado = Conexao.cursor()

        except:
            messagebox.showinfo("ERROR", "CAMPO INVÁLIDO", parent=Windows_User)

        Resultado_Pesq = Cursor_Ja_Cadastrado.execute("SELECT ID FROM USERS WHERE CPF = '%s';" % CPF)
        if Resultado_Pesq != 0:
            messagebox.showinfo("DUPLICADO", "USUÁRIO JA CADASTRADO COM ESSE CPF!", parent=Windows_User)
            Limpar_Dados()
            btSalvar_User.config(state=NORMAL)

        else:

            if Var_Senha_User.get() == Var_Senha_2_User.get():

                resultado = messagebox.askyesno("CONFIRMAÇÃO", f"VOCê CONFIRMA O CADASTRO DO USUÁRIO\n"
                            f"{Var_Nome_User.get().upper()} ?", parent=Windows_User)
                Dt_Nascimento = (f"{Ano_Nasc_User.get()}-{Mes_Nasc_User.get()}-{Dia_Nasc_User.get()}")

                if resultado == True:
                    Insert_User = "INSERT INTO USERS(NAME_USER, CPF, BIRTH_DATE, FONE, EMAIL, LOGIN_USER, PASSWORD)"\
                                     "VALUES(%s, %s, %s, %s, %s, %s, %s);"

                    ParamentrosUsuario = (Var_Nome_User.get().upper(),
                                          Var_Cpf_User.get(),
                                          Dt_Nascimento,
                                          f"{Var_Cod_User.get()}-{Var_Tel.get()}",
                                          EntEmail_User.get(),
                                          EntLogin_User.get(),
                                          Var_Senha_User.get())

                    cursor_bd = Conexao.cursor()
                    cursor_bd.execute(Insert_User, ParamentrosUsuario)
                    Conexao.commit()
                    Conexao.close()
                    Limpar_Dados()
                    messagebox.showinfo("CONFIRMAÇÃO",
                                        f"USUÁRIO {Var_Nome_User.get().upper()} CADASTRADO COM SUCESSO!",
                                        parent=Windows_User)
                    Windows_User.destroy()

                else:
                    Var_Nome_User.set(""), Var_Cpf_User.set(""), EntEmail_User.delete(0, END),\
                    EntLogin_User.delete(0, END), Var_Senha_User.set(""), Var_Senha_2_User.set("")
                    EntNome_User.focus()
                    btSalvar_User.config(state=NORMAL)

            else:
                messagebox.showerror('ERROR', 'Senha não Compactível com a Anterior', parent=Windows_User)
                Var_Senha_User.set("")
                Var_Senha_2_User.set("")
                EntSenha_User.focus()
                btSalvar_User.config(state=NORMAL)

# Estrutura para a Janela de Excluir Produtos ---------------------------------------------------------------------
Windows_User = Toplevel()
Windows_User.geometry("600x475+400+160")
Windows_User.title("SISTEMA DE GERENCIAMENTO")
Windows_User.minsize(600, 475)
Windows_User.maxsize(600, 475)
Windows_User.resizable(False, False)
Windows_User["bg"] = Cinza_Novo
Windows_User.iconbitmap("Imagens/logo.ico")
# -----------------------------------------------------------------------------------------------------------------

# Caminho com Variavel com a foto
Foto_User = PhotoImage(file="Imagens\\usuario.png")
Foto_Salvar = PhotoImage(file="Imagens\\Save.png")
Vcmd = (Windows_User.register(validate), '%d', '%i', '%i', '%s', '%S', '%v', '%V', '%W', '%P')
Vcmd2 = (Windows_User.register(validate_2), '%d', '%i', '%i', '%s', '%S', '%v', '%V', '%W', '%P')
# Recebendo Configurações de Combobox para mudança de Cores
Windows_User.option_add('*TCombobox*Listbox.font', Fonte11)
Windows_User.option_add('*TCombobox*Listbox.selectBackground', Cinza_Novo)
Windows_User.option_add('*TCombobox*Listbox.background', Branco)
Windows_User.option_add('*TCombobox*Listbox.selectForeground', Branco)
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
Lbl_Titulo5 = Label(Windows_User, text="----" * 10, bg=Cinza_Novo, fg=Amarelo_Novo, font=Fonte12I)
Lbl_Titulo5.place(x=0, y=10)
# -----------------------------------------------------------------------------------------------------------------
# Frame Secundários -----------------------------------------------------------------------------------------------
Tela_Principal = LabelFrame(Windows_User, text="CADASTRO DE USUÁRIO", font=Fonte10B, bg=Cinza40, fg=Amarelo_Novo)
Tela_Principal.place(x=90, y=85, width=500, height=380)
# Frame Secundários -----------------------------------------------------------------------------------------------
Tela_Pessoal = LabelFrame(Tela_Principal, text="DADOS PESSOAIS", font=Fonte8B, bg=Cinza40, fg=Amarelo_Novo)
Tela_Pessoal.place(x=0, y=0, width=490, height=235)
Tela_Password = LabelFrame(Tela_Principal, text="LOGIN", font=Fonte8B, bg=Cinza40, fg=Amarelo_Novo)
Tela_Password.place(x=0, y=237, width=490, height=115)
# -----------------------------------------------------------------------------------------------------------------

# Label para criar aviso do botão Salvar
Lbl_txt_Salvar = Label(Windows_User, text="Salvar", bg=Cinza_Novo, fg=Cinza_Novo, font=Fonte10)
Lbl_txt_Salvar.place(x=535, y=58)
# -----------------------------------------------------------------------------------------------------------------

# Imagem do Usuario
Label_Imagem_User = Label(Windows_User, image=Foto_User, border=0, bg=Cinza_Novo)
Label_Imagem_User.image = Foto_User
Label_Imagem_User.place(x=5, y=30)
# -----------------------------------------------------------------------------------------------------------------

# Label e Entry do CÓDIGO do Usuário
Conexao_Id = pymysql.connect(host="localhost", user="root", passwd="P@ssw0rd", db="BD_SYSTEM")
Cursor_id_User = Conexao_Id.cursor()
Cursor_id_User.execute("SELECT MAX(ID) FROM USERS")
Maximo_User = ""
for i in Cursor_id_User.fetchall():
    if i[0] == None:
        Maximo_User = "1"
    else:
        Maximo_User = int(i[0]) + 1
Var_Cod_User = StringVar()
Var_Cod_User.set(Maximo_User)
LblCod_User = Label(Tela_Pessoal, text="COD:", font=Fonte11B, bg=Cinza40, fg=Branco)
LblCod_User.place(x=10, y=5)
EntCod_User = Entry(Tela_Pessoal, font=Fonte12, width=8, textvariable=Var_Cod_User, state=DISABLED, justify=CENTER)
EntCod_User.place(x=80, y=5)
EntCod_User.bind("<KeyRelease>", Nome_Maisc)
# -----------------------------------------------------------------------------------------------------------------

# Label e Entry do NOME do Usuário
Var_Nome_User = StringVar()
Var_Nome_User.set("")
LblNome_User = Label(Tela_Pessoal, text="NOME:", font=Fonte11B, bg=Cinza40, fg=Branco)
LblNome_User.place(x=10, y=40)
EntNome_User = Entry(Tela_Pessoal, font=Fonte12, width=35, textvariable=Var_Nome_User)
EntNome_User.place(x=80, y=40)
EntNome_User.bind("<KeyRelease>", Nome_Maisc)
EntNome_User.focus()
# -----------------------------------------------------------------------------------------------------------------

# Label e Entry do CPF do Usuário
Var_Cpf_User = StringVar()
LblCpf_User = Label(Tela_Pessoal, text="CPF:", font=Fonte11B, bg=Cinza40, fg=Branco)
LblCpf_User.place(x=10, y=75)
Valided_Cpf = Tela_Password.register(func=limitar_Size_Cpf)
EntCpf_User = Entry(Tela_Pessoal, font=Fonte12, width=18, textvariable=Var_Cpf_User, justify=CENTER)
EntCpf_User.config(validate='key', validatecommand=(Valided_Cpf, '%P'))
EntCpf_User.bind("<KeyRelease>", format_cpf)
EntCpf_User.place(x=80, y=75)
# -----------------------------------------------------------------------------------------------------------------

# Label e Entry Data de Nascimento do Usuário
# Dia ---------------------------------------
Dia_Nasc_User = StringVar()
Dia_Nasc_User.set("")
LblDT_Nasc_User = Label(Tela_Pessoal, text='DATA NASC:', font=Fonte12B, bg=Cinza40, fg=Branco)
LblDT_Nasc_User.place(x=10, y=110)
CMBDia_Nasc_User = Combobox(Tela_Pessoal, font=Fonte12, textvariable=Dia_Nasc_User)
CMBDia_Nasc_User['values'] = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                         '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                         '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')
CMBDia_Nasc_User.set("DIA")
CMBDia_Nasc_User['state'] = 'readonly'
CMBDia_Nasc_User.place(x=125, y=110, width=50)

# Mês ---------------------------------------
Mes_Nasc_User = StringVar()
Mes_Nasc_User.set("")
CMBMes_Nasc_User = Combobox(Tela_Pessoal, font=Fonte12, textvariable=Mes_Nasc_User)
CMBMes_Nasc_User['values'] = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
CMBMes_Nasc_User.set("MÊS")
CMBMes_Nasc_User['state'] = 'readonly'
CMBMes_Nasc_User.place(x=185, y=110, width=60)

# Ano ---------------------------------------
Ano_Nasc_User = StringVar()
Ano_Nasc_User.set("")
CMBAno_Nasc_User = Combobox(Tela_Pessoal, font=Fonte12, background=Cinza40, textvariable=Ano_Nasc_User)
CMBAno_Nasc_User['values'] = List_Ano_Nasc
CMBAno_Nasc_User.set("ANO")
CMBAno_Nasc_User['state'] = 'readonly'
CMBAno_Nasc_User.place(x=255, y=110, width=60)

# Calculando Idade ------------------------------------------------------------------------------------------------
idade_User = StringVar()
LblAnos_User = Label(Tela_Pessoal, text='IDADE: ', font=Fonte12B, bg=Cinza40, fg=Branco)
LblAnos_User.place(x=320, y=110)
LblAnos2_User = Label(Tela_Pessoal, textvariable=idade_User, font=Fonte12B, bg=Cinza40, fg=Preto)
LblAnos2_User.place(x=400, y=110)
LblAnos3_User = Label(Tela_Pessoal, text='Anos.', font=Fonte12B, bg=Cinza40, fg=Branco)
LblAnos3_User.place(x=430, y=110)
CMBMes_Nasc_User.bind('<<ComboboxSelected>>', Calcula_Idade)
CMBDia_Nasc_User.bind('<<ComboboxSelected>>', Calcula_Idade)
CMBAno_Nasc_User.bind('<<ComboboxSelected>>', Calcula_Idade)
Calcula_Idade()
# -----------------------------------------------------------------------------------------------------------------

# Label e Entry Email do Usuário
Var_Email_User = StringVar()
Var_Email_User.set("")
LblEmail_User = Label(Tela_Pessoal, text="EMAIL:", font=Fonte12B, bg=Cinza40, fg=Branco)
LblEmail_User.place(x=10, y=145)
EntEmail_User = Entry(Tela_Pessoal, width=33, font=Fonte12, textvariable=Var_Email_User)
EntEmail_User.place(x=80, y=145)
# -----------------------------------------------------------------------------------------------------------------

# Label e Entry de Telefone
# ------------------
Var_Cod_Tel = StringVar()
Var_Tel = StringVar()
LTelCel = Label(Tela_Pessoal, text='TEL:', font=Fonte11B, bg=Cinza40, fg=Branco)
LTelCel.place(x=10, y=180)
ETelCelCodA = Entry(Tela_Pessoal, width=5, font=Fonte11, validatecommand=Vcmd, validate='key', justify=CENTER,
                    textvariable=Var_Cod_Tel)
ETelCelCodA.place(x=80, y=180, width=30)
ETelCelCodA.bind("<KeyRelease>", Cod_Area)

ETelCel = Entry(Tela_Pessoal, font=Fonte11, validatecommand=Vcmd2, validate='key', textvariable=Var_Tel)
ETelCel.place(x=130, y=180, width=100)

Lbl_3 = Label(Tela_Pessoal, text="-", font=Fonte11B, bg=Cinza40, fg=Branco).place(x=115, y=180)
Lbl_4 = Label(Tela_Pessoal, text="-", font=Fonte11B, bg=Cinza40, fg=Branco).place(x=115, y=180)
# -----------------------------------------------------------------------------------------------------------------

# Label e Entry Login do Usuário
Var_Login_User = StringVar()
Var_Login_User.set("")
lblLogin_User = Label(Tela_Password, text='LOGIN:*', font=Fonte12B, bg=Cinza40, fg=Branco)
lblLogin_User.place(x=5, y=5)
Valided = Tela_Password.register(func=limitar_Size_Login)
EntLogin_User = Entry(Tela_Password, validate='key', validatecommand=(Valided, '%P'), font=Fonte11, width=15)
EntLogin_User.config(textvariable=Var_Login_User)
EntLogin_User.place(x=100, y=5)
# -----------------------------------------------------------------------------------------------------------------

# Label e Entry 1° Senha do Usuário
Var_Senha_User = StringVar()
Var_Senha_User.set("")
lbSenha_User = Label(Tela_Password, text='SENHA:*', font=Fonte12B, bg=Cinza40, fg=Branco)
lbSenha_User.place(x=5, y=35)
Valided_Senha1 = Tela_Password.register(func=limitar_Size_Senha)
EntSenha_User = Entry(Tela_Password, validate='key', validatecommand=(Valided_Senha1, '%P'))
EntSenha_User.config(font=Fonte11, width=10, show="*", textvariable=Var_Senha_User)
EntSenha_User.place(x=100, y=35)
# -----------------------------------------------------------------------------------------------------------------

# Label e Entry 2° Senha do Usuário
Var_Senha_2_User = StringVar()
Var_Senha_2_User.set("")
lbSenha2_User = Label(Tela_Password, text='CONFIRMAR SENHA:*', font=Fonte12B, bg=Cinza40, fg=Branco)
lbSenha2_User.place(x=200, y=35)
Valided_Senha2 = Tela_Password.register(func=limitar_Size_Senha)
EntSenha2_User = Entry(Tela_Password, validate='key', validatecommand=(Valided_Senha2, '%P'))
EntSenha2_User.config(font=Fonte11, width=10, textvariable=Var_Senha_2_User, show="*")
EntSenha2_User.place(x=380, y=35)
EntSenha2_User.bind("<Return>", Salvar_User)
# -----------------------------------------------------------------------------------------------------------------

# CheckButton pra mostrar a senha ou não
Var_Show_Senha = StringVar()
Var_Show_Senha.set("0")
Chkbt_Show_Senha = Checkbutton(Tela_Password, text="MOSTRAR SENHA", bg=Cinza40, fg=Branco, font=Fonte8, onvalue=1)
Chkbt_Show_Senha.config(activebackground=Cinza40, activeforeground=Branco, variable=Var_Show_Senha,
                        selectcolor=Cinza40)
Chkbt_Show_Senha.place(x=5, y=65)
Chkbt_Show_Senha.bind("<Button>", Show_Senha)
# -----------------------------------------------------------------------------------------------------------------

# Label e Avisos de Login e Senha
lbRecado_User = Label(Tela_Password, text='Login com Máximo 8 Caracteres', font=Fonte8, bg=Cinza40, fg=Branco)
lbRecado_User.place(x=280, y=5)
lbRecado2_User = Label(Tela_Password, text='Senha com Máximo 6 Caracteres', font=Fonte8, bg=Cinza40, fg=Branco)
lbRecado2_User.place(x=280, y=65)
# -----------------------------------------------------------------------------------------------------------------

# BOTÕES.....
# Botão SALVAR
btSalvar_User = Button(Windows_User, bg=Cinza_Novo, image=Foto_Salvar, activebackground=Cinza_Novo, borderwidth=0)
btSalvar_User.config(command=Salvar_User)
btSalvar_User.image = Foto_Salvar
btSalvar_User.place(x=532, y=12)
btSalvar_User.bind("<Enter>", Up_Salvar)
btSalvar_User.bind("<Leave>", Dawn_Salvar)
# ------------------------ FIM ----------------------------------------------------------------------------------------
Windows_User.mainloop()
