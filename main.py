import json
import os

RUTA_PRODUCTOS = "data/productos.json"
RUTA_LOTES = "data/lotes.json"
RUTA_MOVIMIENTOS = "data/movimientos.json"
RUTA_VENTAS = "data/ventas.json"

def cargar_datos(ruta):
    if not os.path.exists(ruta):
        return []

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (json.JSONDecodeError, OSError):
        return []

def guardar_datos(ruta, datos):
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
    except OSError as error:
        print("Error al guardar los datos:", error)

def cargar_todos_los_datos():
    productos = cargar_datos(RUTA_PRODUCTOS)
    lotes = cargar_datos(RUTA_LOTES)
    movimientos = cargar_datos(RUTA_MOVIMIENTOS)
    ventas = cargar_datos(RUTA_VENTAS)

    return productos, lotes, movimientos, ventas

def mostrar_menu():
    print("==============================")
    print("      AGROCONTROL CBA")
    print("==============================")
    print("1. Gestión de productos")
    print("2. Gestión de lotes productivos")
    print("3. Movimientos de inventario")
    print("4. Registrar venta")
    print("5. Consultar ventas")
    print("6. Alertas de stock")
    print("7. Reportes")
    print("8. Guardar datos")
    print("0. Salir")


def main():
    productos, lotes, movimientos, ventas = cargar_todos_los_datos()

    print("Datos cargados correctamente.")
    print("Productos:", len(productos))
    print("Lotes:", len(lotes))
    print("Movimientos:", len(movimientos))
    print("Ventas:", len(ventas))

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            print("Saliendo de AgroControl CBA...")
            break

        print("Opción seleccionada:", opcion)


if __name__ == "__main__":
    main()