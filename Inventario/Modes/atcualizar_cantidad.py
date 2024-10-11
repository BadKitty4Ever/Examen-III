from Service.inventario import actualizar_cantidad

def actualizar_cantidad_mode():
    nombre = input("Ingrese el nombre del producto: ")
    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
    actualizar_cantidad(nombre, nueva_cantidad)
    print(f"Cantidad del producto '{nombre}' actualizada.")