from django.shortcuts import redirect, render

from .storeCart import storeCart
from .models import Producto

# Create your views here.
def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda.html", {'productos': productos})

def agregar_producto(request, producto_id):
    carrito = storeCart(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.addProduct(producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = storeCart(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_carrito(request, producto_id):
    carrito = storeCart(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.quitar(producto)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = storeCart(request)
    carrito.clean()
    return redirect("Tienda")