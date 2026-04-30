import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow
import os

# -------------------------
# FUNCIONES
# -------------------------
def abrir_registro_productos():
    messagebox.showinfo("Registro de Productos", "Aquí irá el módulo de registro de productos.")

def abrir_registro_ventas():
    messagebox.showinfo("Registro de Ventas", "Aquí irá el módulo de registro de ventas.")

def abrir_reportes():
    messagebox.showinfo("Reportes", "Aquí irá el módulo de reportes.")

def abrir_acerca_de():
    messagebox.showinfo("Acerca de", "Punto de Venta de Ropa\nProyecto Escolar\nVersión 1.0")


# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("Punto de Venta - NOMBREPROYECTO")
ventana.geometry("500x600")
ventana.resizable(False, False)


# -------------------------
# LOGO
# -------------------------
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    imagen = Image.open(os.path.join(BASE_DIR, "logo.png"))
    imagen = imagen.resize((250, 250))
    img_logo = ImageTk.PhotoImage(imagen)
    lbl_logo = tk.Label(ventana, image=img_logo)
    lbl_logo.pack(pady=20)
except:
    lbl_sin_logo = tk.Label(ventana, text="(Aquí va el logo del sistema)", font=("Arial", 14))
    lbl_sin_logo.pack(pady=40)


# -------------------------
# ESTILO DE BOTONES
# -------------------------
# Se usa tk.Button en lugar de ttk.Button para poder personalizar colores
FUENTE_BOTON = ("Arial", 12, "italic")   # Tamaño 12, cursiva
COLOR_FONDO  = "black"
COLOR_LETRA  = "white"
ANCHO_BOTON  = 25   # Ancho uniforme en caracteres

btn_reg_prod = tk.Button(
    ventana,
    text="Registro de Productos",
    command=abrir_registro_productos,
    font=FUENTE_BOTON,
    bg=COLOR_FONDO,
    fg=COLOR_LETRA,
    activebackground="#FF8DC6",   # Color al hacer clic (gris oscuro)
    activeforeground="white",
    width=ANCHO_BOTON,
    pady=6,
    relief="flat",
    cursor="hand2"
)
btn_reg_prod.pack(pady=10)

btn_reg_ventas = tk.Button(
    ventana,
    text="Registro de Ventas",
    command=abrir_registro_ventas,
    font=FUENTE_BOTON,
    bg=COLOR_FONDO,
    fg=COLOR_LETRA,
    activebackground="#333333",
    activeforeground="white",
    width=ANCHO_BOTON,
    pady=6,
    relief="flat",
    cursor="hand2"
)
btn_reg_ventas.pack(pady=10)

btn_reportes = tk.Button(
    ventana,
    text="Reportes",
    command=abrir_reportes,
    font=FUENTE_BOTON,
    bg=COLOR_FONDO,
    fg=COLOR_LETRA,
    activebackground="#333333",
    activeforeground="white",
    width=ANCHO_BOTON,
    pady=6,
    relief="flat",
    cursor="hand2"
)
btn_reportes.pack(pady=10)

btn_acerca = tk.Button(
    ventana,
    text="Acerca de",
    command=abrir_acerca_de,
    font=FUENTE_BOTON,
    bg=COLOR_FONDO,
    fg=COLOR_LETRA,
    activebackground="#333333",
    activeforeground="white",
    width=ANCHO_BOTON,
    pady=6,
    relief="flat",
    cursor="hand2"
)
btn_acerca.pack(pady=10)


# -------------------------
# INICIO DE LA APP
# -------------------------
ventana.mainloop()
