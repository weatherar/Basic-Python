#GUI -> graphical user interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

#INIT 
window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("Sapa Dia!")

#frame input
input_frame = ttk.Frame(window)
#penempatan Grid, Pack, Place
input_frame.pack(padx=10,fill="x",expand=True)

#variabel dan fungsi 
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_click():
    print(NAMA_BELAKANG.get())
    pesan = f"halo {NAMA_DEPAN.get()}{NAMA_BELAKANG.get()}, ganteng"
    showinfo(title="whazapp!",message=pesan)
    
#komponen-komponen
#1. label untuk nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan")
nama_depan_label.pack()

#2. entry nama depan
nama_depan_entry = ttk.Entry(input_frame,textvariable = NAMA_DEPAN)
nama_depan_entry.pack(padx=10,fill="x",expand=True)

#3. label untuk nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Belakang")
nama_depan_label.pack()

#4. entry nama belakang
nama_belakang_entry= ttk.Entry(input_frame,textvariable = NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,fill="x",expand=True)

#5. Tombol click
tombol_sapa = ttk.Button(input_frame, text="sapa!", command=tombol_click )
tombol_sapa.pack(fill = 'x', expand=True,padx =10, pady =10)

#main loop window
window.mainloop()