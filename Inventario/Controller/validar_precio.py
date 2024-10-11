def validar_precio(precio):
    return isinstance(precio, (int, float)) and precio >= 0
