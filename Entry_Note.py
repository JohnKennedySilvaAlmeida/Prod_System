# ---------------- CENTRADA DE NOTA -----------------------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
import pymysql
from tkcalendar import DateEntry



def QTDE(action, index, value_if_allowed,
         prior_value, text, validation_type, trigger_type, widget_name):
    if text in '0123456789':
        try:
            float(value_if_allowed)
            return True
        except ValueError:
            return False
    else:
        return False

def Valor(action, index, value_if_allowed,
         prior_value, text, validation_type, trigger_type, widget_name):
    if text in '0123456789.':
        try:
            float(value_if_allowed)
            return True
        except ValueError:
            return False
    else:
        return False

def CimaPed_Salvar(event=None):
    LblNota_Salvar.config(fg=Branco)

def SCimaPed_Salvar(event=None):
    LblNota_Salvar.config(fg=Cinza_Novo)

def Descricao_Prod(event=None):

    try:
        Conexao = pymysql.connect(host="localhost", user="root", passwd="P@ssw0rd", db="BD_SYSTEM")
        Cursor_Descricao = Conexao.cursor()
        Cursor_Descricao.execute("SELECT NAME_PROD FROM PROD WHERE BAR_CODE = '%s';" % Var_Bar_Prod.get())
        global Texto_Prod
        Texto_Prod = ""
        global cod_barras
        cod_barras = Var_Bar_Prod.get()

        for id in Cursor_Descricao.fetchall():
            Texto_Prod = id[0]

        if Texto_Prod == "":
            messagebox.showinfo("ERROR", "CÓDIGO DE PRODUTO INEXISTENTE")
            Var_Bar_Prod.set("")
            EntCod_Prod.focus()
        else:
            if len(Texto_Prod) <= 35:
                Img_Descricao.config(text=Texto_Prod)
            else:
                Img_Descricao.config(text=f"{Texto_Prod[:31]}...")
            EntQtde.config(state=NORMAL)
            EntQtde.focus()
            Conexao.close()

    except:
        messagebox.showinfo("ERROR", "NÃO HÁ CONEXÃO COM O BANCO DE DADOS")

def Qtde_Prod(event=None):
    EntPreco_Unt.config(state=NORMAL)
    Var_Preco_Unt.set("")
    EntPreco_Unt.focus()

def Tot_por_Prod(event=None):

    lista_prod_note = []

    try:
        Preco_Unt = (float(Var_Preco_Unt.get()))
    except:
        messagebox.showinfo("ERRO", "VALOR INVALIDO")
        EntPreco_Unt.focus()
    try:
        Quantidade_Prod = float(Var_Qtde.get())
    except:
        messagebox.showinfo("ERRO", "VALOR INVALIDO")
        EntQtde.focus()

    global cod_barras
    total_prod = Preco_Unt * Quantidade_Prod
    Var_Total.set("{:.2f}".format(float(total_prod)))
    Codigo_bar = Var_Bar_Prod.get()
    if Codigo_bar not in lista_prod_note:
        Confirma = messagebox.askyesno("CONFIRMAÇÃO", "INSERIR ITEM", parent=Windows_Entry_Note)
        if Confirma == True:
            # Conexao = pymysql.connect(host="localhost", user="root", passwd="P@ssw0rd", db="BD_SYSTEM")
            # Cursor_Nota = Conexao.cursor()
            # Nota = "INSERT INTO ITENS_NOTE(COD_NOTE_ITEM, BAR_CODE_PROD, QTDE, VALUE_PROD, VALUE_TOT)" \
            #       "VALUES(%s, %s, %s, %s, %s);"
            # Parametro_nota = (Var_Cod_Nota.get(), Var_Bar_Prod.get(), Quantidade_Prod, Preco_Unt, total_prod)
            # Cursor_Nota.execute(Nota, Parametro_nota)
            # Conexao.commit()
            # Conexao.close()
            lista_prod_note.append(Codigo_bar)
            tree_Fornecedor.insert("", 'end', text=Var_Qtde.get(), tag='oddrow',
                                   values=(
                                   Var_Bar_Prod.get(), Texto_Prod, "R$ {:.2f}".format(float(Var_Preco_Unt.get())),
                                   "R$ {:.2f}".format(float(Var_Total.get()))))
            EntQtde.config(state=DISABLED)
            EntPreco_Unt.config(state=DISABLED)
            Var_Bar_Prod.set("")
            Var_Qtde.set("")
            Var_Total.set("")
            Var_Preco_Unt.set("")
            EntCod_Prod.focus()
            Img_Descricao.config(text="")

        else:
            EntQtde.config(state=DISABLED)
            EntPreco_Unt.config(state=DISABLED)
            Var_Bar_Prod.set("")
            Var_Qtde.set("")
            Var_Total.set("")
            Var_Preco_Unt.set("")
    else:
        print("ok")
        messagebox.showinfo("EXISTENTE", "PRODUTO JA INSERIDO")

def Focus_ID_Forn(event=None):
    EntCod_Nota.config(state=DISABLED)
    Ent_Cod_Fornec.focus()

def Ident_Fornecedor(event=None):

    Conexao = pymysql.connect(host="localhost", user="root", passwd="P@ssw0rd", db="BD_SYSTEM")
    Cursor_Id_Forn = Conexao.cursor()
    Cursor_Id_Forn.execute("SELECT NAME_IND, STREET_IND, NUMBER_IND, BAIRRO_IND, CITY_IND, LAST_PAY_IND FROM INDUSTRY "
                           "WHERE ID_IND = '%s';" % Var_Cod_Forn.get())
    for indus in Cursor_Id_Forn.fetchall():
        Var_Forn_Name.set(indus[0])
        Var_Forn_Rua.set(indus[1])
        Var_Forn_Num.set(indus[2])
        Var_Forn_Bairro.set(indus[3])
        Var_Forn_City.set(indus[4])
        Fornecedor_Ult_Compra = str(indus[5])

    Dia_ULt_Compra.config(state=NORMAL)
    Mes_ULt_Compra.config(state=NORMAL)
    Ano_ULt_Compra.config(state=NORMAL)
    Dia_ULt_Compra.insert(0, str(Fornecedor_Ult_Compra[8:]))
    Mes_ULt_Compra.insert(0, str(Fornecedor_Ult_Compra[5:7]))
    Ano_ULt_Compra.insert(0, str(Fornecedor_Ult_Compra[:4]))
    Dia_ULt_Compra.config(state=DISABLED)
    Mes_ULt_Compra.config(state=DISABLED)
    Ano_ULt_Compra.config(state=DISABLED)
    Ent_User.config(state=NORMAL)
    Ent_User.focus()
    Ent_Cod_Fornec.config(state=DISABLED)


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
Fonte14B = ("Arial", 14, "bold")
Fonte15B = ("Arial", 15, "bold")
Fonte_teste = ("Palatino Linotype", 12, "bold")


Windows_Entry_Note = Toplevel()
Windows_Entry_Note.geometry("870x610+400+150")
Windows_Entry_Note.title("SOFTWARE DE GERENCIAMENTO")
Windows_Entry_Note.minsize(870, 610)
Windows_Entry_Note.maxsize(870, 610)
Windows_Entry_Note.resizable(False, False)
Windows_Entry_Note["bg"] = Cinza_Novo
Windows_Entry_Note.iconbitmap("Imagens/Logo_SFundo.ico")


# Caminho com Variavel com a foto
Foto_Salvar_Pedidos = PhotoImage(file="Imagens//Save.png")
Foto_Sair_Pedidos = PhotoImage(file="Imagens//Cancel.png")
Img_Bar_Code = PhotoImage(file="Imagens//Bar_Cod.png")
QTDE_Number = (Windows_Entry_Note.register(QTDE), '%d', '%i', '%i', '%s', '%S', '%v', '%V', '%W')
Valor_float = (Windows_Entry_Note.register(Valor), '%d', '%i', '%i', '%s', '%S', '%v', '%V', '%W')
# ---------------------------------------------------------------------------------------------------------------------
# Label para criar aviso do botão Salvar
LblNota_Salvar = Label(Windows_Entry_Note, text="Salvar", bg=Cinza_Novo, fg=Cinza_Novo, font=Fonte10)
LblNota_Salvar.place(x=808, y=54)
# ---------------------------------------------------------------------------------------------------------------------
# Imagem do Codigo de Barras
Img_Cod_Bar = Label(Windows_Entry_Note, image=Img_Bar_Code, border=0, bg=Cinza_Novo)
Img_Cod_Bar.image = Img_Bar_Code
Img_Cod_Bar.place(x=260, y=48, width=140, height=80)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Lbl_Titulo11 = Label(Windows_Entry_Note, text="----"*16, bg=Cinza_Novo, fg=Amarelo_Novo, font=Fonte12I)
Lbl_Titulo11.place(x=0, y=10)
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# ---------------------------------------------------------------------------------------------------------------------
# LABELFRAMES -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# N° 1 - Frame da Data
FrData = LabelFrame(Windows_Entry_Note, bg=Cinza40)
FrData.place(x=5, y=48, width=250, height=36)
# ---------------------------------------------------------------------------------------------------------------------
# N° 2 - Frame Cabeçalho da Nota
Fr_Cabecalho = LabelFrame(Windows_Entry_Note, bg=Cinza40, fg=Branco, font=Fonte11B)
Fr_Cabecalho.place(x=5, y=85, width=250, height=40)
# ---------------------------------------------------------------------------------------------------------------------
# N° 3 - Frame Informação do Fornecedor
FrInf_Cli = LabelFrame(Windows_Entry_Note, bg=Cinza_Novo, fg=Amarelo_Novo, font=Fonte8B, text="FORNECEDOR")
FrInf_Cli.place(x=410, y=100, width=445, height=195)
# ---------------------------------------------------------------------------------------------------------------------
# N° 4 - Frame Informação da Última Compra
FrInf_Ult_Compra = LabelFrame(FrInf_Cli, bg=Cinza_Novo, fg=Amarelo_Novo, font=Fonte8, text="ÚLTIMA COMPRA")
FrInf_Ult_Compra.place(x=235, y=0, width=202, height=46)
# ---------------------------------------------------------------------------------------------------------------------
# N° 5 - Frame Dados Inserir a Nota
FrInsert_Ped = LabelFrame(Windows_Entry_Note, bg=Cinza_Novo, fg=Branco, font=Fonte11B)
FrInsert_Ped.place(x=5, y=130, width=400, height=165)
# ---------------------------------------------------------------------------------------------------------------------
# N° 6 - Frame Lista de Produtos da Nota
FrLista_Prod = LabelFrame(Windows_Entry_Note, bg=Cinza_Novo, fg=Branco, font=Fonte11B)
FrLista_Prod.place(x=5, y=300, width=850, height=241)
# ---------------------------------------------------------------------------------------------------------------------
# N° 7 - Frame Total da Nota
FrTotal = LabelFrame(Windows_Entry_Note, bg=Cinza40)
FrTotal.place(x=401, y=550, width=454, height=40)
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# ---------------------------------------------------------------------------------------------------------------------
# Data Entry para chamar o Calendário com a data atual
LblData = Label(FrData, text="DATA:", bg=Cinza40, fg=Branco, font=Fonte11B, justify=LEFT)
LblData.place(x=3, y=2)
Dt_Atual = DateEntry(FrData, date_pattern='dd/MM/yyyy', width=17, bg=Cinza_Novo, fg=Branco, font=Fonte12,
                      headersbackground=Branco, borderwidth=2, selectbackground=Cinza_Novo, headersforeground=Cinza60)
Dt_Atual.place(x=60, y=3)
# ---------------------------------------------------------------------------------------------------------------------
# ----- LABELFRAME PEDIDOS --------------------------------------------------------------------------------------------
# Label e Entry do NÚMERO DO PEDIDO
Var_Cod_Nota = StringVar()
LblCod_Nota = Label(Fr_Cabecalho, text="NUM° NOTA:", font=Fonte11B, bg=Cinza40, fg=Branco)
LblCod_Nota.place(x=5, y=8)
EntCod_Nota = Entry(Fr_Cabecalho, font=Fonte12, width=14, textvariable=Var_Cod_Nota, justify=CENTER)
EntCod_Nota.config(validatecommand=QTDE_Number, validate='key')
EntCod_Nota.place(x=105, y=8)
EntCod_Nota.focus()
EntCod_Nota.bind("<Tab>", Focus_ID_Forn)
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ----- LABELFRAME INFORMAÇÕES DO CLIENTE -----------------------------------------------------------------------------
Var_Cod_Forn = StringVar()
Lbl_Cod_Fornec = Label(FrInf_Cli, text="CÓDIGO:", bg=Cinza_Novo, fg=Branco, font=Fonte11B)
Lbl_Cod_Fornec.place(x=5, y=20)
Ent_Cod_Fornec = Entry(FrInf_Cli, font=Fonte11, width=12, disabledbackground=Cinza60, validate='key', justify=CENTER)
Ent_Cod_Fornec.config(disabledforeground=Preto, validatecommand=QTDE_Number, textvariable=Var_Cod_Forn)
Ent_Cod_Fornec.place(x=90, y=20)
Ent_Cod_Fornec.bind("<Return>", Ident_Fornecedor)
# ---------------------------------------------------------------------------------------------------------------------
Var_Forn_Name = StringVar()
Lbl_Nome_Fornec = Label(FrInf_Cli, text="RAZÃO SOCIAL:", bg=Cinza_Novo, fg=Branco, font=Fonte11B)
Lbl_Nome_Fornec.place(x=5, y=60)
Ent_Nome_Fornec = Entry(FrInf_Cli, font=Fonte11, width=38, state=DISABLED, disabledbackground=Cinza60)
Ent_Nome_Fornec.config(disabledforeground=Preto, textvariable=Var_Forn_Name)
Ent_Nome_Fornec.place(x=130, y=60)
# ---------------------------------------------------------------------------------------------------------------------
Var_Forn_Rua = StringVar()
Lbl_Rua_Fornec = Label(FrInf_Cli, text="RUA:", bg=Cinza_Novo, fg=Branco, font=Fonte11B)
Lbl_Rua_Fornec.place(x=5, y=90)
Ent_Rua_Fornec = Entry(FrInf_Cli, font=Fonte11, width=35, state=DISABLED, disabledbackground=Cinza60)
Ent_Rua_Fornec.config(disabledforeground=Preto, textvariable=Var_Forn_Rua)
Ent_Rua_Fornec.place(x=50, y=90)
# ---------------------------------------------------------------------------------------------------------------------
Var_Forn_Num = StringVar()
Lbl_Num_Fornec = Label(FrInf_Cli, text="N°", bg=Cinza_Novo, fg=Branco, font=Fonte11B)
Lbl_Num_Fornec.place(x=345, y=90)
Ent_Num_Fornec = Entry(FrInf_Cli, font=Fonte11, width=7, state=DISABLED, disabledbackground=Cinza60)
Ent_Num_Fornec.config(disabledforeground=Preto, textvariable=Var_Forn_Num)
Ent_Num_Fornec.place(x=378, y=90)
# ---------------------------------------------------------------------------------------------------------------------
Var_Forn_Bairro = StringVar()
Lbl_Bairro_Fornec = Label(FrInf_Cli, text="BAIRRO:", bg=Cinza_Novo, fg=Branco, font=Fonte11B)
Lbl_Bairro_Fornec.place(x=5, y=120)
Ent_Bairro_Fornec = Entry(FrInf_Cli, font=Fonte11, width=15, state=DISABLED, disabledbackground=Cinza60)
Ent_Bairro_Fornec.config(disabledforeground=Preto, textvariable=Var_Forn_Bairro)
Ent_Bairro_Fornec.place(x=75, y=120)
# ---------------------------------------------------------------------------------------------------------------------
Var_Forn_City = StringVar()
Lbl_Cidade_Fornec = Label(FrInf_Cli, text="CIDADE:", bg=Cinza_Novo, fg=Branco, font=Fonte11B)
Lbl_Cidade_Fornec.place(x=210, y=120)
Ent_Cidade_Fornec = Entry(FrInf_Cli, font=Fonte11, width=19, state=DISABLED, disabledbackground=Cinza60)
Ent_Cidade_Fornec.config(disabledforeground=Preto, textvariable=Var_Forn_City)
Ent_Cidade_Fornec.place(x=281, y=120)
# ---------------------------------------------------------------------------------------------------------------------
Var_Id_Colaborador = StringVar()
Lbl_User = Label(FrInf_Cli, text="COLABORADOR:", bg=Cinza_Novo, fg=Branco, font=Fonte11B)
Lbl_User.place(x=5, y=150)
Ent_User = Entry(FrInf_Cli, font=Fonte11, width=7, state=DISABLED, disabledbackground=Cinza60, justify=CENTER)
Ent_User.config(validatecommand=QTDE_Number, disabledforeground=Branco, validate='key', textvariable=Var_Id_Colaborador)
Ent_User.place(x=140, y=150)
# ---------------------------------------------------------------------------------------------------------------------
# ----- DADOS DA ULTIMA COMPRA ----------------------------------------------------------------------------------------
# Label de DATA da Última Compra
Lbl_Data_Ult_Compra = Label(FrInf_Ult_Compra, font=Fonte11B, text="DATA:", bg=Cinza_Novo, fg=Branco)
Lbl_Data_Ult_Compra.place(x=5, y=3)
# 1° Entry
Dia_ULt_Compra = Entry(FrInf_Ult_Compra, font=Fonte12, width=2, state=DISABLED, disabledbackground=Cinza60,
                     disabledforeground=Preto)
Dia_ULt_Compra.place(x=70, y=3)
# Label da 1° Barra da data
Barra_1 = Label(FrInf_Ult_Compra, text="/", bg=Cinza_Novo, fg=Branco, font=Fonte12B)
Barra_1.place(x=96, y=3)
# Entry do Mes da ultima compra
Mes_ULt_Compra = Entry(FrInf_Ult_Compra, font=Fonte12, width=2, state=DISABLED, disabledbackground=Cinza60,
                     disabledforeground=Preto)
Mes_ULt_Compra.place(x=110, y=3)
# Label da 2° Barra da data
Barra_2 = Label(FrInf_Ult_Compra, text="/", bg=Cinza_Novo, fg=Branco, font=Fonte12B)
Barra_2.place(x=136, y=3)
# Entry do Ano da ultima compra
Ano_ULt_Compra = Entry(FrInf_Ult_Compra, font=Fonte12, width=4, state=DISABLED, disabledbackground=Cinza60,
                     disabledforeground=Preto)
Ano_ULt_Compra.place(x=150, y=3)
# ---------------------------------------------------------------------------------------------------------------------
# ----- LABELFRAME INSERIR PRODUTOS -----------------------------------------------------------------------------------
# Label e Entry Codigo do Produto
Var_Bar_Prod = StringVar()
LblCod_Prod = Label(FrInsert_Ped, text="COD BARRAS:", bg=Cinza_Novo, fg=Branco, font=Fonte12B)
LblCod_Prod.place(x=5, y=10)
EntCod_Prod = Entry(FrInsert_Ped, font=Fonte12, textvariable=Var_Bar_Prod, width=20, justify=CENTER, validate='key')
EntCod_Prod.config(disabledbackground=Cinza90, validatecommand=QTDE_Number)
EntCod_Prod.place(x=130, y=10)
EntCod_Prod.bind("<Return>", Descricao_Prod)
# ---------------------------------------------------------------------------------------------------------------------
# Imagem da Descrição do Produto
Img_Descricao = Label(FrInsert_Ped, bg=Cinza_Novo, fg=Branco, font=Fonte11B, width=27)
Img_Descricao.place(x=140, y=40)
# ---------------------------------------------------------------------------------------------------------------------
# Label e Entry Qusntidade do item
Var_Qtde = StringVar()
Var_Qtde.set("")
LblQtde = Label(FrInsert_Ped, text="QTDE:", bg=Cinza_Novo, fg=Branco, font=Fonte12B)
LblQtde.place(x=5, y=40)
EntQtde = Entry(FrInsert_Ped, font=Fonte12, textvariable=Var_Qtde, width=4, justify=CENTER, validate='key')
EntQtde.config(state=DISABLED, disabledbackground=Cinza90, validatecommand=QTDE_Number)
EntQtde.place(x=85, y=40)
EntQtde.bind("<Return>", Qtde_Prod)
# ---------------------------------------------------------------------------------------------------------------------
# Label e Entry Preço do Item
Var_Preco_Unt = StringVar()
Var_Preco_Unt.set("0.00")
LblPreco_Unt = Label(FrInsert_Ped, text="PREÇO:", bg=Cinza_Novo, fg=Branco, font=Fonte12B)
LblPreco_Unt.place(x=5, y=70)
EntPreco_Unt = Entry(FrInsert_Ped, font=Fonte12, textvariable=Var_Preco_Unt, width=10, justify=CENTER, state=DISABLED)
EntPreco_Unt.config(disabledbackground=Cinza90, disabledforeground=Preto, validate="key", validatecommand=Valor_float)
EntPreco_Unt.place(x=85, y=70)
EntPreco_Unt.bind("<Return>", Tot_por_Prod)
# ---------------------------------------------------------------------------------------------------------------------
# Label e Entry Desconto do Item
Var_Desc = StringVar()
Var_Desc.set("")
LblDesc_Iten = Label(FrInsert_Ped, text="DESC:", bg=Cinza_Novo, fg=Branco, font=Fonte12B)
LblDesc_Iten.place(x=5, y=100)
EntDesc = Entry(FrInsert_Ped, font=Fonte12, textvariable=Var_Desc, width=10, justify=CENTER, state=DISABLED)
EntDesc.config(disabledbackground=Cinza90, disabledforeground=Preto, validatecommand=QTDE_Number)
EntDesc.place(x=85, y=100)
# ---------------------------------------------------------------------------------------------------------------------
# Label e Entry Total do Item
Var_Total = StringVar()
Var_Total.set("")
LblTotal = Label(FrInsert_Ped, text="TOTAL:", bg=Cinza_Novo, fg=Branco, font=Fonte12B)
LblTotal.place(x=5, y=130)
EntTotal = Entry(FrInsert_Ped, font=Fonte12, textvariable=Var_Total, width=10, justify=CENTER, state=DISABLED,
                    disabledbackground=Cinza90, disabledforeground=Preto)
EntTotal.place(x=85, y=130)
# ---------------------------------------------------------------------------------------------------------------------
# Botão Inserir
btInserir = Button(FrInsert_Ped, bg=Cinza40, text="INSERIR", font=Fonte12I, fg=Branco, activebackground=Cinza_Novo)
btInserir.config(activeforeground=Branco)
btInserir.place(x=250, y=77, width=110, height=33)
# Botão Excluir
btExcluir = Button(FrInsert_Ped, bg=Cinza40, text="EXCLUIR", font=Fonte12I, fg=Branco, activebackground=Cinza_Novo)
btExcluir.config(activeforeground=Branco)
btExcluir.place(x=250, y=114, width=110, height=33)
# ---------------------------------------------------------------------------------------------------------------------
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=
# Criando o treeview
tree_Fornecedor = Treeview(FrLista_Prod, height=10)
tree_Fornecedor['columns'] = ('QTDE', 'CODIGO', 'DESCRIÇÃO', 'PREÇO UNT', 'VALOR TOTAL')
tree_Fornecedor.heading('#0', text='QTDE', anchor=CENTER)
tree_Fornecedor.heading('#1', text='CODIGO', anchor=CENTER)
tree_Fornecedor.heading('#2', text='DESCRIÇÃO', anchor=CENTER)
tree_Fornecedor.heading('#3', text='PREÇO UNT', anchor=CENTER)
tree_Fornecedor.heading('#4', text='VALOR TOTAL', anchor=CENTER)

tree_Fornecedor.column('#4', stretch=YES, width=170, minwidth=170, anchor=CENTER)
tree_Fornecedor.column('#3', stretch=YES, width=140, minwidth=140, anchor=CENTER)
tree_Fornecedor.column('#2', stretch=YES, width=300, minwidth=300, anchor=W)
tree_Fornecedor.column('#1', stretch=YES, width=160, minwidth=160, anchor=CENTER)
tree_Fornecedor.column('#0', stretch=YES, width=60, minwidth=60, anchor=CENTER)
tree_Fornecedor.place(x=0, y=5)
#tree_Fornecedor.tag_configure('MonoMetas', background=Branco, font=Fonte12, foreground=Preto)
tree_Fornecedor.tag_configure('oddrow', background=Cinza40, font=Fonte12, foreground=Branco)
barra3 = Scrollbar(tree_Fornecedor, orient='vertical', command=tree_Fornecedor.yview)
barra3.place(x=828, y=1, height=225)
tree_Fornecedor.configure(yscrollcommand=barra3.set)
# ---------------------------------------------------------------------------------------------------------------------
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=
# Labels do Total da Nota
Lb_Desc = Label(FrTotal, bg=Cinza40, text="DESC:", fg=Branco, font=Fonte12B)
Lb_Desc.place(x=44, y=8, height=20)
LbTotal_Desc = Label(FrTotal, bg=Cinza40, text="R$ 0.00", fg=Branco, font=Fonte14B)
LbTotal_Desc.place(x=110, y=8, height=20)

LbTotal_Items = Label(FrTotal, bg=Cinza40, text="TOTAL:", fg=Branco, font=Fonte12B)
LbTotal_Items.place(x=230, y=8, height=20)
LblTotal_Itens = Label(FrTotal, bg=Cinza40, text="R$ 0.00", fg=Branco, font=Fonte15B)
LblTotal_Itens.place(x=300, y=8, height=20)
# ---------------------------------------------------------------------------------------------------------------------
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=
# BOTÕES.....
# Botão Salvar
btSalvar_Pedidos = Button(Windows_Entry_Note, bg=Cinza_Novo, image=Foto_Salvar_Pedidos, activebackground=Cinza_Novo)
btSalvar_Pedidos.config(borderwidth=0)
btSalvar_Pedidos.image = Foto_Salvar_Pedidos
btSalvar_Pedidos.place(x=804, y=9)
btSalvar_Pedidos.bind("<Enter>", CimaPed_Salvar)
btSalvar_Pedidos.bind("<Leave>", SCimaPed_Salvar)
# ------------------------ FIM ----------------------------------------------------------------------------------------
Windows_Entry_Note.mainloop()
