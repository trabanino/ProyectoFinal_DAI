# cart.py
class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        for item in self.items:
            if item['product'].name == product.name:
                item['quantity'] += product.quantity
                return
        self.items.append({'product': product, 'quantity': product.quantity})

    def remove_product(self, product):
        for item in self.items:
            if item['product'].name == product.name:
                self.items.remove(item)
                return

    def get_total(self):
        total = 0
        for item in self.items:
            total += item['product'].price * item['quantity']
        return total

    def get_items(self):
        return self.items
