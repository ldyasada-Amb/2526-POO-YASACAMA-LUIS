import tkinter as tk
from tkinter import messagebox
import os

class TodoApp: # Clase principal de la aplicación
    def __init__(self, root, archivo="tareas.txt"):
        self.root = root
        self.root.title("Lista de Tareas")
        self.archivo = archivo

        # Lista interna de tareas
        self.tareas = []

        # Cargar tareas desde archivo
        self.cargar_tareas()

        # Campo de entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.agregar_tarea_evento)

        # Botones
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        self.btn_add = tk.Button(btn_frame, text="Añadir Tarea", command=self.agregar_tarea)
        self.btn_add.grid(row=0, column=0, padx=5)

        self.btn_complete = tk.Button(btn_frame, text="Marcar como Completada", command=self.marcar_completada)
        self.btn_complete.grid(row=0, column=1, padx=5)

        self.btn_delete = tk.Button(btn_frame, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.btn_delete.grid(row=0, column=2, padx=5)

        # Listbox para mostrar tareas
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)
        self.listbox.bind("<Double-Button-1>", self.marcar_completada_evento)

        # Mostrar tareas cargadas
        self.actualizar_lista()

    # Métodos de la lógica
    def agregar_tarea_evento(self, event): # Método para manejar el evento de presionar Enter
        self.agregar_tarea()

    def agregar_tarea(self):
        tarea = self.entry.get().strip()
        if tarea:
            self.tareas.append({"texto": tarea, "completada": False})
            self.actualizar_lista()
            self.entry.delete(0, tk.END)
            self.guardar_tareas()
        else:
            messagebox.showwarning("Aviso", "No puedes añadir una tarea vacía.")

    def marcar_completada_evento(self, event): # Método para manejar el evento de doble clic en una tarea
        self.marcar_completada()

    def marcar_completada(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            index = seleccion[0]
            self.tareas[index]["completada"] = not self.tareas[index]["completada"]
            self.actualizar_lista()
            self.guardar_tareas()
        else:
            messagebox.showwarning("Aviso", "Selecciona una tarea para marcarla.")

    def eliminar_tarea(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            index = seleccion[0]
            del self.tareas[index]
            self.actualizar_lista()
            self.guardar_tareas()
        else:
            messagebox.showwarning("Aviso", "Selecciona una tarea para eliminarla.")

    def actualizar_lista(self): # Método para actualizar el Listbox con las tareas actuales
        self.listbox.delete(0, tk.END)
        for tarea in self.tareas:
            texto = tarea["texto"]
            if tarea["completada"]:
                texto += " ✔"
            self.listbox.insert(tk.END, texto)

    # Persistencia en archivo
    def guardar_tareas(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            for tarea in self.tareas:
                estado = "1" if tarea["completada"] else "0"
                f.write(f"{tarea['texto']}|{estado}\n")

    def cargar_tareas(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    texto, estado = linea.strip().split("|")
                    self.tareas.append({"texto": texto, "completada": estado == "1"})


if __name__ == "__main__": # Punto de entrada de la aplicación
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
