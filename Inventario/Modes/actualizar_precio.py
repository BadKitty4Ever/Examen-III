from Service.inventario import actualizar_precio
from Controller.validar_precio import validar_precio

def actualizar_precio_mode():
    nombre = input("Ingrese el nombre del producto: ")
    nuevo_precio = float(input("Ingrese el nuevo precio: "))
    
    if validar_precio(nuevo_precio):
        actualizar_precio(nombre, nuevo_precio)
        print(f"Precio del producto '{nombre}' actualizado.")
    else:
        print("Precio inválido.")