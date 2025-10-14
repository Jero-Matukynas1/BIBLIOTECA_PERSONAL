import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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

# BLOQUE CENTRAL
bloque_central = tk.Frame(
    ventana,
    bg="#222222",
    width=900,
    height=800,
    bd=1,
    highlightbackground="#2b2b2b",
    highlightthickness=1
)
bloque_central.pack(side="left", fill="both", padx=6, pady=6)
bloque_central.pack_propagate(False)

#título dentro del bloque central
titulo_libros = tk.Label(
    bloque_central,
    text="Mis Libros",
    font=("Segoe UI", 16, "bold"),
    bg="#222222",
    fg="white"
)
titulo_libros.pack(pady=20)


# Frame que contendrá la grilla
grilla_libros = tk.Frame(bloque_central, bg="#222222")
grilla_libros.pack(fill="both", expand=True, padx=10, pady=10)

#array libros
libros = [
    ("El Principito", "Antoine de Saint-Exupéry"),
    ("1984", "George Orwell"),
    ("Cien Años de Soledad", "Gabriel García Márquez"),
    ("Harry Potter", "J.K. Rowling"),
    ("Don Quijote", "Miguel de Cervantes"),
    ("Fahrenheit 451", "Ray Bradbury"),
    ("Moby Dick", "Herman Melville"),
    ("La Odisea", "Homero"),
    ("Los Juegos del Hambre", "Suzanne Collins"),
]

# Crear la grilla
columnas = 3
for i, (titulo, autor) in enumerate(libros):
    fila = i // columnas
    columna = i % columnas

    # Cada libro es un Frame pequeño
    frame_libro = tk.Frame(
        grilla_libros,
        bg="#2a2a2a",
        width=180,
        height=140,
        highlightbackground="#3a3a3a",
        highlightthickness=1
    )
    frame_libro.grid(row=fila, column=columna, padx=10, pady=10, sticky="nsew")
    frame_libro.grid_propagate(False)  # evita que el frame cambie de tamaño según su contenido

    # Etiquetas dentro del frame del libro
    # Agregar Imagen de libro en text="libro" para mejor apariencia!!!
    tk.Label(frame_libro, text="Libro:", font=("Arial", 26), bg="#2a2a2a").pack(pady=(8, 2))
    tk.Label(frame_libro, text=titulo, fg="white", bg="#2a2a2a", font=("Segoe UI", 10, "bold")).pack()
    tk.Label(frame_libro, text=autor, fg="#bbbbbb", bg="#2a2a2a", font=("Segoe UI", 9)).pack()

# grilla se expandan proporcionalmente
for c in range(columnas):
    grilla_libros.grid_columnconfigure(c, weight=1)

def rebuild_grid():
    # vacía la grilla actual
    for widget in grilla_libros.winfo_children():
        widget.destroy()

    # reconstruye la grilla con los libros actuales
    for i, (titulo, autor) in enumerate(libros):
        fila = i // columnas
        columna = i % columnas

        frame_libro = tk.Frame(
            grilla_libros,
            bg="#2a2a2a",
            width=180,
            height=140,
            highlightbackground="#3a3a3a",
            highlightthickness=1
        )
        frame_libro.grid(row=fila, column=columna, padx=10, pady=10, sticky="nsew")
        frame_libro.grid_propagate(False)

        tk.Label(frame_libro, text="Libro:", font=("Arial", 26), bg="#2a2a2a").pack(pady=(8, 2))
        tk.Label(frame_libro, text=titulo, fg="white", bg="#2a2a2a", font=("Segoe UI", 10, "bold")).pack()
        tk.Label(frame_libro, text=autor, fg="#bbbbbb", bg="#2a2a2a", font=("Segoe UI", 9)).pack()


# BLOQUE DERECHO
bloque_derecho = tk.Frame(
    ventana,
    bg="#1f1f1f",
    width=120,
    bd=1,
    highlightbackground="#2b2b2b",
    highlightthickness=1
)
bloque_derecho.pack(side="right", fill="y", padx=6, pady=6)
bloque_derecho.pack_propagate(False)

titulo_acciones = tk.Label(
    bloque_derecho,
    text="Acciones",
    font=("Segoe UI", 12, "bold"),
    bg="#1f1f1f",
    fg="white"
)
titulo_acciones.pack(pady=20)

def agregar_libro():
    # boton guardar y funcionamiento
    def guardar_libro():
        titulo = entrada_titulo.get().strip()
        autor = entrada_autor.get().strip()
        if not titulo or not autor:
         messagebox.showwarning("Campos Vacíos", "Debe agregar título y autor.")
         return
        
        libros.append((titulo, autor))
        rebuild_grid()
        ventana_agregat.destroy()

    ventana_agregat = tk.Toplevel()
    ventana_agregat.title("Agregar Un Nuevo Libro")
    ventana_agregat.geometry("300x200")
    
    tk.Label(ventana_agregat, text="Titulo:").pack(pady=5)
    entrada_titulo = tk.Entry(ventana_agregat)
    entrada_titulo.pack(pady=5, fill="x", padx=10)

    tk.Label(ventana_agregat, text="Autor:").pack(pady=5)
    entrada_autor = tk.Entry(ventana_agregat)
    entrada_autor.pack(pady=5,fill="x",padx=10)
    boton_guardar = tk.Button(ventana_agregat, text="Guardar",command=guardar_libro)
    boton_guardar.pack(pady=10)

# Boton + && eliminar
btn_agregar = tk.Button(
    bloque_derecho,
    text="Agregar",
    font=("Segoe UI", 10, "bold"),
    bg="#2d2d2d",
    fg="white",
    activebackground="#3d3d3d",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command= agregar_libro
    
)
btn_agregar.pack(pady=10, ipadx=10, ipady=5)

btn_eliminar = tk.Button(
    bloque_derecho,
    text="Eliminar",
    font=("Segoe UI", 10, "bold"),
    bg="#2d2d2d",
    fg="white",
    activebackground="#3d3d3d",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)
btn_eliminar.pack(pady=10, ipadx=10, ipady=5)

ventana.mainloop()

