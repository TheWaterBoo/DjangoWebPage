class storeCart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session["cart"]
        if not cart:
            self.session["cart"] = {}
            self.cart = self.session["cart"]
        else:
            self.cart = cart

    def addProduct(self, producto):
        id = str(producto.id)
        if id not in self.cart.keys():
            self.cart[id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio_total   ": producto.precio,
                "cantidad": 1
            }
        else:
            self.cart[id]["cantidad"] += 1
            self.cart[id]["precio_total"] += producto.precio
        self.save_cart()

    def guardar_cart(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.cart:
            del self.cart[id]
            self.save_cart()

    def quitar(self, producto):
        id = str(producto.id)
        if id in self.cart.keys():
            self.cart[id]["cantidad"] -= 1
            self.cart[id]["precio_total"] -= producto.precio
            if self.cart[id]["cantidad"] <= 0: self.eliminar(producto)
            self.save_cart()

    def clean(self):
        self.session["cart"] = {}
        self.session.modified = True