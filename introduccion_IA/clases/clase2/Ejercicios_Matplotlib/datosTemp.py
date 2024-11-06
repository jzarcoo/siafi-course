import matplotlib.pyplot as plt

# Datos de temperaturas diarias
data_temperaturas = {
    'Día': ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'],
    'Ciudad_A': [22, 24, 23, 25, 26]
}

# Gráfico de barras
plt.style.use('dark_background')
plt.bar(data_temperaturas['Día'], data_temperaturas['Ciudad_A'])
plt.xlabel('Día')
plt.ylabel('Temperatura')
plt.title('Gráfico de barras')
plt.show()
