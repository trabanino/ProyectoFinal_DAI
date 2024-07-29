from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\admin_login_view")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_admin_login_gui():
    window = Toplevel()
    window.withdraw()
    window.geometry("900x600")
    window.configure(bg="#FFFFFF")
    window.title("Admin Login")

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
        30.0,
        259.0,
        anchor="nw",
        text="Bienvenido al sistema de inventario",
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
        window,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(x=420.0, y=268.0, width=244.0, height=40.0)

    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(542.0, 373.0, image=entry_image_2)
    entry_2 = Entry(
        window,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        show="*",
    )
    entry_2.place(x=420.0, y=352.0, width=244.0, height=40.0)

    canvas.create_text(
        417.0,
        250.0,
        anchor="nw",
        text="Usuario",
        fill="#000000",
        font=("SFProDisplay Regular", 15 * -1)
    )

    canvas.create_text(
        417.0,
        334.0,
        anchor="nw",
        text="Contraseña",
        fill="#000000",
        font=("SFProDisplay Regular", 15 * -1)
    )

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(x=419.0, y=426.0, width=123.0, height=28.0)

    window.resizable(False, False)
    window.mainloop()

# This allows you to run this file directly to test the GUI
if __name__ == "__main__":
    root = Tk()
    root.withdraw()  # Hide the root window
    open_admin_login_gui()
    root.mainloop()