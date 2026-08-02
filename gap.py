import tkinter as tk
from playsound import playsound
from pathlib import Path
import sys

# Back-End

# Isso define a pasta raiz do programa
if getattr(sys, "frozen", False):
    BASE_DIR = Path(sys._MEIPASS)
else:
    BASE_DIR = Path(__file__).resolve().parent

# Variavéis
counter = 0

Path_Image_bg = BASE_DIR / "assets" / "images" / "img_background.png"
Path_Image_icon = BASE_DIR / "assets" / "images" / "img_icon.png"

Path_Sound_open = BASE_DIR / "assets" / "sounds" / "snd_open.mp3"
Path_Sound_close = BASE_DIR / "assets" / "sounds" / "snd_close.mp3"
Path_Sound_up = BASE_DIR / "assets" / "sounds" / "snd_counter_up.mp3"
Path_Sound_down = BASE_DIR / "assets" / "sounds" / "snd_counter_down.mp3"
Path_Sound_about = BASE_DIR / "assets" / "sounds" / "snd_about.mp3"


# Funções
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
        
        playsound(str(Path_Sound_about), block=False)

    except Exception as e:
        print("Erro ao tocar som de abrir:", e)


    

def tocar_som_fechar():
    # Toca o som de fechamento (pode usar block=True aqui para garantir que toca antes de sair)
    try:
        playsound(str(Path_Sound_close), block=True)
    except Exception as e:
        print("Erro ao tocar som de fechar:", e)
    
    # Destrói a janela de fato após o som
    app.destroy()

def adicionar():
    global counter
    counter += 1
    num_panel.config(text=str(counter))
    playsound(str(Path_Sound_up), block=False)

def remover():
    global counter
    if counter > 0:
        counter -= 1
        num_panel.config(text=str(counter))
        playsound(str(Path_Sound_down), block=False)

try:
    playsound(str(Path_Sound_open), block=False)
except Exception as e:
    print("Erro ao tocar som de abrir:", e)


# Front-End
# Janela principal
app = tk.Tk()

icon = tk.PhotoImage(file=str(Path_Image_icon))

app.title("ETI's Gap Meter 98 Deluxe")
app.geometry("300x241")
app.resizable(False, False)
app.iconphoto(True, icon)

# Frame Principal

et_photo = tk.PhotoImage(file=str(Path_Image_bg))

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
