import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Biblioteca Personal")
ventana.geometry("800x600")
ventana.configure(bg="#181818")

# BLOQUE IZQUIERDO
bloque_izquierdo = tk.Frame(ventana, bg="#1f1f1f", width=300, bd=1, highlightbackground="#2b2b2b", highlightthickness=1)
bloque_izquierdo.pack(side="left", fill="y", padx=6, pady=6)
bloque_izquierdo.pack_propagate(False)
imagen_logo = tk.PhotoImage(file=r"dfdsf\BIBLIOTECA_PERSONAL\logo-mibi.png").subsample(4, 4)
logo = tk.Label(bloque_izquierdo, image=imagen_logo, bg="#1f1f1f")
logo.pack(side="left", anchor="n", pady=10, padx=10)



ventana.mainloop()