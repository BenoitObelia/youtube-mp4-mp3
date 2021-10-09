from pathlib import Path
from tkinter import *
from tkinter import filedialog

from fonctions import mp3, mp4
from settings import COLOR_BG_CADRE, COLOR_BG_FENETRE, COLOR_BG_BOUTONS, COLOR_TEXT_BOUTONS

path = str(Path.home() / "Downloads")


def edit_path():
    global path
    new_path = filedialog.askdirectory(initialdir=path)
    if new_path != "":
        path = new_path
        var.set(f"Le fichier sera enregistré dans {path}")


fenetre1 = Tk()
fenetre1.title("Télécharger une vidéo MP3 / MP4")
fenetre1.iconbitmap("assets/YouTube.ico")

fenetre1.config(bg = COLOR_BG_FENETRE)

fenetre1.geometry("640x300")
f1 = Frame(fenetre1, bd = 5)
f1.config(bg = COLOR_BG_CADRE)
f1.pack()

cadre1 = Frame(f1, bd = 5)
cadre1.config(bg = COLOR_BG_CADRE)
cadre1.pack()

cadre2 = Frame(f1, bd = 5)
cadre2.config(bg = COLOR_BG_CADRE)
cadre2.pack()

cadre3 = Frame(f1, bd = 5)
cadre3.config(bg = COLOR_BG_CADRE)
cadre3.pack()

texteTelechargement = Label(
    cadre1, text="Collez le lien de la vidéo puis choisissez le mode de téléchargement")
texteTelechargement.config(bg=COLOR_BG_BOUTONS, fg = COLOR_TEXT_BOUTONS)
texteTelechargement.pack()

maLegende = Label(cadre2, text='URL : ')
maLegende.config(bg=COLOR_BG_BOUTONS, fg = COLOR_TEXT_BOUTONS)
maLegende.pack(padx=5, pady=5, side=LEFT)

saisie = Entry(cadre2)
URL = saisie.get()
saisie.pack(padx=5, pady=5)

boutonMP4 = Button(cadre3, text="MP4", command=lambda: mp4(saisie.get(), path))
boutonMP4.config(bg=COLOR_BG_BOUTONS, fg = COLOR_TEXT_BOUTONS)
boutonMP4.pack()

boutonMP3 = Button(cadre3, text="MP3", command=lambda: mp3(saisie.get()))
boutonMP3.config(bg=COLOR_BG_BOUTONS, fg = COLOR_TEXT_BOUTONS)
boutonMP3.pack()
var = StringVar()
defaultPath = Label(cadre3, textvariable=var)
defaultPath.config(bg=COLOR_BG_BOUTONS, fg = COLOR_TEXT_BOUTONS)
defaultPath.pack()
var.set(f"Le fichier sera enregistré dans {path}")

buttonEditPathFile = Button(cadre3, text="edit", command=edit_path, bg = COLOR_BG_BOUTONS, fg ="white" )
boutonMP3.config(bg=COLOR_BG_BOUTONS, fg = COLOR_TEXT_BOUTONS)
buttonEditPathFile.pack()

f1.mainloop()

print(f'Lien de la vidéo : {URL}')
