from Service.inventario import calcular_valor_total

def mostrar_valor_total_mode():
    total = calcular_valor_total()
    print(f"El valor total del inventario es: {total}")