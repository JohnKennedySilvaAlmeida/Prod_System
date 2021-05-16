# -------------- Tela Pra Cadastro de Produtos ------------------------------------------------------------------------

from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import pymysql

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

Lista_Group = []

def CMBGroup():
    try:
        Conexao = pymysql.connect(host="localhost", user="root", passwd="P@ssw0rd", db="BD_SYSTEM")
        cursor_Group = Conexao.cursor()
        cursor_Group.execute('SELECT NAME_GROUP FROM GROUP_PROD ORDER BY ID_GROUP')

        for row in cursor_Group.fetchall():
            Lista_Group.append(row[0])

        return Lista_Group
    except:
        messagebox.showinfo("ERROR", "NÃO HÁ CONEXÃO COM O BANCO DE DADOS", parent=Windows_Cad_Prod)

def validate(action, index, value_if_allowed,
             prior_value, text, validation_type, trigger_type, widget_name):
    if text in '0123456789.':
        try:
            float(value_if_allowed)
            return True
        except ValueError:
            return False
    else:
        return False

def Title_Prod(event=None):
    Var_Nome_Prod.set(EntNome_Prod.get().title())

def Value_Prod(event=None):
    VarPreco_Prod.set("")
    EntPreco_Prod.focus()

def Max_Dig_Code(event=None):
    if len(Var_Cod_Barras.get()) == 13:
        EntNome_Prod.focus()

def Next_Prod():
    Conexao = pymysql.connect(host="localhost", user="root", passwd="P@ssw0rd", db="BD_SYSTEM")
    Cursor_Prod = Conexao.cursor()
    Cursor_Prod.execute("SELECT MAX(ID_PROD) FROM PROD")
    global Maximo_Prod
    Maximo_Prod = ""
    for e in Cursor_Prod.fetchall():
        if e[0] == None:
            Maximo_Prod = "1"
        else:
            Maximo_Prod = int(e[0]) + 1
    Conexao.close()

def Salvar_Produto(event=None):

    Conexao = pymysql.connect(host="localhost", user="root", passwd="P@ssw0rd", db="BD_SYSTEM")
    Lista_ID_Prod = []

    # Verificando se há campos em Branco
    if Var_Cod_Barras.get() == "" or Var_Nome_Prod.get() == "" or VarGroup_Prod.get() == "SELECIONE" or\
            VarPreco_Prod.get() == "":
        messagebox.showinfo("ERROR", "HÁ DADOS FALTANDO", parent=Windows_Cad_Prod)

    else:
        Cursor_Exist_Prod = Conexao.cursor()
        Cursor_Exist_Prod.execute("SELECT BAR_CODE FROM PROD")
        for ind in Cursor_Exist_Prod.fetchall():
            Lista_ID_Prod.append(int(ind[0]))

        Codigo = int(Var_Cod_Barras.get())

        if Codigo not in Lista_ID_Prod:
            # Verificando qual Banco de Dados será gravado
            Confirmacao = messagebox.askyesno("CONFIRMAÇÃO", "DESEJA CADASTRAR O PRODUTO\n"
                                                             f"{Var_Nome_Prod.get()}?", parent=Windows_Cad_Prod)
            if Confirmacao == True:

                Cursor_Prod = Conexao.cursor()

                Prod = ("INSERT INTO PROD(NAME_PROD, BAR_CODE, GROUP_PROD, VALUE_PROD)VALUES(%s, %s, %s, %s);")

                Paramentros_Prod = (Var_Nome_Prod.get(),
                                    Var_Cod_Barras.get(),
                                    VarGroup_Prod.get(),
                                    float(VarPreco_Prod.get()))

                Cursor_Prod.execute(Prod, Paramentros_Prod)
                Conexao.commit()
                Conexao.close()
                Prox_Prod = messagebox.askyesno("PRÓXIMO", "DESEJA CADASTRAR OUTRO PRODUTO",
                                                parent=Windows_Cad_Prod)

                if Prox_Prod == True:
                    Next_Prod()
                    Var_Cod_Prod.set(Maximo_Prod)
                    Var_Nome_Prod.set("")
                    Var_Cod_Barras.set("")
                    VarGroup_Prod.set("SELECIONE")
                    VarPreco_Prod.set("0.00")
                    EntCod_Barras.focus()
                else:
                    Windows_Cad_Prod.destroy()

            else:
                Var_Nome_Prod.set("")
                Var_Cod_Barras.set("")
                VarGroup_Prod.set("SELECIONE")
                VarPreco_Prod.set("0.00")
                EntNome_Prod.focus()

        else:
            messagebox.showinfo("DUPLICADO", "PRODUTO JÁ EXISTENTE!", parent=Windows_Cad_Prod)
            Var_Nome_Prod.set("")
            Var_Cod_Barras.set("")
            VarGroup_Prod.set("SELECIONE")
            VarPreco_Prod.set("0.00")
            EntCod_Barras.focus()
    #except:
     #   messagebox.showinfo("ERROR", "NÃO HÁ CONEXÃO COM O BANCO DE DADOS")

Windows_Cad_Prod = Toplevel()
Windows_Cad_Prod.geometry("450x270+540+280")
Windows_Cad_Prod.title("SISTEMA DE GERENCIAMENTO")
Windows_Cad_Prod.minsize(450, 270)
Windows_Cad_Prod.maxsize(450, 270)
Windows_Cad_Prod.resizable(False, False)
Windows_Cad_Prod["bg"] = Cinza_Novo
Windows_Cad_Prod.iconbitmap("Imagens/Logo_SFundo.ico")

# Caminho com Variavel com a foto
Foto_Salvar_Prod = PhotoImage(file="Imagens//Save.png")
vcmd_Prod = (Windows_Cad_Prod.register(validate), '%d', '%i', '%i', '%s', '%S', '%v', '%V', '%W')

# -----------------------------------------------------------------------------------------------------------------
Lbl_Titulo3 = Label(Windows_Cad_Prod, text="----" * 6, bg=Cinza_Novo, fg=Amarelo_Novo, font=Fonte12I)
Lbl_Titulo3.place(x=0, y=10)
# -----------------------------------------------------------------------------------------------------------------
FrProdutos = LabelFrame(Windows_Cad_Prod, text="CADASTRO DE PRODUTOS", bg=Cinza40, fg=Amarelo_Novo, font=Fonte11B)
FrProdutos.place(x=5, y=80, width=440, height=180)

# -----------------------------------------------------------------------------------------------------------------
# Label e Entry do CODIGO
Next_Prod()
Var_Cod_Prod = StringVar()
Var_Cod_Prod.set(Maximo_Prod)
LblCod_Prod = Label(FrProdutos, text="CODIGO:", font=Fonte11B, bg=Cinza40, fg=Branco)
LblCod_Prod.place(x=5, y=5)
EntCod_Prod = Entry(FrProdutos, font=Fonte12, width=8, textvariable=Var_Cod_Prod, justify=CENTER, state=DISABLED)
EntCod_Prod.place(x=83, y=5)
# -----------------------------------------------------------------------------------------------------------------

# Label e Entry do CODIGO de BARRAS
Var_Cod_Barras = StringVar()
Var_Cod_Barras.set("")
LblCod_Barras = Label(FrProdutos, text="COD BARRAS:", font=Fonte11B, bg=Cinza40, fg=Branco)
LblCod_Barras.place(x=170, y=5)
EntCod_Barras = Entry(FrProdutos, font=Fonte12, textvariable=Var_Cod_Barras, validate='key', justify=CENTER,
                    validatecommand=vcmd_Prod, width=13)
EntCod_Barras.place(x=290, y=5)
EntCod_Barras.bind("<KeyRelease>", Max_Dig_Code)
EntCod_Barras.focus()
# -----------------------------------------------------------------------------------------------------------------

# Label e Entry do NOME
Var_Nome_Prod = StringVar()
Var_Nome_Prod.set("")
LblNome_Prod = Label(FrProdutos, text="NOME:", font=Fonte11B, bg=Cinza40, fg=Branco)
LblNome_Prod.place(x=5, y=45)
EntNome_Prod = Entry(FrProdutos, font=Fonte12, width=37, textvariable=Var_Nome_Prod)
EntNome_Prod.place(x=83, y=45)
EntNome_Prod.bind("<KeyRelease>", Title_Prod)
# -----------------------------------------------------------------------------------------------------------------

# Label e Entry de GROUP
VarGroup_Prod = StringVar()
VarGroup_Prod.set("")
LblGroup_Prod = Label(FrProdutos, text="GRUPO:", font=Fonte11B, bg=Cinza40, fg=Branco)
LblGroup_Prod.place(x=5, y=85)
CMBGroup_Prod = Combobox(FrProdutos, font=Fonte11, width=20, textvariable=VarGroup_Prod)
CMBGroup_Prod.set("SELECIONE")
CMBGroup_Prod['values'] = CMBGroup()
CMBGroup_Prod["state"] = 'readonly'
CMBGroup_Prod.bind("<Return>", Value_Prod)
CMBGroup_Prod.bind("<<ComboboxSelected>>", Value_Prod)
CMBGroup_Prod.place(x=83, y=85)
FrProdutos.option_add('*TCombobox*Listbox.font', Fonte11)
FrProdutos.option_add('*TCombobox*Listbox.selectBackground', Cinza_Novo)
FrProdutos.option_add('*TCombobox*Listbox.background', Branco)
FrProdutos.option_add('*TCombobox*Listbox.selectForeground', Branco)
# -----------------------------------------------------------------------------------------------------------------

# Label e Entry do PREÇO
VarPreco_Prod = StringVar()
VarPreco_Prod.set("0.00")
LblPreco_Prod = Label(FrProdutos, text="PREÇO:", font=Fonte11B, bg=Cinza40, fg=Branco)
LblPreco_Prod.place(x=5, y=125)
EntPreco_Prod = Entry(FrProdutos, font=Fonte12, width=8, textvariable=VarPreco_Prod, justify=RIGHT, validate='key',
                      validatecommand=vcmd_Prod)
EntPreco_Prod.place(x=110, y=125)
EntPreco_Prod.bind("<Return>", Salvar_Produto)

LblPorc = Label(FrProdutos, text="R$", font=Fonte11B, bg=Cinza40, fg=Branco)
LblPorc.place(x=80, y=125)
# -----------------------------------------------------------------------------------------------------------------

# BOTÕES.....
# Botão Salvar
btSalvar_Prod = Button(Windows_Cad_Prod, bg=Cinza_Novo, image=Foto_Salvar_Prod, activebackground=Cinza_Novo)
btSalvar_Prod.config(borderwidth=0, command=Salvar_Produto)
btSalvar_Prod.image = Foto_Salvar_Prod
btSalvar_Prod.place(x=380, y=12)
# ------------------------ FIM ----------------------------------------------------------------------------------------
Windows_Cad_Prod.mainloop()

