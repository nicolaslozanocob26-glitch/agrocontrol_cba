import json
import os
from datetime import datetime

RUTA_PRODUCTOS = "data/productos.json"
RUTA_LOTES = "data/lotes.json"
RUTA_MOVIMIENTOS = "data/movimientos.json"
RUTA_VENTAS = "data/ventas.json"

def cargar_datos(ruta):
    if not os.path.exists(ruta):
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        return []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (json.JSONDecodeError, OSError):
        return []

def guardar_datos(ruta, datos):
    try:
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
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
    
    while True:
        codigo = input("Código del producto: ").strip().upper()
        
        if not codigo:
            print("Error: el código no puede estar vacío.")
            continue
        
        codigo_existe = False
        for producto in productos:
            if producto["codigo"] == codigo:
                codigo_existe = True
                break
        
        if codigo_existe:
            print("Error: el código del producto ya existe.")
            continue
        
        break
    
    while True:
        nombre = input("Nombre del producto: ").strip()
        if not nombre:
            print("Error: el nombre no puede estar vacío.")
            continue
        break
    
    while True:
        categoria = input("Categoría: ").strip()
        if not categoria:
            print("Error: la categoría no puede estar vacía.")
            continue
        break
    
    while True:
        unidad = input("Unidad: ").strip()
        if not unidad:
            print("Error: la unidad no puede estar vacía.")
            continue
        break
    
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
    print("\n╔══════════════════════════════════════════════════════════════════════════════════╗")
    print("║                              PRODUCTOS ACTIVOS                                   ║")
    print("╠══════════════════════════════════════════════════════════════════════════════════╣")

    productos_activos = [producto for producto in productos if producto["activo"]]

    if not productos_activos:
        print("║              No hay productos activos registrados.                               ║")
        print("╚══════════════════════════════════════════════════════════════════════════════════╝")
        return

    print(f"║ {'Código':<10} {'Nombre':<20} {'Categoría':<15} {'Unidad':<10} {'Precio':<12} {'Stock mínimo':<8} ║")
    print("╠══════════════════════════════════════════════════════════════════════════════════╣")

    for producto in productos_activos:
        codigo = producto["codigo"][:10]
        nombre = producto["nombre"][:20]
        categoria = producto["categoria"][:15]
        unidad = producto["unidad"][:10]
        precio = f"${producto['precio']:,.0f}".replace(",", ".")
        stock_minimo = str(producto["stock_minimo"])

        print(f"║ {codigo:<10} {nombre:<20} {categoria:<15} {unidad:<10} {precio:<12} {stock_minimo:<8} ║")

    print("╚══════════════════════════════════════════════════════════════════════════════════╝")
    print(f"Total productos activos: {len(productos_activos)}")

def buscar_producto(productos):
    print("\n========== BUSCAR PRODUCTO ==========")
    
    while True:
        busqueda = input("Ingrese código o parte del nombre: ").strip().lower()
        
        if not busqueda:
            print("Error: debe ingresar un criterio de búsqueda.")
            continue
        
        break

    encontrados = []

    for producto in productos:
        if not producto["activo"]:
            continue

        if busqueda in producto["codigo"].lower() or busqueda in producto["nombre"].lower():
            encontrados.append(producto)

    if not encontrados:
        print("No se encontraron productos.")
        return

    print("\n" + "-" * 80)
    print(f"{'Código':<10} {'Nombre':<20} {'Categoría':<15} {'Unidad':<10} {'Precio':<12} {'Stock Min':<10}")
    print("-" * 80)

    for producto in encontrados:
        codigo = producto["codigo"][:10]
        nombre = producto["nombre"][:20]
        categoria = producto["categoria"][:15]
        unidad = producto["unidad"][:10]
        precio = f"Precio: ${producto['precio']:,.0f}".replace(",", ".")
        stock_minimo = str(producto["stock_minimo"])
        
        print(f"{codigo:<10} {nombre:<20} {categoria:<15} {unidad:<10} {precio:<12} {stock_minimo:<10}")

    print("-" * 80)
    print(f"Productos encontrados: {len(encontrados)}")

def actualizar_producto(productos):
    print("\n========== ACTUALIZAR PRODUCTO ==========")
    
    while True:
        codigo = input("Código del producto a actualizar: ").strip().upper()
        
        if not codigo:
            print("Error: el código no puede estar vacío.")
            continue
        
        producto_encontrado = None

        for producto in productos:
            if producto["codigo"] == codigo:
                producto_encontrado = producto
                break

        if producto_encontrado is None:
            print("Error: producto no encontrado. Intente nuevamente.")
            continue
        
        break

    print("Deje vacío un campo si desea conservar su valor actual.")
    
    nombre = input(f"Nombre [{producto_encontrado['nombre']}]: ").strip()
    if nombre:
        producto_encontrado["nombre"] = nombre
    
    categoria = input(f"Categoría [{producto_encontrado['categoria']}]: ").strip()
    if categoria:
        producto_encontrado["categoria"] = categoria
    
    unidad = input(f"Unidad [{producto_encontrado['unidad']}]: ").strip()
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
    
    while True:
        codigo = input("Código del producto: ").strip().upper()
        
        if not codigo:
            print("Error: el código no puede estar vacío.")
            continue
        
        producto_encontrado = None
        
        for producto in productos:
            if producto["codigo"] == codigo:
                producto_encontrado = producto
                break

        if producto_encontrado is None:
            print("Error: producto no encontrado. Intente nuevamente.")
            continue
        
        if not producto_encontrado["activo"]:
            print("El producto ya está desactivado.")
            return

        producto_encontrado["activo"] = False
        guardar_datos(RUTA_PRODUCTOS, productos)
        print("Producto desactivado correctamente.")
        return

def activar_producto(productos):
    print("\n========== ACTIVAR PRODUCTO ==========")
    
    while True:
        codigo = input("Código del producto: ").strip().upper()
        
        if not codigo:
            print("Error: el código no puede estar vacío.")
            continue
        
        producto_encontrado = None
        
        for producto in productos:
            if producto["codigo"] == codigo:
                producto_encontrado = producto
                break

        if producto_encontrado is None:
            print("Error: producto no encontrado. Intente nuevamente.")
            continue
        
        if producto_encontrado["activo"]:
            print("El producto ya está activo.")
            return

        producto_encontrado["activo"] = True
        guardar_datos(RUTA_PRODUCTOS, productos)
        print("Producto activado correctamente.")
        return

def registrar_lote(lotes, productos):
    print("\n========== REGISTRAR LOTE ==========")

    id_lote = input("ID del lote: ").strip().upper()

    if not id_lote:
        print("Error: el ID no puede estar vacío.")
        return

    for lote in lotes:
        if lote["id_lote"] == id_lote:
            print("Error: el ID del lote ya existe.")
            return

    codigo = input("Código del producto: ").strip().upper()

    producto_encontrado = None

    for producto in productos:
        if producto["codigo"] == codigo and producto["activo"]:
            producto_encontrado = producto
            break

    if producto_encontrado is None:
        print("Error: el producto no existe o está desactivado.")
        return

    fecha = input("Fecha de siembra (AAAA-MM-DD): ").strip()

    try:
        datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError:
        print("Error: formato de fecha inválido.")
        return

    while True:
        try:
            area = float(input("Área en m2: "))

            if area > 0:
                break

            print("Error: el área debe ser mayor que 0.")

        except ValueError:
            print("Error: ingrese un número válido.")

    lote = {
        "id_lote": id_lote,
        "producto_codigo": producto_encontrado["codigo"],
        "fecha_siembra": fecha,
        "area_m2": area,
        "cantidad_producida": 0,
        "estado": "EN_PRODUCCION"
    }

    lotes.append(lote)
    guardar_datos(RUTA_LOTES, lotes)

    print("Lote registrado correctamente.")


def listar_lotes(lotes, productos):
    print("\n╔══════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("║                                    LOTES PRODUCTIVOS                                             ║")
    print("╠══════════════════════════════════════════════════════════════════════════════════════════════════╣")

    if not lotes:
        print("║                            No hay lotes registrados.                                             ║")
        print("╚══════════════════════════════════════════════════════════════════════════════════════════════════╝")
        return

    print(f"║ {'ID Lote':<10} {'Producto':<20} {'Fecha Siembra':<15} {'Área m²':<10} {'Cantidad':<12} {'Estado':<15}          ║")
    print("╠══════════════════════════════════════════════════════════════════════════════════════════════════╣")

    for lote in lotes:
        nombre_producto = "No encontrado"

        for producto in productos:
            if producto["codigo"] == lote["producto_codigo"]:
                nombre_producto = producto["nombre"]
                break

        id_lote = lote["id_lote"][:10]
        producto = f"{lote['producto_codigo']} - {nombre_producto}"[:20]
        fecha = lote["fecha_siembra"][:15]
        area = f"{lote['area_m2']:.2f}"
        cantidad = str(lote["cantidad_producida"])
        estado = lote["estado"][:15]

        print(f"║ {id_lote:<10} {producto:<20} {fecha:<15} {area:<10} {cantidad:<12} {estado:<15}          ║")

    print("╚══════════════════════════════════════════════════════════════════════════════════════════════════╝")
    print(f"Total de lotes: {len(lotes)}")

def cambiar_estado_lote(lotes):
    print("\n========== CAMBIAR ESTADO DE LOTE ==========")

    id_lote = input("ID del lote: ").strip().upper()

    lote_encontrado = None

    for lote in lotes:
        if lote["id_lote"] == id_lote:
            lote_encontrado = lote
            break

    if lote_encontrado is None:
        print("Error: lote no encontrado.")
        return

    if lote_encontrado["estado"] == "COSECHADO":
        print("Error: un lote cosechado no puede volver a cambiar de estado.")
        return

    print("1. EN_PRODUCCION")
    print("2. CANCELADO")

    opcion = input("Seleccione el nuevo estado: ")

    if opcion == "1":
        lote_encontrado["estado"] = "EN_PRODUCCION"

    elif opcion == "2":
        lote_encontrado["estado"] = "CANCELADO"

    else:
        print("Opción inválida.")
        return

    guardar_datos(RUTA_LOTES, lotes)

    print("Estado actualizado correctamente.")

def calcular_stock(producto_codigo, movimientos):
    stock = 0

    for movimiento in movimientos:
        if movimiento["producto_codigo"] == producto_codigo:
            if movimiento["tipo"] == "ENTRADA":
                stock += movimiento["cantidad"]
            elif movimiento["tipo"] == "SALIDA":
                stock -= movimiento["cantidad"]

    return stock

def registrar_entrada(movimientos, productos):
    print("\n========== REGISTRAR ENTRADA ==========")

    codigo = input("Código del producto: ").strip().upper()

    producto_encontrado = None

    for producto in productos:
        if producto["codigo"] == codigo and producto["activo"]:
            producto_encontrado = producto
            break

    if producto_encontrado is None:
        print("Error: producto no encontrado o desactivado.")
        return

    while True:
        try:
            cantidad = int(input("Cantidad de entrada: "))

            if cantidad > 0:
                break

            print("Error: la cantidad debe ser mayor que 0.")
        except ValueError:
            print("Error: ingrese un número entero válido.")

    while True:
        motivo = input("Motivo de la entrada: ").strip()

        if motivo:
            break

        print("Error: el motivo es obligatorio.")

    numero = len(movimientos) + 1
    id_movimiento = f"M{numero:04d}"

    movimiento = {
        "id": id_movimiento,
        "producto_codigo": codigo,
        "tipo": "ENTRADA",
        "cantidad": cantidad,
        "motivo": motivo,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    movimientos.append(movimiento)
    guardar_datos(RUTA_MOVIMIENTOS, movimientos)

    print("Entrada registrada correctamente.")
    print("Movimiento generado:", id_movimiento)

def registrar_salida(movimientos, productos):
    print("\n========== REGISTRAR SALIDA ==========")

    codigo = input("Código del producto: ").strip().upper()

    producto_encontrado = None

    for producto in productos:
        if producto["codigo"] == codigo and producto["activo"]:
            producto_encontrado = producto
            break

    if producto_encontrado is None:
        print("Error: producto no encontrado o desactivado.")
        return

    stock_actual = calcular_stock(codigo, movimientos)

    print("Stock actual:", stock_actual)

    while True:
        try:
            cantidad = int(input("Cantidad de salida: "))

            if cantidad <= 0:
                print("Error: la cantidad debe ser mayor que 0.")
            elif cantidad > stock_actual:
                print("Error: no hay suficiente stock.")
            else:
                break

        except ValueError:
            print("Error: ingrese un número entero válido.")

    motivo = input("Motivo de la salida: ").strip()

    numero = len(movimientos) + 1
    id_movimiento = f"M{numero:04d}"

    movimiento = {
        "id": id_movimiento,
        "producto_codigo": codigo,
        "tipo": "SALIDA",
        "cantidad": cantidad,
        "motivo": motivo,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    movimientos.append(movimiento)

    guardar_datos(RUTA_MOVIMIENTOS, movimientos)

    print("Salida registrada correctamente.")
    print("Movimiento generado:", id_movimiento)

def listar_inventario(productos, movimientos):
    print("\n╔══════════════════════════════════════════════════════════════════════════════════╗")
    print("║                                INVENTARIO                                        ║")
    print("╠══════════════════════════════════════════════════════════════════════════════════╣")

    if not productos:
        print("║                    No hay productos registrados.                                ║")
        print("╚══════════════════════════════════════════════════════════════════════════════════╝")
        return

    print(f"║ {'Código':<10} {'Producto':<20} {'Unidad':<10} {'Stock':<10} {'Mínimo':<10} {'Estado':<15} ║")
    print("╠══════════════════════════════════════════════════════════════════════════════════╣")

    for producto in productos:
        if not producto["activo"]:
            continue

        stock = calcular_stock(producto["codigo"], movimientos)

        if stock <= producto["stock_minimo"]:
            estado = "BAJO"
        else:
            estado = "OK"

        codigo = producto["codigo"][:10]
        nombre = producto["nombre"][:20]
        unidad = producto["unidad"][:10]
        stock_actual = str(stock)
        stock_minimo = str(producto["stock_minimo"])

        print(
            f"║ {codigo:<10} "
            f"{nombre:<20} "
            f"{unidad:<10} "
            f"{stock_actual:<10} "
            f"{stock_minimo:<10} "
            f"{estado:<15} ║"
        )

    print("╚══════════════════════════════════════════════════════════════════════════════════╝")

def alertas_stock(productos, movimientos):
    print("\n╔═══════════════════════════════════════════════════════╗")
    print("║                   ALERTAS DE STOCK                    ║")
    print("╠═══════════════════════════════════════════════════════╣")

    alertas = []

    for producto in productos:
        if not producto["activo"]:
            continue

        stock = calcular_stock(producto["codigo"], movimientos)

        if stock <= producto["stock_minimo"]:
            alertas.append((producto, stock))

    if not alertas:
        print("║              No hay productos con stock bajo.                     ║")
        print("╚══════════════════════════════════════════════════════════════════════╝")
        return

    print(f"║ {'Código':<10} {'Producto':<20} {'Stock':<10} {'Mínimo':<10} ║")
    print("╠═══════════════════════════════════════════════════════╣")

    for producto, stock in alertas:
        codigo = producto["codigo"][:10]
        nombre = producto["nombre"][:20]
        minimo = str(producto["stock_minimo"])

        print(f"║ {codigo:<10} {nombre:<20} {stock:<10} {minimo:<10} ║")

    print("╚═══════════════════════════════════════════════════════╝")
    print(f"Productos con stock bajo: {len(alertas)}")

def menu_inventario(movimientos, productos):
    while True:
        print("\n========== INVENTARIO ==========")
        print("1. Registrar entrada")
        print("2. Registrar salida")
        print("3. Listar inventario")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_entrada(movimientos, productos)
        elif opcion == "2":
            registrar_salida(movimientos, productos)
        elif opcion == "3":
            listar_inventario(productos, movimientos)
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")



def menu_lotes(lotes, productos, movimientos):
    while True:
        print("\n========== GESTIÓN DE LOTES ==========")
        print("1. Registrar lote")
        print("2. Listar lotes")
        print("3. Cambiar estado de lote")
        print("4. Cosechar lote")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_lote(lotes, productos)

        elif opcion == "2":
            listar_lotes(lotes, productos)

        elif opcion == "3":
            cambiar_estado_lote(lotes)

        elif opcion == "4":
            cosechar_lote(lotes, movimientos)

        elif opcion == "0":
            break

        else:
            print("Opción inválida.")


def cosechar_lote(lotes, movimientos):
    print("\n========== COSECHAR LOTE ==========")

    id_lote = input("ID del lote: ").strip().upper()

    lote_encontrado = None

    for lote in lotes:
        if lote["id_lote"] == id_lote:
            lote_encontrado = lote
            break

    if lote_encontrado is None:
        print("Error: lote no encontrado.")
        return

    if lote_encontrado["estado"] == "COSECHADO":
        print("Error: el lote ya fue cosechado.")
        return

    if lote_encontrado["estado"] == "CANCELADO":
        print("Error: el lote está cancelado.")
        return

    while True:
        try:
            cantidad = int(input("Cantidad producida: "))

            if cantidad > 0:
                break

            print("Error: la cantidad debe ser mayor que 0.")

        except ValueError:
            print("Error: ingrese un número entero válido.")

    lote_encontrado["cantidad_producida"] = cantidad
    lote_encontrado["estado"] = "COSECHADO"

    numero = len(movimientos) + 1
    id_movimiento = f"M{numero:04d}"

    movimiento = {
        "id": id_movimiento,
        "producto_codigo": lote_encontrado["producto_codigo"],
        "tipo": "ENTRADA",
        "cantidad": cantidad,
        "motivo": f"Cosecha lote {id_lote}",
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    movimientos.append(movimiento)

    guardar_datos(RUTA_LOTES, lotes)
    guardar_datos(RUTA_MOVIMIENTOS, movimientos)

    print("Lote cosechado correctamente.")
    print("Movimiento generado:", id_movimiento)


def registrar_venta(ventas, movimientos, productos):
    print("\n========== REGISTRAR VENTA ==========")

    items = []

    while True:
        codigo = input("Código del producto (0 para finalizar): ").strip().upper()

        if codigo == "0":
            break

        producto_encontrado = None

        for producto in productos:
            if producto["codigo"] == codigo and producto["activo"]:
                producto_encontrado = producto
                break

        if producto_encontrado is None:
            print("Error: producto no encontrado o desactivado.")
            continue

        for item in items:
            if item["codigo"] == codigo:
                print("Error: el producto ya fue agregado a la venta.")
                producto_encontrado = None
                break

        if producto_encontrado is None:
            continue

        stock_actual = calcular_stock(codigo, movimientos)

        print("Stock disponible:", stock_actual)

        while True:
            try:
                cantidad = int(input("Cantidad: "))

                if cantidad <= 0:
                    print("Error: la cantidad debe ser mayor que 0.")
                elif cantidad > stock_actual:
                    print("Error: stock insuficiente.")
                else:
                    break
            except ValueError:
                print("Error: ingrese un número entero válido.")

        precio_unitario = producto_encontrado["precio"]
        subtotal = cantidad * precio_unitario

        item = {
            "codigo": codigo,
            "cantidad": cantidad,
            "precio_unitario": precio_unitario,
            "subtotal": subtotal
        }

        items.append(item)

        print("Producto agregado.")
        print("Subtotal:", f"${subtotal:,.0f}".replace(",", "."))

    if not items:
        print("Venta cancelada.")
        return

    numero = len(ventas) + 1
    id_venta = f"V{numero:04d}"

    total = sum(item["subtotal"] for item in items)

    venta = {
        "id": id_venta,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "items": items,
        "total": total
    }

    for item in items:
        movimiento = {
            "id": f"M{len(movimientos) + 1:04d}",
            "producto_codigo": item["codigo"],
            "tipo": "SALIDA",
            "cantidad": item["cantidad"],
            "motivo": f"Venta {id_venta}",
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M")
        }

        movimientos.append(movimiento)

    ventas.append(venta)

    guardar_datos(RUTA_VENTAS, ventas)
    guardar_datos(RUTA_MOVIMIENTOS, movimientos)

    print("\n========== RESUMEN DE VENTA ==========")
    print("Venta:", id_venta)

    for item in items:
        print(
            item["codigo"],
            "| Cantidad:",
            item["cantidad"],
            "| Precio:",
            f"${item['precio_unitario']:,.0f}".replace(",", "."),
            "| Subtotal:",
            f"${item['subtotal']:,.0f}".replace(",", ".")
        )

    print("TOTAL:", f"${total:,.0f}".replace(",", "."))
    print("Venta registrada correctamente.")
def listar_ventas(ventas, productos):
    print("\n╔════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("║                                      VENTAS                                                ║")
    print("╠════════════════════════════════════════════════════════════════════════════════════════════╣")

    if not ventas:
        print("║                         No hay ventas registradas.                                         ║")
        print("╚════════════════════════════════════════════════════════════════════════════════════════════╝")
        return

    print(f"║ {'ID':<8} {'Producto':<20} {'Cantidad':<10} {'Precio':<15} {'Subtotal':<15} {'Fecha':<17} ║")
    print("╠════════════════════════════════════════════════════════════════════════════════════════════╣")

    for venta in ventas:
        for item in venta.get("items", []):
            nombre_producto = "No encontrado"

            for producto in productos:
                if producto.get("codigo") == item["codigo"]:
                    nombre_producto = producto["nombre"]
                    break

            id_venta = venta["id"][:8]
            nombre = nombre_producto[:20]
            cantidad = str(item["cantidad"])
            precio = f"${item['precio_unitario']:,.0f}".replace(",", ".")
            subtotal = f"${item['subtotal']:,.0f}".replace(",", ".")
            fecha = venta["fecha"][:17]

            print(
                f"║ {id_venta:<8} "
                f"{nombre:<20} "
                f"{cantidad:<10} "
                f"{precio:<15} "
                f"{subtotal:<15} "
                f"{fecha:<17} ║"
            )

        print("╠════════════════════════════════════════════════════════════════════════════════════════════╣")

        total = f"${venta['total']:,.0f}".replace(",", ".")
        print(f"║ {'TOTAL DE VENTA:':<58}                  {total:<15}║")

    print("╚════════════════════════════════════════════════════════════════════════════════════════════╝")
    print(f"Total de ventas: {len(ventas)}")
def menu_ventas(ventas, productos, movimientos):
    while True:
        print("\n========== VENTAS ==========")
        print("1. Registrar venta")
        print("2. Consultar ventas")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_venta(ventas, movimientos, productos)
        elif opcion == "2":
            listar_ventas(ventas, productos)
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

def generar_reporte(productos, lotes, movimientos, ventas):
    productos_activos = 0
    valor_inventario = 0
    total_ventas = 0
    unidades_vendidas = 0
    ventas_realizadas = len(ventas)
    productos_vendidos = {}

    for producto in productos:
        if producto["activo"]:
            productos_activos += 1
            stock = calcular_stock(producto["codigo"], movimientos)
            valor_inventario += stock * producto["precio"]

    for venta in ventas:
        total_ventas += venta["total"]

        for item in venta.get("items", []):
            unidades_vendidas += item["cantidad"]

            codigo = item["codigo"]

            if codigo in productos_vendidos:
                productos_vendidos[codigo] += item["cantidad"]
            else:
                productos_vendidos[codigo] = item["cantidad"]

    ranking = sorted(
        productos_vendidos.items(),
        key=lambda x: x[1],
        reverse=True
    )

    print("\n╔══════════════════════════════════════════════════════════════╗")
    print("║                       REPORTE GENERAL                        ║")
    print("╠══════════════════════════════════════════════════════════════╣")
    print(f"║ Productos activos:     {productos_activos:<34}    ║")
    print(f"║ Total de lotes:        {len(lotes):<34}    ║")
    print(f"║ Total movimientos:     {len(movimientos):<34}    ║")
    print(f"║ Valor del inventario:  {f'${valor_inventario:,.0f}'.replace(',', '.'):<34}    ║")
    print("╠══════════════════════════════════════════════════════════════╣")
    print("║                       REPORTE DE VENTAS                      ║")
    print("╠══════════════════════════════════════════════════════════════╣")
    print(f"║ Ventas realizadas:     {ventas_realizadas:<34}    ║")
    print(f"║ Unidades vendidas:     {unidades_vendidas:<34}    ║")
    print(f"║ Ingresos acumulados:   {f'${total_ventas:,.0f}'.replace(',', '.'):<34}    ║")
    print("╠══════════════════════════════════════════════════════════════╣")
    print("║                    TOP 3 PRODUCTOS VENDIDOS                  ║")
    print("╠══════════════════════════════════════════════════════════════╣")

    if not ranking:
        print("║ No hay productos vendidos todavía.                           ║")
    else:
        posicion = 1

        for codigo, cantidad in ranking[:3]:
            nombre = codigo

            for producto in productos:
                if producto.get("codigo") == codigo:
                    nombre = producto["nombre"]
                    break

            print(f"║ {posicion}. {nombre[:25]:<25} {cantidad:<10} Unidades             ║")
            posicion += 1

    print("╚══════════════════════════════════════════════════════════════╝")
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
        elif opcion == "6":
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
    print("4. Ventas")
    print("5. Alertas de stock")
    print("6. Reportes")
    print("7. Guardar datos")
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
        elif opcion == "2":
            menu_lotes(lotes, productos, movimientos)
        elif opcion == "3":
            menu_inventario(movimientos, productos)
        elif opcion == "4":
            menu_ventas(ventas, productos, movimientos)
        elif opcion == "5":
            alertas_stock(productos, movimientos)
        elif opcion == "6":
            generar_reporte(productos, lotes, movimientos, ventas)
        elif opcion == "7":
            guardar_datos(RUTA_PRODUCTOS, productos)
            guardar_datos(RUTA_LOTES, lotes)
            guardar_datos(RUTA_MOVIMIENTOS, movimientos)
            guardar_datos(RUTA_VENTAS, ventas)
            print("Datos guardados correctamente.")
        elif opcion == "0":
            print("Saliendo de AgroControl CBA...")
            break
        else:
            print("Opción no implementada todavía.")

if __name__ == "__main__":
    main()