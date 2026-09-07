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
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            print("Saliendo de AgroControl CBA...")
            break

        print("Opción seleccionada:", opcion)


if __name__ == "__main__":
    main()