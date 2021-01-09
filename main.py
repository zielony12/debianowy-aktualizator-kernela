import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import getpass
from subprocess import Popen, PIPE
import distro

root = Tk()
root.resizable(False,False)
root.geometry("400x300")
root.config(bg="#f0f0f0")
class vars():
    is_launched = False
    dist = str(distro.linux_distribution())
    inf = font.Font(family="Ubuntu Thin", size=5)
    titlefont = font.Font(family="Ubuntu Thin", size=20)
    font1 = font.Font(family="Ubuntu Thin", size=10)
    connection = os.system("ping -c 1 google.com")
    username = str(getpass.getuser())
def launch():
    title = Label(text="Witaj w menedżerze\naktualizacji jądra Linuxa Debiana.", font=vars.titlefont, bg="#f0f0f0")
    subtitle = Label(text="\ninstalator działa równierz na dystrybucjach:\nUbuntu\nMint\nMx\nPop!_os\nXubuntu\nLubuntu\nKubuntu", font=vars.font1, bg="#f0f0f0")
    authors = Label(text="\nAutorzy: działanie programu: Edzio, interfejs graficzny: skubaniec\n\n", font=vars.inf, bg="#f0f0f0")
    authors.pack()
    def next():
        title.config(text="Proszę potwierdzić aktualizację")
        subtitle.config(text="\nAktualizacja nie spowoduje usunięcia plików, ale każda\nniesie za sobą ryzyko uszkodzenia danych,\nmoże do tego dojść kiedy: na przykład:\nzabraknie prądu, i komputer się wyłączy, albo ktoś celowo\nwyłączy komputer.")
        button_next.destroy()
        button_install.place(x=320,y=260)
    
    button_next = Button(text="Dalej", font=vars.font1, width=5, command=next)
    button_exit = Button(text="Anuluj", font=vars.font1, width=5, command=lambda: root.destroy())
    title.pack()
    subtitle.pack()
    button_next.place(x=320,y=260)
    button_exit.place(x=15,y=260)
def check():
    if vars.connection == 0:
        is_root = os.getuid()
        if is_root == 0:
            if "Mint" in vars.dist or "buntu" in vars.dist or "Debian" in vars.dist or "Mx" in vars.dist:
                if vars.is_launched == False:
                    vars.is_launched = True
                    launch()
            else:
                messagebox.showerror("Błąd", "Twoja dystrybucja nie pochodzi od Debiana. Kernel nie zostanie zaktualizowany.")
                root.destroy()
        else:
            messagebox.showerror("Błąd", "Musisz być super-użytkownikiem, aby skorzystać z aktualizatora. Spróbuj uruchomić ten program jako root używając polecenia 'sudo'")
            root.destroy()
    else:
        messagebox.showerror("Błąd", "Nie można połączyć się z serwerem w celu pobrania najnowszej wersji jądra Debiana. Sprawdź swoje połączenie internetowe i spróbuj ponownie puźniej.")
        root.destroy()
check()
def kernel_update():
    print("Checking important informations...")
    check()
    print("\nOK\n\n")
    print("Downloading latest kernel update to /home/"+vars.username+"/ ...")
    os.system("wget https://raw.githubusercontent.com/pimlie/ubuntu-mainline-kernel.sh/master/ubuntu-mainline-kernel.sh")
    print("OK\n\n")
    print("installing update...")
    os.system("sudo install ubuntu-mainline-kernel.sh /usr/local/bin/")
    os.system("sudo ubuntu-mainline-kernel.sh -i -f")
    print("\nOK\n\n")
    messagebox.showinfo("Informacja", "Pomyślnie zaktualizowano jądro linuxa, uruchom ponownie komputer, aby zastosować zmiany. Jeżeli wersja jądra pozostaje bez zmian, uruchom ponownie narzędzie do aktualizowania jądra i spróbuj ponownie.")
    root.destroy()

button_install = Button(text="Aktualizuj", font=vars.font1, width=5, command=kernel_update)
root.mainloop()
