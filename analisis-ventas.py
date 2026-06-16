import pandas as pd

datos = {
    "cliente": ["Ricardo", "Ana", "Pedro", "Luis", "María"],
    "venta": [1200, 800, 1500, 900, 2000]
}

df = pd.DataFrame(datos)

total = df["venta"].sum()
promedio = df["venta"].mean()
cliente_ventas_alta = df[df["venta"] == df["venta"].max()]["cliente"].iloc[0]
venta_alta = df["venta"].max()
cliente_ventas_baja = df[df["venta"] == df["venta"].min()]["cliente"].iloc[0]
venta_baja = df["venta"].min()
cliente_ventas_mil = df[df["venta"] > 1000]["cliente"]

print("=" * 30)
print("REPORTE DE VENTAS")
print("=" * 30)

print()
print(f"Total vendido: ${total:,.2f}")
print(f"Promedio: ${promedio:,.2f}")

print("\nVenta más alta:")
print(f"{cliente_ventas_alta} - ${venta_alta:,.2f}")

print(f"\nVenta más baja:")
print(f"{cliente_ventas_baja} - ${venta_baja:,.2f}")

print("\nClientes con ventas mayores a $1,000.00:")
for cliente in cliente_ventas_mil:
    print(cliente)