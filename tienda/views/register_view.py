# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tienda.controllers.register_controller import handle_register

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/register_view")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def open_register_view():
    window = Tk()
    window.withdraw()
    window.geometry("900x600")
    window.configure(bg="#FFFFFF")
    window.title("Registrarse")

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
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        172.0,
        300.0,
        image=image_image_1
    )

    canvas.create_text(
        485.0,
        62.0,
        anchor="nw",
        text="Crea tu cuenta!",
        fill="#000000",
        font=("SFProDisplay Bold", 26 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        548.0,
        171.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=426.0,
        y=150.0,
        width=244.0,
        height=40.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        548.0,
        264.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=426.0,
        y=243.0,
        width=244.0,
        height=40.0
    )

    canvas.create_text(
        405.0,
        125.0,
        anchor="nw",
        text="Usuario",
        fill="#000000",
        font=("SFProDisplay Regular", 15 * -1)
    )

    canvas.create_text(
        405.0,
        218.0,
        anchor="nw",
        text="Nombre",
        fill="#000000",
        font=("SFProDisplay Regular", 15 * -1)
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        548.0,
        450.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=426.0,
        y=429.0,
        width=244.0,
        height=40.0
    )

    canvas.create_text(
        405.0,
        404.0,
        anchor="nw",
        text="Contraseña",
        fill="#000000",
        font=("SFProDisplay Regular", 15 * -1)
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        548.0,
        357.0,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=426.0,
        y=336.0,
        width=244.0,
        height=40.0
    )

    canvas.create_text(
        405.0,
        311.0,
        anchor="nw",
        text="Email",
        fill="#000000",
        font=("SFProDisplay Regular", 15 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: handle_register(entry_1, entry_2, entry_4, entry_3, window),
        relief="flat"
    )
    button_1.place(
        x=414.0,
        y=497.0,
        width=123.0,
        height=28.0
    )
    window.resizable(False, False)
    window.mainloop()
