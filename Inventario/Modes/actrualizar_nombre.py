from Service.inventario import productos

def actualizar_nombre_mode():
    nombre_actual = input("Ingrese el nombre actual del producto: ")
    nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
    
    if nombre_actual in productos:
        productos[nuevo_nombre] = productos.pop(nombre_actual)
        print(f"Nombre del producto actualizado de '{nombre_actual}' a '{nuevo_nombre}'.")
    else:
        print("Producto no encontrado.")