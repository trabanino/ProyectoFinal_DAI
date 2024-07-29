import io
import tkinter as tk
import urllib.request
from PIL import ImageTk, Image
from tkinter import PhotoImage
from pathlib import Path
from tienda.session import Session
from tienda.database.queries import get_products_by_category
from tienda.cart import Cart


cart = Cart()  # Crear una instancia del carrito

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/productos_view")

image_references = []  # Lista para mantener referencias a las imágenes

def irse():
    from tienda.views.usuario_view import open_usuario_gui
    open_usuario_gui()

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

        image = image.resize((175, 125))
        photo = ImageTk.PhotoImage(image)
        image_references.append(photo)  # Mantener referencia a la imagen
        return photo
    except (urllib.error.URLError, FileNotFoundError, IOError) as e:
        print(f"Error al cargar la imagen {source}: {e}")
        default_image_path = relative_to_assets("default_image.png")
        if default_image_path.exists():
            default_image = Image.open(default_image_path)
            default_image = default_image.resize((175, 125))
            photo = ImageTk.PhotoImage(default_image)
            image_references.append(photo)  # Mantener referencia a la imagen
            return photo
        else:
            print("La imagen por defecto no fue encontrada")
            return None

class Product:
    def __init__(self, name, price, image_source):
        self.name = name
        self.price = price
        self.image_source = image_source
        self.quantity = 1
        self.image = None

    def load_image(self):
        self.image = display_image(self.image_source)

class ProductView:
    def __init__(self, master, canvas, product, x, y):
        self.master = master
        self.canvas = canvas
        self.product = product
        self.x = x
        self.y = y
        self.create_view()

    def create_view(self):
        self.canvas.create_rectangle(
            self.x, self.y, self.x + 224, self.y + 256,
            fill="#720902", outline=""
        )

        self.canvas.create_rectangle(
            self.x + 11, self.y + 227, self.x + 121, self.y + 247,
            fill="#9D0000", outline=""
        )

        self.canvas.create_text(
            self.x + 11, self.y + 185,
            anchor="nw", text=self.product.name,
            fill="#FFFFFF", font=("Inter", 18 * -1)
        )
        self.canvas.create_text(
            self.x + 11, self.y + 168,
            anchor="nw", text=f"${self.product.price:.2f}",
            fill="#FFFFFF", font=("Inter", 16 * -1)
        )

        self.create_button("button_minus", self.x + 17, self.y + 229, 6, 15, self.decrease_quantity)
        self.create_button("button_plus", self.x + 105, self.y + 229, 8, 15, self.increase_quantity)
        self.create_button("button_add", self.x + 183, self.y + 224, 25, 25, self.add_to_cart)

        self.quantity_text = self.canvas.create_text(
            self.x + 54, self.y + 229,
            anchor="nw", text=str(self.product.quantity),
            fill="#FFFFFF", font=("Inter", 12 * -1)
        )

        self.create_product_image()

    def create_button(self, name, x, y, width, height, command):
        image_path = relative_to_assets(f"{name}.png")
        if not image_path.exists():
            print(f"Advertencia: El archivo de la imagen del boton no fue encontrado en: {image_path}")
            return

        image = PhotoImage(file=image_path)
        button = tk.Button(
            self.master,
            image=image,
            borderwidth=0,
            highlightthickness=0,
            command=command,
            relief="flat"
        )
        button.image = image  # Mantener referencia
        button.place(x=x, y=y, width=width, height=height)
        setattr(self, f"{name}_image", image)

    def create_product_image(self):
        if self.product.image is None:
            self.product.load_image()

        if self.product.image:
            label = tk.Label(self.master, image=self.product.image)
            label.image = self.product.image  # Keep a reference
            self.canvas.create_window(self.x + 112, self.y + 87, window=label)
        else:
            print(f"Error al cargar la imagen de {self.product.name}")

    def decrease_quantity(self):
        if self.product.quantity > 1:
            self.product.quantity -= 1
            self.update_quantity_display()

    def increase_quantity(self):
        self.product.quantity += 1
        self.update_quantity_display()

    def add_to_cart(self):
        cart.add_product(self.product)
        print(f"Se agrego {self.product.quantity} de {self.product.name} al carrito, "
              f"con un precio unitario de: ${self.product.price:.2f}, "
              f"para un total de: ${self.product.price * self.product.quantity:.2f}")
        print(f"Total en el carrito: ${cart.get_total():.2f}")

    def update_quantity_display(self):
        self.canvas.itemconfig(self.quantity_text, text=str(self.product.quantity))

def create_product_grid(window, canvas, category_id, return_callback):
    products_data = get_products_by_category(category_id)  # Obtener productos por categoría desde la BD
    products = [Product(name, price, image_source) for name, price, image_source in products_data]

    for product in products:
        product.load_image()

    for i, product in enumerate(products):
        x = 19 + (i % 4) * 254
        y = 159 + (i // 4) * 276
        ProductView(window, canvas, product, x, y)

    # Re-crear los elementos superiores
    canvas.create_rectangle(
        0.0,
        0.0,
        1024.0,
        99.0,
        fill="#720902",
        outline=""
    )

    canvas.create_text(
        39.0,
        120.0,
        anchor="nw",
        text="Productos",
        fill="#720902",
        font=("Inter", 25 * -1)
    )

    # Botón de usuario
    user_button_image = PhotoImage(
        file=relative_to_assets("user.png"))
    user_button = tk.Button(
        window,
        image=user_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print(Session.get("usuario")),
        relief="flat"
    )
    user_button.image = user_button_image  # Mantener referencia
    user_button.place(
        x=829.0,
        y=24.0,
        width=171.0,
        height=60.0
    )

    # Botón del carrito
    cart_button_image = PhotoImage(
        file=relative_to_assets("cart.png"))
    cart_button = tk.Button(
        window,
        image=cart_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_cart_view(window, canvas),
        relief="flat"
    )
    cart_button.image = cart_button_image  # Mantener referencia
    cart_button.place(
        x=743.0,
        y=24.0,
        width=50.0,
        height=50.0
    )

    # Botón de búsqueda
    search_button_image = PhotoImage(
        file=relative_to_assets("search.png"))
    search_button = tk.Button(
        window,
        image=search_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("search clicked"),
        relief="flat"
    )
    search_button.image = search_button_image  # Mantener referencia
    search_button.place(
        x=599.0,
        y=24.0,
        width=50.0,
        height=50.0
    )

    # Botón del logo (Inicio)
    logo_button_image = PhotoImage(
        file=relative_to_assets("logo.png"))
    logo_button = tk.Button(
        window,
        image=logo_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: window.destroy() or irse(),
        relief="flat"
    )
    logo_button.image = logo_button_image  # Mantener referencia
    logo_button.place(
        x=54.0,
        y=10.0,
        width=73.0,
        height=70.0
    )

def open_cart_view(window, canvas):
    # Limpiar el canvas actual
    for widget in window.winfo_children():
        widget.destroy()

    # Crear un nuevo canvas
    canvas = tk.Canvas(
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

    canvas.create_text(
        50, 120,
        anchor="nw",
        text="Carrito de Compras",
        fill="#720902",
        font=("Inter", 25 * -1)
    )

    y_position = 160
    for item in cart.get_items():
        product = item['product']
        quantity = item['quantity']
        canvas.create_text(
            50, y_position,
            anchor="nw",
            text=f"{product.name} - ${product.price:.2f} x {quantity} = ${product.price * quantity:.2f}",
            fill="#000000",
            font=("Inter", 16 * -1)
        )
        y_position += 30

    canvas.create_text(
        50, y_position + 20,
        anchor="nw",
        text=f"Total: ${cart.get_total():.2f}",
        fill="#000000",
        font=("Inter", 18 * -1)
    )

    back_button = tk.Button(
        window,
        text="Volver",
        command=lambda: window.destroy() or irse(),
        relief="flat"
    )
    back_button.place(x=50, y=y_position + 60, width=100, height=30)

def main():
    irse()

if __name__ == "__main__":
    main()
