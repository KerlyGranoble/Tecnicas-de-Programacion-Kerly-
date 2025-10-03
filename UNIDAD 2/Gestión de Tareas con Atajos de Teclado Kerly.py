import tkinter as tk
from tkinter import messagebox

# FUNCIONES DE LA APLICACIÓN 

def agregar_tarea(event=None):
    """Función para AGREGAR una tarea nueva"""
    tarea = entrada.get()  # Obtener el texto escrito de la caja de entrada
    if tarea.strip():  # Verifica que la casilla no esté vacía
        lista_tareas.insert(tk.END, tarea)  # Agrega la tarea al final de la lista
        entrada.delete(0, tk.END)  # Limpia la caja de texto
    else:
        messagebox.showwarning("Aviso", "No escribiste nada")

def completar_tarea(event=None):
    """Función para MARCAR una tarea como COMPLETADA"""
    seleccion = lista_tareas.curselection()  # Ver qué tarea está seleccionada
    if seleccion:  # Si hay algo seleccionado
        indice = seleccion[0]
        tarea = lista_tareas.get(indice)

        # Si la tarea ya está completada, no hacer nada
        if tarea.startswith("✔ "):
            messagebox.showinfo("Info", "Esta tarea ya está completada")
        else:
            lista_tareas.delete(indice)  # Borra la tarea antigua
            lista_tareas.insert(indice, "✔ " + tarea)  # Agrega con marca
    else:
        messagebox.showwarning("Aviso", "Primero selecciona una tarea")

def eliminar_tarea(event=None):
    """Función para ELIMINAR una tarea"""
    seleccion = lista_tareas.curselection()
    if seleccion:
        lista_tareas.delete(seleccion[0])
    else:
        messagebox.showwarning("Aviso", "Primero selecciona una tarea")

def cerrar_app(event=None):
    """Función para cerrar la aplicación con la tecla scape"""
    root.destroy()

# INTERFAZ GRÁFICA 
root = tk.Tk()
root.title("Gestor de Tareas con Atajos")
root.geometry("400x400")

# Campo de entrada 
entrada = tk.Entry(root, width=30, font=("Arial", 12))
entrada.pack(pady=10)

# Botones 
frame_botones = tk.Frame(root)
frame_botones.pack()

btn_agregar = tk.Button(frame_botones, text="Agregar", command=agregar_tarea)
btn_agregar.grid(row=0, column=0, padx=5)

btn_completar = tk.Button(frame_botones, text="Completar", command=completar_tarea)
btn_completar.grid(row=0, column=1, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar", command=eliminar_tarea)
btn_eliminar.grid(row=0, column=2, padx=5)

# Lista de tareas 
lista_tareas = tk.Listbox(root, width=40, height=15, font=("Arial", 12))
lista_tareas.pack(pady=10)

# Atajos de Teclado 
root.bind("<Return>", agregar_tarea)    # Enter para agregar tarea
root.bind("<c>", completar_tarea)       # C para completar
root.bind("<C>", completar_tarea)       # Mayúscula C también sirve para completar
root.bind("<Delete>", eliminar_tarea)   # Supr para eliminar
root.bind("<d>", eliminar_tarea)        # d para eliminar
root.bind("<D>", eliminar_tarea)        # D también sirve ra eliminar
root.bind("<Escape>", cerrar_app)       # Scape para salir

# Ejecutar aplicación 
root.mainloop()

