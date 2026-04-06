import csv

def guardar_csv(inventario, ruta):
    """Guarda la lista en un archivo CSV."""
    try:
        with open(ruta, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["nombre", "precio", "cantidad"])
            writer.writeheader()
            writer.writerows(inventario)
        return True
    except Exception: return False

def cargar_csv(ruta):
    """Carga y valida filas del CSV."""
    productos, errores = [], 0
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for fila in reader:
                try:
                    p, c = float(fila["precio"]), int(fila["cantidad"])
                    if p < 0 or c < 0: raise ValueError
                    productos.append({"nombre": fila["nombre"], "precio": p, "cantidad": c})
                except: errores += 1
        return productos, errores
    except FileNotFoundError: return None, 0