# Análisis de Ventas con Python y Pandas

## Descripción

Proyecto de análisis de datos desarrollado con **Python** y **Pandas**.

El programa procesa un archivo CSV de ventas y genera automáticamente un reporte con métricas, estadísticas y rankings de clientes y productos. Además, exporta los resultados a un archivo de texto para su consulta posterior.

## Funcionalidades

- Total vendido
- Promedio de ventas
- Venta más alta
- Venta más baja
- Clientes con ventas superiores a $1,000
- Cantidad de productos distintos
- Producto más vendido
- Ventas totales por producto utilizando `groupby()`
- Producto con mayor facturación
- TOP 3 clientes por monto de compra
- Ventas totales por cliente
- Cliente que más gastó
- Cliente que menos gastó
- Exportación automática del reporte a `Reporte.txt`
- Validación de archivo CSV vacío

## Tecnologías

- Python
- Pandas

## Ejecución

Instalar Pandas:

```bash
python3 -m pip install pandas
```

Ejecutar el programa:

```bash
python3 analisis.py
```

## Objetivo

Practicar conceptos fundamentales de análisis de datos utilizando Python y Pandas, incluyendo:

- Lectura de archivos CSV
- Manipulación de DataFrames
- Filtrado de información
- Estadísticas básicas
- Agrupación de datos con `groupby()`
- Conteo de registros con `value_counts()`
- Ordenamiento con `sort_values()`
- Exportación de información a archivos de texto
- Generación de reportes automáticos

## Ejemplo de salida

```text
========================================
REPORTE DE VENTAS
========================================

Total vendido 
- $6,400.00

Promedio de ventas 
- $1,280.00

Venta más alta
- María: $2,000.00

Venta más baja
- Ana: $800.00

Clientes con ventas mayores a $1,000.00
- Ricardo
- Pedro
- María

Productos distintos 
- 4 productos

Producto más vendido
- Laptop: 2 ventas

Ventas por producto
- Laptop: $2,700.00
- Monitor: $2,000.00
- Mouse: $800.00
- Teclado: $900.00

Producto con mayor facturación
- Laptop: $2,700.00

TOP 3 CLIENTES
- María: $2,000.00
- Pedro: $1,500.00
- Ricardo: $1,200.00

Ventas por clientes
- María: $2,000.00
- Pedro: $1,500.00
- Ricardo: $1,200.00
- Luis: $900.00
- Ana: $800.00

Cliente que más gastó
- María: $2,000.00

Cliente que menos gastó
- Ana: $800.00
```

## Evolución del Proyecto

### Versión inicial

![Versión inicial](imagenes/reporte_v1.png)

### Segunda versión

![Segunda versión](imagenes/reporte_v2.png)

### Tercera versión

![Tercera versión](imagenes/reporte_v3.png)

### Versión 1.0

![Versión 1.0 - Parte 1](imagenes/reporte_v4_1.png)

![Versión 1.0 - Parte 2](imagenes/reporte_v4_2.png)

## Autor

**Ricardo Romero**

Proyecto realizado como parte de mi aprendizaje de Python y análisis de datos con Pandas.