from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\productos_view")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1024x700")
window.configure(bg = "#FFFFFF")

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
    781.0,
    435.0,
    1005.0,
    691.0,
    fill="#720902",
    outline="")

canvas.create_rectangle(
    792.0,
    662.0,
    902.0,
    682.0,
    fill="#9D0000",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=964.0,
    y=659.0,
    width=25.0,
    height=25.0
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
    x=886.0,
    y=664.0,
    width=8.0,
    height=15.0
)

canvas.create_text(
    835.0,
    664.0,
    anchor="nw",
    text="1.00",
    fill="#FFFFFF",
    font=("Inter", 12 * -1)
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
    x=798.0,
    y=664.0,
    width=6.0,
    height=15.0
)

canvas.create_text(
    792.0,
    638.0,
    anchor="nw",
    text="CATEGORIA ",
    fill="#FFFFFF",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    792.0,
    620.0,
    anchor="nw",
    text="NOMBRE PRODUCTO",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    792.0,
    603.0,
    anchor="nw",
    text="$0.00",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    893.0,
    522.0,
    image=image_image_1
)

canvas.create_rectangle(
    527.0,
    435.0,
    751.0,
    691.0,
    fill="#720902",
    outline="")

canvas.create_rectangle(
    538.0,
    662.0,
    648.0,
    682.0,
    fill="#9D0000",
    outline="")

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
    x=710.0,
    y=659.0,
    width=25.0,
    height=25.0
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
    x=632.0,
    y=664.0,
    width=8.0,
    height=15.0
)

canvas.create_text(
    581.0,
    664.0,
    anchor="nw",
    text="1.00",
    fill="#FFFFFF",
    font=("Inter", 12 * -1)
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
    x=544.0,
    y=664.0,
    width=6.0,
    height=15.0
)

canvas.create_text(
    538.0,
    638.0,
    anchor="nw",
    text="CATEGORIA ",
    fill="#FFFFFF",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    538.0,
    620.0,
    anchor="nw",
    text="NOMBRE PRODUCTO",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    538.0,
    603.0,
    anchor="nw",
    text="$0.00",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    639.0,
    522.0,
    image=image_image_2
)

canvas.create_rectangle(
    273.0,
    435.0,
    497.0,
    691.0,
    fill="#720902",
    outline="")

canvas.create_rectangle(
    284.0,
    662.0,
    394.0,
    682.0,
    fill="#9D0000",
    outline="")

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
    x=456.0,
    y=659.0,
    width=25.0,
    height=25.0
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
    x=378.0,
    y=664.0,
    width=8.0,
    height=15.0
)

canvas.create_text(
    327.0,
    664.0,
    anchor="nw",
    text="1.00",
    fill="#FFFFFF",
    font=("Inter", 12 * -1)
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
    x=290.0,
    y=664.0,
    width=6.0,
    height=15.0
)

canvas.create_text(
    284.0,
    638.0,
    anchor="nw",
    text="CATEGORIA ",
    fill="#FFFFFF",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    284.0,
    620.0,
    anchor="nw",
    text="NOMBRE PRODUCTO",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    284.0,
    603.0,
    anchor="nw",
    text="$0.00",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    385.0,
    522.0,
    image=image_image_3
)

canvas.create_rectangle(
    19.0,
    435.0,
    243.0,
    691.0,
    fill="#720902",
    outline="")

canvas.create_rectangle(
    30.0,
    662.0,
    140.0,
    682.0,
    fill="#9D0000",
    outline="")

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
    x=202.0,
    y=659.0,
    width=25.0,
    height=25.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=124.0,
    y=664.0,
    width=8.0,
    height=15.0
)

canvas.create_text(
    73.0,
    664.0,
    anchor="nw",
    text="1.00",
    fill="#FFFFFF",
    font=("Inter", 12 * -1)
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_12 clicked"),
    relief="flat"
)
button_12.place(
    x=36.0,
    y=664.0,
    width=6.0,
    height=15.0
)

canvas.create_text(
    30.0,
    638.0,
    anchor="nw",
    text="CATEGORIA ",
    fill="#FFFFFF",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    30.0,
    620.0,
    anchor="nw",
    text="NOMBRE PRODUCTO",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    30.0,
    603.0,
    anchor="nw",
    text="$0.00",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    131.0,
    522.0,
    image=image_image_4
)

canvas.create_rectangle(
    781.0,
    159.0,
    1005.0,
    415.0,
    fill="#720902",
    outline="")

canvas.create_rectangle(
    792.0,
    386.0,
    902.0,
    406.0,
    fill="#9D0000",
    outline="")

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_13 clicked"),
    relief="flat"
)
button_13.place(
    x=964.0,
    y=383.0,
    width=25.0,
    height=25.0
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_14 clicked"),
    relief="flat"
)
button_14.place(
    x=886.0,
    y=388.0,
    width=8.0,
    height=15.0
)

canvas.create_text(
    835.0,
    388.0,
    anchor="nw",
    text="1.00",
    fill="#FFFFFF",
    font=("Inter", 12 * -1)
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_15 clicked"),
    relief="flat"
)
button_15.place(
    x=798.0,
    y=388.0,
    width=6.0,
    height=15.0
)

canvas.create_text(
    792.0,
    362.0,
    anchor="nw",
    text="CATEGORIA ",
    fill="#FFFFFF",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    792.0,
    344.0,
    anchor="nw",
    text="NOMBRE PRODUCTO",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    792.0,
    327.0,
    anchor="nw",
    text="$0.00",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    893.0,
    246.0,
    image=image_image_5
)

canvas.create_rectangle(
    527.0,
    159.0,
    751.0,
    415.0,
    fill="#720902",
    outline="")

canvas.create_rectangle(
    538.0,
    386.0,
    648.0,
    406.0,
    fill="#9D0000",
    outline="")

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_16 clicked"),
    relief="flat"
)
button_16.place(
    x=710.0,
    y=383.0,
    width=25.0,
    height=25.0
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_17 clicked"),
    relief="flat"
)
button_17.place(
    x=632.0,
    y=388.0,
    width=8.0,
    height=15.0
)

canvas.create_text(
    581.0,
    388.0,
    anchor="nw",
    text="1.00",
    fill="#FFFFFF",
    font=("Inter", 12 * -1)
)

button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_18 clicked"),
    relief="flat"
)
button_18.place(
    x=544.0,
    y=388.0,
    width=6.0,
    height=15.0
)

canvas.create_text(
    538.0,
    362.0,
    anchor="nw",
    text="CATEGORIA ",
    fill="#FFFFFF",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    538.0,
    344.0,
    anchor="nw",
    text="NOMBRE PRODUCTO",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    538.0,
    327.0,
    anchor="nw",
    text="$0.00",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    639.0,
    246.0,
    image=image_image_6
)

canvas.create_rectangle(
    273.0,
    159.0,
    497.0,
    415.0,
    fill="#720902",
    outline="")

canvas.create_rectangle(
    284.0,
    386.0,
    394.0,
    406.0,
    fill="#9D0000",
    outline="")

button_image_19 = PhotoImage(
    file=relative_to_assets("button_19.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_19 clicked"),
    relief="flat"
)
button_19.place(
    x=456.0,
    y=383.0,
    width=25.0,
    height=25.0
)

button_image_20 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_20 = Button(
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_20 clicked"),
    relief="flat"
)
button_20.place(
    x=378.0,
    y=388.0,
    width=8.0,
    height=15.0
)

canvas.create_text(
    327.0,
    388.0,
    anchor="nw",
    text="1.00",
    fill="#FFFFFF",
    font=("Inter", 12 * -1)
)

button_image_21 = PhotoImage(
    file=relative_to_assets("button_21.png"))
button_21 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_21 clicked"),
    relief="flat"
)
button_21.place(
    x=290.0,
    y=388.0,
    width=6.0,
    height=15.0
)

canvas.create_text(
    284.0,
    362.0,
    anchor="nw",
    text="CATEGORIA ",
    fill="#FFFFFF",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    284.0,
    344.0,
    anchor="nw",
    text="NOMBRE PRODUCTO",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    284.0,
    327.0,
    anchor="nw",
    text="$0.00",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    385.0,
    246.0,
    image=image_image_7
)

canvas.create_rectangle(
    19.0,
    159.0,
    243.0,
    415.0,
    fill="#720902",
    outline="")

canvas.create_rectangle(
    30.0,
    386.0,
    140.0,
    406.0,
    fill="#9D0000",
    outline="")

button_image_22 = PhotoImage(
    file=relative_to_assets("button_22.png"))
button_22 = Button(
    image=button_image_22,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_22 clicked"),
    relief="flat"
)
button_22.place(
    x=202.0,
    y=383.0,
    width=25.0,
    height=25.0
)

button_image_23 = PhotoImage(
    file=relative_to_assets("button_23.png"))
button_23 = Button(
    image=button_image_23,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_23 clicked"),
    relief="flat"
)
button_23.place(
    x=124.0,
    y=388.0,
    width=8.0,
    height=15.0
)

canvas.create_text(
    73.0,
    388.0,
    anchor="nw",
    text="1.00",
    fill="#FFFFFF",
    font=("Inter", 12 * -1)
)

button_image_24 = PhotoImage(
    file=relative_to_assets("button_24.png"))
button_24 = Button(
    image=button_image_24,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_24 clicked"),
    relief="flat"
)
button_24.place(
    x=36.0,
    y=388.0,
    width=6.0,
    height=15.0
)

canvas.create_text(
    30.0,
    362.0,
    anchor="nw",
    text="CATEGORIA ",
    fill="#FFFFFF",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    30.0,
    344.0,
    anchor="nw",
    text="NOMBRE PRODUCTO",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    30.0,
    327.0,
    anchor="nw",
    text="$0.00",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    131.0,
    246.0,
    image=image_image_8
)

canvas.create_text(
    39.0,
    120.0,
    anchor="nw",
    text="Productos: PENDIENTE",
    fill="#720902",
    font=("Inter", 25 * -1)
)

canvas.create_rectangle(
    0.0,
    0.0,
    1024.0,
    99.0,
    fill="#720902",
    outline="")

button_image_25 = PhotoImage(
    file=relative_to_assets("button_25.png"))
button_25 = Button(
    image=button_image_25,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_25 clicked"),
    relief="flat"
)
button_25.place(
    x=829.0,
    y=24.0,
    width=171.0,
    height=60.0
)

button_image_26 = PhotoImage(
    file=relative_to_assets("button_26.png"))
button_26 = Button(
    image=button_image_26,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_26 clicked"),
    relief="flat"
)
button_26.place(
    x=743.0,
    y=24.0,
    width=50.0,
    height=50.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    440.0,
    49.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#9D0000",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=248.0,
    y=19.0,
    width=384.0,
    height=59.0
)

button_image_27 = PhotoImage(
    file=relative_to_assets("button_27.png"))
button_27 = Button(
    image=button_image_27,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_27 clicked"),
    relief="flat"
)
button_27.place(
    x=599.0,
    y=24.0,
    width=50.0,
    height=50.0
)

button_image_28 = PhotoImage(
    file=relative_to_assets("button_28.png"))
button_28 = Button(
    image=button_image_28,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_28 clicked"),
    relief="flat"
)
button_28.place(
    x=54.0,
    y=10.0,
    width=73.0,
    height=70.0
)
window.resizable(False, False)
window.mainloop()
