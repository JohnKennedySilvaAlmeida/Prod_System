# ---------------- CENTRADA DE NOTA -----------------------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter.ttk import Combobox
from tkinter.ttk import Treeview
import pymysql
import datetime


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
Qtde_unt = (Windows_Entry_Note.register(QTDE), '%d', '%i', '%i', '%s', '%S', '%v', '%V', '%W')
# ---------------------------------------------------------------------------------------------------------------------
# Label para criar aviso do botão Salvar
LblPed_Salvar = Label(Windows_Entry_Note, text="Salvar", bg=Cinza_Novo, fg=Cinza_Novo, font=Fonte10)
LblPed_Salvar.place(x=754, y=54)
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
#Dt_Atual.bind("<Tab>", Cursor_Num_Ped)
# ---------------------------------------------------------------------------------------------------------------------
# ----- LABELFRAME PEDIDOS --------------------------------------------------------------------------------------------
# Label e Entry do NÚMERO DO PEDIDO
Var_Cod_Nota = StringVar()
LblCod_Nota = Label(Fr_Cabecalho, text="NUM° NOTA:", font=Fonte11B, bg=Cinza40, fg=Branco)
LblCod_Nota.place(x=5, y=8)
EntCod_Nota = Entry(Fr_Cabecalho, font=Fonte12, width=14, textvariable=Var_Cod_Nota, justify=CENTER)
EntCod_Nota.place(x=105, y=8)
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ----- LABELFRAME INFORMAÇÕES DO CLIENTE -----------------------------------------------------------------------------
Lbl_Cod_Fornec = Label(FrInf_Cli, text="CÓDIGO:", bg=Cinza_Novo, fg=Branco, font=Fonte11B)
Lbl_Cod_Fornec.place(x=5, y=20)
Lbl_Cod_Fornec = Entry(FrInf_Cli, font=Fonte11, width=12, disabledbackground=Cinza90, disabledforeground=Branco)
Lbl_Cod_Fornec.place(x=90, y=20)
# ---------------------------------------------------------------------------------------------------------------------
Lbl_Nome_Fornec = Label(FrInf_Cli, text="RAZÃO SOCIAL:", bg=Cinza_Novo, fg=Branco, font=Fonte11B)
Lbl_Nome_Fornec.place(x=5, y=60)
Ent_Nome_Fornec = Entry(FrInf_Cli, font=Fonte11, width=38, state=DISABLED, disabledbackground=Cinza90,
                     disabledforeground=Branco)
Ent_Nome_Fornec.place(x=130, y=60)
# ---------------------------------------------------------------------------------------------------------------------
Lbl_Rua_Fornec = Label(FrInf_Cli, text="RUA:", bg=Cinza_Novo, fg=Branco, font=Fonte11B)
Lbl_Rua_Fornec.place(x=5, y=90)
Ent_Rua_Fornec = Entry(FrInf_Cli, font=Fonte11, width=35, state=DISABLED, disabledbackground=Cinza90,
                     disabledforeground=Branco)
Ent_Rua_Fornec.place(x=50, y=90)
# ---------------------------------------------------------------------------------------------------------------------
Lbl_Num_Fornec = Label(FrInf_Cli, text="N°", bg=Cinza_Novo, fg=Branco, font=Fonte11B)
Lbl_Num_Fornec.place(x=345, y=90)
Ent_Num_Fornec = Entry(FrInf_Cli, font=Fonte11, width=7, state=DISABLED, disabledbackground=Cinza90,
                     disabledforeground=Branco)
Ent_Num_Fornec.place(x=378, y=90)
# ---------------------------------------------------------------------------------------------------------------------
Lbl_Bairro_Fornec = Label(FrInf_Cli, text="BAIRRO:", bg=Cinza_Novo, fg=Branco, font=Fonte11B)
Lbl_Bairro_Fornec.place(x=5, y=120)
Ent_Bairro_Fornec = Entry(FrInf_Cli, font=Fonte11, width=15, state=DISABLED, disabledbackground=Cinza90,
                     disabledforeground=Branco)
Ent_Bairro_Fornec.place(x=75, y=120)
# ---------------------------------------------------------------------------------------------------------------------
Lbl_Cidade_Fornec = Label(FrInf_Cli, text="CIDADE:", bg=Cinza_Novo, fg=Branco, font=Fonte11B)
Lbl_Cidade_Fornec.place(x=210, y=120)
Ent_Cidade_Fornec = Entry(FrInf_Cli, font=Fonte11, width=19, state=DISABLED, disabledbackground=Cinza90,
                     disabledforeground=Branco)
Ent_Cidade_Fornec.place(x=281, y=120)
# ---------------------------------------------------------------------------------------------------------------------
Lbl_User = Label(FrInf_Cli, text="COLABORADOR:", bg=Cinza_Novo, fg=Branco, font=Fonte11B)
Lbl_User.place(x=5, y=150)
Ent_User = Entry(FrInf_Cli, font=Fonte11, width=7, state=DISABLED, disabledbackground=Cinza90,
                     disabledforeground=Branco)
Ent_User.place(x=140, y=150)
# ---------------------------------------------------------------------------------------------------------------------
# ----- DADOS DA ULTIMA COMPRA ----------------------------------------------------------------------------------------
# Label de DATA da Última Compra
Lbl_Data_Ult_Compra = Label(FrInf_Ult_Compra, font=Fonte11B, text="DATA:", bg=Cinza_Novo, fg=Branco)
Lbl_Data_Ult_Compra.place(x=5, y=3)
# 1° Entry
Dia_ULt_Compra = Entry(FrInf_Ult_Compra, font=Fonte12, width=2, state=DISABLED, disabledbackground=Cinza90,
                     disabledforeground=Branco)
Dia_ULt_Compra.place(x=70, y=3)
# Label da 1° Barra da data
Barra_1 = Label(FrInf_Ult_Compra, text="/", bg=Cinza_Novo, fg=Branco, font=Fonte12B)
Barra_1.place(x=96, y=3)
# Entry do Mes da ultima compra
Mes_ULt_Compra = Entry(FrInf_Ult_Compra, font=Fonte12, width=2, state=DISABLED, disabledbackground=Cinza90,
                     disabledforeground=Branco)
Mes_ULt_Compra.place(x=110, y=3)
# Label da 2° Barra da data
Barra_2 = Label(FrInf_Ult_Compra, text="/", bg=Cinza_Novo, fg=Branco, font=Fonte12B)
Barra_2.place(x=136, y=3)
# Entry do Ano da ultima compra
Ano_ULt_Compra = Entry(FrInf_Ult_Compra, font=Fonte12, width=4, state=DISABLED, disabledbackground=Cinza90,
                     disabledforeground=Branco)
Ano_ULt_Compra.place(x=150, y=3)
# ---------------------------------------------------------------------------------------------------------------------
# ----- LABELFRAME INSERIR PRODUTOS -----------------------------------------------------------------------------------
# Label e Entry Codigo do Produto
Var_Cod_Prod = StringVar()
Var_Cod_Prod.set("")
LblCod_Prod = Label(FrInsert_Ped, text="COD BARRAS:", bg=Cinza_Novo, fg=Branco, font=Fonte12B)
LblCod_Prod.place(x=5, y=10)
EntCod_Prod = Entry(FrInsert_Ped, font=Fonte12, textvariable=Var_Cod_Prod, width=20, justify=CENTER,
                    disabledbackground=Cinza90)
EntCod_Prod.place(x=130, y=10)
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
EntQtde = Entry(FrInsert_Ped, font=Fonte12, textvariable=Var_Qtde, width=4, justify=CENTER, validate='key',
                state=DISABLED, disabledbackground=Cinza90)
EntQtde.place(x=85, y=40)
# ---------------------------------------------------------------------------------------------------------------------
# Label e Entry Preço do Item
Var_Preco_Unt = StringVar()
Var_Preco_Unt.set("")
LblPreco_Unt = Label(FrInsert_Ped, text="PREÇO:", bg=Cinza_Novo, fg=Branco, font=Fonte12B)
LblPreco_Unt.place(x=5, y=70)
EntPreco_Unt = Entry(FrInsert_Ped, font=Fonte12, textvariable=Var_Preco_Unt, width=10, justify=CENTER,
                     state=DISABLED, disabledbackground=Cinza90, disabledforeground=Branco)
EntPreco_Unt.place(x=85, y=70)
# ---------------------------------------------------------------------------------------------------------------------
# Label e Entry Desconto do Item
Var_Desc = StringVar()
Var_Desc.set("")
LblDesc_Iten = Label(FrInsert_Ped, text="DESC:", bg=Cinza_Novo, fg=Branco, font=Fonte12B)
LblDesc_Iten.place(x=5, y=100)
EntDesc = Entry(FrInsert_Ped, font=Fonte12, textvariable=Var_Desc, width=10, justify=CENTER, state=DISABLED,
                 disabledbackground=Cinza90, disabledforeground=Branco)
EntDesc.place(x=85, y=100)
# ---------------------------------------------------------------------------------------------------------------------
# Label e Entry Total do Item
Var_Total = StringVar()
Var_Total.set("")
LblTotal = Label(FrInsert_Ped, text="TOTAL:", bg=Cinza_Novo, fg=Branco, font=Fonte12B)
LblTotal.place(x=5, y=130)
EntTotal = Entry(FrInsert_Ped, font=Fonte12, textvariable=Var_Total, width=10, justify=CENTER, state=DISABLED,
                    disabledbackground=Cinza90, disabledforeground=Branco)
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
tree_Fornecedor.column('#2', stretch=YES, width=360, minwidth=360, anchor=W)
tree_Fornecedor.column('#1', stretch=YES, width=100, minwidth=100, anchor=CENTER)
tree_Fornecedor.column('#0', stretch=YES, width=60, minwidth=60, anchor=CENTER)
tree_Fornecedor.place(x=0, y=5)
tree_Fornecedor.tag_configure('MonoMetas', background=Branco, font=Fonte12, foreground=Preto)
tree_Fornecedor.tag_configure('oddrow', background=Cinza60, font=Fonte12, foreground=Preto)
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
# ------------------------ FIM ----------------------------------------------------------------------------------------
Windows_Entry_Note.mainloop()
