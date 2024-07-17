def login_required(func):
    def wrapper(*args, **kwargs):

        authenticated = True
        if not authenticated:
            raise Exception("Usuario no autenticado")
        return func(*args, **kwargs)
    return wrapper
