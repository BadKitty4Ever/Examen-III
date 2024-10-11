from Service.inventario import agregar_producto
from Controller.validar_precio import validar_precio

def agregar_producto_mode():
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))
    
    if validar_precio(precio):
        agregar_producto(nombre, cantidad, precio)
        print(f"Producto '{nombre}' agregado.")
    else:
        print("Precio inválido.")