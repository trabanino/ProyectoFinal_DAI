def login_required(func):
    def wrapper(*args, **kwargs):
        # Lógica para verificar si el usuario está autenticado
        # Por ejemplo, verificar si hay un usuario en la sesión
        authenticated = True  # Placeholder, cambiar por la lógica real
        if not authenticated:
            raise Exception("Usuario no autenticado")
        return func(*args, **kwargs)
    return wrapper
