
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\usuario_view")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1024x700")
window.configure(bg = "#FFFFFF")


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

canvas.create_rectangle(
    223.0,
    19.0,
    657.0,
    80.0,
    fill="#D9D9D9",
    outline="")

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
    text="Usuario ",
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

canvas.create_rectangle(
    33.0,
    322.0,
    205.0,
    356.0,
    fill="#D9D9D9",
    outline="")

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    904.0,
    284.0,
    image=image_image_4
)

canvas.create_rectangle(
    818.0,
    322.0,
    990.0,
    356.0,
    fill="#D9D9D9",
    outline="")

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    711.0,
    287.0,
    image=image_image_5
)

canvas.create_rectangle(
    625.0,
    325.0,
    797.0,
    359.0,
    fill="#D9D9D9",
    outline="")

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    512.0,
    287.0,
    image=image_image_6
)

canvas.create_rectangle(
    426.0,
    325.0,
    598.0,
    359.0,
    fill="#D9D9D9",
    outline="")

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    707.0,
    488.0,
    image=image_image_7
)

canvas.create_rectangle(
    621.0,
    526.0,
    793.0,
    560.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    641.0,
    529.0,
    anchor="nw",
    text="Snacks",
    fill="#720902",
    font=("Inter", 25 * -1)
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    511.0,
    488.0,
    image=image_image_8
)

canvas.create_rectangle(
    425.0,
    526.0,
    597.0,
    560.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    432.0,
    531.0,
    anchor="nw",
    text="Limpieza Personal",
    fill="#720902",
    font=("Inter", 18 * -1)
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    314.0,
    488.0,
    image=image_image_9
)

canvas.create_rectangle(
    228.0,
    526.0,
    400.0,
    560.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    230.0,
    325.0,
    402.0,
    359.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    237.0,
    328.0,
    anchor="nw",
    text="Frutas y verduras",
    fill="#720902",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    75.0,
    322.0,
    anchor="nw",
    text="Lácteos",
    fill="#720902",
    font=("Inter", 25 * -1)
)

canvas.create_text(
    472.0,
    328.0,
    anchor="nw",
    text="Carnes",
    fill="#720902",
    font=("Inter", 25 * -1)
)

canvas.create_text(
    650.0,
    328.0,
    anchor="nw",
    text="Panadería",
    fill="#720902",
    font=("Inter", 25 * -1)
)

canvas.create_text(
    259.0,
    526.0,
    anchor="nw",
    text="Limpieza",
    fill="#720902",
    font=("Inter", 25 * -1)
)

canvas.create_text(
    837.0,
    325.0,
    anchor="nw",
    text="Bebidas",
    fill="#720902",
    font=("Inter", 25 * -1)
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    623.25,
    48.25,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    765.0833740234375,
    47.16667175292969,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    853.3333740234375,
    47.33332824707031,
    image=image_image_12
)
window.resizable(False, False)
window.mainloop()
