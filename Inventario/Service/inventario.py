productos = {}

def agregar_producto(nombre, cantidad, precio):
    if nombre in productos:
        productos[nombre]['cantidad'] += cantidad
    else:
        productos[nombre] = {'cantidad': cantidad, 'precio': precio}

def eliminar_producto(nombre):
    if nombre in productos:
        del productos[nombre]

def actualizar_precio(nombre, nuevo_precio):
    if nombre in productos:
        productos[nombre]['precio'] = nuevo_precio

def actualizar_cantidad(nombre, nueva_cantidad):
    if nombre in productos:
        productos[nombre]['cantidad'] = nueva_cantidad

def mostrar_inventario():
    return productos

def calcular_valor_total():
    total = sum(item['cantidad'] * item['precio'] for item in productos.values())
    return total
