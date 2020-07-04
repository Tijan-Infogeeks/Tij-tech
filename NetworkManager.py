
# Network manager project by Tijan


from tkinter import *
import time
from PIL import ImageTk,Image
import os.path
from os import path
from tkinter import ttk
import nmap 



if os.path.exists("proj/.transp.ini") != True:
    with open("proj/.transp.ini", "w+"):
        pass
if os.path.exists("proj/ip.ini") != True:
    with open("proj/.ip.ini", "w+"):
        pass


root = Tk()
try:    
    root.iconbitmap("proj/my.ico")
except Exception:
    pass
root.title("Network Manager by Tij")
root.geometry('520x428+50+50')
root.overrideredirect(False)
root.config(bg='white')
with open("proj/.transp.ini", 'r') as f:
    nbr = f.read()
if nbr != "":
    root.attributes("-alpha", nbr)

def step():
    for x in range(100):
        root.update()
        my_progress['value'] += 5
        
        time.sleep(0.01)
my_progress = ttk.Progressbar(root, orient=HORIZONTAL, length=200, mode='determinate')
my_progress.grid(pady=200, padx=150)
step()
root.after(0, my_progress.destroy)
    
def wait():
    time.sleep(0.05)
def dim(t):
    root.attributes("-alpha", t)

def ferm():
    root.quit()
def get():
    s = int(w.get())
    if s == 0:
        with open("proj/.transp.ini.", "w") as f:
            f.write('1')
        
        root.attributes("-alpha", 1)
       
    if s == 1:
        with open("proj/.transp.ini.", "w") as f:
            f.write('0.97')
        root.attributes("-alpha", 0.97)
        
    if s == 2:
        root.attributes("-alpha", 0.95)
        
    if s == 3:
        root.attributes("-alpha", 0.93)
        
    if s == 4:
        root.attributes("-alpha", 0.90)
        
    if s == 5:
        root.attributes("-alpha", 0.87)
        
    if s == 6:
        root.attributes("-alpha", 0.84)
        
    if s == 7:
        root.attributes("-alpha", 0.81)
        
    if s == 8:
        root.attributes("-alpha", 0.78)
        
    if s == 9:
        root.attributes("-alpha", 0.75)
        
    if s == 10:
        root.attributes("-alpha", 0.73)
        

def fermer(e):
   
    root.quit()
def show(e):
    root.overrideredirect(False)

# f_colors 

def jaune(e):
    root.config(bg='#fff176')
    fr.config(bg='white')
    lbl2.config(bg='#fff176')
    lbl.config(bg='#fff176')
    w.config(bg='#fff176')
def rouge(e):
    root.config(bg='#263238')
    lbl2.config(bg='grey')
    lbl.config(bg='grey')
def gris(e):
    root.config(bg='grey')
    lbl2.config(bg='grey')
    lbl.config(bg='grey')
    w.config(bg='white')



def blanc(e):
    root.config(bg='white')
    lbl2.config(bg='white')
    lbl.config(bg='white')
    w.config(bg='#8bc34a')
    btn_principal.config(bg='#e0e0e0')         #4  #buttons = (btn_principal, but1, but_2, but_3, but_4)
    but1.config(bg='#bdbdbd')
    but_2.config(bg='#9e9e9e')
    but_3.config(bg='#757575')
    but_4.config(bg='#616161')

                                                  # code
def btn_bind(e):
    btn.config(bg='#ef5350')
def btn_leave(e):
    btn.config(bg='#f0f4c3')
#################################
def bxes(e):
    lac.config(relief="solid")
def bxes_l(e):
    lac.config(relief="flat")
def bxes1(e):
    lac3.config(relief="solid")
def bxes_l1(e):
    lac3.config(relief="flat")
def bxes2(e):
    lac4.config(relief="solid")
def bxes_l2(e):
    lac4.config(relief="flat")
def show_button():
    frame_principal.grid_forget()
    fr3.grid_forget()
    fr.grid(row=0, column=1)
    root.config(bg="#5c6bc0")
def hide():
   
    fr.grid_forget()

def show2():
    frame_principal.grid_forget()
    fr.grid_forget()
    fr3.grid(row=0, column=1)
   


def overfl(e):
    but1.config(bg="#ef5350")
def overfl_leave(e):
    but1.config(bg="#5c6bc0")
def overfl2(e):
    but_2.config(bg="#ef5350")
def overfl_leave2(e):
    but_2.config(bg="#4db6ac")
def overfl3(e):
        but_3.config(bg="#ef5350")
def overfl_leave3(e):
    but_3.config(bg="#ff8a65")
def overfl4(e):
    but_4.config(bg="#ef5350")
def overfl_leave4(e):
    but_4.config(bg="#f48fb1")

def show_principal(e):
    fr.grid_forget()
    fr3.grid_forget()
    frame_principal.grid(row=0, column=1, sticky='n')
    
def bpenter(e):
    btn_principal.config(bg="#ef5350")
def bpleave(e):
    btn_principal.config(bg="#bdbdbd")

def scan():
    with open("proj/ip.ini", 'a') as r:
        r.writelines(e.get())
    text.insert(INSERT, 'Scan en cours...\n')
    root.update()
    ns = nmap.PortScanner()
    print(ns.nmap_version())
    ns.scan(e.get(),'1-1024','-v')
    print(ns.scaninfo())
    a=ns.csv()
    b=(a.replace(';', ' '))
    text.insert(INSERT, b)
def entrer(e):
    scan()
##################################

fr = Frame(root, bg='white', bd=0)
fr2 = Frame(root, bg='white', relief=RAISED, bd=0)
fr2.grid(row=0, column=0, sticky='n')
fr3 = Frame(root, bg='white', bd=2, relief=RAISED)

lbl = Label(fr, text='transparence : ', bg='white', font=('Helvetica 10 bold'))
lbl.grid(row=1, column=0, padx=10, pady=10)

w = Spinbox(fr, from_=0, to=10, bg='white', font=('Helvetica 10 bold'))
w.grid(row=1, column=1, pady=10)
frame_principal = Frame(root, bg="#bdbdbd")
frame_principal.grid(column=1, row=0, sticky="n")
# row length 

#fr.grid_rowconfigure(2, weight=0)

btn = Button(fr, text= 'appliquer', command=lambda:[get()], font=('Helvetica 10 bold'), relief=FLAT)
btn.grid(row=1, column=2, padx=10, pady=10)

bq = Button(fr, text="Quitter", font=("Helvetica 10 bold"), relief=FLAT, fg='red', command=lambda:[dim(0.95), wait(), dim(0.90), wait(), dim(0.85), wait(), dim(0.80), wait(), dim(0.75), wait(), dim(0.70), wait(), dim(0.65), wait(), dim(0.60), wait(), dim(0.55), wait(), dim(0.50), wait(), dim(0.45), wait(), dim(0.40), wait(), dim(0.35), wait(), dim(0.30), wait(), dim(0.25), wait(), dim(0.20), wait(), dim(0.15), wait(), dim(0.10), wait(), dim(0.5), wait(), dim(0), ferm()])
bq.grid(row=4, column=2)
root.bind("<Enter>", show)

lbl2 = Label(fr, text="Thémes : ", font=("Helvetica 10 bold"), bg="white")
lbl2.grid(column=0, row=2, sticky='w', padx=13)
btn.bind("<Enter>", btn_bind)
btn.bind("<Leave>", btn_leave)

#colors####################################
myfr = Frame(fr)
myfr.grid(column=1, row=2, )

lac = Label(myfr, text="    ", bg='yellow')
lac.grid(column=0, row=0, sticky='w', pady=5, padx=5)

lac1 = Label(myfr, text="    ", bg='#263238')
lac1.grid(column=1, row=0, sticky='w', pady=5, padx=5)

lac3 = Label(myfr, text="    ", bg='grey')
lac3.grid(column=2, row=0, sticky='w', pady=5, padx=5)

lac4 = Label(myfr, text="    ", bg='white')
lac4.grid(column=3, row=0, sticky='w', pady=5, padx=5)

##################################################""
lac.bind("<Enter>", bxes)
lac.bind("<Leave>", bxes_l)
lac3.bind("<Enter>", bxes1)
lac3.bind("<Leave>", bxes_l1)
lac4.bind("<Enter>", bxes2)
lac4.bind("<Leave>", bxes_l2)

lac.bind("<Button-1>", jaune)
lac1.bind("<Button-1>", rouge)
lac3.bind('<Button-1>', gris)
lac4.bind('<Button-1>', blanc)

#img = ImageTk.PhotoImage(Image.open("C:/Users/Tijan/Desktop/Text-file-to-handwritten-pdf-file-master/Text-file-to-handwritten-pdf-file-master/my3.ico"))
#ytb = Label(fr, image=img, height=50, width=50)
#ytb.grid(row=7, column=0)
lbb = Label(root, text='cacher')
btn_principal = Button(fr2, text="General", font=('Helvetica'), relief=FLAT, bg='#bdbdbd', width=10, height=4)
btn_principal.grid(row=0, column=0, sticky='n')
#butttons
but1 = Button(fr2, text="🛠\n Réglages", command=show_button, font=('Arial'), relief=FLAT, bg='#5c6bc0', height=4, width=10)
but1.grid(row=1, column=0, sticky='n')
but_2 = Button(fr2, text='🔑', relief=FLAT, font=('Helvetica'), bg='#4db6ac', command=show2, width=10, height=4)
but_2.grid(row=2, column=0, sticky='n')
but_3 = Button(fr2, text='🔊', relief=FLAT, font=('Helvetica'), bg='#ff8a65', command=show2, width=10, height=4)
but_3.grid(row=3, column=0, sticky='n')
but_4 = Button(fr2, text='🎲', relief=FLAT, font=('Helvetica'), bg='#f48fb1', command=show2, width=10, height=4)
but_4.grid(row=4, column=0, sticky='n')

btn_principal.bind("<Button-1>", show_principal)
btn_principal.bind("<Enter>", bpenter)
btn_principal.bind("<Leave>", bpleave)
but1.bind("<Enter>", overfl)
but1.bind("<Leave>", overfl_leave)
but_2.bind("<Enter>", overfl2)
but_2.bind("<Leave>", overfl_leave2)
but_3.bind("<Enter>", overfl3)
but_3.bind("<Leave>", overfl_leave3)
but_4.bind("<Enter>", overfl4)
but_4.bind("<Leave>", overfl_leave4)
l = Label(frame_principal, text="Adresse IP : ", font=('Helvetica 10 bold'))
l.grid(column=0, row=0,sticky='n', pady=10, padx=10)
e = Entry(frame_principal, width=20, font=("Cambria 12 bold"))
e.grid(column=1, row=0, sticky='n', pady=10)
b = Button(frame_principal, text="Scanner", font=('Helvetica 10 bold'), relief=FLAT, command=scan)
b.grid(row=0, column=2, sticky='n', pady=10, padx=10)
butto = Button(frame_principal, text='reduire', command=root.iconify)

text = Text(frame_principal, height=50, width=53,  wrap=WORD, font=('Helvetica 11 bold'), fg='#4caf50', bg='black')
text.grid(row=1, column=0, columnspan=4)
e.bind("<Return>", entrer)

root.mainloop()