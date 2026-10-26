# Reporte de ventas automático

Toma el CSV de ventas que exporta cualquier punto de venta o ERP y genera, en segundos, un Excel con formato listo para mandar:

- Ventas y unidades por mes, con gráfica de barras
- Ranking por producto y por vendedor
- Tabla de mes por sucursal
- Detalle completo con totales calculados

Sirve para reemplazar el reporte que alguien arma a mano cada semana.

## Uso

```bash
pip install -r requirements.txt
python datos_ejemplo.py               # crea ventas.csv con datos ficticios
python reporte.py ventas.csv --salida reporte_ventas.xlsx
```

El CSV necesita las columnas `fecha, sucursal, vendedor, producto, cantidad, precio_unitario`.  Si falta alguna, el programa dice cuál.

## Pruebas

```bash
pip install -r requirements-dev.txt
pytest
```

## Siguientes pasos típicos con un cliente

- Programarlo para que corra solo cada lunes (cron o Programador de tareas de Windows).
- Mandarlo por correo o subirlo a Google Drive automáticamente.
- Leer directo de la base de datos en vez del CSV.
