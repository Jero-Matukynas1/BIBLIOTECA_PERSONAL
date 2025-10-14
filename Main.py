import tkinter as tk
from tkinter import ttk, messagebox, Toplevel

# Configuración inicial
ventana = tk.Tk()
ventana.title("Mi Biblioteca Personal")
ventana.geometry("1200x600")
ventana.minsize(1200, 600)
ventana.configure(bg="#15171e")

# Lista para almacenar libros
libros = []

# FUNCIONES 
def modificar_libro():
    print("Función de modificar libro no implementada aún.")

def eliminar_libro():
    seleccion = categoria.selection()
    
    if not seleccion:
        messagebox.showwarning("Advertencia", "Selecciona un libro para eliminar")
        return
    
    item = seleccion[0]

    confirmacion = messagebox.askyesno("Desea eliminar el libro?", "Esta acción no se puede deshacer.")
    
    if confirmacion:
        categoria.delete(item)
        del libros[categoria.index(item)]
        
        actualizar_tabla()

def actualizar_tabla():
    for item in categoria.get_children():
        categoria.delete(item)

    for libro in libros:
        categoria.insert("", "end", values=(libro['titulo'], libro['autor'], libro['año'], libro['genero']))

    barra_inf.config(text=f"Mostrando {len(categoria.get_children())} libro(s). Total: {len(libros)}.")

def abrir_ventana_agregar(): 
        ventana_agregar = Toplevel(ventana)
        ventana_agregar.title("Agregar Libro")
        ventana_agregar.geometry("400x300")
        ventana_agregar.configure(bg="#15171e")

        etiquetas = ["Título:", "Autor:", "Año:", "Género:"]
        entradas = []

        for i in range(len(etiquetas)):  
            etiqueta = tk.Label(ventana_agregar, text=etiquetas[i], bg="#15171e", fg="white", font=("Arial", 12))
            etiqueta.grid(row=i, column=0, padx=10, pady=10, sticky="e")  
            entrada = tk.Entry(ventana_agregar, width=30, bg="#252A36", fg="white", font=("Arial", 12), bd=0)
            entrada.grid(row=i, column=1, padx=10, pady=10)
            entradas.append(entrada)
            
        def validar_entradas(entradas=entradas):
            titulo = entradas[0].get().strip()
            autor = entradas[1].get().strip()
            anio = entradas[2].get().strip()
            genero = entradas[3].get().strip()

            if titulo and autor and anio and genero:
                if not anio.isdigit() and not (0 < int(anio) < 2025):
                    messagebox.showwarning("Año inválido", "Por favor, ingrese un año válido.")
                    return
                else:print("Libro agregado:", titulo, autor, anio, genero)
                libros.append({"titulo": titulo, "autor": autor, "año": anio, "genero": genero})
                actualizar_tabla()
                ventana_agregar.destroy()
            else:
                messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos.")
            

        boton_aceptar = tk.Button(ventana_agregar, text="Aceptar", bg="#252A36", fg="white", font=("Arial", 12), command=validar_entradas)
        boton_aceptar.grid(row=len(etiquetas), column=1, padx=10, pady=20, sticky="e")

        boton_cancelar = tk.Button(ventana_agregar, text="Cancelar", bg="#252A36", fg="white", font=("Arial", 12), command=ventana_agregar.destroy)
        boton_cancelar.grid(row=len(etiquetas), column=1, padx=10, pady=20, sticky="w")

def mostrar_todos_libros():
    actualizar_tabla()
    entry_buscar.delete(0, tk.END)
    autor_combobox.set('')
    año_combobox.set('')
    genero_combobox.set('')


# BLOQUE IZQUIERDO
bloque_izquierdo = tk.Frame(ventana, bg="#1b1e27", width=300, bd=1, highlightbackground="#2b2b2b", highlightthickness=1)
bloque_izquierdo.pack(side="left", fill="y", padx=5, pady=5)
bloque_izquierdo.pack_propagate(False)

imagen_logo = tk.PhotoImage(file="BIBLIOTECA_PERSONAL\logo-mibi.png").subsample(4, 4)
logo = tk.Label(bloque_izquierdo, image=imagen_logo, bg="#1b1e27")
logo.image = imagen_logo
logo.pack(side="bottom", anchor="n", pady=10, padx=10)

# BOTONES (TIRA LATERAL)
botones_frame = tk.Frame(bloque_izquierdo, bg="#1b1e27")
botones_frame.pack(side="top", fill="x", padx=10, pady=20)

# CONTENIDO PRINCIPAL
contenido_principal = tk.Frame(ventana, bg="#15171e")
contenido_principal.pack(side="top", fill="both", expand=True, padx=5, pady=5)

# BARRA SUPERIOR CON BÚSQUEDA
barra_superior = tk.Frame(contenido_principal, bg="#1b1e27", height=80)
barra_superior.pack(side="top", fill="x", padx=5, pady=5)
barra_superior.pack_propagate(False)

# BUSCADOR
busqueda_frame = tk.Frame(barra_superior, bg="#1b1e27")
busqueda_frame.pack(side="right", padx=15, pady=10)

label_buscar = tk.Label(busqueda_frame, text="BUSCAR:", bg="#1b1e27", fg="white",font=("Arial", 13, "bold"))
label_buscar.pack(side="left", padx=(0, 5))

entry_buscar = tk.Entry(busqueda_frame, width=20, bg="#252A36", fg="white",font=("Arial", 13), bd=0)
entry_buscar.pack(side="left", padx=5)

# FILTROS DE BÚSQUEDA
filtros_frame = tk.Frame(barra_superior, bg="#1b1e27")
filtros_frame.pack(side="left", padx=20, pady=10)

    # Autor
lbl_autor = tk.Label(filtros_frame, text="Autor:", bg="#1b1e27", fg="white", font=("Arial", 13, "bold"))
lbl_autor.pack(side="left", padx=(0, 5))

autor_combobox = ttk.Combobox(filtros_frame, values=[], width=12, state="readonly")
autor_combobox.pack(side="left", padx=5)

    # Año
lbl_anio = tk.Label(filtros_frame, text="Año:", bg="#1b1e27", fg="white",font=("Arial", 13, "bold"))
lbl_anio.pack(side="left", padx=(10, 5))

año_combobox = ttk.Combobox(filtros_frame, values=[], width=8, state="readonly")
año_combobox.pack(side="left", padx=5)

    # Género
lbl_genero = tk.Label(filtros_frame, text="Género:", bg="#1b1e27", fg="white",font=("Arial", 13, "bold"))
lbl_genero.pack(side="left", padx=(10, 5))

genero_combobox = ttk.Combobox(filtros_frame, values=[], width=12, state="readonly")
genero_combobox.pack(side="left", padx=5)

# LISTA DE LIBROS
lista_frame = tk.Frame(contenido_principal, bg="#1b1e27")
lista_frame.pack(side="top", fill="both", expand=True, padx=5, pady=5)
estilo = ttk.Style()
estilo.theme_use('default')
estilo.configure("Treeview", background="#252A36", foreground="white",fieldbackground="#252A36",  borderwidth=0, font=("Arial", 11))
estilo.configure("Treeview.Heading",background="#1b1e27",foreground="white",borderwidth=0,font=("Arial", 11, "bold"))

# Columnas libros
columnas = ("titulo", "autor", "año", "genero")
categoria = ttk.Treeview(lista_frame, columns=columnas, show="headings", height=15)

categoria.heading("titulo", text="Título")
categoria.heading("autor", text="Autor")
categoria.heading("año", text="Año")
categoria.heading("genero", text="Género")

categoria.column("titulo", width=250)
categoria.column("autor", width=150)
categoria.column("año", width=80)
categoria.column("genero", width=120)

# BARRA SCROLL
scrollbar = tk.Scrollbar(lista_frame, orient="vertical", command=categoria.yview)               
categoria.configure(yscrollcommand=scrollbar.set)

categoria.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# BARRA INFERIOR
barra_inf = tk.Label(contenido_principal, text="Mostrando 0 libro(s). Total: 0.", bg="#1b1e27", fg="white", font=("Arial", 10))
barra_inf.pack(side="bottom", fill="x", padx=5, pady=5)

# BOTONES
boton_agregar = tk.Button(bloque_izquierdo, text="+ AGREGAR", bg="#252A36",height=5,bd=0, fg="white",font=("Arial", 12, "bold"), command=abrir_ventana_agregar)
boton_agregar.pack( fill="x",pady=5,padx=5)
boton_agregar.pack_propagate(False)

boton_eliminar = tk.Button(bloque_izquierdo, text="- ELIMINAR", bg="#252A36",height=5,bd=0, fg="white",font=("Arial", 12, "bold"), command=eliminar_libro)
boton_eliminar.pack( fill="x",pady=5,padx=5)
boton_eliminar.pack_propagate(False)

boton_editar= tk.Button(bloque_izquierdo, text="✐ EDITAR", bg="#252A36",height=5,bd=0, fg="white",font=("Arial", 12, "bold"), command=modificar_libro)
boton_editar.pack( fill="x",pady=5,padx=5)
boton_editar.pack_propagate(False)

boton_mostrar_todo = tk.Button(bloque_izquierdo, text="LIMPIAR FILTROS", bg="#252A36",height=5,bd=0,fg="white",font=("Arial", 12, "bold"), command=mostrar_todos_libros)
boton_mostrar_todo.pack( fill="x",pady=5,padx=5)
boton_mostrar_todo.pack_propagate(False)

ventana.mainloop()