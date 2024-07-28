from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from .admin_login_view import open_admin_login_gui
from tienda.controllers.login_controller import handle_login

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/login_view")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def open_login_gui():
    window = Tk()
    window.withdraw()
    window.geometry("900x600")
    window.configure(bg="#FFFFFF")
    window.title("Login")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (900 / 2)
    y = (screen_height / 2) - (600 / 2)

    window.geometry('+%d+%d' % (x, y))

    window.deiconify()

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=600,
        width=900,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        0.0,
        345.0,
        600.0,
        fill="#2C2C2C",
        outline="")

    canvas.create_text(
        47.0,
        258.0,
        anchor="nw",
        text="Bienvenido!",
        fill="#FFFFFF",
        font=("SFProDisplay Bold", 26 * -1)
    )

    canvas.create_text(
        444.0,
        195.0,
        anchor="nw",
        text="Iniciar sesión",
        fill="#000000",
        font=("SFProDisplay Bold", 26 * -1)
    )

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(542.0, 289.0, image=entry_image_1)
    entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(x=420.0, y=268.0, width=244.0, height=40.0)

    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(542.0, 373.0, image=entry_image_2)
    entry_2 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(x=420.0, y=352.0, width=244.0, height=40.0)

    canvas.create_text(
        417.0,
        250.0,
        anchor="nw",
        text="Usuario PISTA: Alvin",
        fill="#000000",
        font=("SFProDisplay Regular", 15 * -1)
    )

    canvas.create_text(
        417.0,
        334.0,
        anchor="nw",
        text="Contraseña PISTA: Pajaritos",
        fill="#000000",
        font=("SFProDisplay Regular", 15 * -1)
    )

    canvas.create_text(
        472.0,
        504.0,
        anchor="nw",
        text="Administrador? Haga click aca:",
        fill="#000000",
        font=("SFProDisplay Regular", 12 * -1)
    )

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=open_admin_login_gui,
        relief="flat"
    )
    button_1.place(x=483.0, y=527.0, width=123.0, height=28.0)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: handle_login(entry_1, entry_2, window),
        relief="flat"
    )
    button_2.place(x=419.0, y=426.0, width=123.0, height=28.0)

    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=715.0,
        y=527.0,
        width=123.0,
        height=28.0
    )

    window.resizable(False, False)
    window.mainloop()
