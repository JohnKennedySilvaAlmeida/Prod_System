from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import pymysql
from tkcalendar import DateEntry
import datetime
from tkinter.filedialog import askopenfile
import re
#from reportlab.pdfgen.canvas import Canvas
#from reportlab.lib.pagesizes import A4, landscape
import webbrowser
#from PIL import Image
#from PIL import ImageTk

# Variaveis de Cor
Branco = "White"
Preto = "Black"
Vermelho = "Red4"
Verde = "#276955"
Azul = "Blue"
Azul_2 = "light gray"
Azul_Receita = "DodgerBlue4"
Azul_Receita_Claro = "DodgerBlue3"
Gold = "Gold"
Cinza20 = "Gray20"
Cinza60 = "Gray60"
Cinza40 = "Gray40"
Cinza90 = "Gray90"
text_font = ('Arial', '12')
Cinza_Romano = "#5f626a"
Cinza_Novo = "#262f36"
Amarelo_Novo = "#f99c11"
Verde_Novo = "#6ba610"


# Variavéis de Fonte
Fonte8 = "Arial, 8"
Fonte8B = ("Arial", 8, "bold")
Fonte10 = "Arial, 10"
Fonte10B = ("Arial", 10, "bold")
Fonte11 = "Arial, 11"
Fonte11B = ("Arial", 11, "bold")
Fonte12 = "Arial, 12"
Fonte12B = ("Arial", 12, "bold")
Fonte13 = "Arial, 13"
Fonte13B = ("Arial", 13, "bold")
Fonte14 = "Arial, 14"
Fonte14B = ("Arial", 14, "bold")
Fonte18 = "Arial, 18"
Fonte18B = ("Arial", 18, "bold")
Fonte12I = ("Courier", 12, "italic")

Windows = Tk()
Windows.geometry("1500x750+10+10")
Windows.title("TK8 - SOFTWARE DE GERENCIAMENTO")
Windows.minsize(1500, 750)
Windows.maxsize(1500, 750)
Windows.resizable(False, False)
Windows["bg"] = Branco


def Row_Up_Button_1(event=None):
    Row_Arquivo.config(bg=Branco)

def Row_Down_Button_1(event=None):
    Row_Arquivo.config(bg=Amarelo_Novo)

def Row_Up_Button_2(event=None):
    Row_Consultas.config(bg=Branco)

def Row_Down_Button_2(event=None):
    Row_Consultas.config(bg=Amarelo_Novo)

def Row_Up_Button_3(event=None):
    Row_Relatorios.config(bg=Branco)

def Row_Down_Button_3(event=None):
    Row_Relatorios.config(bg=Amarelo_Novo)

def Row_Up_Button_4(event=None):
    Row_Agenda.config(bg=Branco)

def Row_Down_Button_4(event=None):
    Row_Agenda.config(bg=Amarelo_Novo)

def Row_Up_Button_5(event=None):
    Row_Suporte.config(bg=Branco)

def Row_Down_Button_5(event=None):
    Row_Suporte.config(bg=Amarelo_Novo)

# Função Para Desativar Botão Sair da Janela Principal
def Desativar_Max(event=None):
    pass
# ------------------------ FIM ----------------------------------------------------------------------------------------
# Função Criada para Destruir Janela Principal com o Botão "Sair" do Menu
def Sair_Tela_Inicial(event=None):
    Windows.destroy()
# ------------------------ FIM ----------------------------------------------------------------------------------------

# Função para CADASTRO DE GRUPO --------------------------------------------------------------------------------------
def Register_Group(event=None):

    def Title(event=None):
        Var_Nome_Group.set(EntNome_Group.get().upper())

    def Save_Group(event=None):


        Conexao = pymysql.connect(host="localhost", user="root", passwd="P@ssw0rd", db="BD_SYSTEM")
        Lista_ID = []

        # Verificando se há campos em Branco
        if EntNome_Group.get() == "":
            messagebox.showinfo("ERROR", "POR FAVOR PREENCHA O NOME DO GRUPO!", parent=Windows_Cad_Group)

        else:
            Cursor_Existente = Conexao.cursor()
            Cursor_Existente.execute("SELECT ID_GROUP FROM GROUP_PROD")
            for ind in Cursor_Existente.fetchall():
                Lista_ID.append(int(ind[0]))

            codigo = Var_Cod_Group.get()
            if codigo not in Lista_ID:

                # Verificando qual Banco de Dados será gravado
                Confirmacao = messagebox.askyesno("CONFIRMAÇÃO",
                                                  "DESEJA CADASTRAR O GRUPO\n"
                                                  f"{Var_Nome_Group.get()}?", parent=Windows_Cad_Group)
                if Confirmacao == True:

                    Cursor_Marca = Conexao.cursor()

                    Marca = ("INSERT INTO GROUP_PROD(NAME_GROUP)VALUES(%s);")

                    Paramentroe_Med = (Var_Nome_Group.get())

                    Cursor_Marca.execute(Marca, Paramentroe_Med)
                    Conexao.commit()
                    Conexao.close()
                    messagebox.showinfo("SUCESSO", f"O GRUPO {Var_Nome_Group.get()}\nFOI CADASTRADO COM SUCESSO!",
                                        parent=Windows_Cad_Group)
                    Windows_Cad_Group.destroy()


                else:
                    Var_Nome_Group.set("")
                    EntNome_Group.focus()

            else:
                messagebox.showinfo("DUPLICADO", "GRUPO JÁ EXISTENTE!", parent=Windows_Cad_Group)
                Var_Nome_Group.set("")
                EntNome_Group.focus()
        #except:
         #   messagebox.showinfo("ERROS", "NÃO HÁ CONEXÃO COM O BANCO DE DADOS", parent=Windows_Cad_Group)

    Windows_Cad_Group = Toplevel()
    Windows_Cad_Group.geometry("370x200+250+200")
    Windows_Cad_Group.title("SISTEMA DE GERENCIAMENTO")
    Windows_Cad_Group.minsize(370, 200)
    Windows_Cad_Group.maxsize(370, 200)
    Windows_Cad_Group.resizable(False, False)
    Windows_Cad_Group["bg"] = Cinza_Novo
    Windows_Cad_Group.iconbitmap("Imagens/Logo_SFundo.ico")

    # Caminho com Variavel com a foto
    Foto_Salvar_Group = PhotoImage(file="Imagens//Save.png")
    # -----------------------------------------------------------------------------------------------------------------
    Lbl_Titulo4 = Label(Windows_Cad_Group, text="----" * 6, bg=Cinza_Novo, fg=Amarelo_Novo, font=Fonte12I)
    Lbl_Titulo4.place(x=0, y=10)
    # -----------------------------------------------------------------------------------------------------------------

    Frame_Group = LabelFrame(Windows_Cad_Group, text="CADASTRO DE GRUPO", bg=Cinza40, fg=Amarelo_Novo, font=Fonte11B)
    Frame_Group.place(x=5, y=70, width=350, height=115)
    # -----------------------------------------------------------------------------------------------------------------
    # Label e Entry do CODIGO do GROUP
    Conexao_Id = pymysql.connect(host="localhost", user="root", passwd="P@ssw0rd", db="BD_SYSTEM")
    Cursor_id = Conexao_Id.cursor()
    Cursor_id.execute("SELECT MAX(ID_GROUP) FROM GROUP_PROD")
    Maximo = ""
    for i in Cursor_id.fetchall():
        if i[0] == None:
            Maximo = "1"
        else:
            Maximo = int(i[0]) + 1
    Var_Cod_Group = StringVar()
    Var_Cod_Group.set(str(Maximo))
    Conexao_Id.close()
    LblCod_Group = Label(Frame_Group, text="COD:", font=Fonte11B, bg=Cinza40, fg=Branco)
    LblCod_Group.place(x=5, y=5)
    EntCod_Group = Entry(Frame_Group, font=Fonte12, width=10, textvariable=Var_Cod_Group, justify=CENTER, state=DISABLED)
    EntCod_Group.place(x=80, y=5)
    # -----------------------------------------------------------------------------------------------------------------
    # Label e Entry do NOME do GROUP
    Var_Nome_Group = StringVar()
    LblNome_Group = Label(Frame_Group, text="NOME:", font=Fonte11B, bg=Cinza40, fg=Branco)
    LblNome_Group.place(x=5, y=45)
    EntNome_Group = Entry(Frame_Group, font=Fonte12, width=25, textvariable=Var_Nome_Group)
    EntNome_Group.place(x=80, y=45)
    EntNome_Group.bind("<KeyRelease>", Title)
    EntNome_Group.bind("<Return>", Save_Group)
    EntNome_Group.focus()
    # -----------------------------------------------------------------------------------------------------------------
    # BOTÕES.....
    btSalvar_Group = Button(Windows_Cad_Group, bg=Cinza_Novo, image=Foto_Salvar_Group, activebackground=Cinza_Novo,
                              borderwidth=0, command=Save_Group)
    btSalvar_Group.image = Foto_Salvar_Group
    btSalvar_Group.place(x=304, y=12)
# ------------------------ FIM ----------------------------------------------------------------------------------------

# Função para EXCLUIR GRUPO --------------------------------------------------------------------------------------
def Delete_Group(event=None):

    Lista_Grupo_2 = []

    def Caixa_Grupo():
        try:
            Conexao = pymysql.connect(host="localhost", user="root", passwd="P@ssw0rd", db="BD_SYSTEM")
            cursor_Group = Conexao.cursor()
            cursor_Group.execute('SELECT NAME_GROUP FROM GROUP_PROD ORDER BY ID_GROUP')

            for row in cursor_Group.fetchall():
                Lista_Grupo_2.append(row[0])

            Conexao.close()
            return Lista_Grupo_2
        except:
            messagebox.showinfo("ERROR", "NÃO HÁ CONEXÃO COM O BANCO DE DADOS", parent=Windows_Del_Group)

    def Group_Select(event=None):
        try:
            Conexao = pymysql.connect(host="localhost", user="root", passwd="P@ssw0rd", db="BD_SYSTEM")
            Cursor_Id_Group = Conexao.cursor()
            Cursor_Id_Group.execute("SELECT ID_GROUP FROM GROUP_PROD WHERE NAME_GROUP = '%s'" % Var_Name_Group.get())

            for id in Cursor_Id_Group.fetchall():
                Var_Id_Group.set(id[0])
            Conexao.close()

        except:
            messagebox.showinfo("ERROR", "NÃO HÁ CONEXÃO COM O BANCO DE DADOS", parent=Windows_Del_Group)

    def Del_Group(event=None):

        try:
            Conexao = pymysql.connect(host="localhost", user="root", passwd="P@ssw0rd", db="BD_SYSTEM")
            # Verificando se há campos em Branco
            if Var_Name_Group.get() == "SELECIONE":
                messagebox.showinfo("ERROR", "POR FAVOR SELECIONE UM GRUPO A SER DELETADO", parent=Windows_Del_Group)

            else:
                Cursor_Del = Conexao.cursor()
                # Verificando qual Banco de Dados será gravado
                Confirmacao = messagebox.askyesno("CONFIRMAÇÃO",
                                                  "DESEJA EXCLUIR O GRUPO\n"
                                                  f"{Var_Name_Group.get()}", parent=Windows_Del_Group)
                if Confirmacao == True:

                    Cursor_Del.execute("DELETE FROM GROUP_PROD WHERE ID_GROUP = '%s'" % Var_Id_Group.get())
                    Conexao.commit()
                    Conexao.close()
                    messagebox.showinfo("SUCESSO", f"O GRUPO {Var_Name_Group.get()}\nFOI DELETADO COM SUCESSO!",
                                        parent=Windows_Del_Group)
                    Windows_Del_Group.destroy()
                else:
                    pass
        except:
            messagebox.showinfo("ERROR", "ALGO DEU ERRADO, TENTE NOVAMENTE", parent=Windows_Del_Group)


    Windows_Del_Group = Toplevel()
    Windows_Del_Group.geometry("370x200+250+200")
    Windows_Del_Group.title("SISTEMA DE GERENCIAMENTO")
    Windows_Del_Group.minsize(370, 200)
    Windows_Del_Group.maxsize(370, 200)
    Windows_Del_Group.resizable(False, False)
    Windows_Del_Group["bg"] = Cinza_Novo
    Windows_Del_Group.iconbitmap("Imagens/Logo_SFundo.ico")

    # Caminho com Variavel com a foto
    Foto_Conf_Del_Group = PhotoImage(file="Imagens//Btn_Excluir.png")
    Windows_Del_Group.option_add('*TCombobox*Listbox.font', Fonte11)
    Windows_Del_Group.option_add('*TCombobox*Listbox.selectBackground', Verde)
    Windows_Del_Group.option_add('*TCombobox*Listbox.background', Branco)
    Windows_Del_Group.option_add('*TCombobox*Listbox.selectForeground', Branco)
    # -----------------------------------------------------------------------------------------------------------------
    Lbl_Titulo7 = Label(Windows_Del_Group, text="----" * 6, bg=Cinza_Novo, fg=Amarelo_Novo, font=Fonte12I)
    Lbl_Titulo7.place(x=0, y=10)
    # -----------------------------------------------------------------------------------------------------------------

    Frame_Group = LabelFrame(Windows_Del_Group, text="EXCLUIR GRUPO", bg=Cinza40, fg=Amarelo_Novo, font=Fonte11B)
    Frame_Group.place(x=5, y=70, width=350, height=115)
    # -----------------------------------------------------------------------------------------------------------------
    Var_Id_Group = StringVar()
    LblCod_Group = Label(Frame_Group, text="COD:", font=Fonte11B, bg=Cinza40, fg=Branco)
    LblCod_Group.place(x=5, y=5)
    EntCod_Group = Entry(Frame_Group, font=Fonte12, width=10, textvariable=Var_Id_Group, justify=CENTER, state=DISABLED)
    EntCod_Group.place(x=80, y=5)
    # -----------------------------------------------------------------------------------------------------------------
    # Label e Entry do NOME do GROUP
    Var_Name_Group = StringVar()
    LblNome_Group = Label(Frame_Group, text="NOME:", font=Fonte11B, bg=Cinza40, fg=Branco)
    LblNome_Group.place(x=5, y=45)
    CMB_Del_Group = Combobox(Frame_Group, width=25, textvariable=Var_Name_Group)
    CMB_Del_Group['values'] = Caixa_Grupo()
    CMB_Del_Group["state"] = 'readonly'
    CMB_Del_Group.bind("<Return>", Group_Select)
    CMB_Del_Group.bind("<<ComboboxSelected>>", Group_Select)
    CMB_Del_Group.place(x=80, y=45)
    # -----------------------------------------------------------------------------------------------------------------
    # BOTÕES.....
    btConf_Del_Group = Button(Windows_Del_Group, bg=Cinza_Novo, image=Foto_Conf_Del_Group, activebackground=Cinza_Novo,
                              borderwidth=0, command=Del_Group)
    btConf_Del_Group.image = Foto_Conf_Del_Group
    btConf_Del_Group.place(x=304, y=12)
# ------------------------ FIM ----------------------------------------------------------------------------------------

# ---- Função para CADASTRO DE PRODUTOS -------------------------------------------------------------------------------
def Register_Prod(event=None):

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
    FrProdutos.option_add('*TCombobox*Listbox.selectBackground', Verde)
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

# ---------------- EXCLUIR PRODUTOS -----------------------------------------------------------------------------------
def Excluir_Produtos(event=None):

    Lista_Group_Prod = []

    def CMBGroup_Prod():
        try:
            Conexao = pymysql.connect(host="localhost", user="root", passwd="P@ssw0rd", db="BD_SYSTEM")
            Cursor_Produto = Conexao.cursor()
            Cursor_Produto.execute('SELECT NAME_GROUP FROM GROUP_PROD ORDER BY NAME_GROUP')

            for row in Cursor_Produto.fetchall():
                Lista_Group_Prod.append(row[0])

            return Lista_Group_Prod
        except:
            messagebox.showinfo("ERROR", "NÃO HÁ CONEXÃO COM O BANCO DE DADOS", parent=Windows_Exc_Prod)

    def Deletar_Produto(event=None):

        try:
            Conexao = pymysql.connect(host="localhost", user="root", passwd="P@ssw0rd", db="BD_SYSTEM")
            Cursor_Exc_Prod = Conexao.cursor()
            confirma_Exc = messagebox.askyesno(
                "CONFIRMAÇÃO", f"VOCÊ DESEJA EXCLUIR O PRODUTO\n"
                               f"{Var_Exc_Nome_Prod.get(). upper()}",
                               parent=Windows_Exc_Prod)
            if confirma_Exc == True:

                Cursor_Exc_Prod.execute("DELETE FROM PROD WHERE ID_PROD = '%s'" % Var_Cod_Prod_Exc.get())
                Conexao.commit()
                Conexao.close()
                messagebox.showinfo("SUCESSO", "PRODUTO EXCLUÍDO COM SUCESSO", parent=Windows_Exc_Prod)
                Windows_Exc_Prod.destroy()

            else:
                Ent_Cod_Prod_Exc.config(state=NORMAL)
                Var_Cod_Prod_Exc.set("")
                Var_Cod_Barras_Exc.set("")
                Var_Exc_Prod_Group.set("SELECIONE")
                Var_Preco_Exc.set("0.00")
                Var_Exc_Nome_Prod.set("")
        except:
            messagebox.showinfo("ERROR", "NÃO HÁ CONEXÃO COM O BANCO DE DADOS", parent=Windows_Exc_Prod)

    def Select_Cod_Prod(event=None):

        try:
            if str(Var_Cod_Prod_Exc.get()) == "":
                messagebox.showinfo("ERROR", "DIGITE UM CÓDIGO DE PRODUTO", parent=Windows_Exc_Prod)
            else:
                Conexao = pymysql.connect(host="localhost", user="root", passwd="P@ssw0rd", db="BD_SYSTEM")
                Cursor_Cod_Prod = Conexao.cursor()
                Cursor_Cod_Prod.execute("SELECT NAME_PROD, BAR_CODE, GROUP_PROD, VALUE_PROD FROM PROD WHERE "
                                        "ID_PROD = '%s'"
                                        % str(Var_Cod_Prod_Exc.get()))
                Get_Cod_Prod = Cursor_Cod_Prod.fetchall()
                if Get_Cod_Prod == ():
                    messagebox.showinfo("INEXISTENTE", "CÓDIGO INEXISTENTE", parent=Windows_Exc_Prod)
                else:
                    for cod in Get_Cod_Prod:
                        Var_Exc_Nome_Prod.set(cod[0])
                        Var_Cod_Barras_Exc.set(cod[1])
                        Var_Exc_Prod_Group.set(cod[2])
                        Var_Preco_Exc.set(cod[3])
                    Ent_Cod_Prod_Exc.config(state=DISABLED)
        except:
            messagebox.showinfo("ERROR", "NÃO HÁ CONEXÃO COM O BANCO DE DADOS", parent=Windows_Exc_Prod)

    def UP_Button(event=None):
        if Ent_Cod_Prod_Exc['state'] == DISABLED:
            LSalvar.config(fg=Branco)
        else:
            pass

    def Down_Button(event=None):
        if Ent_Cod_Prod_Exc['state'] == DISABLED:
            LSalvar.config(fg=Cinza_Novo)
        else:
            pass

    # Estrutura para a Janela de Excluir Produtos ---------------------------------------------------------------------
    Windows_Exc_Prod = Toplevel()
    Windows_Exc_Prod.geometry("450x270+500+250")
    Windows_Exc_Prod.title("SISTEMA DE GERENCIAMENTO")
    Windows_Exc_Prod.minsize(450, 270)
    Windows_Exc_Prod.maxsize(450, 270)
    Windows_Exc_Prod.resizable(False, False)
    Windows_Exc_Prod["bg"] = Cinza_Novo
    Windows_Exc_Prod.iconbitmap("Imagens/Logo_SFundo.ico")
    # -----------------------------------------------------------------------------------------------------------------
    # Caminho com Variavel com a foto
    Foto_Ex_Save_Produtos = PhotoImage(file="Imagens//Btn_Excluir.png")

    # Label para criar aviso do botão Salvar
    LSalvar = Label(Windows_Exc_Prod, text="Excluir", bg=Cinza_Novo, fg=Cinza_Novo, font=Fonte10)
    LSalvar.place(x=382, y=58)
    # -----------------------------------------------------------------------------------------------------------------
    Lbl_Titulo5 = Label(Windows_Exc_Prod, text="----" * 6, bg=Cinza_Novo, fg=Amarelo_Novo, font=Fonte12I)
    Lbl_Titulo5.place(x=0, y=10)
    # -----------------------------------------------------------------------------------------------------------------

    # Frame Principal da Janela
    Frame_Exc_Produtos = LabelFrame(Windows_Exc_Prod, text="EXCLUIR PRODUTO")
    Frame_Exc_Produtos.config(font=Fonte11B, bg=Cinza_Romano, fg=Amarelo_Novo)
    Frame_Exc_Produtos.place(x=5, y=80, width=440, height=180)
    # -----------------------------------------------------------------------------------------------------------------
    # Label e Entry do CODIGO do PRODUTO
    Var_Cod_Prod_Exc = StringVar()
    Var_Cod_Prod_Exc.set("")
    Lbl_Cod_Prod_Exc = Label(Frame_Exc_Produtos, text="CODIGO:", font=Fonte11B, bg=Cinza_Romano, fg=Branco)
    Lbl_Cod_Prod_Exc.place(x=5, y=5)
    Ent_Cod_Prod_Exc = Entry(Frame_Exc_Produtos, textvariable=Var_Cod_Prod_Exc)
    Ent_Cod_Prod_Exc.config(font=Fonte12, width=8, justify=CENTER)
    Ent_Cod_Prod_Exc.place(x=83, y=5)
    Ent_Cod_Prod_Exc.focus()
    Ent_Cod_Prod_Exc.bind("<Return>", Select_Cod_Prod)
    # -----------------------------------------------------------------------------------------------------------------
    # Label e Entry do CODIGO de BARRAS DO PRODUTO
    Var_Cod_Barras_Exc = StringVar()
    Var_Cod_Barras_Exc.set("")
    Lbl_Cod_Barras_Exc = Label(Frame_Exc_Produtos, text="COD BARRAS:", font=Fonte11B, bg=Cinza_Romano, fg=Branco)
    Lbl_Cod_Barras_Exc.place(x=170, y=5)
    Ent_Cod_Barras_Exc = Entry(Frame_Exc_Produtos, textvariable=Var_Cod_Barras_Exc)
    Ent_Cod_Barras_Exc.config(width=13, justify=CENTER, font=Fonte12, state=DISABLED)
    Ent_Cod_Barras_Exc.place(x=290, y=5)
    # -----------------------------------------------------------------------------------------------------------------
    # Label e Entry do NOME DO PRODUTO
    Var_Exc_Nome_Prod = StringVar()
    Var_Exc_Nome_Prod.set("")
    Lbl_Nome_Prod = Label(Frame_Exc_Produtos, text="NOME:", font=Fonte11B, bg=Cinza_Romano, fg=Branco)
    Lbl_Nome_Prod.place(x=5, y=45)
    Ent_Nome_Prod = Entry(Frame_Exc_Produtos, font=Fonte12, width=37, textvariable=Var_Exc_Nome_Prod, state=DISABLED)
    Ent_Nome_Prod.place(x=83, y=45)
    # -----------------------------------------------------------------------------------------------------------------
    # Label e Entry de MARCA DO PRODUTO
    Var_Exc_Prod_Group = StringVar()
    Var_Exc_Prod_Group.set("")
    Lbl_Exc_Prod_Group = Label(Frame_Exc_Produtos, text="GRUPO:", font=Fonte11B, bg=Cinza_Romano, fg=Branco)
    Lbl_Exc_Prod_Group.place(x=5, y=85)
    CMB_Exc_Prod_Group = Combobox(Frame_Exc_Produtos, font=Fonte11, width=20, textvariable=Var_Exc_Prod_Group)
    CMB_Exc_Prod_Group.config(state=DISABLED)
    CMB_Exc_Prod_Group['values'] = CMBGroup_Prod()
    CMB_Exc_Prod_Group.place(x=83, y=85)
    Frame_Exc_Produtos.option_add('*TCombobox*Listbox.font', Fonte11)
    Frame_Exc_Produtos.option_add('*TCombobox*Listbox.selectBackground', Verde)
    Frame_Exc_Produtos.option_add('*TCombobox*Listbox.background', Branco)
    Frame_Exc_Produtos.option_add('*TCombobox*Listbox.selectForeground', Branco)
    # -----------------------------------------------------------------------------------------------------------------
    # Label e Entry PREÇO do Produto
    Var_Preco_Exc = StringVar()
    Var_Preco_Exc.set("")
    Lbl_Preco_Exc = Label(Frame_Exc_Produtos, text="PREÇO:", font=Fonte11B, bg=Cinza_Romano, fg=Branco)
    Lbl_Preco_Exc.place(x=5, y=125)
    Ent_Preco_Exc = Entry(Frame_Exc_Produtos, font=Fonte12, width=8, textvariable=Var_Preco_Exc, justify=RIGHT)
    Ent_Preco_Exc.config(state=DISABLED)
    Ent_Preco_Exc.place(x=110, y=125)
    # -----------------------------------------------------------------------------------------------------------------
    Lbl_Preco_Exc = Label(Frame_Exc_Produtos, text="R$", font=Fonte11B, bg=Cinza_Romano, fg=Branco)
    Lbl_Preco_Exc.place(x=80, y=125)
    # -----------------------------------------------------------------------------------------------------------------
    # BOTÕES.....
    # Botão Deletar Produtos
    BtnExcluir_Prod = Button(Windows_Exc_Prod, bg=Cinza_Novo, image=Foto_Ex_Save_Produtos, activebackground=Cinza_Novo)
    BtnExcluir_Prod.config(borderwidth=0, command=Deletar_Produto)
    BtnExcluir_Prod.image = Foto_Ex_Save_Produtos
    BtnExcluir_Prod.place(x=380, y=12)
    BtnExcluir_Prod.bind("<Enter>", UP_Button)
    BtnExcluir_Prod.bind("<Leave>", Down_Button)
    # -----------------------------------------------------------------------------------------------------------------
# ------------------------ FIM ----------------------------------------------------------------------------------------

# ------------------------ CADASTRO DE USUARIO ------------------------------------------------------------------------
def Register_Users(event=None):

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
    Windows_User.iconbitmap("Imagens/Logo_SFundo.ico")
    # -----------------------------------------------------------------------------------------------------------------

    # Caminho com Variavel com a foto
    Foto_User = PhotoImage(file="Imagens\\usuario.png")
    Foto_Salvar = PhotoImage(file="Imagens\\Save.png")
    Vcmd = (Windows_User.register(validate), '%d', '%i', '%i', '%s', '%S', '%v', '%V', '%W', '%P')
    # Recebendo Configurações de Combobox para mudança de Cores
    Windows_User.option_add('*TCombobox*Listbox.font', Fonte11)
    Windows_User.option_add('*TCombobox*Listbox.selectBackground', Verde)
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
    EntCpf_User = Entry(Tela_Pessoal, font=Fonte12, width=18, textvariable=Var_Cpf_User, justify=CENTER)
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

    ETelCel = Entry(Tela_Pessoal, font=Fonte11, validatecommand=Vcmd, validate='key', textvariable=Var_Tel)
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

# ---------------- CONSULTAS ESTOQUE ----------------------------------------------------------------------------------
def Consulta_Prod(event=None):


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
    Windows_Cons_Prod.option_add('*TCombobox*Listbox.selectBackground', Verde)
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
    # -----------------------------------------------------------------------------------------------------------------
    # BOTÕES.....
    # Botão Salvar Cidade
    btSalvar_Consulta = Button(Windows_Cons_Prod, bg=Cinza_Novo, image=Img_Listar_Consulta, borderwidth=0)
    btSalvar_Consulta.config(activebackground=Cinza_Novo)
    btSalvar_Consulta.image = Img_Listar_Consulta
    btSalvar_Consulta.place(x=520, y=12)
    # -----------------------------------------------------------------------------------------------------------------
# ------------------------ FIM ----------------------------------------------------------------------------------------
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# ---------------------------------------------------------------------------------------------------------------------
Lbl_Linha_1 = Label(Windows, bg=Cinza_Novo)
Lbl_Linha_1.place(x=0, y=0, width=1500, height=100)
# ---------------------------------------------------------------------------------------------------------------------
Lbl_Linha_2 = Label(Windows, bg=Branco)
Lbl_Linha_2.place(x=0, y=5, width=1500, height=4)
# ---------------------------------------------------------------------------------------------------------------------
Lbl_Linha_3 = Label(Windows, bg=Amarelo_Novo)
Lbl_Linha_3.place(x=0, y=91, width=1500, height=4)
# ---------------------------------------------------------------------------------------------------------------------
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Lbl_Titulo = Label(Windows, text="SISTEMA DE GERENCIAMENTO", bg=Cinza_Novo, fg=Amarelo_Novo, font=Fonte12I)
Lbl_Titulo.place(x=1220, y=20)
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Lbl_Titulo2 = Label(Windows, text="----"*27, bg=Cinza_Novo, fg=Amarelo_Novo, font=Fonte12I)
Lbl_Titulo2.place(x=0, y=20)
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Logo = PhotoImage(file="Imagens\\Work.png")
Lbl_Logo = Label(Windows, bg=Amarelo_Novo, image=Logo, borderwidth=9)
Lbl_Logo.image= Logo
Lbl_Logo.place(x=15, y=50)
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Fundo_Tela = PhotoImage(file="Imagens\\Fundo.png")
Lbl_Logo2 = Label(Windows, bg=Cinza_Novo, image=Fundo_Tela, borderwidth=9)
Lbl_Logo2.image = Fundo_Tela
Lbl_Logo2.place(x=0, y=100, width=1500, height=750)
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Row_Arquivo = Label(Windows, bg=Amarelo_Novo)
Row_Arquivo.place(x=65, y=91, width=74, height=4)
# ---------------------------------------------------------------------------------------------------------------------
Row_Consultas = Label(Windows, bg=Amarelo_Novo)
Row_Consultas.place(x=156, y=91, width=90, height=4)
# ---------------------------------------------------------------------------------------------------------------------
Row_Relatorios = Label(Windows, bg=Amarelo_Novo)
Row_Relatorios.place(x=274, y=91, width=103, height=4)
# ---------------------------------------------------------------------------------------------------------------------
Row_Agenda = Label(Windows, bg=Amarelo_Novo)
Row_Agenda.place(x=396, y=91, width=68, height=4)
# ---------------------------------------------------------------------------------------------------------------------
Row_Suporte = Label(Windows, bg=Amarelo_Novo)
Row_Suporte.place(x=486, y=91, width=80, height=4)
# ---------------------------------------------------------------------------------------------------------------------
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Criando MENU Arquivo
Arquivo = Menubutton(Windows, text="ARQUIVO", background=Cinza_Novo, foreground=Branco, font=Fonte12B,
                     activebackground=Cinza_Novo, activeforeground=Branco)
Arquivo.place(x=60, y=68, height=20)
Arquivo.bind("<Enter>", Row_Up_Button_1)  # Ação Para Aparecer a linha embaixo da Label
Arquivo.bind("<Leave>", Row_Down_Button_1)  # Ação Para Desaparecer a linha embaixo da Label
Arquivo.menu = Menu(Arquivo, background=Cinza60, fg=Branco, tearoff=0, activebackground=Cinza_Novo)
Arquivo["menu"] = Arquivo.menu  # Criando Atributo menu pro MENU Arquivo
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Consultas = Menubutton(Windows, text="CONSULTA", background=Cinza_Novo, foreground=Branco, font=Fonte12B,
                     activebackground=Cinza_Novo, activeforeground=Branco)
Consultas.place(x=153, y=68, height=20)
Consultas.bind("<Enter>", Row_Up_Button_2)  # Ação Para Aparecer a linha embaixo da Label
Consultas.bind("<Leave>", Row_Down_Button_2)  # Ação Para Desaparecer a linha embaixo da Label
Consultas.menu = Menu(Consultas, background=Cinza60, fg=Branco, tearoff=0, activebackground=Cinza_Novo)
Consultas["menu"] = Consultas.menu  # Criando Atributo menu pro MENU Consultas
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Relatorios = Menubutton(Windows, text="RELATÓRIOS", background=Cinza_Novo, foreground=Branco, font=Fonte12B,
                     activebackground=Cinza_Novo, activeforeground=Branco)
Relatorios.place(x=266, y=68, height=20)
Relatorios.bind("<Enter>", Row_Up_Button_3)  # Ação Para Aparecer a linha embaixo da Label
Relatorios.bind("<Leave>", Row_Down_Button_3)  # Ação Para Desaparecer a linha embaixo da Label
Relatorios.menu = Menu(Relatorios, background=Cinza60, fg=Branco, tearoff=0, activebackground=Cinza_Novo)
Relatorios["menu"] = Relatorios.menu  # Criando Atributo menu pro MENU Relatorios
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Agenda = Menubutton(Windows, text="AGENDA", background=Cinza_Novo, foreground=Branco, font=Fonte12B,
                     activebackground=Cinza_Novo, activeforeground=Branco)
Agenda.place(x=390, y=68, height=20)
Agenda.bind("<Enter>", Row_Up_Button_4)  # Ação Para Aparecer a linha embaixo da Label
Agenda.bind("<Leave>", Row_Down_Button_4)  # Ação Para Desaparecer a linha embaixo da Label
Agenda.menu = Menu(Agenda, background=Cinza60, fg=Branco, tearoff=0, activebackground=Cinza_Novo)
Agenda["menu"] = Agenda.menu  # Criando Atributo menu pro MENU Agenda
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Suporte = Menubutton(Windows, text="SUPORTE", background=Cinza_Novo, foreground=Branco, font=Fonte12B,
                     activebackground=Cinza_Novo, activeforeground=Branco)
Suporte.place(x=480, y=68, height=20)
Suporte.bind("<Enter>", Row_Up_Button_5)  # Ação Para Aparecer a linha embaixo da Label
Suporte.bind("<Leave>", Row_Down_Button_5)  # Ação Para Desaparecer a linha embaixo da Label
Suporte.menu = Menu(Suporte, background=Cinza_Novo, fg=Branco, tearoff=0, activebackground=Cinza40)
Suporte["menu"] = Suporte.menu  # Criando Atributo menu pro MENU Historicos
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Criando Clientes Menu com funções NOVO e EXCLUIR e EDITAR
ClientesMenu = Menu(Arquivo, background=Cinza_Novo, fg=Branco, tearoff=False, activebackground=Cinza40)
ClientesMenu.add_command(label='NOVO', font=Fonte12B)
ClientesMenu.add_command(label='EXCLUIR', font=Fonte12B)
ClientesMenu.add_command(label='EDITAR', font=Fonte12B)
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# Criando Usuario Menu com funções NOVO e EXCLUIR
UsuarioMenu = Menu(Arquivo, background=Cinza_Novo, fg=Branco, tearoff=False, activebackground=Cinza40)
UsuarioMenu.add_command(label='NOVO', font=Fonte12B, command=Register_Users)
UsuarioMenu.add_command(label='EXCLUIR', font=Fonte12B)
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# Criando Grupo Menu com funções NOVO e EXCLUIR
GrupoMenu = Menu(Arquivo, background=Cinza_Novo, fg=Branco, tearoff=False, activebackground=Cinza40)
GrupoMenu.add_command(label='NOVO', font=Fonte12B, command=Register_Group)
GrupoMenu.add_command(label='EXCLUIR', font=Fonte12B, command=Delete_Group)
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# Criando Produtos Menu com funções NOVO e EXCLUIR
ProdutosMenu = Menu(Arquivo, background=Cinza_Novo, fg=Branco, tearoff=False, activebackground=Cinza40)
ProdutosMenu.add_command(label='NOVO', font=Fonte12B, command=Register_Prod)
ProdutosMenu.add_command(label='EXCLUIR', font=Fonte12B, command=Excluir_Produtos)
# ---------------------------------------------------------------------------------------------------------------------
# Criando Consultas Menu com funções ESTOQUE, VENDAS, PRODUTO
Consultas.menu.add_command(label='ESTOQUE', font=Fonte12B, background=Cinza_Novo, activebackground=Cinza40)
Consultas.menu.add_command(label='VENDAS', font=Fonte12B, background=Cinza_Novo, activebackground=Cinza40)
Consultas.menu.add_command(label='PRODUTO', font=Fonte12B, background=Cinza_Novo, activebackground=Cinza40,
                           command=Consulta_Prod)
# ---------------------------------------------------------------------------------------------------------------------
# Criando Relatorios Menu com função VENDAS
Relatorios.menu.add_command(label='VENDAS', font=Fonte12B, background=Cinza_Novo, activebackground=Cinza40)
# ---------------------------------------------------------------------------------------------------------------------
# Criando Agenda Menu com função Telefonica
Agenda.menu.add_command(label='TELEFÔNICA', font=Fonte12B, background=Cinza_Novo, activebackground=Cinza40)
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
Arquivo.menu.add_cascade(label='CLIENTES', menu=ClientesMenu, font=Fonte12B, background=Cinza_Novo,
                         activebackground=Cinza40)
Arquivo.menu.add_cascade(label="USUÁRIOS", menu=UsuarioMenu, font=Fonte12B, background=Cinza_Novo,
                         activebackground=Cinza40)
Arquivo.menu.add_cascade(label="GRUPO", menu=GrupoMenu, font=Fonte12B, background=Cinza_Novo,
                         activebackground=Cinza40)
Arquivo.menu.add_cascade(label="PRODUTOS", font=Fonte12B, menu=ProdutosMenu, background=Cinza_Novo,
                         activebackground=Cinza40)
Arquivo.menu.add_command(label="SAIR", font=Fonte12, background=Cinza_Novo, activebackground=Vermelho,
                         command=Sair_Tela_Inicial)
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


# Cadastro de Tecla Atalho
Windows.bind_all("<Control-u>", Register_Users)
Windows.bind_all("<Control-s>", Sair_Tela_Inicial)
Windows.bind_all("<Control-p>", Register_Prod)
Windows.bind_all("<Control-m>", Register_Group)
#Windows.bind_all("<Control-e>", Excluir_usuario)
#Windows.bind_all("<Control-m>", Cadastro_Consulta_Medicamento)

# Desativando o Botão X da Tela
Windows.protocol("WM_DELETE_WINDOW", Desativar_Max)
Windows.iconbitmap("Imagens/Logo_SFundo.ico")
Windows.mainloop()
