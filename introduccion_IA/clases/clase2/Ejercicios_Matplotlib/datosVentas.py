import matplotlib.pyplot as plt

# Datos de ventas mensuales
data_ventas = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
    'Producto_A': [1500, 1800, 1700, 1900, 2200, 2100],
    'Producto_B': [2000, 2100, 2300, 2000, 1900, 2100],
    'Producto_C': [2300, 3000, 3200, 2600, 2700, 2900]
}

# Hagan un gráfico de líneas :D 
plt.style.use('Solarize_Light2')
plt.plot(data_ventas['Mes'], data_ventas['Producto_A'], label='Producto A', marker='o', markersize=10, color='gold', linestyle='dashed')
plt.plot(data_ventas['Mes'], data_ventas['Producto_B'], label='Producto B', marker='o', markersize=10, color='indigo', linestyle='dotted')
plt.plot(data_ventas['Mes'], data_ventas['Producto_C'], label='Producto C', marker='o', markersize=10, color='crimson', linestyle='dashdot')
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.title('Ventas mensuales')
plt.legend()
plt.show()