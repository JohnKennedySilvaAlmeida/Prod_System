# Tela para EXCLUIR GRUPO ---------------------------------------------------------------------------------------------
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
Windows_Del_Group.option_add('*TCombobox*Listbox.selectBackground', Cinza_Novo)
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
Windows_Del_Group.mainloop()
