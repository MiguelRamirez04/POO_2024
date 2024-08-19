import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
from tkinter import font as tkfont
from personas import Empleados, Clientes
from material import Material
from prestamo import Prestamo
from conexionBD import get_connection, get_cursor, mysql

sesion_empleado = None
sesion_cliente = None

root = tk.Tk()
root.title("Sistema de Préstamos de Biblioteca")
root.geometry("1000x800")
root.configure(bg='#5ea6cf')

def menu_principal():
    menu_frame = tk.Frame(root, bg='#5ea6cf')
    menu_frame.pack(pady=50)

    tk.Button(menu_frame, text="Registrar Cliente", command=log_cli, font=("Helvetica", 20)).pack(pady=20)
    tk.Button(menu_frame, text="Registrar Empleado", command=log_emp, font=("Helvetica", 20)).pack(pady=20)
    tk.Button(menu_frame, text="Login Empleados", command=iniciar_sesion_empleado, font=("Helvetica", 20)).pack(pady=20)
    tk.Button(menu_frame, text="Login Clientes", command=iniciar_sesion_cliente, font=("Helvetica", 20)).pack(pady=20)
    tk.Button(menu_frame, text="Salir", command=root.quit, font=("Helvetica", 20)).pack(pady=20)

def log_emp():
    registro_window = tk.Toplevel(root)
    registro_window.title("Registro de Empleado")
    registro_window.geometry("1000x800")
    font_style = tkfont.Font(family="Arial", size=12)
    label_font = tkfont.Font(family="Arial", size=10, weight="bold")
    
    tk.Label(registro_window, text="Nombre:", font=label_font).grid(row=0, column=0, padx=10, pady=5, sticky='w')
    entry_nombre = tk.Entry(registro_window, font=font_style)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(registro_window, text="Dirección:", font=label_font).grid(row=1, column=0, padx=10, pady=5, sticky='w')
    entry_direccion = tk.Entry(registro_window, font=font_style)
    entry_direccion.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(registro_window, text="Teléfono:", font=label_font).grid(row=2, column=0, padx=10, pady=5, sticky='w')
    entry_tel = tk.Entry(registro_window, font=font_style)
    entry_tel.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(registro_window, text="Correo:", font=label_font).grid(row=3, column=0, padx=10, pady=5, sticky='w')
    entry_correo = tk.Entry(registro_window, font=font_style)
    entry_correo.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(registro_window, text="Nombre de Usuario:", font=label_font).grid(row=4, column=0, padx=10, pady=5, sticky='w')
    entry_username = tk.Entry(registro_window, font=font_style)
    entry_username.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(registro_window, text="Contraseña:", font=label_font).grid(row=5, column=0, padx=10, pady=5, sticky='w')
    entry_password = tk.Entry(registro_window, show="*", font=font_style)
    entry_password.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(registro_window, text="Puesto:", font=label_font).grid(row=8, column=0, padx=10, pady=5, sticky='w')
    entry_puesto = tk.Entry(registro_window, font=font_style)
    entry_puesto.grid(row=8, column=1, padx=10, pady=5)

    tk.Label(registro_window, text="Salario:", font=label_font).grid(row=9, column=0, padx=10, pady=5, sticky='w')
    entry_salario = tk.Entry(registro_window, font=font_style)
    entry_salario.grid(row=9, column=1, padx=10, pady=5)

    def submit_registration():
        nombre = entry_nombre.get()
        direccion = entry_direccion.get()
        tel = entry_tel.get()
        correo = entry_correo.get()
        username = entry_username.get()
        password = entry_password.get()
        puesto = entry_puesto.get()
        salario = entry_salario.get()

        empleado = Empleados(None, nombre, direccion, tel, correo, username, password, puesto, salario)
        
        if empleado.registrar_emp():
            messagebox.showinfo("Registro Exitoso", "El empleado ha sido registrado exitosamente.")
            registro_window.destroy()
        else:
            messagebox.showerror("Error", "No se pudo registrar el empleado.")

    tk.Button(registro_window, text="Registrar", command=submit_registration, font=font_style).grid(row=10, column=0, columnspan=2, pady=10)

def log_cli():
    registro_window = tk.Toplevel(root)
    registro_window.title("Registro de Cliente")
    registro_window.geometry("1000x800")
    font_style = tkfont.Font(family="Arial", size=12)
    label_font = tkfont.Font(family="Arial", size=10, weight="bold")
    
    tk.Label(registro_window, text="Nombre:", font=label_font).grid(row=0, column=0, padx=10, pady=5, sticky='w')
    entry_nombre = tk.Entry(registro_window, font=font_style)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(registro_window, text="Dirección:", font=label_font).grid(row=1, column=0, padx=10, pady=5, sticky='w')
    entry_direccion = tk.Entry(registro_window, font=font_style)
    entry_direccion.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(registro_window, text="Teléfono:", font=label_font).grid(row=2, column=0, padx=10, pady=5, sticky='w')
    entry_tel = tk.Entry(registro_window, font=font_style)
    entry_tel.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(registro_window, text="Correo:", font=label_font).grid(row=3, column=0, padx=10, pady=5, sticky='w')
    entry_correo = tk.Entry(registro_window, font=font_style)
    entry_correo.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(registro_window, text="Nombre de Usuario:", font=label_font).grid(row=4, column=0, padx=10, pady=5, sticky='w')
    entry_username = tk.Entry(registro_window, font=font_style)
    entry_username.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(registro_window, text="Contraseña:", font=label_font).grid(row=5, column=0, padx=10, pady=5, sticky='w')
    entry_password = tk.Entry(registro_window, show="*", font=font_style)
    entry_password.grid(row=5, column=1, padx=10, pady=5)

    def submit_registration():
        nombre = entry_nombre.get()
        direccion = entry_direccion.get()
        tel = entry_tel.get()
        correo = entry_correo.get()
        username = entry_username.get()
        password = entry_password.get()

        cliente = Clientes(None, nombre, direccion, tel, correo, username, password, tipo="")

        
        if cliente.registrar_cli():
            messagebox.showinfo("Registro Exitoso", "El cliente ha sido registrado exitosamente.")
            registro_window.destroy()
        else:
            messagebox.showerror("Error", "No se pudo registrar el cliente.")

    tk.Button(registro_window, text="Registrar", command=submit_registration, font=font_style).grid(row=6, column=0, columnspan=2, pady=10)

def cerrar_sesion_empleado():
    for widget in root.winfo_children():
        widget.destroy()
    menu_principal()

def menu_empleados():
    empleado_window = tk.Toplevel(root)
    empleado_window.title("Menú de Empleados")
    empleado_window.geometry("1000x800")
    empleado_window.configure(bg='#5ea6cf')

    menu_frame = tk.Frame(empleado_window, bg='#5ea6cf')
    menu_frame.pack(pady=50)

    tk.Button(menu_frame, text="Ver Clientes", command=ver_clientes, font=("Helvetica", 20)).pack(pady=20)
    tk.Button(menu_frame, text="Ver Empleados", command=ver_empleados, font=("Helvetica", 20)).pack(pady=20)
    tk.Button(menu_frame, text="Agregar Material", command=agregar_material, font=("Helvetica", 20)).pack(pady=20)
    tk.Button(menu_frame, text="Cerrar Sesión", command=lambda: cerrar_sesion_empleado(empleado_window), font=("Helvetica", 20)).pack(pady=20)

def cerrar_sesion_empleado(ventana_actual):
    ventana_actual.destroy()


def ver_clientes():
    conexion = get_connection()
    cursor = get_cursor(conexion)

    clientes_window = tk.Toplevel(root)
    clientes_window.title("Clientes Registrados")
    clientes_window.geometry("1000x800")

    cursor.execute("SELECT nombre, direccion, tel, correo FROM personas WHERE tipo='Cliente'")
    clientes = cursor.fetchall()

    for i, cliente in enumerate(clientes):
        cliente_info = f"Nombre: {cliente[0]}, Dirección: {cliente[1]}, Teléfono: {cliente[2]}, Correo: {cliente[3]}"
        tk.Label(clientes_window, text=cliente_info, font=("Helvetica", 12)).pack(anchor='w')


def ver_empleados():
    conexion = get_connection()
    cursor = get_cursor(conexion)

    empleados_window = tk.Toplevel(root)
    empleados_window.title("Empleados Registrados")
    empleados_window.geometry("1000x800")

    cursor.execute("SELECT nombre, direccion, tel, correo FROM personas WHERE tipo='Empleado'")
    empleados = cursor.fetchall()
    
    for i, empleado in enumerate(empleados):
        empleado_info = f"Nombre: {empleado[0]}, Dirección: {empleado[1]}, Teléfono: {empleado[2]}, Correo: {empleado[3]}"
        tk.Label(empleados_window, text=empleado_info, font=("Helvetica", 12)).pack(anchor='w')

def agregar_material():
    tipo_window = tk.Toplevel(root)
    tipo_window.title("Seleccionar Tipo de Material")
    tipo_window.geometry("1000x800")
    font_style = tkfont.Font(family="Arial", size=12)
    
    def abrir_formulario(tipo):
        tipo_window.destroy()
        enter_material(tipo)
    
    tk.Label(tipo_window, text="Selecciona el tipo de material:", font=font_style).pack(pady=20)
    
    tk.Button(tipo_window, text="Revista", command=lambda: abrir_formulario("Revista"), font=font_style).pack(pady=10)
    tk.Button(tipo_window, text="DVD", command=lambda: abrir_formulario("DVD"), font=font_style).pack(pady=10)
    tk.Button(tipo_window, text="Libro", command=lambda: abrir_formulario("Libro"), font=font_style).pack(pady=10)

def enter_material(tipo):
    material_window = tk.Toplevel(root)
    material_window.title(f"Agregar {tipo}")
    material_window.geometry("1000x800")
    font_style = tkfont.Font(family="Arial", size=12)
    label_font = tkfont.Font(family="Arial", size=10, weight="bold")
    
    tk.Label(material_window, text="Nombre:", font=label_font).grid(row=0, column=0, padx=10, pady=5, sticky='w')
    entry_nombre = tk.Entry(material_window, font=font_style)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5)
    
    tk.Label(material_window, text="Autor:", font=label_font).grid(row=1, column=0, padx=10, pady=5, sticky='w')
    entry_autor = tk.Entry(material_window, font=font_style)
    entry_autor.grid(row=1, column=1, padx=10, pady=5)
    
    tk.Label(material_window, text="Año:", font=label_font).grid(row=2, column=0, padx=10, pady=5, sticky='w')
    entry_anio = tk.Entry(material_window, font=font_style)
    entry_anio.grid(row=2, column=1, padx=10, pady=5)
    
    if tipo == "Revista":
        tk.Label(material_window, text="Número:", font=label_font).grid(row=3, column=0, padx=10, pady=5, sticky='w')
        entry_numero = tk.Entry(material_window, font=font_style)
        entry_numero.grid(row=3, column=1, padx=10, pady=5)
        
        def submit_material():
            nombre = entry_nombre.get()
            autor = entry_autor.get()
            anio = entry_anio.get()
            numero = entry_numero.get()
            tipo_material = "Revista"
            
            material = Material(None, nombre, autor, anio, tipo_material, True)
            
            if material.agregar_material():
                try:
                    conexion = get_connection()
                    cursor = get_cursor(conexion)
                    
                    material_id = material.id
                    
                    if material_id is None:
                        raise ValueError("No se pudo obtener el ID del material insertado.")
                    
                    cursor.execute("INSERT INTO revistas (id, numero) VALUES (%s, %s)", (material_id, numero))
                    
                    conexion.commit()
                    messagebox.showinfo("Registro Exitoso", "La revista ha sido agregada exitosamente.")
                    material_window.destroy()
                
                except mysql.connector.Error as err:
                    messagebox.showerror("Error", f"No se pudo agregar la revista: {err}")
                finally:
                    cursor.close()
                    conexion.close()
            else:
                messagebox.showerror("Error", "No se pudo agregar la revista.")
        
    elif tipo == "DVD":
        tk.Label(material_window, text="Duración (min):", font=label_font).grid(row=3, column=0, padx=10, pady=5, sticky='w')
        entry_duracion = tk.Entry(material_window, font=font_style)
        entry_duracion.grid(row=3, column=1, padx=10, pady=5)
        
        def submit_material():
            nombre = entry_nombre.get()
            autor = entry_autor.get()
            anio = entry_anio.get()
            duracion = entry_duracion.get()
            tipo_material = "DVD"
            
            material = Material(None, nombre, autor, anio, tipo_material, True)
            
            if material.agregar_material():
                try:
                    conexion = get_connection()
                    cursor = get_cursor(conexion)
                    
                    material_id = material.id
                    
                    if material_id is None:
                        raise ValueError("No se pudo obtener el ID del material insertado.")
                    
                    cursor.execute("INSERT INTO dvds (id, duracion) VALUES (%s, %s)", (material_id, duracion))
                    
                    conexion.commit()
                    messagebox.showinfo("Registro Exitoso", "El DVD ha sido agregado exitosamente.")
                    material_window.destroy()
                
                except mysql.connector.Error as err:
                    messagebox.showerror("Error", f"No se pudo agregar el DVD: {err}")
                finally:
                    cursor.close()
                    conexion.close()
            else:
                messagebox.showerror("Error", "No se pudo agregar el DVD.")
        
    elif tipo == "Libro":
        tk.Label(material_window, text="Número de Páginas:", font=label_font).grid(row=3, column=0, padx=10, pady=5, sticky='w')
        entry_paginas = tk.Entry(material_window, font=font_style)
        entry_paginas.grid(row=3, column=1, padx=10, pady=5)
        
        def submit_material():
            nombre = entry_nombre.get()
            autor = entry_autor.get()
            anio = entry_anio.get()
            paginas = entry_paginas.get()
            tipo_material = "Libro"
            
            material = Material(None, nombre, autor, anio, tipo_material, True)
            
            if material.agregar_material():
                try:
                    conexion = get_connection()
                    cursor = get_cursor(conexion)
                    
                    material_id = material.id
                    
                    if material_id is None:
                        raise ValueError("No se pudo obtener el ID del material insertado.")
                    
                    cursor.execute("INSERT INTO libros (id, num_paginas) VALUES (%s, %s)", (material_id, paginas))
                    
                    conexion.commit()
                    messagebox.showinfo("Registro Exitoso", "El libro ha sido agregado exitosamente.")
                    material_window.destroy()
                
                except mysql.connector.Error as err:
                    messagebox.showerror("Error", f"No se pudo agregar el libro: {err}")
                finally:
                    cursor.close()
                    conexion.close()
            else:
                messagebox.showerror("Error", "No se pudo agregar el libro.")
    
    tk.Button(material_window, text="Agregar", command=submit_material, font=font_style).grid(row=4, column=0, columnspan=2, pady=10)

def menu_clientes():
    menu_window = tk.Toplevel(root)
    menu_window.title("Menú de Clientes")
    menu_window.geometry("1000x800")
    menu_frame = tk.Frame(menu_window, bg='#5ea6cf')
    menu_frame.pack(fill='both', expand=True, pady=50)

    tk.Button(menu_frame, text="Consultar Material", command=consultar_material, font=("Helvetica", 20)).pack(pady=20)
    tk.Button(menu_frame, text="Pedir Prestado", command=pedir_prestado, font=("Helvetica", 20)).pack(pady=20)
    tk.Button(menu_frame, text="Cerrar Sesión", command=menu_principal, font=("Helvetica", 20)).pack(pady=20)


def consultar_material():
    conexion = get_connection()
    cursor = get_cursor(conexion)

    material_window = tk.Toplevel(root)
    material_window.title("Material Disponible")
    material_window.geometry("1000x800")
    
    cursor.execute("SELECT id, titulo, autor, tipo FROM material WHERE disponible=TRUE")
    materiales = cursor.fetchall()

    for material in materiales:
        material_info = f"ID: {material[0]}, Título: {material[1]}, Autor: {material[2]}, Tipo: {material[3]}"
        tk.Label(material_window, text=material_info, font=("Helvetica", 12)).pack(anchor='w')

    cursor.close()
    conexion.close()

def pedir_prestado():
    prestamo_window = tk.Toplevel(root)
    prestamo_window.title("Pedir Prestado")
    prestamo_window.geometry("1000x800")
    font_style = tkfont.Font(family="Arial", size=12)
    label_font = tkfont.Font(family="Arial", size=10, weight="bold")
    
    tk.Label(prestamo_window, text="ID Material:", font=label_font).grid(row=0, column=0, padx=10, pady=5, sticky='w')
    entry_id_material = tk.Entry(prestamo_window, font=font_style)
    entry_id_material.grid(row=0, column=1, padx=10, pady=5)
    
    def submit_prestamo():
        id_material = entry_id_material.get()
        cliente_id = sesion_cliente.id if sesion_cliente else None
        
        if not cliente_id:
            messagebox.showerror("Error", "Debe estar registrado como cliente para pedir prestado.")
            return
        
        fecha_prestamo = datetime.now()
        fecha_entrega = fecha_prestamo + timedelta(days=14)

        prestamo = Prestamo(None, id_material, fecha_prestamo, fecha_entrega, cliente_id)
        
        if prestamo.pedir_prestado():
            messagebox.showinfo("Préstamo Exitoso", "El material ha sido prestado exitosamente.")
            prestamo_window.destroy()
        else:
            messagebox.showinfo("Préstamo Exitoso", "El material ha sido prestado exitosamente.")

    tk.Button(prestamo_window, text="Pedir Prestado", command=submit_prestamo, font=font_style).grid(row=1, column=0, columnspan=2, pady=20)


def iniciar_sesion_empleado():
    login_window = tk.Toplevel(root)
    login_window.title("Inicio de Sesión - Empleado")
    login_window.geometry("1000x800")
    font_style = tkfont.Font(family="Arial", size=12)
    label_font = tkfont.Font(family="Arial", size=10, weight="bold")

    tk.Label(login_window, text="Nombre de Usuario:", font=label_font).grid(row=0, column=0, padx=10, pady=10)
    entry_username = tk.Entry(login_window, font=font_style)
    entry_username.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(login_window, text="Contraseña:", font=label_font).grid(row=1, column=0, padx=10, pady=10)
    entry_password = tk.Entry(login_window, show="*", font=font_style)
    entry_password.grid(row=1, column=1, padx=10, pady=10)

    def autenticar_empleado():
        global sesion_empleado
        username = entry_username.get()
        password = entry_password.get()
        empleado = Empleados.iniciar_sesion(username, password)
        if empleado:
            sesion_empleado = empleado
            login_window.destroy()
            menu_empleados()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    tk.Button(login_window, text="Iniciar Sesión", command=autenticar_empleado, font=font_style).grid(row=2, column=0, columnspan=2, pady=20)

def iniciar_sesion_cliente():
    login_window = tk.Toplevel(root)
    login_window.title("Inicio de Sesión - Cliente")
    login_window.geometry("1000x800")
    font_style = tkfont.Font(family="Arial", size=12)
    label_font = tkfont.Font(family="Arial", size=10, weight="bold")

    tk.Label(login_window, text="Nombre de Usuario:", font=label_font).grid(row=0, column=0, padx=10, pady=10)
    entry_username = tk.Entry(login_window, font=font_style)
    entry_username.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(login_window, text="Contraseña:", font=label_font).grid(row=1, column=0, padx=10, pady=10)
    entry_password = tk.Entry(login_window, show="*", font=font_style)
    entry_password.grid(row=1, column=1, padx=10, pady=10)

    def autenticar_cliente():
        global sesion_cliente
        username = entry_username.get()
        password = entry_password.get()

        cliente = Clientes.iniciar_sesion(username, password)
        if cliente:
            sesion_cliente = cliente
            login_window.destroy()
            menu_clientes()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    tk.Button(login_window, text="Iniciar Sesión", command=autenticar_cliente, font=font_style).grid(row=2, column=0, columnspan=2, pady=20)


menu_principal()
root.mainloop()
