from tkinter import messagebox
from tienda.database.queries import handle_login_attempt
from tienda.views.usuario_view import open_usuario_gui

import requests

def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org")
        return response.text
    except requests.RequestException:
        return "Unknown"


def handle_login(username_entry, password_entry, window):
    username = username_entry.get()
    password = password_entry.get()

    ip_address = get_public_ip()

    success, message = handle_login_attempt(username, password, ip_address)

    if success:
        messagebox.showinfo("Login exitoso", message)
        window.destroy()
        open_usuario_gui()
    else:
        messagebox.showerror("Login fallido", message)
