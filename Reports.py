# ---------- TELA Relatorios --------------------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


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

Windows_Cad_Group = Toplevel()
Windows_Cad_Group.geometry("370x200+250+200")
Windows_Cad_Group.title("SISTEMA DE GERENCIAMENTO")
Windows_Cad_Group.minsize(710, 480)
Windows_Cad_Group.maxsize(710, 480)
Windows_Cad_Group.resizable(False, False)
Windows_Cad_Group["bg"] = Cinza_Novo
Windows_Cad_Group.iconbitmap("Imagens/Logo_SFundo.ico")

imagemLogo = PhotoImage(file="Imagens//Save.png")
# -----------------------------------------------------------------------------------------------------------------
Lbl_Titulo4 = Label(Windows_Cad_Group, text="----" * 10, bg=Cinza_Novo, fg=Amarelo_Novo, font=Fonte12I)
Lbl_Titulo4.place(x=0, y=10)
# -----------------------------------------------------------------------------------------------------------------
Frame_Group = LabelFrame(Windows_Cad_Group, text="Relatorios", bg=Cinza40, fg=Amarelo_Novo, font=Fonte11B)
Frame_Group.place(x=5, y=70, width=700, height=400)

# -----------------------------------------------------------------------------------------------------------------

Windows_Cad_Group.mainloop()
