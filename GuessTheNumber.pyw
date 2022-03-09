from tkinter import *
import random

ZgNumer = Tk()
ZgNumer.title("Zgadnij Liczbę!")
ZgNumer.minsize(
    width=500,
    height=400
    
)
ZgNumer.maxsize(
    width=500,
    height=400
)

poz_trudnosci = Frame(
    ZgNumer,
    width=500,
    height=400,
    bg="#111111"
)
poz_trudnosci.pack(fill="both",expand=1)

tekst = Label(
    poz_trudnosci,
    text="Wybierz poziom trudnosci",
    font=("Sans Serif", 22, "bold"),
    fg="white",
    bg="#111111"
)
tekst.place(
    x=250,
    y=100,
    anchor=CENTER
)

copyright = Label(
    poz_trudnosci,
    text="Copyright © 2022, kndxiu. Wszelkie prawa zastrzeżone",
    font=("Sans Serif", 8, "bold"),
    fg="white",
    bg="#111111"
)
copyright.place(
    x=250,
    y=390,
    anchor=CENTER
)

def latwy():
    klatka_pozLatwy.pack(fill="both",expand=1)
    poz_trudnosci.forget()
    global zakresLatwySprawdz
    zakresLatwySprawdz = 100
    global liczbaLatwy
    liczbaLatwy = random.randint(1,100)
    print(liczbaLatwy)
    wpisz_liczbeLatwy.delete(0, "end")
    tekstOdpowiedzLatwy.config(text="")

def sredni():
    klatka_pozSredni.pack(fill="both",expand=1)
    poz_trudnosci.forget()
    global zakresSredniSprawdz
    zakresSredniSprawdz = 1000
    global liczbaSredni
    liczbaSredni = random.randint(1,1000)
    print(liczbaSredni)
    wpisz_liczbeSredni.delete(0, "end")
    tekstOdpowiedzSredni.config(text="")

def trudny():
    klatka_pozTrudny.pack(fill="both",expand=1)
    poz_trudnosci.forget()
    global zakresTrudnySprawdz
    zakresTrudnySprawdz = 10000
    global liczbaTrudny
    liczbaTrudny = random.randint(1,10000)
    print(liczbaTrudny)
    wpisz_liczbeTrudny.delete(0, "end")
    tekstOdpowiedzTrudny.config(text="")

def wrocLatwy():
    poz_trudnosci.pack(fill="both",expand=1)
    klatka_pozLatwy.forget()

def wrocSredni():
    poz_trudnosci.pack(fill="both",expand=1)
    klatka_pozSredni.forget()

def wrocTrudny():
    poz_trudnosci.pack(fill="both",expand=1)
    klatka_pozTrudny.forget()

def naPrzyciskuLatwy(e):
    poz_latwy['bg']='#25dae9'
    poz_latwy['fg']='#111111'

def zPrzyciskuLatwy(e):
    poz_latwy['bg']='#111111'
    poz_latwy['fg']='#25dae9'

def naPrzyciskuSredni(e):
    poz_sredni['bg']='#ffcc66'
    poz_sredni['fg']='#111111'

def zPrzyciskuSredni(e):
    poz_sredni['bg']='#111111'
    poz_sredni['fg']='#ffcc66'

def naPrzyciskuTrudny(e):
    poz_trudny['bg']='#f86263'
    poz_trudny['fg']='#111111'

def zPrzyciskuTrudny(e):
    poz_trudny['bg']='#111111'
    poz_trudny['fg']='#f86263'

poz_latwy = Button(
    poz_trudnosci,
    width=500,
    text="Łatwy",
    font=("Sans Serif", 16, "bold"),
    bg="#111111",
    fg="#25dae9",
    activebackground="#167f87",
    activeforeground="#1a1a1a",
    borderwidth=0,
    cursor="hand2",
    command=latwy
)
poz_latwy.place(
    x=250,
    y=175,
    anchor=CENTER
)

zakresLatwy = Label(
    poz_trudnosci,
    text="1-100",
    font=("Sans Serif",9,"bold"),
    bg="#111111",
    fg="white"
)
zakresLatwy.place(
    x=250,
    y=205,
    anchor=CENTER
)
poz_sredni = Button(
    poz_trudnosci,
    width=500,
    text="Średni",
    font=("Sans Serif", 16, "bold"),
    bg="#111111",
    fg="#ffcc66",
    activebackground="#a38549",
    activeforeground="#1a1a1a",
    borderwidth=0,
    cursor="hand2",
    command=sredni
)
poz_sredni.place(
    x=250,
    y=250,
    anchor=CENTER
)

zakresSredni = Label(
    poz_trudnosci,
    text="1-1000",
    font=("Sans Serif",9,"bold"),
    bg="#111111",
    fg="white"
)
zakresSredni.place(
    x=250,
    y=280,
    anchor=CENTER
)

poz_trudny = Button(
    poz_trudnosci,
    width=500,
    text="Trudny",
    font=("Sans Serif", 16, "bold"),
    bg="#111111",
    fg="#f86263",
    activebackground="#913c3c",
    activeforeground="#1a1a1a",
    borderwidth=0,
    cursor="hand2",
    command=trudny
)
poz_trudny.place(
    x=250,
    y=325,
    anchor=CENTER
)

zakresTrudny = Label(
    poz_trudnosci,
    text="1-10000",
    font=("Sans Serif",9,"bold"),
    bg="#111111",
    fg="white"
)
zakresTrudny.place(
    x=250,
    y=355,
    anchor=CENTER
)

poz_latwy.bind('<Enter>',naPrzyciskuLatwy)
poz_latwy.bind('<Leave>',zPrzyciskuLatwy)

poz_sredni.bind('<Enter>',naPrzyciskuSredni)
poz_sredni.bind('<Leave>',zPrzyciskuSredni)

poz_trudny.bind('<Enter>',naPrzyciskuTrudny)
poz_trudny.bind('<Leave>',zPrzyciskuTrudny)

klatka_pozLatwy = Frame(
    ZgNumer,
    width=500,
    height=400,
    bg="#111111"
)

btn_wrocLatwy = Button(
    klatka_pozLatwy,
    width=1,
    height=1,
    font=("Sans Serif", 18, "bold"),
    bg="#111111",
    fg="white",
    activebackground="#111111",
    activeforeground="white",
    borderwidth=0,
    cursor="hand2",
    text="←",
    command=wrocLatwy
)
btn_wrocLatwy.place(
    x=20,
    y=7
)

def naPrzyciskuSprawdz(e):
    btnLatwy['bg']='#dedede'
    btnLatwy['fg']='#111111'

def zPrzyciskuSprawdz(e):
    btnLatwy['bg']='#111111'
    btnLatwy['fg']='#dedede'

tekstLatwy = Label(
    klatka_pozLatwy,
    text="Zgadnij liczbę w zakresie 1 - 100",
    font=("Sans Serif", 17, "bold"),
    fg="white",
    bg="#111111"
)
tekstLatwy.place(
    x=250,
    y=90,
    anchor=CENTER
)
tekstLatwy1 = Label(
    klatka_pozLatwy,
    text="Wpisz liczbę poniżej",
    font=("Sans Serif", 13, "underline"),
    fg="#f86263",
    bg="#111111"
)
tekstLatwy1.place(
    x=250,
    y=120,
    anchor=CENTER
)

inputLatwy=IntVar()

wpisz_liczbeLatwy = Entry(
    klatka_pozLatwy,
    text=inputLatwy,
    font=("Sans Serif",16,"bold"),
    bg="#111111",
    fg="white",
    border=3,
    insertbackground="white"
)
wpisz_liczbeLatwy.place(
    x=250,
    y=170,
    anchor=CENTER
)

def sprawdzLatwy():
    odpowiedzLatwy = int(wpisz_liczbeLatwy.get())

    if odpowiedzLatwy == liczbaLatwy:
        tekstOdpowiedzLatwy.config(text="Brawo! Udało Ci się zgadnąć!",fg="lime")
    elif odpowiedzLatwy < liczbaLatwy:
        tekstOdpowiedzLatwy.config(text="Liczba jest za mała, spróbuj ponownie.",fg="red")
    elif odpowiedzLatwy > liczbaLatwy and odpowiedzLatwy < zakresLatwySprawdz:
        tekstOdpowiedzLatwy.config(text="Liczba jest za duża, spróbuj ponownie.",fg="red")
    elif odpowiedzLatwy > zakresLatwySprawdz:
        tekstOdpowiedzLatwy.config(text="Nie wychodź poza zakres.",fg="red")

btnLatwy = Button(
    klatka_pozLatwy,
    width=100,
    font=("Sans Serif", 16, "bold"),
    bg="#111111",
    fg="#dedede",
    activebackground="#bfbfbf",
    activeforeground="#1a1a1a",
    borderwidth=0,
    cursor="hand2",
    text="SPRAWDŹ",
    command=sprawdzLatwy
)
btnLatwy.place(
    x=250,
    y=240,
    anchor=CENTER
)

tekstOdpowiedzLatwy = Label(
    klatka_pozLatwy,
    text="",
    font=("Sans Serif", 12, "bold"),
    bg="#111111"
)
tekstOdpowiedzLatwy.place(
    x=250,
    y=205,
    anchor=CENTER
)

btnLatwy.bind('<Enter>',naPrzyciskuSprawdz)
btnLatwy.bind('<Leave>',zPrzyciskuSprawdz)

klatka_pozSredni = Frame(
    ZgNumer,
    width=500,
    height=400,
    bg="#111111"
)

btn_wrocSredni = Button(
    klatka_pozSredni,
    width=1,
    height=1,
    font=("Sans Serif", 18, "bold"),
    bg="#111111",
    fg="white",
    activebackground="#111111",
    activeforeground="white",
    borderwidth=0,
    cursor="hand2",
    text="←",
    command=wrocSredni
)
btn_wrocSredni.place(
    x=20,
    y=7
)

def naPrzyciskuSprawdz(e):
    btnSredni['bg']='#dedede'
    btnSredni['fg']='#111111'

def zPrzyciskuSprawdz(e):
    btnSredni['bg']='#111111'
    btnSredni['fg']='#dedede'

tekstSredni = Label(
    klatka_pozSredni,
    text="Zgadnij liczbę w zakresie 1 - 1000",
    font=("Sans Serif", 17, "bold"),
    fg="white",
    bg="#111111"
)
tekstSredni.place(
    x=250,
    y=90,
    anchor=CENTER
)
tekstSredni1 = Label(
    klatka_pozSredni,
    text="Wpisz liczbę poniżej",
    font=("Sans Serif", 13, "underline"),
    fg="#f86263",
    bg="#111111"
)
tekstSredni1.place(
    x=250,
    y=120,
    anchor=CENTER
)

inputSredni=IntVar()

wpisz_liczbeSredni = Entry(
    klatka_pozSredni,
    text=inputSredni,
    font=("Sans Serif",16,"bold"),
    bg="#111111",
    fg="white",
    border=3,
    insertbackground="white"
)
wpisz_liczbeSredni.place(
    x=250,
    y=170,
    anchor=CENTER
)

def sprawdzSredni():
    odpowiedzSredni = int(wpisz_liczbeSredni.get())

    if odpowiedzSredni == liczbaSredni:
        tekstOdpowiedzSredni.config(text="Brawo! Udało Ci się zgadnąć!",fg="lime")
    elif odpowiedzSredni < liczbaSredni:
        tekstOdpowiedzSredni.config(text="Liczba jest za mała, spróbuj ponownie.",fg="red")
    elif odpowiedzSredni > liczbaSredni and odpowiedzSredni < zakresSredniSprawdz:
        tekstOdpowiedzSredni.config(text="Liczba jest za duża, spróbuj ponownie.",fg="red")
    elif odpowiedzSredni > zakresSredniSprawdz:
        tekstOdpowiedzSredni.config(text="Nie wychodź poza zakres.",fg="red")

btnSredni = Button(
    klatka_pozSredni,
    width=100,
    font=("Sans Serif", 16, "bold"),
    bg="#111111",
    fg="#dedede",
    activebackground="#bfbfbf",
    activeforeground="#1a1a1a",
    borderwidth=0,
    cursor="hand2",
    text="SPRAWDŹ",
    command=sprawdzSredni
)
btnSredni.place(
    x=250,
    y=240,
    anchor=CENTER
)

tekstOdpowiedzSredni = Label(
    klatka_pozSredni,
    text="",
    font=("Sans Serif", 12, "bold"),
    bg="#111111"
)
tekstOdpowiedzSredni.place(
    x=250,
    y=205,
    anchor=CENTER
)

btnSredni.bind('<Enter>',naPrzyciskuSprawdz)
btnSredni.bind('<Leave>',zPrzyciskuSprawdz)

klatka_pozTrudny = Frame(
    ZgNumer,
    width=500,
    height=400,
    bg="#111111"
)

btn_wrocTrudny = Button(
    klatka_pozTrudny,
    width=1,
    height=1,
    font=("Sans Serif", 18, "bold"),
    bg="#111111",
    fg="white",
    activebackground="#111111",
    activeforeground="white",
    borderwidth=0,
    cursor="hand2",
    text="←",
    command=wrocTrudny
)
btn_wrocTrudny.place(
    x=20,
    y=7
)

def naPrzyciskuSprawdz(e):
    btnTrudny['bg']='#dedede'
    btnTrudny['fg']='#111111'

def zPrzyciskuSprawdz(e):
    btnTrudny['bg']='#111111'
    btnTrudny['fg']='#dedede'

tekstTrudny = Label(
    klatka_pozTrudny,
    text="Zgadnij liczbę w zakresie 1 - 10000",
    font=("Sans Serif", 17, "bold"),
    fg="white",
    bg="#111111"
)
tekstTrudny.place(
    x=250,
    y=90,
    anchor=CENTER
)
tekstTrudny1 = Label(
    klatka_pozTrudny,
    text="Wpisz liczbę poniżej",
    font=("Sans Serif", 13, "underline"),
    fg="#f86263",
    bg="#111111"
)
tekstTrudny1.place(
    x=250,
    y=120,
    anchor=CENTER
)

inputTrudny=IntVar()

wpisz_liczbeTrudny = Entry(
    klatka_pozTrudny,
    text=inputTrudny,
    font=("Sans Serif",16,"bold"),
    bg="#111111",
    fg="white",
    border=3,
    insertbackground="white"
)
wpisz_liczbeTrudny.place(
    x=250,
    y=170,
    anchor=CENTER
)

def sprawdzTrudny():
    odpowiedzTrudny = int(wpisz_liczbeTrudny.get())
    odpowiedzTrudny = len(wpisz_liczbeTrudny.get())

    if odpowiedzTrudny == liczbaTrudny:
        tekstOdpowiedzTrudny.config(text="Brawo! Udało Ci się zgadnąć!",fg="lime")
    elif odpowiedzTrudny < liczbaTrudny:
        tekstOdpowiedzTrudny.config(text="Liczba jest za mała, spróbuj ponownie.",fg="red")
    elif odpowiedzTrudny > liczbaTrudny and odpowiedzTrudny < zakresTrudnySprawdz:
        tekstOdpowiedzTrudny.config(text="Liczba jest za duża, spróbuj ponownie.",fg="red")
    elif odpowiedzTrudny > zakresTrudnySprawdz:
        tekstOdpowiedzTrudny.config(text="Nie wychodź poza zakres.",fg="red")

btnTrudny = Button(
    klatka_pozTrudny,
    width=100,
    font=("Sans Serif", 16, "bold"),
    bg="#111111",
    fg="#dedede",
    activebackground="#bfbfbf",
    activeforeground="#1a1a1a",
    borderwidth=0,
    cursor="hand2",
    text="SPRAWDŹ",
    command=sprawdzTrudny
)
btnTrudny.place(
    x=250,
    y=240,
    anchor=CENTER
)

tekstOdpowiedzTrudny = Label(
    klatka_pozTrudny,
    text="",
    font=("Sans Serif", 12, "bold"),
    bg="#111111"
)
tekstOdpowiedzTrudny.place(
    x=250,
    y=205,
    anchor=CENTER
)

btnTrudny.bind('<Enter>',naPrzyciskuSprawdz)
btnTrudny.bind('<Leave>',zPrzyciskuSprawdz)

ZgNumer.mainloop()