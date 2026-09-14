# AgroControl CBA

Sistema de gestión agrícola desarrollado en Python para administrar productos, lotes productivos, inventario, cosechas y ventas mediante una aplicación de consola.

## Descripción

AgroControl CBA permite llevar el control de productos agrícolas, registrar lotes de producción, realizar cosechas, controlar los movimientos de inventario y registrar las ventas.

La información del sistema se almacena en archivos JSON para mantener los datos guardados entre ejecuciones del programa.

## Tecnologías utilizadas

- Python 3
- JSON
- Git
- GitHub

## Funcionalidades

### Gestión de productos

Permite:

- Registrar productos.
- Consultar productos.
- Buscar productos.
- Actualizar productos.
- Activar productos.
- Desactivar productos.
- Validar códigos de producto duplicados.
- Validar precios mayores que cero.
- Definir un stock mínimo.

### Gestión de lotes

Permite:

- Registrar lotes productivos.
- Consultar lotes.
- Cambiar el estado de los lotes.
- Registrar cosechas.
- Controlar que un lote no pueda ser cosechado dos veces.
- Asociar cada lote con un producto.

Los estados utilizados son:

- `EN_PRODUCCION`
- `COSECHADO`
- `CANCELADO`

### Inventario

El inventario se calcula mediante los movimientos registrados.

Los movimientos pueden ser:

- `ENTRADA`
- `SALIDA`

Las entradas aumentan el stock y las salidas lo disminuyen.

El sistema evita realizar salidas superiores al stock disponible.

También permite consultar alertas cuando el stock actual se encuentra por debajo del stock mínimo establecido.

### Ventas

Permite:

- Registrar ventas.
- Consultar ventas.
- Calcular el total de cada venta.
- Descontar automáticamente el producto vendido del inventario.
- Evitar ventas superiores al stock disponible.

### Cosechas

Al registrar una cosecha:

1. Se verifica que el lote exista.
2. Se verifica que no haya sido cosechado anteriormente.
3. Se registra la cantidad producida.
4. El lote cambia a estado `COSECHADO`.
5. Se genera automáticamente un movimiento de tipo `ENTRADA`.
6. El inventario se actualiza mediante el movimiento generado.

### Reportes

El sistema permite consultar información general sobre:

- Productos.
- Lotes.
- Movimientos de inventario.
- Ventas.
- Valores totales de ventas.

## Estructura del proyecto

```text
agrocontrol_cba/
│
├── main.py
│
├── data/
│   ├── productos.json
│   ├── lotes.json
│   ├── movimientos.json
│   └── ventas.json
│
├── evidencias/
│   ├── PF001_codigo_duplicado.png
│   ├── PF002_precio_invalido.png
│   ├── PF003_lote_inexistente.png
│   ├── PF004_doble_cosecha_1.png
│   ├── PF004_doble_cosecha_2.png
│   ├── PF005_stock_insuficiente.png
│   ├── PF006_producto_desactivado.png
│   ├── PF007_cosecha_inventario.png
│   └── PF008_persistencia.png
│
├── README.md
└── .gitignore