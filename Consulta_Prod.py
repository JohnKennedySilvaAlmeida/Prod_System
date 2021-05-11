# ------------ TELA DE CONSULTA PRODUTOS POR GRUPO --------------------------------------------------------------------
from tkinter.ttk import *
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


# Estrutura para a Janela de Excluir Produtos ---------------------------------------------------------------------
Windows_Cons_Prod = Toplevel()
Windows_Cons_Prod.geometry("595x480+450+150")
Windows_Cons_Prod.title("SISTEMA DE GERENCIAMENTO")
Windows_Cons_Prod.minsize(595, 480)
Windows_Cons_Prod.maxsize(595, 480)
Windows_Cons_Prod.resizable(False, False)
Windows_Cons_Prod["bg"] = Cinza_Novo
Windows_Cons_Prod.iconbitmap("Imagens/Logo_SFundo.ico")

# Caminho com Variavel com a foto
Img_Listar_Consulta = PhotoImage(file="Imagens//Listar.png")
Windows_Cons_Prod.option_add('*TCombobox*Listbox.font', Fonte10)
Windows_Cons_Prod.option_add('*TCombobox*Listbox.selectBackground', Cinza_Novo)
Windows_Cons_Prod.option_add('*TCombobox*Listbox.background', Branco)
Windows_Cons_Prod.option_add('*TCombobox*Listbox.selectForeground', Branco)

FrGroup = LabelFrame(Windows_Cons_Prod, bg=Cinza40, fg=Branco, font=Fonte11B)
FrGroup.place(x=5, y=60, width=350, height=40)
FrResultados = LabelFrame(Windows_Cons_Prod, bg=Cinza40, fg=Branco, font=Fonte11B)
FrResultados.place(x=5, y=105, width=585, height=360)

# -----------------------------------------------------------------------------------------------------------------
Lbl_Titulo8 = Label(Windows_Cons_Prod, text="----" * 10, bg=Cinza_Novo, fg=Amarelo_Novo, font=Fonte12I)
Lbl_Titulo8.place(x=0, y=10)
# -----------------------------------------------------------------------------------------------------------------

# Label e Combobox de Cidades
Var_Name_Group = StringVar()
Lbl_Name_Group = Label(FrGroup, text="GRUPO:", font=Fonte11B, bg=Cinza40, fg=Branco)
Lbl_Name_Group.place(x=5, y=6)
CMB_NAme_GRoup = Combobox(FrGroup, font=Fonte11, width=25, textvariable=Var_Name_Group)
CMB_NAme_GRoup.set("SELECIONE")
#CMB_City['values'] = CMBCidade()
CMB_NAme_GRoup["state"] = 'readonly'
CMB_NAme_GRoup.place(x=100, y=7)
#CMB_NAme_GRoup.bind("<<ComboboxSelected>>", Selct_City)

# -----------------------------------------------------------------------------------------------------------------
# Criando o treeview
# Criando o treeview
Relacao = Treeview(FrResultados, height=16, columns=('1', '2', '3'))
Relacao.heading('#0', text='COD', anchor=CENTER)
Relacao.heading('1', text='NOME', anchor=CENTER)
Relacao.heading('2', text='PREÇO', anchor=CENTER)
Relacao.heading('3', text='DATA CADASTRO', anchor=CENTER)

Relacao.column('3', width=120, minwidth=120, anchor=W, stretch=NO)
Relacao.column('2', width=120, minwidth=120, anchor=W, stretch=NO)
Relacao.column('1', width=240, minwidth=240, anchor=CENTER, stretch=NO)
Relacao.column('#0', width=70, minwidth=70, anchor=CENTER, stretch=NO)
Relacao.place(x=5, y=5)
Relacao.tag_configure('Metas', background=Branco, font=Fonte12, foreground=Preto)
barra = Scrollbar(FrResultados, orient='vertical', command=Relacao.yview)
barra.place(x=558, y=5, height=346)
Relacao.configure(yscrollcommand=barra.set)
# ---------------------------------------------------------------------------------------------------------------------
# BOTÕES.....
# Botão Salvar Cidade
btSalvar_Consulta = Button(Windows_Cons_Prod, bg=Cinza_Novo, image=Img_Listar_Consulta, borderwidth=0)
btSalvar_Consulta.config(activebackground=Cinza_Novo)
btSalvar_Consulta.image = Img_Listar_Consulta
btSalvar_Consulta.place(x=520, y=12)
# ------------------------ FIM ----------------------------------------------------------------------------------------
Windows_Cons_Prod.mainloop()
