import tkinter as tk # Importamos la biblioteca tkinter para crear la interfaz gráfica
from tkinter import ttk, messagebox # Importamos ttk para usar widgets más modernos y messagebox para mostrar mensajes de alerta

class Evento:
    """Clase que representa un evento con fecha, hora y descripción"""
    def __init__(self, fecha, hora, descripcion):
        self.fecha = fecha
        self.hora = hora
        self.descripcion = descripcion

class AgendaApp:
    """Clase principal de la aplicación Agenda"""
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda de Eventos")
        self.root.geometry("600x400")

        self.eventos = []

        # --- Lista de eventos ---
        frame_lista = ttk.Frame(root) # Creamos un frame para contener la lista de eventos
        frame_lista.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(fill="both", expand=True)

        # --- Entradas ---
        frame_entradas = ttk.Frame(root) # Creamos un frame para contener las entradas de fecha, hora y descripción
        frame_entradas.pack(fill="x", padx=10, pady=5)

        ttk.Label(frame_entradas, text="Fecha (dd/mm/aaaa):").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = ttk.Entry(frame_entradas, width=12)
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_entradas, text="Hora (HH:MM):").grid(row=0, column=2, padx=5, pady=5)
        self.hora_entry = ttk.Entry(frame_entradas, width=10)
        self.hora_entry.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(frame_entradas, text="Descripción:").grid(row=0, column=4, padx=5, pady=5)
        self.desc_entry = ttk.Entry(frame_entradas, width=25)
        self.desc_entry.grid(row=0, column=5, padx=5, pady=5)

        # --- Botones ---
        frame_botones = ttk.Frame(root) # Creamos un frame para contener los botones de agregar, eliminar y salir
        frame_botones.pack(fill="x", padx=10, pady=10)

        ttk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Salir", command=root.quit).pack(side="right", padx=5)

    def agregar_evento(self): # Función para agregar un evento a la lista y mostrarlo en el Treeview
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        desc = self.desc_entry.get()

        if not fecha or not hora or not desc:
            messagebox.showwarning("Campos incompletos", "Por favor ingrese fecha, hora y descripción.")
            return

        evento = Evento(fecha, hora, desc)
        self.eventos.append(evento)

        self.tree.insert("", "end", values=(evento.fecha, evento.hora, evento.descripcion))
        self.fecha_entry.delete(0, tk.END)
        self.hora_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Selección vacía", "Seleccione un evento para eliminar.")
            return

        confirmar = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de eliminar el evento seleccionado?")
        if confirmar:
            self.tree.delete(seleccionado)

# --- Ejecutar aplicación ---
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
