# --------------- TELA DE EXCLUIR PRODUTOS ----------------------------------------------------------------------------
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
Frame_Exc_Produtos.config(font=Fonte11B, bg=Cinza40, fg=Amarelo_Novo)
Frame_Exc_Produtos.place(x=5, y=80, width=440, height=180)
# -----------------------------------------------------------------------------------------------------------------
# Label e Entry do CODIGO do PRODUTO
Var_Cod_Prod_Exc = StringVar()
Var_Cod_Prod_Exc.set("")
Lbl_Cod_Prod_Exc = Label(Frame_Exc_Produtos, text="CODIGO:", font=Fonte11B, bg=Cinza40, fg=Branco)
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
Lbl_Cod_Barras_Exc = Label(Frame_Exc_Produtos, text="COD BARRAS:", font=Fonte11B, bg=Cinza40, fg=Branco)
Lbl_Cod_Barras_Exc.place(x=170, y=5)
Ent_Cod_Barras_Exc = Entry(Frame_Exc_Produtos, textvariable=Var_Cod_Barras_Exc)
Ent_Cod_Barras_Exc.config(width=13, justify=CENTER, font=Fonte12, state=DISABLED)
Ent_Cod_Barras_Exc.place(x=290, y=5)
# -----------------------------------------------------------------------------------------------------------------
# Label e Entry do NOME DO PRODUTO
Var_Exc_Nome_Prod = StringVar()
Var_Exc_Nome_Prod.set("")
Lbl_Nome_Prod = Label(Frame_Exc_Produtos, text="NOME:", font=Fonte11B, bg=Cinza40, fg=Branco)
Lbl_Nome_Prod.place(x=5, y=45)
Ent_Nome_Prod = Entry(Frame_Exc_Produtos, font=Fonte12, width=37, textvariable=Var_Exc_Nome_Prod, state=DISABLED)
Ent_Nome_Prod.place(x=83, y=45)
# -----------------------------------------------------------------------------------------------------------------
# Label e Entry de MARCA DO PRODUTO
Var_Exc_Prod_Group = StringVar()
Var_Exc_Prod_Group.set("")
Lbl_Exc_Prod_Group = Label(Frame_Exc_Produtos, text="GRUPO:", font=Fonte11B, bg=Cinza40, fg=Branco)
Lbl_Exc_Prod_Group.place(x=5, y=85)
CMB_Exc_Prod_Group = Combobox(Frame_Exc_Produtos, font=Fonte11, width=20, textvariable=Var_Exc_Prod_Group)
CMB_Exc_Prod_Group.config(state=DISABLED)
CMB_Exc_Prod_Group['values'] = CMBGroup_Prod()
CMB_Exc_Prod_Group.place(x=83, y=85)
Frame_Exc_Produtos.option_add('*TCombobox*Listbox.font', Fonte11)
Frame_Exc_Produtos.option_add('*TCombobox*Listbox.selectBackground', Cinza_Novo)
Frame_Exc_Produtos.option_add('*TCombobox*Listbox.background', Branco)
Frame_Exc_Produtos.option_add('*TCombobox*Listbox.selectForeground', Branco)
# -----------------------------------------------------------------------------------------------------------------
# Label e Entry PREÇO do Produto
Var_Preco_Exc = StringVar()
Var_Preco_Exc.set("")
Lbl_Preco_Exc = Label(Frame_Exc_Produtos, text="PREÇO:", font=Fonte11B, bg=Cinza40, fg=Branco)
Lbl_Preco_Exc.place(x=5, y=125)
Ent_Preco_Exc = Entry(Frame_Exc_Produtos, font=Fonte12, width=8, textvariable=Var_Preco_Exc, justify=RIGHT)
Ent_Preco_Exc.config(state=DISABLED)
Ent_Preco_Exc.place(x=110, y=125)
# -----------------------------------------------------------------------------------------------------------------
Lbl_Preco_Exc = Label(Frame_Exc_Produtos, text="R$", font=Fonte11B, bg=Cinza40, fg=Branco)
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

# ------------------------ FIM ----------------------------------------------------------------------------------------
Windows_Exc_Prod.mainloop()
