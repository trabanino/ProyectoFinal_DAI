from idlelib import window
from tkinter import messagebox
from tienda.database.queries import handle_register_process


def handle_register(username_entry, nombre_entry, email_entry, password_entry, window):
    from tienda.views.login_view import open_login_gui
    username = username_entry.get()
    nombre = nombre_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    print(f"Username: {username}, Nombre: {nombre}, Email: {email}, Password: {password}")  # Debug print

    success, message = handle_register_process(username, nombre, email, password)

    if success:
        messagebox.showinfo("Registrado correctamente", message)
        window.destroy()
        open_login_gui()
    else:
        messagebox.showerror("Registrado incorrectamente", message)
