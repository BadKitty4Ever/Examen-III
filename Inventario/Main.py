import os
from Modes.menu import mostrar_menu
from Modes.agregar_producto import agregar_producto_mode
from Modes.eliminar_producto import eliminar_producto_mode
from Modes.mostrar_inventario import mostrar_inventario_mode
from Modes.mostrar_valor_total import mostrar_valor_total_mode
from Modes.actrualizar_nombre import actualizar_nombre_mode
from Modes.atcualizar_cantidad import actualizar_cantidad_mode
from Modes.actualizar_precio import actualizar_precio_mode

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_producto_mode()
        elif opcion == '2':
            eliminar_producto_mode()
        elif opcion == '3':
            mostrar_inventario_mode()
        elif opcion == '4':
            mostrar_valor_total_mode()
        elif opcion == '5':
            actualizar_nombre_mode()
        elif opcion == '6':
            actualizar_cantidad_mode()
        elif opcion == '7':
            actualizar_precio_mode()
        elif opcion == '0':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()