# ------------ TELA DE CONSULTA PRODUTOS POR GRUPO 
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import pymysql

Lista_Grupos = []

def CMB_Group_BD():
    try:
        Conexao = pymysql.connect(host="localhost", user="root", passwd="P@ssw0rd", db="BD_SYSTEM")
        cursor_Group = Conexao.cursor()
        cursor_Group.execute('SELECT GROUP_PROD FROM PROD ORDER BY ID_PROD')

        for row in cursor_Group.fetchall():
            Lista_Grupos.append(row[0])
        Conexao.close()
        return Lista_Grupos
    except:
        messagebox.showinfo("ERROR", "NÃO HÁ CONEXÃO COM O BANCO DE DADOS", parent=Windows_Cons_Prod)

def Listar_Produtos():
    Relacao.delete(*Relacao.get_children())
    Conexao = pymysql.connect(host="localhost", user="root", passwd="P@ssw0rd", db="BD_SYSTEM")
    Cursor_Listar = Conexao.cursor()
    Cursor_Listar.execute("SELECT ID_PROD, NAME_PROD, VALUE_PROD, CREATED_AT FROM PROD WHERE GROUP_PROD = '%s';"
                          % Var_Name_Group.get())
    global Contando
    Contando = 0
    for row in Cursor_Listar.fetchall():
        Data_Criado = str(row[3])
        Dt = f"{Data_Criado[8:10]}/{Data_Criado[5:7]}/{Data_Criado[:4]}"
        if Contando % 2 == 0:
            Relacao.insert("", 'end', text=row[0], tag='oddrow', values=(row[1], f"R$ {row[2]}", Dt))
        else:
            Relacao.insert("", 'end', text=row[0], tag='evenrow', values=(row[1], f"R$ {row[2]}", Dt))
        Contando += 1

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

FrGroup = LabelFrame(Windows_Cons_Prod, bg=Cinza40, fg=Amarelo_Novo, font=Fonte11, text="CONSULTA PRODUTOS")
FrGroup.place(x=5, y=48, width=350, height=50)
FrResultados = LabelFrame(Windows_Cons_Prod, bg=Cinza40, fg=Branco, font=Fonte11B)
FrResultados.place(x=5, y=105, width=585, height=360)

# -----------------------------------------------------------------------------------------------------------------
Lbl_Titulo8 = Label(Windows_Cons_Prod, text="----" * 10, bg=Cinza_Novo, fg=Amarelo_Novo, font=Fonte12I)
Lbl_Titulo8.place(x=0, y=10)
# -----------------------------------------------------------------------------------------------------------------

# Label e Combobox de Cidades
Var_Name_Group = StringVar()
Lbl_Name_Group = Label(FrGroup, text="GRUPO:", font=Fonte11B, bg=Cinza40, fg=Branco)
Lbl_Name_Group.place(x=5, y=3)
CMB_Name_GRoup = Combobox(FrGroup, font=Fonte11, width=25, textvariable=Var_Name_Group)
CMB_Name_GRoup.set("SELECIONE")
CMB_Name_GRoup['values'] = CMB_Group_BD()
CMB_Name_GRoup["state"] = 'readonly'
CMB_Name_GRoup.place(x=100, y=3)
#CMB_NAme_GRoup.bind("<<ComboboxSelected>>", Selct_City)

# -----------------------------------------------------------------------------------------------------------------
# Criando o treeview
# Criando o treeview
Relacao = Treeview(FrResultados, height=16, columns=('1', '2', '3'))
Relacao.heading('#0', text='COD', anchor=CENTER)
Relacao.heading('1', text='NOME', anchor=CENTER)
Relacao.heading('2', text='PREÇO', anchor=CENTER)
Relacao.heading('3', text='DATA CADASTRO', anchor=CENTER)

Relacao.column('3', width=120, minwidth=120, anchor=CENTER, stretch=NO)
Relacao.column('2', width=120, minwidth=120, anchor=W, stretch=NO)
Relacao.column('1', width=240, minwidth=240, anchor=W, stretch=NO)
Relacao.column('#0', width=70, minwidth=70, anchor=CENTER, stretch=NO)
Relacao.place(x=5, y=5)
Relacao.tag_configure('oddrow', background=Cinza_Novo, font=Fonte12, foreground=Branco)
Relacao.tag_configure('evenrow', background=Cinza40, font=Fonte12, foreground=Branco)
barra = Scrollbar(FrResultados, orient='vertical', command=Relacao.yview)
barra.place(x=558, y=5, height=346)
Relacao.configure(yscrollcommand=barra.set)
# ---------------------------------------------------------------------------------------------------------------------
# BOTÕES.....
# Botão Salvar Cidade
btSalvar_Consulta = Button(Windows_Cons_Prod, bg=Cinza_Novo, image=Img_Listar_Consulta, borderwidth=0)
btSalvar_Consulta.config(activebackground=Cinza_Novo, command=Listar_Produtos)
btSalvar_Consulta.image = Img_Listar_Consulta
btSalvar_Consulta.place(x=520, y=12)
# ------------------------ FIM ----------------------------------------------------------------------------------------
Windows_Cons_Prod.mainloop()
