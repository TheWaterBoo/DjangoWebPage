from django.contrib import admin
from .models import Producto, Pedido, DetallePedido, Categoria, Cliente

# Register your models here.
admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(DetallePedido)
admin.site.register(Categoria)
admin.site.register(Cliente)
