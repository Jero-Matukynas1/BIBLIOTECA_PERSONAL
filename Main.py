
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


root = tk.Tk()
root.title("Biblioteca Personal")
root.geometry("900x500")
root.config(bg="#1a1a1a")


style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#1a1a1a")
style.configure("TLabel", background="#1a1a1a", foreground="white")
style.configure("TButton", background="#333333", foreground="white", padding=6, relief="flat")
style.map("TButton",
          background=[("active", "#555555")],
          relief=[("pressed", "flat")])


frame_left = ttk.Frame(root, width=180)
frame_left.pack(side="left", fill="y")
label_biblio = ttk.Label(frame_left, text="BIBLIOTECA PERSONAL", font=("Segoe UI", 10, "bold"), foreground="#888888")
label_biblio.pack(pady=10)

listbox_biblio = tk.Listbox(frame_left, bg="#2a2a2a", fg="white", selectbackground="#555555", border=0)
listbox_biblio.pack(fill="both", expand=True, padx=10, pady=5)


frame_center = ttk.Frame(root)
frame_center.pack(side="left", fill="both", expand=True, padx=5, pady=5)

label_archivos = ttk.Label(frame_center, text="ARCHIVOS DE BIBLIOTECA (LIBRO)", font=("Segoe UI", 10, "bold"))
label_archivos.pack(pady=10)

listbox_archivos = tk.Listbox(frame_center, bg="#2a2a2a", fg="white", selectbackground="#555555", border=0)
listbox_archivos.pack(fill="both", expand=True, padx=20, pady=5)


frame_right = ttk.Frame(root, width=80)
frame_right.pack(side="right", fill="y", padx=10, pady=10)

def agregar_libro():
    nombre = "Nuevo libro"
    listbox_biblio.insert(tk.END, nombre)
    messagebox.showinfo("Agregar", f"Se agregó '{nombre}' a la biblioteca.")

def eliminar_libro():
    seleccion = listbox_biblio.curselection()
    if not seleccion:
        messagebox.showwarning("Eliminar", "Selecciona un libro para eliminar.")
        return
    listbox_biblio.delete(seleccion)
    messagebox.showinfo("Eliminar", "Libro eliminado.")

btn_agregar = ttk.Button(frame_right, text="+", command=agregar_libro, width=4)
btn_agregar.pack(pady=10)

btn_eliminar = ttk.Button(frame_right, text="🗑", command=eliminar_libro, width=4)
btn_eliminar.pack(pady=10)


frame_bottom = ttk.Frame(root)
frame_bottom.pack(side="bottom", fill="x", pady=10)

entry_buscar = ttk.Entry(frame_bottom, font=("Segoe UI", 10))
entry_buscar.pack(fill="x", padx=100, pady=5)
entry_buscar.insert(0, "Buscar libro...")

root.mainloop()

