
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from tienda.decoradores import login_required
from tienda.session import Session

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\usuario_view")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

@login_required
def open_usuario_gui():

    window = Tk()
    window.withdraw()
    window.geometry("1024x700")
    window.configure(bg="#FFFFFF")
    window.title("Menu principal")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (1024 / 2)
    y = (screen_height / 2) - (700 / 2)

    window.geometry('+%d+%d' % (x, y))

    window.deiconify()

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 700,
        width = 1024,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1024.0,
        99.0,
        fill="#720902",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        440.0,
        49.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=223.0,
        y=19.0,
        width=434.0,
        height=59.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        90.0,
        45.0,
        image=image_image_1
    )

    canvas.create_text(
        887.0,
        31.0,
        anchor="nw",
        text=Session.get("usuario"),
        fill="#FFFFFF",
        font=("Inter", 25 * -1)
    )

    canvas.create_text(
        71.0,
        123.0,
        anchor="nw",
        text="Categorias",
        fill="#720902",
        font=("Inter", 25 * -1)
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        119.0,
        284.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        315.0,
        287.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        904.0,
        284.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        711.0,
        287.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        512.0,
        287.0,
        image=image_image_6
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        707.0,
        488.0,
        image=image_image_7
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Snacks clicked"),
        relief="flat"
    )
    button_1.place(
        x=621.0,
        y=526.0,
        width=172.0,
        height=34.0
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        511.0,
        488.0,
        image=image_image_8
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=425.0,
        y=526.0,
        width=189.0,
        height=34.0
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets("image_9.png"))
    image_9 = canvas.create_image(
        314.0,
        488.0,
        image=image_image_9
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=230.0,
        y=325.0,
        width=183.0,
        height=34.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=33.0,
        y=322.0,
        width=172.0,
        height=34.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    button_5.place(
        x=426.0,
        y=325.0,
        width=172.0,
        height=34.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_6 clicked"),
        relief="flat"
    )
    button_6.place(
        x=625.0,
        y=325.0,
        width=172.0,
        height=34.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_7 clicked"),
        relief="flat"
    )
    button_7.place(
        x=228.0,
        y=526.0,
        width=172.0,
        height=34.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_8 clicked"),
        relief="flat"
    )
    button_8.place(
        x=818.0,
        y=322.0,
        width=172.0,
        height=34.0
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("button_9.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_9 clicked"),
        relief="flat"
    )
    button_9.place(
        x=597.0,
        y=27.0,
        width=48.0,
        height=49.0
    )

    button_image_10 = PhotoImage(
        file=relative_to_assets("button_10.png"))
    button_10 = Button(
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_10 clicked"),
        relief="flat"
    )
    button_10.place(
        x=739.0,
        y=22.0,
        width=54.0,
        height=58.0
    )

    button_image_11 = PhotoImage(
        file=relative_to_assets("button_11.png"))
    button_11 = Button(
        image=button_image_11,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print(Session.get("usuario")),
        relief="flat"
    )
    button_11.place(
        x=813.0,
        y=22.0,
        width=53.0,
        height=52.0
    )
    window.resizable(False, False)
    window.mainloop()
