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

def registrar_producto(productos):
    print("\n========== REGISTRAR PRODUCTO ==========")
    codigo = input("Código del producto: ").strip().upper()

    if not codigo:
        print("Error: el código no puede estar vacío.")
        return

    for producto in productos:
        if producto["codigo"] == codigo:
            print("Error: el código del producto ya existe.")
            return

    nombre = input("Nombre del producto: ").strip()
    if not nombre:
        print("Error: el nombre no puede estar vacío.")
        return

    categoria = input("Categoría: ").strip()
    if not categoria:
        print("Error: la categoría no puede estar vacía.")
        return

    unidad = input("Unidad de medida: ").strip()
    if not unidad:
        print("Error: la unidad no puede estar vacía.")
        return

    while True:
        try:
            precio = float(input("Precio: "))
            if precio > 0:
                break
            print("Error: el precio debe ser mayor que 0.")
        except ValueError:
            print("Error: ingrese un precio válido.")

    while True:
        try:
            stock_minimo = int(input("Stock mínimo: "))
            if stock_minimo >= 0:
                break
            print("Error: el stock mínimo no puede ser negativo.")
        except ValueError:
            print("Error: ingrese un número entero válido.")

    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "unidad": unidad,
        "precio": precio,
        "stock_minimo": stock_minimo,
        "activo": True
    }

    productos.append(producto)
    guardar_datos(RUTA_PRODUCTOS, productos)
    print("Producto registrado correctamente.")

def listar_productos(productos):
    print("\n========== PRODUCTOS ACTIVOS ==========")
    productos_activos = [producto for producto in productos if producto["activo"]]

    if not productos_activos:
        print("No hay productos activos registrados.")
        return

    for producto in productos_activos:
        print("-----------------------------------")
        print("Código:", producto["codigo"])
        print("Nombre:", producto["nombre"])
        print("Categoría:", producto["categoria"])
        print("Unidad:", producto["unidad"])
        print("Precio:", producto["precio"])
        print("Stock mínimo:", producto["stock_minimo"])

def buscar_producto(productos):
    print("\n========== BUSCAR PRODUCTO ==========")
    busqueda = input("Ingrese código o parte del nombre: ").strip().lower()

    if not busqueda:
        print("Error: debe ingresar un criterio de búsqueda.")
        return

    encontrados = []

    for producto in productos:
        if not producto["activo"]:
            continue

        if busqueda in producto["codigo"].lower() or busqueda in producto["nombre"].lower():
            encontrados.append(producto)

    if not encontrados:
        print("No se encontraron productos.")
        return

    for producto in encontrados:
        print("-----------------------------------")
        print("Código:", producto["codigo"])
        print("Nombre:", producto["nombre"])
        print("Categoría:", producto["categoria"])
        print("Unidad:", producto["unidad"])
        print("Precio:", producto["precio"])
        print("Stock mínimo:", producto["stock_minimo"])

def actualizar_producto(productos):
    print("\n========== ACTUALIZAR PRODUCTO ==========")
    codigo = input("Código del producto a actualizar: ").strip().upper()

    producto_encontrado = None

    for producto in productos:
        if producto["codigo"] == codigo:
            producto_encontrado = producto
            break

    if producto_encontrado is None:
        print("Error: producto no encontrado.")
        return

    nombre = input(f"Nombre [{producto_encontrado['nombre']}]: ").strip()
    categoria = input(f"Categoría [{producto_encontrado['categoria']}]: ").strip()
    unidad = input(f"Unidad [{producto_encontrado['unidad']}]: ").strip()

    if nombre:
        producto_encontrado["nombre"] = nombre
    if categoria:
        producto_encontrado["categoria"] = categoria
    if unidad:
        producto_encontrado["unidad"] = unidad

    while True:
        precio = input(f"Precio [{producto_encontrado['precio']}]: ").strip()

        if precio == "":
            break

        try:
            precio = float(precio)
            if precio > 0:
                producto_encontrado["precio"] = precio
                break
            print("Error: el precio debe ser mayor que 0.")
        except ValueError:
            print("Error: ingrese un precio válido.")

    while True:
        stock_minimo = input(f"Stock mínimo [{producto_encontrado['stock_minimo']}]: ").strip()

        if stock_minimo == "":
            break

        try:
            stock_minimo = int(stock_minimo)
            if stock_minimo >= 0:
                producto_encontrado["stock_minimo"] = stock_minimo
                break
            print("Error: el stock mínimo no puede ser negativo.")
        except ValueError:
            print("Error: ingrese un número entero válido.")

    guardar_datos(RUTA_PRODUCTOS, productos)
    print("Producto actualizado correctamente.")

def desactivar_producto(productos):
    print("\n========== DESACTIVAR PRODUCTO ==========")
    codigo = input("Código del producto: ").strip().upper()

    for producto in productos:
        if producto["codigo"] == codigo:
            if not producto["activo"]:
                print("El producto ya está desactivado.")
                return

            producto["activo"] = False
            guardar_datos(RUTA_PRODUCTOS, productos)
            print("Producto desactivado correctamente.")
            return

    print("Error: producto no encontrado.")
def activar_producto(productos):
    print("\n========== ACTIVAR PRODUCTO ==========")
    codigo = input("Código del producto: ").strip().upper()

    for producto in productos:
        if producto["codigo"] == codigo:
            if producto["activo"]:
                print("El producto ya está activo.")
                return

            producto["activo"] = True
            guardar_datos(RUTA_PRODUCTOS, productos)
            print("Producto activado correctamente.")
            return

    print("Error: producto no encontrado.")

def menu_productos(productos):
    while True:
        print("\n========== GESTIÓN DE PRODUCTOS ==========")
        print("1. Registrar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Desactivar producto")
        print("6. Activar producto")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto(productos)
        elif opcion == "2":
            listar_productos(productos)
        elif opcion == "3":
            buscar_producto(productos)
        elif opcion == "4":
            actualizar_producto(productos)
        elif opcion == "5":
            desactivar_producto(productos)
        elif opcion =="6":
            activar_producto(productos)
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

def mostrar_menu():
    print("\n========== AGROCONTROL CBA ==========")
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

    print("AgroControl CBA iniciado.")
    print("Productos:", len(productos))
    print("Lotes:", len(lotes))
    print("Movimientos:", len(movimientos))
    print("Ventas:", len(ventas))

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_productos(productos)
        elif opcion == "0":
            print("Saliendo de AgroControl CBA...")
            break
        else:
            print("Opción no implementada todavía.")

if __name__ == "__main__":
    main()