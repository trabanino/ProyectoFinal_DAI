from functools import wraps
from tienda.session import Session
from tkinter import messagebox

def login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not Session.get('usuario'):
            messagebox.showerror("Error", "Usuario no autenticado")
            return
        return func(*args, **kwargs)
    return decorated_view
