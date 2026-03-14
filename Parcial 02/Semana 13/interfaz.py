import tkinter as tk
from tkinter import messagebox

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Información")
ventana.geometry("400x300")

# Etiqueta
label = tk.Label(ventana, text="Ingrese un dato:")
label.pack(pady=5)

# Campo de texto
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

# Lista para mostrar datos
lista = tk.Listbox(ventana, width=40, height=10)
lista.pack(pady=10)

# Función para agregar datos
def agregar_dato():
    dato = entrada.get()
    if dato.strip():  # Verifica que no esté vacío
        lista.insert(tk.END, dato)
        entrada.delete(0, tk.END)  # Limpia el campo de texto
    else:
        messagebox.showwarning("Advertencia", "Debe ingresar un dato válido.")

# Función para limpiar datos
def limpiar_dato():
    seleccion = lista.curselection()
    if seleccion:  # Si hay un elemento seleccionado
        lista.delete(seleccion)
    else:  # Si no hay selección, limpia toda la lista
        lista.delete(0, tk.END)

# Botones
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_dato)
boton_limpiar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
