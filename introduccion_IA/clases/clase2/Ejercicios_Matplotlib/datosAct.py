import matplotlib.pyplot as plt

# Datos de participación en actividades extracurriculares
data_actividades = {
    'Actividad': ['Deportes', 'Música', 'Artes', 'Ciencia', 'Club de Lectura'],
    'Participación': [40, 30, 20, 5, 5]
}

# Hagan un gráfico de pastel :)  
plt.style.use('bmh')
plt.pie(data_actividades['Participación'], labels=data_actividades['Actividad'])
plt.legend(title="Actividades", loc="upper left")
plt.title('Participación en actividades extracurriculares')
plt.show()