"""
Módulo de Persistencia
"""

def guardar_pedido(nombre, apellidos):
    """
    Guarda el pedido en el archivo pedidos.txt
    """
    
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write(nombre + " " + apellidos + "\n")
        file.close()
