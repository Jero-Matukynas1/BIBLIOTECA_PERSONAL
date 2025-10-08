import tkinter as tk
root = tk.Tk()
root.title("pack(): side + fill + expand")
root.geometry("560x420")
root.configure(bg="#e9e9e9")

# ---------- BLOQUE 1: side="top" (apila vertical) ----------
b1 = tk.LabelFrame(root, text='side="top"', bg="#f7f7f7")
b1.pack(fill="x", padx=10, pady=10)

# Sin fill: ocupa sólo lo que necesita
tk.Label(b1, text='TOP - sin fill', bg="#ffd6d6").pack(side="top", pady=4)

# fill="x": se estira a lo ancho
tk.Label(b1, text='TOP - fill="x"', bg="#d6ffd6").pack(side="top", fill="x", pady=4)

# fill="x" + ipady para notar altura
tk.Label(b1, text='TOP - fill="x" + ipady=10', bg="#d6e0ff").pack(side="top", fill="x", ipady=10, pady=4)

# ---------- BLOQUE 2: side="left" (apila horizontal) ----------
b2 = tk.LabelFrame(root, text='side="left"', bg="#f7f7f7")
b2.pack(fill="x", padx=10, pady=10, ipady=8)

# Sin fill: ancho según contenido
tk.Label(b2, text='LEFT', bg="#ffe0b3").pack(side="left", padx=5)

# fill="y": se estira a lo alto del contenedor b2
tk.Label(b2, text='LEFT fill="y"', bg="#b3e6ff").pack(side="left", fill="y", padx=5)

# fill="y" + ipady para exagerar
tk.Label(b2, text='LEFT fill="y" + ipady=15', bg="#e6b3ff").pack(side="left", fill="y", padx=5, ipady=15)

# ---------- BLOQUE 3: fill="both" + expand (ocupan espacio extra) ----------
b3 = tk.LabelFrame(root, text='fill="both" + expand', bg="#f7f7f7")
b3.pack(fill="both", expand=True, padx=10, pady=10)

# Tres paneles lado a lado que comparten el espacio libre
p1 = tk.Label(b3, text='A\n(side=left, fill=both, expand=1)', bg="#c6f7d0")
p1.pack(side="left", fill="both", expand=True, padx=5, pady=5)

p2 = tk.Label(b3, text='B\n(side=left, fill=both, expand=1)', bg="#fbd38d")
p2.pack(side="left", fill="both", expand=True, padx=5, pady=5)

# Este no expande: queda más chico aunque tenga fill
p3 = tk.Label(b3, text='C\n(fill=both, expand=0)', bg="#fbb6ce")
p3.pack(side="left", fill="both", expand=False, padx=5, pady=5)

root.mainloop()