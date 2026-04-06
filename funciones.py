def agregar_producto(inventario, nombre, precio, cantidad):

    """Agrega un diccionario a la lista."""

    inventario.append({
        "nombre": nombre.capitalize(), 
        "precio": precio, 
        "cantidad": cantidad
    })




def buscar_producto(inventario, nombre):

    """Retorna el producto o None."""

    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None




def actualizar_producto(inventario, nombre, n_precio=None, n_cantidad=None):
    """Actualiza datos de un producto existente."""
    p = buscar_producto(inventario, nombre)
    if p:
        if n_precio is not None: p["precio"] = n_precio
        if n_cantidad is not None: p["cantidad"] = n_cantidad
        return True
    return False




def eliminar_producto(inventario, nombre):
    """Elimina por nombre. Retorna True si lo logra."""

    p = buscar_producto(inventario, nombre)
    if p:
        inventario.remove(p)
        return True
    return False



def calcular_estadisticas(inventario):

    """Calcula totales y destacados."""


    if not inventario: return None
    v_total = sum(p["precio"] * p["cantidad"] for p in inventario)
    u_total = sum(p["cantidad"] for p in inventario)
    return {
        "v_total": v_total, "u_total": u_total,
        "caro": max(inventario, key=lambda x: x["precio"]),
        "stock": max(inventario, key=lambda x: x["cantidad"])
    }