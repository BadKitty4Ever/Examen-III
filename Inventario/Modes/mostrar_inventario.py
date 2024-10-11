from Service.inventario import mostrar_inventario

def mostrar_inventario_mode():
    inventario = mostrar_inventario()
    if inventario:
        print("Inventario:")
        for nombre, detalles in inventario.items():
            print(f"Nombre: {nombre}, Cantidad: {detalles['cantidad']}, Precio: {detalles['precio']}")
    else:
        print("El inventario está vacío.")