import tkinter as tk
from playsound import playsound

# Back-End
# Funções dos botões

contador = 0

def Top_Level_About(event=None):

    about_window = tk.Toplevel(app)
    about_window.title("Sobre o Programa!")
    about_window.geometry("300x350")

    about_window.grab_set()

    txt_info = tk.Label(about_window, text="Gapômetro ETi 98 v1.0")
    txt_info.pack()

    p_info = tk.Label(about_window, text="""
    Salve Et, meu nome é Cecilio, tenho 15 anos,
    e tive essa ideia dps de você receber os dois
    contadores de gap fisicos, ent decidi fazer a
    versão digital do dispositivo revolucionario.

    Produzido com:
    Python 3.8.10
    Tkinter
    Playsound
    Testado no Windows 7

    Feito por: Energato Dev (github.com/energatodev)
    Para: Enzo Tulio, vulgo ET

    Assets pegos na Net

    Um abraço do Dev!
    """)
    p_info.pack()

    try:
        
        playsound('assets/sounds/som_meme.mp3', block=False)

    except Exception as e:
        print("Erro ao tocar som de abrir:", e)


    

def tocar_som_fechar():
    # Toca o som de fechamento (pode usar block=True aqui para garantir que toca antes de sair)
    try:
        playsound('assets/sounds/som_fechar.mp3', block=True)
    except Exception as e:
        print("Erro ao tocar som de fechar:", e)
    
    # Destrói a janela de fato após o som
    app.destroy()

def adicionar():
    global contador
    contador += 1
    num_panel.config(text=str(contador))
    playsound("assets/sounds/som_(+1).mp3", block=False)

def remover():
    global contador
    if contador > 0:
        contador -= 1
        num_panel.config(text=str(contador))
        playsound("assets/sounds/som_(-1).mp3", block=False)

try:
    playsound('assets/sounds/som_abrir.mp3', block=False)
except Exception as e:
    print("Erro ao tocar som de abrir:", e)


# Front-End
# Janela principal
app = tk.Tk()
app.title("ETI's Gap Meter 98 Deluxe")
app.geometry("300x241")
app.resizable(False, False)

# Frame Principal

et_photo = tk.PhotoImage(file="./assets/images/Design sem nome.png")

principal_frame = tk.LabelFrame(master=app, borderwidth=1, highlightbackground="blue", highlightthickness=5)
principal_frame.pack(expand=True, fill='both')

background_img = tk.Label(principal_frame, image=et_photo)
background_img.place(x=0, y=0, relwidth=1, relheight=1)

# Frame do título do topo
title_frame = tk.LabelFrame(master=principal_frame, borderwidth=4, cursor="hand2")
title_frame.pack(pady=5)

# Título "Gap Meter 98"
title = tk.Label(title_frame, text="GAP METER 98", font="Fixedsys 20")
title.pack()

title.bind("<Button-1>", Top_Level_About)

# Subtítulo "Dekuxe Edition"
subtitle = tk.Label(title_frame, text="DELUXE EDITION", font="Fixedsys 14")
subtitle.pack()

# Frame dos botões e do painel
panel_frame = tk.LabelFrame(master=principal_frame, borderwidth=4)
panel_frame.pack(pady=10, padx=10)

title_panel = tk.Label(panel_frame, text="Total de Gap's", font="Fixedsys 16")
title_panel.pack()

num_panel = tk.Label(panel_frame, text="0", font="Fixedsys 40")
num_panel.pack(pady=10)

add_btn = tk.Button(panel_frame, text="+1", command=adicionar, font="Fixedsys 17", cursor="hand2")
add_btn.pack(side=tk.LEFT, padx=2)


remove_btn = tk.Button(panel_frame, text="-1", command=remover, font="Fixedsys 17", cursor="hand2")
remove_btn.pack(side=tk.RIGHT, padx=2)

app.protocol("WM_DELETE_WINDOW", tocar_som_fechar)

app.mainloop()
