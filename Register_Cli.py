# ---------------- CADASTRO DE CLIENTES -------------------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox
from tkinter import Canvas as CV
from pycep_correios import get_address_from_cep
import pymysql
import datetime
from tkcalendar import DateEntry

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


global Contador
Contador = 1

def Consulta_Existente(event=None):
    try:
        Conexao = pymysql.connect(host="localhost", user="root", passwd="P@ssw0rd", db="ROMANO")
        Cursor_Existente_Cliente = Conexao.cursor()
        Cursor_Existente_Cliente.execute("SELECT IDCLIENTE FROM CLIENTES WHERE IDCLIENTE = '%s'"
                                         % Var_Cod_Loja.get().strip())
        Cod_Valido = Cursor_Existente_Cliente.fetchall()
        if Cod_Valido == ():
            pass
        else:
            messagebox.showinfo("ERROR", "CLIENTE JÁ CADASTRADO")
            Var_Cod_Loja.set("")
            EntCod_Loja.focus()
    except:
        messagebox.showinfo("ERROR", "ALGO DEU ERRADO")

def Codigo_num(action, index, value_if_allowed,
             prior_value, text, validation_type, trigger_type, widget_name):
    if text in '0123456789':
        try:
            float(value_if_allowed)
            return True
        except ValueError:
            return False
    else:
        return False


def Codigo_num_Tel(action, index, value_if_allowed,
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

def Title2(event=None):
    Var_Nome_Loja.set(EntNome_Loja.get().upper())

def Codigo_Area(event=None):
    if len(VarCod_Tel_Loja.get()) == 2:
        ETelCel_Loja.focus()

def Capitalise(event=None):
    Var_Rua_Loja.set(EntRua_Loja.get().title())

def Format_cnpj(event=None):
    text = Var_cnpj_Loja.get().replace(".", "").replace("-", "")[:15]
    new_text = ""

    if event.keysym.lower() == "backspace": return

    for index in range(len(text)):

        if not text[index] in "0123456789": continue
        if index in [1, 4]:
            new_text += text[index] + "."
        elif index == 7:
            new_text += text[index] + "/"
        elif index == 12:
            new_text += text[index] + "-"
        else:
            new_text += text[index]

    Ent_cnpj_Loja.delete(0, "end")
    Ent_cnpj_Loja.insert(0, new_text)

def Capitalise2(event=None):
    Var_Bairro_Loja.set(EntBairro_Loja.get().title())

def Cursor_1(event=None):
    ECep_Loja.focus()

def Cursor_2(event=None):
    if Var_Bairro_Loja.get() == "":
        EntBairro_Loja.focus()
    else:
        if Var_Cidade_Loja.get() == "":
            EntCidade_Loja.focus()
        else:
            EntEmail_Loja.focus()

def Cursor_3(event=None):
    EntEmail_Loja.focus()

def Hifem(event=None):
    Contar = len(ECep_Loja.get())
    if Contar == 5:
        ECep2_Loja.focus()

def Passando_Cliente(event=None):
    LblCliente_ori.config(fg=Branco)

def Saindo_Cliente(event=None):
    LblCliente_ori.config(fg=Cinza40)

def Botao_Salvar_emcima(event=None):
    LblBtn_Salvar.config(fg=Branco)

def Botap_Salvar_saindo(event=None):
    LblBtn_Salvar.config(fg=Cinza_Novo)

def Salvar_Cliente(event=None):

    if Var_Cod_Clientes.get() == "" or Var_Nome_Clientes.get() == "" or ECep.get() == "" or Var_Email.get() == "":
        messagebox.showinfo("VAZIO", "HÁ DADOS FALTANDO!")

    else:
        Confir = messagebox.askyesno("CONFIRMAÇÃO",
                                     f"VOCÊ CONFIRMA O CADASTRO DO CLIENTE\n{Var_Nome_Clientes.get().upper()}")
        if Confir == True:
            try:
                Dt_Objeto = datetime.datetime.strptime(Var_Data.get(), '%d/%m/%Y')
                Dt_formatado = datetime.datetime.strftime(Dt_Objeto, '%Y/%m/%d')
                Conexao = pymysql.connect(host="localhost", user="root", passwd="P@ssw0rd", db="ROMANO")
                Cursor_Bd_Clientes = Conexao.cursor()
                Clientes = ("INSERT INTO CLIENTES(IDCLIENTE, RAZAO, RUA, NUMERO, BAIRRO, CIDADE, EMAIL, ULT_COMPRA)"
                            "VALUES(%s, %s, %s, %s, %s, %s, %s, %s);")
                Parametros_Clientes = (Var_Cod_Clientes.get(), Var_Nome_Clientes.get(),
                                       Var_Rua_Clientes.get(), Var_Num_Clientes.get(),
                                       Var_Bairro_Clientes.get(), Var_Cidade_Clientes.get(),
                                       Var_Email.get(), Dt_formatado)
                Cursor_Bd_Clientes.execute(Clientes, Parametros_Clientes)
                Conexao.commit()
                Conexao.close()
                messagebox.showinfo("SUCESSO", f"CLIENTE {Var_Nome_Clientes.get()}\nCADASTRADO COM SUCESSO!")
                Windows_Cad_Cli.destroy()
            except:
                    messagebox.showinfo("CONEXÃO", "CLIENTE JÁ CADASTRADO")
                    Var_Cod_Clientes.set("")
                    Var_Nome_Clientes.set("")
                    ECep.delete(0, END)
                    Var_Rua_Clientes.set("")
                    Var_Cidade_Clientes.set("")
                    Var_Num_Clientes.set("")
                    Var_Bairro_Clientes.set("")
                    EntCod_Clientes.focus()
        else:
            Var_Cod_Clientes.set("")
            Var_Nome_Clientes.set("")
            ECep.delete(0, END)
            Var_Rua_Clientes.set("")
            Var_Cidade_Clientes.set("")
            Var_Num_Clientes.set("")
            Var_Bairro_Clientes.set("")
            EntCod_Clientes.focus()

def Upper_City(event=None):
    Var_Cidade_Loja.set(EntCidade_Loja.get().upper())

def Upper_Uf(event=None):
    Var_Uf_Loja.set(EntUf_Loja.get().upper())

def MudarStatus(habilitar):
    if habilitar == True:
        novoestado = NORMAL
    else:
        novoestado = DISABLED

    EntRua_Loja.config(state=novoestado)
    EntBairro_Loja.config(state=novoestado)
    EntCidade_Loja.config(state=novoestado)
    EntUf_Loja.config(state=novoestado)

def ConsultarCep(event=None):
    try:
        resultado = dict()
        resultado = get_address_from_cep(ECep_Loja.get() + ECep2_Loja.get())
        try:
            # Carregar Campos retornados na Tela
            MudarStatus(True)
            if resultado['cidade'] == '' and resultado['uf'] == '':
                EntRua_Loja.config(state=NORMAL)
                EntBairro_Loja.config(state=NORMAL)
                EntCidade_Loja.config(state=NORMAL)
                EntCidade_Loja.bind("<KeyRelease>", Upper_City)
                EntUf_Loja.bind("<KeyRelease>", Upper_Uf)
                EntUf_Loja.config(state=NORMAL)
                EntRua_Loja.focus()

            elif resultado['logradouro'] == '' and resultado['bairro'] == '':
                EntRua_Loja.config(state=NORMAL)
                EntBairro_Loja.config(state=NORMAL)
                EntRua_Loja.focus()
                EntCidade_Loja.delete(0, END)
                EntCidade_Loja.insert(0, resultado['cidade'].upper())
                EntUf_Loja.delete(0, END)
                EntUf_Loja.insert(0, resultado['uf'])
                EntCidade_Loja.config(state=DISABLED)
                EntUf_Loja.config(state=DISABLED)

            else:
                EntRua_Loja.delete(0, END)
                EntRua_Loja.insert(0, resultado['logradouro'])
                EntBairro_Loja.delete(0, END)
                EntBairro_Loja.insert(0, resultado['bairro'])
                EntCidade_Loja.delete(0, END)
                EntCidade_Loja.insert(0, resultado['cidade'].upper())
                EntUf_Loja.delete(0, END)
                EntUf_Loja.insert(0, resultado['uf'])
                MudarStatus(False)
                EntNum_Loja.focus()
        except:
            messagebox.showerror("Erro Consulta CEP", "O CEP informado não é válido", parent=Windows_Cad_Cli)
            ECep_Loja.focus()

        return resultado
    except:
        Cep_Consulta = messagebox.askyesno("SEM CONEXÃO", "SEM CONEXÃO COM INTERNET! DESEJA CONTINUAR",
                                           parent=Windows_Cad_Cli)
        if Cep_Consulta == True:
            EntRua_Loja.config(state=NORMAL)
            EntBairro_Loja.config(state=NORMAL)
            EntCidade_Loja.config(state=NORMAL)
            EntUf_Loja.config(state=NORMAL)
            EntRua_Loja.focus()
            EntCidade_Loja.bind("<KeyRelease>", Upper_City)
            EntUf_Loja.bind("<KeyRelease>", Upper_Uf)
        else:
            Windows_Cad_Cli.destroy()


Windows_Cad_Cli = Tk()
Windows_Cad_Cli.geometry("555x485+400+150")
Windows_Cad_Cli.title("SOFTWARE DE GERENCIAMENTO")
Windows_Cad_Cli.minsize(555, 485)
Windows_Cad_Cli.maxsize(555, 485)
Windows_Cad_Cli.resizable(False, False)
Windows_Cad_Cli["bg"] = Cinza_Novo
Windows_Cad_Cli.iconbitmap("Imagens/Logo_SFundo.ico")


# Caminho com Variavel com a foto
Foto_Salvar_Loja = PhotoImage(file="Imagens//Save.png")
Imagem_Validate = PhotoImage(file='Imagens//Validate.png')
cod_unt = (Windows_Cad_Cli.register(Codigo_num), '%d', '%i', '%i', '%s', '%S', '%v', '%V', '%W')
cod_tel = (Windows_Cad_Cli.register(Codigo_num_Tel), '%d', '%i', '%i', '%s', '%S', '%v', '%V', '%W', '%P')

FrLoja_Geral = LabelFrame(Windows_Cad_Cli, text="CADASTRO DE LOJA", bg=Cinza40, fg=Amarelo_Novo, font=Fonte11B)
FrLoja_Geral.place(x=5, y=80, width=540, height=395)

FrEnd_Loja = LabelFrame(FrLoja_Geral, text="ENDEREÇO", bg=Cinza40, fg=Amarelo_Novo, font=Fonte10)
FrEnd_Loja.place(x=3, y=170, width=530, height=160)

# Label para criar aviso do botão Consultar Cep
LblCliente_ori = Label(FrEnd_Loja, text="Consultar Cep", bg=Cinza40, fg=Cinza40, font=Fonte10)
LblCliente_ori.place(x=180, y=5)
# -----------------------------------------------------------------------------------------------------------------
Lbl_Titulo4 = Label(Windows_Cad_Cli, text="----" * 8, bg=Cinza_Novo, fg=Amarelo_Novo, font=Fonte12I)
Lbl_Titulo4.place(x=0, y=10)
# -----------------------------------------------------------------------------------------------------------------
# Label para criar aviso do botão Salvar
LblBtn_Salvar = Label(Windows_Cad_Cli, text="Salvar", bg=Cinza_Novo, fg=Cinza_Novo, font=Fonte10)
LblBtn_Salvar.place(x=487, y=57)

# ---------------------------------------------------------------------------------------------------------------------
# Label e Entry do CODIGO da Loja
Var_Cod_Loja = StringVar()
LblCod_Loja = Label(FrLoja_Geral, text="COD:", font=Fonte11B, bg=Cinza40, fg=Branco)
LblCod_Loja.place(x=5, y=5)
EntCod_Loja = Entry(FrLoja_Geral, font=Fonte12, width=10, textvariable=Var_Cod_Loja, justify=CENTER,
                        validate='key', validatecommand=cod_unt)
EntCod_Loja.place(x=80, y=5)
EntCod_Loja.focus()
EntCod_Loja.bind("<FocusOut>", Consulta_Existente)
# ---------------------------------------------------------------------------------------------------------------------

# Label e Entry da Última Compra do Cliente
Var_Data = StringVar()
LblDAta = Label(FrLoja_Geral, text="DATA CADASTRO:", font=Fonte11B, bg=Cinza40, fg=Branco)
LblDAta.place(x=220, y=5)
Dt_Cadastro = DateEntry(FrLoja_Geral, date_pattern='dd/MM/yyyy', width=12, bg=Cinza_Novo, fg=Branco, font=Fonte12,
                     borderwidth=2, textvariable=Var_Data, state=DISABLED)
Dt_Cadastro.place(x=360, y=5)
# ---------------------------------------------------------------------------------------------------------------------

# Label e Entry da Razão da Loja
Var_Nome_Loja = StringVar()
LblNome_Loja = Label(FrLoja_Geral, text="RAZÃO:", font=Fonte11B, bg=Cinza40, fg=Branco)
LblNome_Loja.place(x=5, y=40)
EntNome_Loja = Entry(FrLoja_Geral, font=Fonte12, width=35, textvariable=Var_Nome_Loja)
EntNome_Loja.place(x=100, y=40)
EntNome_Loja.bind("<KeyRelease>", Title2)
EntNome_Loja.bind("<Tab>", Cursor_1)
EntNome_Loja.bind("<FocusOut>", Cursor_1)
# ---------------------------------------------------------------------------------------------------------------------

# Label e Entry do Nome Fantasia da Loja
Var_Fantasia_Loja = StringVar()
LblFantasia_Loja = Label(FrLoja_Geral, text="FANTASIA:", font=Fonte11B, bg=Cinza40, fg=Branco)
LblFantasia_Loja.place(x=5, y=75)
EntFantasia_Loja = Entry(FrLoja_Geral, font=Fonte12, width=35, textvariable=Var_Fantasia_Loja)
EntFantasia_Loja.place(x=100, y=75)
# ---------------------------------------------------------------------------------------------------------------------

# Label e Entry de Telefone da Loja
VarCod_Tel_Loja = StringVar()
Var_Tel_Loja = StringVar()
LTelCel_Loja = Label(FrLoja_Geral, text='TELEFONE:', font=Fonte11B, bg=Cinza40, fg=Branco)
LTelCel_Loja.place(x=5, y=110)
ETelCelCodA_Loja = Entry(FrLoja_Geral, width=5, font=Fonte11, validatecommand=cod_tel, validate='key', justify=CENTER,
                    textvariable=VarCod_Tel_Loja)
ETelCelCodA_Loja.place(x=100, y=110, width=30)
ETelCelCodA_Loja.bind("<KeyRelease>", Codigo_Area)

ETelCel_Loja = Entry(FrLoja_Geral, font=Fonte11, validatecommand=cod_tel, validate='key', textvariable=Var_Tel_Loja)
ETelCel_Loja.place(x=150, y=110, width=100)

Lbl_6 = Label(FrLoja_Geral, text="-", font=Fonte11B, bg=Cinza40, fg=Branco).place(x=135, y=110)
Lbl_7 = Label(FrLoja_Geral, text="-", font=Fonte11B, bg=Cinza40, fg=Branco).place(x=135, y=110)
# ---------------------------------------------------------------------------------------------------------------------

# Label e Entry do CNPJ da Loja
Var_cnpj_Loja = StringVar()
Lbl_cnpj_Loja = Label(FrLoja_Geral, text="CNPJ:", font=Fonte11B, bg=Cinza40, fg=Branco)
Lbl_cnpj_Loja.place(x=5, y=145)
Ent_cnpj_Loja = Entry(FrLoja_Geral, font=Fonte12, width=20, textvariable=Var_cnpj_Loja, justify=CENTER)
Ent_cnpj_Loja.place(x=70, y=145)
Ent_cnpj_Loja.bind("<KeyRelease>", Format_cnpj)
# ---------------------------------------------------------------------------------------------------------------------

# Label e Entry da Inscrição Estadual da Loja
Var_insc_est_Loja = StringVar()
Lbl_insc_est_Loja = Label(FrLoja_Geral, text="INSCRIÇÃO EST:", font=Fonte11B, bg=Cinza40, fg=Branco)
Lbl_insc_est_Loja.place(x=260, y=145)
Ent_insc_est_Loja = Entry(FrLoja_Geral, font=Fonte12, width=15, textvariable=Var_insc_est_Loja, justify=CENTER)
Ent_insc_est_Loja.place(x=390, y=145)
# ---------------------------------------------------------------------------------------------------------------------

# Campo CEP da Loja
Var_Cep_Loja = StringVar()
LblCep_Loja = Label(FrEnd_Loja, text='CEP: *', font=Fonte11B, background=Cinza40, fg=Branco)
LblCep_Loja.place(x=5, y=5)
ECep_Loja = Entry(FrEnd_Loja, font=Fonte11, width=5, validatecommand=cod_unt, validate='key', justify=CENTER)
ECep_Loja.place(x=60, y=5)
ECep_Loja.bind("<KeyRelease>", Hifem)
LblHifen = Label(FrEnd_Loja, text='-', font=Fonte12B, bg=Cinza40, fg=Branco)
LblHifen.place(x=105, y=4)
ECep2_Loja = Entry(FrEnd_Loja, font=Fonte11, width=3, validatecommand=cod_unt, validate='key', justify=CENTER)
ECep2_Loja.place(x=117, y=5)
ECep2_Loja.bind("<Return>", ConsultarCep)
# ---------------------------------------------------------------------------------------------------------------------

# Label e Entry da Rua da Loja
Var_Rua_Loja = StringVar()
LblRua_Loja = Label(FrEnd_Loja, text="RUA:", font=Fonte11B, bg=Cinza40, fg=Branco)
LblRua_Loja.place(x=5, y=40)
EntRua_Loja = Entry(FrEnd_Loja, font=Fonte12, width=29, textvariable=Var_Rua_Loja, state=DISABLED)
EntRua_Loja.place(x=60, y=40)
EntRua_Loja.bind("<KeyRelease>", Capitalise)
# ---------------------------------------------------------------------------------------------------------------------

# Label e Entry do Números da Loja
Var_Num_Loja = StringVar()
LblNum_Loja = Label(FrEnd_Loja, text="N°", font=Fonte11B, bg=Cinza40, fg=Branco)
LblNum_Loja.place(x=330, y=40)
EntNum_Loja = Entry(FrEnd_Loja, font=Fonte12, width=6, textvariable=Var_Num_Loja, validate='key',
               validatecommand=cod_unt)
EntNum_Loja.place(x=360, y=40)
EntNum_Loja.bind("<FocusOut>", Cursor_2)
# ---------------------------------------------------------------------------------------------------------------------

# Label e Entry do Bairro da Loja
Var_Bairro_Loja = StringVar()
LblBairro_Loja = Label(FrEnd_Loja, text="BAIRRO:", font=Fonte11B, bg=Cinza40, fg=Branco)
LblBairro_Loja.place(x=5, y=75)
EntBairro_Loja = Entry(FrEnd_Loja, font=Fonte12, width=20, textvariable=Var_Bairro_Loja, state=DISABLED)
EntBairro_Loja.place(x=80, y=75)
EntBairro_Loja.bind("<KeyRelease>", Capitalise2)
EntBairro_Loja.bind("<FocusOut>", Cursor_2)
# ---------------------------------------------------------------------------------------------------------------------

# Label e Entry do Cidade da Loja
Var_Cidade_Loja = StringVar()
LblCidade_Loja = Label(FrEnd_Loja, text="CIDADE:", font=Fonte11B, bg=Cinza40, fg=Branco)
LblCidade_Loja.place(x=5, y=110)
EntCidade_Loja = Entry(FrEnd_Loja, font=Fonte12, width=25, textvariable=Var_Cidade_Loja, state=DISABLED)
EntCidade_Loja.place(x=80, y=110)
# ---------------------------------------------------------------------------------------------------------------------

# Label e Entry do UF da Loja
Var_Uf_Loja = StringVar()
LblUf_Loja = Label(FrEnd_Loja, text="UF:", font=Fonte11B, bg=Cinza40, fg=Branco)
LblUf_Loja.place(x=320, y=110)
EntUf_Loja = Entry(FrEnd_Loja, font=Fonte12, width=3, state=DISABLED, justify=CENTER, textvariable=Var_Uf_Loja)
EntUf_Loja.place(x=350, y=110)
EntUf_Loja.bind("<FocusOut>", Cursor_3)
# ---------------------------------------------------------------------------------------------------------------------

# Label e Entry do Email do Cliente
Var_Email_Loja = StringVar()
LblEmail_Loja = Label(FrLoja_Geral, text="EMAIL:", font=Fonte11B, bg=Cinza40, fg=Branco)
LblEmail_Loja.place(x=5, y=340)
EntEmail_Loja = Entry(FrLoja_Geral, font=Fonte12, width=45, textvariable=Var_Email_Loja)
EntEmail_Loja.place(x=80, y=340)
EntEmail_Loja.bind("<F2>", Salvar_Cliente)
EntEmail_Loja.bind("<Return>", Salvar_Cliente)
# ---------------------------------------------------------------------------------------------------------------------

# ---- BOTÃO ----------------------------------------------------------------------------------------------------------
# Botão CEP Validar
Btn_cep = Button(FrEnd_Loja, bg=Cinza40, takefocus=False, activebackground=Cinza40, command=ConsultarCep)
Btn_cep.place(x=155, y=5)
Btn_cep.config(image=Imagem_Validate)
Btn_cep.imagem = Imagem_Validate
Btn_cep.bind("<Enter>", Passando_Cliente)
Btn_cep.bind("<Leave>", Saindo_Cliente)
# ---------------------------------------------------------------------------------------------------------------------
# ---- BOTÃO ----------------------------------------------------------------------------------------------------------
btSalvar_Clientes = Button(Windows_Cad_Cli, bg=Cinza_Novo, image=Foto_Salvar_Loja, activebackground=Cinza_Novo,
                           command=Salvar_Cliente, borderwidth=0)
btSalvar_Clientes.image = Foto_Salvar_Loja
btSalvar_Clientes.place(x=484, y=12)
btSalvar_Clientes.bind("<Enter>", Botao_Salvar_emcima)
btSalvar_Clientes.bind("<Leave>", Botap_Salvar_saindo)
# ------------------------ FIM ----------------------------------------------------------------------------------------
Windows_Cad_Cli.mainloop()
