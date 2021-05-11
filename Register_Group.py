# ---------- TELA DE CADASTRO DE GRUPO --------------------------------------------------------------------------------
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
Windows_Cad_Group.mainloop()