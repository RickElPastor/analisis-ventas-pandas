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

# REPORTE
with open("Reporte.txt", "w") as archivo:

    archivo.write("=" * 40 + "\n")
    archivo.write("REPORTE DE VENTAS\n")
    archivo.write("=" * 40 + "\n\n")

    archivo.write(f"Total vendido \n- ${total:,.2f}\n\n")
    archivo.write(f"Promedio de ventas \n- ${promedio:,.2f}\n\n")

    archivo.write("Venta más alta\n")
    archivo.write(f"- {cliente_venta_alta}: ${venta_alta:,.2f}\n\n")

    archivo.write("Venta más baja\n")
    archivo.write(f"- {cliente_venta_baja}: ${venta_baja:,.2f}\n\n")

    archivo.write("Clientes con ventas mayores a $1,000.00\n")
    for cliente in clientes_mayor_1000:
        archivo.write(f"- {cliente}\n")

    archivo.write(f"\nProductos distintos \n- {productos_distintos} productos\n\n")

    archivo.write("Producto más vendido\n")
    archivo.write(f"- {producto_mas_vendido}: {cantidad_vendida} ventas\n\n")

    archivo.write("Ventas por producto\n")
    grupos = df.groupby("producto")

    mayor_facturacion = 0
    producto_top = ""

    for nombre, grupo in grupos:
        total_producto = grupo["venta"].sum()

        archivo.write(f"- {nombre}: ${total_producto:,.2f}\n")

        if total_producto > mayor_facturacion:
            mayor_facturacion = total_producto
            producto_top = nombre

    archivo.write("\nProducto con mayor facturación\n")
    archivo.write(f"- {producto_top}: ${mayor_facturacion:,.2f}\n\n")

    archivo.write("TOP 3 CLIENTES\n")

    top = df.sort_values("venta", ascending=False).iloc[:3]

    for i in range(len(top)):
        archivo.write(f"- {top['cliente'].iloc[i]}: ${top['venta'].iloc[i]:,.2f}\n")

    archivo.write("\nVentas por clientes\n")
    resultado = df.groupby('cliente')['venta'].sum().sort_values(ascending=False)
        
    for cliente, venta in resultado.items():
        archivo.write(f"- {cliente}: ${venta:,.2f}\n")