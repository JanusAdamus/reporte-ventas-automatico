"""Genera un CSV de ventas ficticias para probar el reporte."""
import random
from datetime import date, timedelta

import pandas as pd

PRODUCTOS = {"Café 1kg": 320, "Té verde": 180, "Taza": 150, "Prensa francesa": 650, "Filtros": 90}
VENDEDORES = ["Ana", "Luis", "Sofía", "Carlos"]
SUCURSALES = ["CDMX", "Guadalajara", "Monterrey"]


def generar(filas: int = 600, semilla: int = 7) -> pd.DataFrame:
    rng = random.Random(semilla)
    inicio = date(2026, 1, 1)
    registros = []
    for _ in range(filas):
        producto = rng.choice(list(PRODUCTOS))
        registros.append({
            "fecha": inicio + timedelta(days=rng.randrange(180)),
            "sucursal": rng.choice(SUCURSALES),
            "vendedor": rng.choice(VENDEDORES),
            "producto": producto,
            "cantidad": rng.randint(1, 10),
            "precio_unitario": PRODUCTOS[producto],
        })
    return pd.DataFrame(registros)


if __name__ == "__main__":
    generar().to_csv("ventas.csv", index=False)
    print("Listo: ventas.csv")
