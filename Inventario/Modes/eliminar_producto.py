from Service.inventario import eliminar_producto

def eliminar_producto_mode():
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    eliminar_producto(nombre)
    print(f"Producto '{nombre}' eliminado.")