# usuario_view.py
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from tienda.decoradores import login_required
from tienda.session import Session
from tienda.database.queries import get_categories
from tienda.views.productos_view import create_product_grid

import urllib.request
import io
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/usuario_view")

image_references = []  # Lista para mantener referencias a las imágenes

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def display_image(source):
    if source is None:
        source = "default_image.png"

    try:
        if source.startswith(('http://', 'https://')):
            with urllib.request.urlopen(source) as u:
                raw_data = u.read()
            image = Image.open(io.BytesIO(raw_data))
        else:
            image_path = relative_to_assets(source)
            if not image_path.exists():
                raise FileNotFoundError(f"El archivo de la imagen no fue encontrado en: {image_path}")
            image = Image.open(image_path)

        image = image.resize((125, 125))  # Ajustar tamaño de la imagen
        photo = ImageTk.PhotoImage(image)
        image_references.append(photo)  # Mantener referencia a la imagen
        return photo
    except (urllib.error.URLError, FileNotFoundError, IOError) as e:
        print(f"Error al cargar la imagen {source}: {e}")
        default_image_path = relative_to_assets("default_image.png")
        if default_image_path.exists():
            default_image = Image.open(default_image_path)
            default_image = default_image.resize((125, 125))  # Ajustar tamaño de la imagen
            photo = ImageTk.PhotoImage(default_image)
            image_references.append(photo)  # Mantener referencia a la imagen
            return photo
        else:
            print("La imagen por defecto no fue encontrada")
            return None

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
        bg="#FFFFFF",
        height=700,
        width=1024,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
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

    # Mantener referencias a las imágenes
    category_images = []

    # Obtener categorías desde la base de datos
    categories = get_categories()

    # Crear botones de categorías dinámicamente
    for i, category in enumerate(categories):
        category_id, category_name, category_image_path = category

        # Usar display_image para obtener la imagen
        category_image = display_image(category_image_path)
        category_images.append(category_image)  # Guardar la referencia de la imagen

        # Crear un canvas para cada categoría
        category_canvas = Canvas(
            window,
            width=200,
            height=250,
            bg="#FFFFFF",
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        # Dibujar fondo rojo
        category_canvas.create_rectangle(
            0, 0, 200, 250,
            fill="#720902", outline=""
        )

        # Añadir imagen de categoría
        if category_image:
            category_canvas.create_image(
                100, 75,
                image=category_image
            )

        # Añadir nombre de categoría
        category_canvas.create_text(
            100, 200,
            text=category_name,
            fill="#FFFFFF",
            font=("Inter", 16, "bold")
        )

        # Colocar el canvas en la ventana
        category_canvas.place(x=(i % 4) * 220 + 50, y=(i // 4) * 270 + 150)

        # Asociar el evento de clic al canvas
        category_canvas.bind("<Button-1>", lambda event, cid=category_id: open_product_view(window, cid))

    window.resizable(False, False)
    window.mainloop()

def open_product_view(window, category_id):
    # Limpiar el canvas actual
    for widget in window.winfo_children():
        widget.destroy()

    # Crear un nuevo canvas
    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=700,
        width=1024,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    # Aquí puedes cargar la vista de productos para la categoría específica
    create_product_grid(window, canvas, category_id, lambda: open_usuario_gui())

if __name__ == "__main__":
    open_usuario_gui()
