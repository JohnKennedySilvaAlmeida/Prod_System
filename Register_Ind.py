# ---------------- CADASTRO DE FORNECEDOR -----------------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox
import pymysql
from pycep_correios import get_address_from_cep
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
Fonte_teste = ("Palatino Linotype", 12, "bold")

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

def Title2(event=None):
    Var_Name_Ind.set(EntNome_Ind.get().upper())

def Capitalise(event=None):
    Var_Street_Ind.set(EntStreet_Ind.get().title())

def Capitalise2(event=None):
    Var_Bairro_Ind.set(EntBairro_Ind.get().title())

def Cursor_1(event=None):
    EntEmail_Ind.focus()

def Cursor_2(event=None):
    if Var_Bairro_Ind.get() == "":
        EntBairro_Ind.focus()
    else:
        if Var_City_Ind.get() == "":
            Ent_City_Ind.focus()
        else:
            EntEmail_Ind.focus()

def Cursor_3(event=None):
    EntCep1_Ind.focus()

def Hifem(event=None):
    Contar = len(Var_Cep1_Ind.get())
    if Contar == 5:
        EntCep2_Ind.focus()

def Passando_Cliente(event=None):
    Lbl_Ind_Consulta_Cep.config(fg=Branco)

def Saindo_Cliente(event=None):
    Lbl_Ind_Consulta_Cep.config(fg=Cinza40)

def Botao_Salvar_emcima(event=None):
    LblBtn_Save.config(fg=Branco)

def Botap_Salvar_saindo(event=None):
    LblBtn_Save.config(fg=Cinza_Novo)

def Save_Industry(event=None):

    if Var_Name_Ind.get() == "" or \
            Var_Email_Ind.get() == "" or \
            Var_Cep1_Ind.get() == "" or \
            Var_Cep2_Ind.get() == "" or \
            Var_Street_Ind.get() == "" or \
            Var_Numb_Ind.get() == "" or \
            Var_Bairro_Ind.get() == "" or \
            Var_City_Ind.get() == "" or \
            Var_Uf_Ind.get() == "":
        messagebox.showinfo("VAZIO", "HÁ DADOS FALTANDO!", parent=Windows_Cad_Ind)

    else:
        Confir = messagebox.askyesno("CONFIRMAÇÃO",
                                     f"VOCÊ CONFIRMA O CADASTRO DO FORNECEDOR\n{Var_Name_Ind.get().upper()}")
        if Confir == True:

            try:
                tempo = datetime.datetime.now()
                data = f"{tempo.day}/{tempo.month}/{tempo.year}"
                Conexao = pymysql.connect(host="localhost", user="root", passwd="P@ssw0rd", db="BD_SYSTEM")
                Cursor__BDInd = Conexao.cursor()
                Dt_Objeto = datetime.datetime.strptime(data, '%d/%m/%Y')
                Dt_formatado = datetime.datetime.strftime(Dt_Objeto, '%Y/%m/%d')
                Industria = ("INSERT INTO INDUSTRY(ID_IND, NAME_IND, EMAIL_IND, CEP_IND, STREET_IND, NUMBER_IND, "
                             "BAIRRO_IND, CITY_IND, STATE_IND, LAST_PAY_IND)"
                            "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);")
                Parametros_Industry = (Var_Cod_Ind.get(),
                                       Var_Name_Ind.get(),
                                       Var_Email_Ind.get(),
                                       f"{Var_Cep1_Ind.get()}-{Var_Cep2_Ind.get()}",
                                       Var_Street_Ind.get(),
                                       Var_Numb_Ind.get(),
                                       Var_Bairro_Ind.get(),
                                       Var_City_Ind.get(),
                                       Var_Uf_Ind.get(),
                                       Dt_formatado)
                Cursor__BDInd.execute(Industria, Parametros_Industry)
                Conexao.commit()
                Conexao.close()
                messagebox.showinfo("SUCESSO", f"FORNECEDOR {Var_Name_Ind.get()}\nCADASTRADO COM SUCESSO!",
                                    parent=Windows_Cad_Ind)
                Windows_Cad_Ind.destroy()
            except:
                messagebox.showinfo("ERRO", "ALGO DEU ERRADO", parent=Windows_Cad_Ind)

        else:
            Var_Name_Ind.set("")
            Var_Email_Ind.set("")
            Var_Cep1_Ind.set("")
            Var_Cep2_Ind.set("")
            Var_Street_Ind.set("")
            Var_Numb_Ind.set("")
            Var_Bairro_Ind.set("")
            Var_City_Ind.set("")
            Var_Uf_Ind.set("")
            EntNome_Ind.focus()

def Upper_City(event=None):
    Var_City_Ind.set(Ent_City_Ind.get().upper())

def Upper_Uf(event=None):
    Var_Uf_Ind.set(EntUf_Ind.get().upper())

def MudarStatus(habilitar):
    if habilitar == True:
        novoestado = NORMAL
    else:
        novoestado = DISABLED

    EntStreet_Ind.config(state=novoestado)
    EntBairro_Ind.config(state=novoestado)
    Ent_City_Ind.config(state=novoestado)
    EntUf_Ind.config(state=novoestado)

def ConsultarCep(event=None):
    try:
        resultado = dict()
        resultado = get_address_from_cep(Var_Cep1_Ind.get() + Var_Cep2_Ind.get())
        try:
            # Carregar Campos retornados na Tela
            MudarStatus(True)
            if resultado['cidade'] == '' and resultado['uf'] == '':
                EntStreet_Ind.config(state=NORMAL)
                EntBairro_Ind.config(state=NORMAL)
                Ent_City_Ind.config(state=NORMAL)
                Ent_City_Ind.bind("<KeyRelease>", Upper_City)
                EntUf_Ind.bind("<KeyRelease>", Upper_Uf)
                EntUf_Ind.config(state=NORMAL)
                EntStreet_Ind.focus()

            elif resultado['logradouro'] == '' and resultado['bairro'] == '':
                EntStreet_Ind.config(state=NORMAL)
                EntBairro_Ind.config(state=NORMAL)
                EntStreet_Ind.focus()
                Ent_City_Ind.delete(0, END)
                Ent_City_Ind.insert(0, resultado['cidade'].upper())
                EntUf_Ind.delete(0, END)
                EntUf_Ind.insert(0, resultado['uf'])
                Ent_City_Ind.config(state=DISABLED)
                EntUf_Ind.config(state=DISABLED)

            else:
                EntStreet_Ind.delete(0, END)
                EntStreet_Ind.insert(0, resultado['logradouro'])
                EntBairro_Ind.delete(0, END)
                EntBairro_Ind.insert(0, resultado['bairro'])
                Ent_City_Ind.delete(0, END)
                Ent_City_Ind.insert(0, resultado['cidade'].upper())
                EntUf_Ind.delete(0, END)
                EntUf_Ind.insert(0, resultado['uf'])
                MudarStatus(False)
                EntNumb_Ind.focus()
        except:
            messagebox.showerror("Erro Consulta CEP", "O CEP informado não é válido", parent=Windows_Cad_Ind)
            EntCep1_Ind.focus()

        return resultado
    except:
        messagebox.showinfo("SEM CONEXÃO", "ALGO DEU ERRADO", parent=Windows_Cad_Ind)


Windows_Cad_Ind = Toplevel()
Windows_Cad_Ind.geometry("455x390+400+150")
Windows_Cad_Ind.title("SOFTWARE DE GERENCIAMENTO")
Windows_Cad_Ind.minsize(455, 390)
Windows_Cad_Ind.maxsize(455, 390)
Windows_Cad_Ind.resizable(False, False)
Windows_Cad_Ind["bg"] = Cinza_Novo
Windows_Cad_Ind.iconbitmap("Imagens/Logo_SFundo.ico")

# Caminho com Variavel com a foto
Img_Save_Ind = PhotoImage(file="Imagens//Save.png")
Img_Validate = PhotoImage(file='Imagens//Validate.png')
Just_Numb = (Windows_Cad_Ind.register(Codigo_num), '%d', '%i', '%i', '%s', '%S', '%v', '%V', '%W')
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Fr_Industria = LabelFrame(Windows_Cad_Ind, text="CADASTRO DE FORNECEDOR", bg=Cinza40, fg=Amarelo_Novo, font=Fonte11B)
Fr_Industria.place(x=5, y=80, width=440, height=290)
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Fr_Street_Ind = LabelFrame(Fr_Industria, text="ENDEREÇO", bg=Cinza40, fg=Branco, font=Fonte8B)
Fr_Street_Ind.place(x=3, y=105, width=430, height=160)
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Lbl_Titulo10 = Label(Windows_Cad_Ind, text="----"*8, bg=Cinza_Novo, fg=Amarelo_Novo, font=Fonte12I)
Lbl_Titulo10.place(x=0, y=20)
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Label para criar aviso do botão Consultar Cep
Lbl_Ind_Consulta_Cep = Label(Fr_Street_Ind, text="Consultar Cep", bg=Cinza40, fg=Cinza40, font=Fonte10)
Lbl_Ind_Consulta_Cep.place(x=180, y=5)

# Label para criar aviso do botão Salvar
LblBtn_Save = Label(Windows_Cad_Ind, text="Salvar", bg=Cinza_Novo, fg=Cinza_Novo, font=Fonte10)
LblBtn_Save.place(x=388, y=57)
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# ---------------------------------------------------------------------------------------------------------------------
# Label e Entry do CODIGO DA INDÚSTRIA
Var_Cod_Ind = StringVar()
Conexao = pymysql.connect(host="localhost", user="root", passwd="P@ssw0rd", db="BD_SYSTEM")
Cursor_Id_Ind = Conexao.cursor()
Cursor_Id_Ind.execute("SELECT MAX(ID_IND) FROM INDUSTRY")
for ind in Cursor_Id_Ind.fetchall():
    if ind[0] == None:
        Var_Cod_Ind.set("1")
    else:
        Var_Cod_Ind.set(ind[0])
Conexao.commit()
Conexao.close()
LblCod_Ind = Label(Fr_Industria, text="COD:", font=Fonte11B, bg=Cinza40, fg=Branco)
LblCod_Ind.place(x=5, y=5)
EntCod_Ind = Entry(Fr_Industria, font=Fonte12, width=10, textvariable=Var_Cod_Ind, justify=CENTER)
EntCod_Ind.config(validate='key', validatecommand=Just_Numb, state=DISABLED)
EntCod_Ind.place(x=80, y=5)
# ---------------------------------------------------------------------------------------------------------------------
# Label e Entry do NOME Da Indústria
Var_Name_Ind = StringVar()
LblNome_Ind = Label(Fr_Industria, text="RAZÃO:", font=Fonte11B, bg=Cinza40, fg=Branco)
LblNome_Ind.place(x=5, y=40)
EntNome_Ind = Entry(Fr_Industria, font=Fonte12, width=35, textvariable=Var_Name_Ind)
EntNome_Ind.place(x=80, y=40)
EntNome_Ind.bind("<KeyRelease>", Title2)
EntNome_Ind.bind("<Tab>", Cursor_1)
EntNome_Ind.bind("<FocusOut>", Cursor_1)
EntNome_Ind.focus()
# ---------------------------------------------------------------------------------------------------------------------
# Label e Entry do Email da Indústria
Var_Email_Ind = StringVar()
LblEmail_Ind = Label(Fr_Industria, text="EMAIL:", font=Fonte11B, bg=Cinza40, fg=Branco)
LblEmail_Ind.place(x=5, y=75)
EntEmail_Ind = Entry(Fr_Industria, font=Fonte12, width=35, textvariable=Var_Email_Ind)
EntEmail_Ind.place(x=80, y=75)
EntEmail_Ind.bind("<Tab>", Cursor_3)
EntEmail_Ind.bind("<FocusOut>", Cursor_3)
# ---------------------------------------------------------------------------------------------------------------------
# Campo CEP da Indústria
Var_Cep1_Ind = StringVar()
LblCep_Ind = Label(Fr_Street_Ind, text='CEP: *', font=Fonte11B, background=Cinza40, fg=Branco)
LblCep_Ind.place(x=5, y=5)
EntCep1_Ind = Entry(Fr_Street_Ind, font=Fonte11, width=5, validatecommand=Just_Numb, validate='key', justify=CENTER)
EntCep1_Ind.config(textvariable=Var_Cep1_Ind)
EntCep1_Ind.place(x=60, y=5)
EntCep1_Ind.bind("<KeyRelease>", Hifem)
# ---------------------------------------------------------------------------------------------------------------------
LblHifen = Label(Fr_Street_Ind, text='-', font=Fonte12B, bg=Cinza40, fg=Branco)
LblHifen.place(x=105, y=4)
# ---------------------------------------------------------------------------------------------------------------------
Var_Cep2_Ind = StringVar()
EntCep2_Ind = Entry(Fr_Street_Ind, font=Fonte11, width=3, validatecommand=Just_Numb, validate='key', justify=CENTER)
EntCep2_Ind.config(textvariable=Var_Cep2_Ind)
EntCep2_Ind.place(x=117, y=5)
EntCep2_Ind.bind("<Return>", ConsultarCep)
# ---------------------------------------------------------------------------------------------------------------------
# Label e Entry da Rua da Indústria
Var_Street_Ind = StringVar()
LblStreet_Ind = Label(Fr_Street_Ind, text="RUA:", font=Fonte11B, bg=Cinza40, fg=Branco)
LblStreet_Ind.place(x=5, y=40)
EntStreet_Ind = Entry(Fr_Street_Ind, font=Fonte12, width=29, textvariable=Var_Street_Ind, state=DISABLED)
EntStreet_Ind.place(x=60, y=40)
EntStreet_Ind.bind("<KeyRelease>", Capitalise)
# ---------------------------------------------------------------------------------------------------------------------
# Label e Entry do Números da Indústria
Var_Numb_Ind = StringVar()
LblNumb_Ind = Label(Fr_Street_Ind, text="N°", font=Fonte11B, bg=Cinza40, fg=Branco)
LblNumb_Ind.place(x=330, y=40)
EntNumb_Ind = Entry(Fr_Street_Ind, font=Fonte12, width=6, textvariable=Var_Numb_Ind, validate='key')
EntNumb_Ind.config(validatecommand=Just_Numb)
EntNumb_Ind.place(x=360, y=40)
EntNumb_Ind.bind("<FocusOut>", Cursor_2)
EntNumb_Ind.bind("<Return>", Save_Industry)
# ---------------------------------------------------------------------------------------------------------------------
# Label e Entry do Bairro da Indústria
Var_Bairro_Ind = StringVar()
LblBairro_Ind = Label(Fr_Street_Ind, text="BAIRRO:", font=Fonte11B, bg=Cinza40, fg=Branco)
LblBairro_Ind.place(x=5, y=75)
EntBairro_Ind = Entry(Fr_Street_Ind, font=Fonte12, width=20, textvariable=Var_Bairro_Ind, state=DISABLED)
EntBairro_Ind.place(x=80, y=75)
EntBairro_Ind.bind("<KeyRelease>", Capitalise2)
EntBairro_Ind.bind("<FocusOut>", Cursor_2)
# ---------------------------------------------------------------------------------------------------------------------
# Label e Entry do Cidade da Indústria
Var_City_Ind = StringVar()
Lbl_City_Ind = Label(Fr_Street_Ind, text="CIDADE:", font=Fonte11B, bg=Cinza40, fg=Branco)
Lbl_City_Ind.place(x=5, y=110)
Ent_City_Ind = Entry(Fr_Street_Ind, font=Fonte12, width=25, textvariable=Var_City_Ind, state=DISABLED)
Ent_City_Ind.place(x=80, y=110)
# ---------------------------------------------------------------------------------------------------------------------
# Label e Entry do Estado da Indústria
Var_Uf_Ind = StringVar()
LblUf_Ind = Label(Fr_Street_Ind, text="UF:", font=Fonte11B, bg=Cinza40, fg=Branco)
LblUf_Ind.place(x=320, y=110)
EntUf_Ind = Entry(Fr_Street_Ind, font=Fonte12, width=3, state=DISABLED, justify=CENTER, textvariable=Var_Uf_Ind)
EntUf_Ind.place(x=350, y=110)
EntUf_Ind.bind("<FocusOut>", Cursor_3)
# ---------------------------------------------------------------------------------------------------------------------
# Botão CEP Validar
Btncep = Button(Fr_Street_Ind, bg=Cinza_Novo, takefocus=False, activebackground=Cinza_Novo, command=ConsultarCep)
Btncep.place(x=155, y=5)
Btncep.config(image=Img_Validate)
Btncep.imagem = Img_Validate
Btncep.bind("<Enter>", Passando_Cliente)
Btncep.bind("<Leave>", Saindo_Cliente)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# BOTÕES.....
btSalvar_Clientes = Button(Windows_Cad_Ind, bg=Cinza_Novo, image=Img_Save_Ind, activebackground=Cinza_Novo,
                           command=Save_Industry, borderwidth=0)
btSalvar_Clientes.image = Img_Save_Ind
btSalvar_Clientes.place(x=384, y=12)
btSalvar_Clientes.bind("<Enter>", Botao_Salvar_emcima)
btSalvar_Clientes.bind("<Leave>", Botap_Salvar_saindo)
# ------------------------ FIM ----------------------------------------------------------------------------------------
Windows_Cad_Ind.mainloop()
