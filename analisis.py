import pandas as pd

# Leer archivo CSV
df = pd.read_csv("ventas.csv")

# Métricas generales
total = df["venta"].sum()
promedio = df["venta"].mean()

# Venta más alta
cliente_venta_alta = df[df["venta"] == df["venta"].max()]["cliente"].iloc[0]
venta_alta = df["venta"].max()

# Venta más baja
cliente_venta_baja = df[df["venta"] == df["venta"].min()]["cliente"].iloc[0]
venta_baja = df["venta"].min()

# Clientes con ventas mayores a $1,000
clientes_mayor_1000 = df[df["venta"] > 1000]["cliente"]

# Productos únicos
productos_distintos = len(df["producto"].unique())

# Producto más vendido
productos_vendidos = df["producto"].value_counts()
producto_mas_vendido = productos_vendidos.index[0]
cantidad_vendida = productos_vendidos.iloc[0]

# Reporte
print("=" * 40)
print("REPORTE DE VENTAS")
print("=" * 40)

print(f"\nTotal vendido: ${total:,.2f}")
print(f"Promedio de ventas: ${promedio:,.2f}")

print("\nVenta más alta:")
print(f"{cliente_venta_alta} - ${venta_alta:,.2f}")

print("\nVenta más baja:")
print(f"{cliente_venta_baja} - ${venta_baja:,.2f}")

print("\nClientes con ventas mayores a $1,000.00:")
for cliente in clientes_mayor_1000:
    print(f"- {cliente}")

print(f"\nProductos distintos: {productos_distintos}")

print("\nProducto más vendido:")
print(f"{producto_mas_vendido} - {cantidad_vendida} ventas")

print("\nVentas por producto:")
grupos = df.groupby("producto")

for nombre, grupo in grupos:
    total_producto = grupo["venta"].sum()
    print(f"- {nombre}: ${total_producto:,.2f}")
