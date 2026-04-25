import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Programa para subir a repositorio")
ventana.geometry("500x300")  # tamaño de la ventana
ventana.configure(bg="#1e1e1e")  # fondo oscuro elegante

# Crear etiqueta con tipografía grande y colores llamativos, centrada
etiqueta = tk.Label(
    ventana,
    text="Este programa es de Diego y Christian",
    font=("Arial", 18, "bold"),  # fuente grande y negrita
    fg="#ff5733",  # color del texto
    bg="#1e1e1e",  # mismo color que el fondo
    anchor="center"  # alinear el texto al centro
)
etiqueta.pack(expand=True, fill='both')  # expandirse y llenar la ventana

# Ejecutar la ventana
ventana.mainloop()