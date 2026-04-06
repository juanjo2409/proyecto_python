from funciones import *
from archivos import *

def pedir_numero(mensaje, tipo):
    """Valida que la entrada sea número y no negativo."""
    while True:
        try:
            valor = tipo(input(mensaje))
            if valor < 0:
                print("No se permiten números negativos.")
                continue
            return valor
        except ValueError:
            print(f"Error: Ingrese un valor {'entero' if tipo == int else 'decimal'} válido.")

def menu():
    inventario = []
    ruta = "inventario_final.csv"

    while True:
        print("\n" + "="*30 + "\n  SISTEMA DE GESTIÓN TOTAL\n" + "="*30)
        print("1. Agregar      2. Mostrar     3. Buscar")
        print("4. Actualizar   5. Eliminar    6. Estadísticas")
        print("7. Guardar CSV  8. Cargar CSV  9. Salir")
        
        option = input("\nSeleccione (1-9): ")

        if option == "1":
            nombre = input("Nombre: ")
            precio = pedir_numero("Precio: ", float)
            cantidad = pedir_numero("Cantidad: ", int)
            agregar_producto(inventario, nombre, precio, cantidad)
            print("Producto registrado.")

        elif option == "2":
            if not inventario: 
                print("Inventario vacío.")
                continue
            for p in inventario:
                print(f"{p['nombre']} | ${p['precio']} | Stock: {p['cantidad']}")

        elif option == "3":
            nombre = input("Nombre a buscar: ")
            producto = buscar_producto(inventario, nombre)
            if producto:
                print(f" Resultado: {producto}")
            else:
                print("No encontrado.")

        elif option == "4":
            nombre = input("Nombre a editar: ")
            pr = input("Nuevo precio (Enter para omitir): ")
            ca = input("Nueva cantidad (Enter para omitir): ")

            precio = float(pr) if pr else None
            cantidad = int(ca) if ca else None

            if actualizar_producto(inventario, nombre, precio, cantidad):
                print("Actualizado.")
            else:
                print("No encontrado.")

        elif option == "5":
            nombre = input("Nombre a eliminar: ")
            if eliminar_producto(inventario, nombre):
                print(" Eliminado.")
            else:
                print("No encontrado.")

        elif option == "6":
            s = calcular_estadisticas(inventario)
            if s:
                print(f"Valor Total: ${s['v_total']:,.2f} | Unidades: {s['u_total']}")
                print(f"Más caro: {s['caro']['nombre']} | Mayor Stock: {s['stock']['nombre']}")
            else:
                print("Sin datos.")

        elif option == "7":
            if guardar_csv(inventario, ruta):
                print(f"Guardado en {ruta}")
            else:
                print("Error al guardar.")

        elif option == "8":
            nuevos, err = cargar_csv(ruta)
            if nuevos is not None:
                resp = input("¿Sobrescribir (S) o Fusionar (N)?: ").upper()
                if resp == "S":
                    inventario = nuevos
                else:
                    for nuevo in nuevos:
                        existente = buscar_producto(inventario, nuevo["nombre"])
                        if existente:
                            existente["cantidad"] += nuevo["cantidad"]
                        else:
                            inventario.append(nuevo)
                print(f"Carga completa. Filas inválidas omitidas: {err}")

        elif option == "9":
            print("Saliendo del sistema...")
            break

        else:
            print(f"'{option}' no es una opción válida (1-9).")

if __name__ == "__main__":
    menu()

