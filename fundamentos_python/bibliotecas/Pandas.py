import pandas as pd

# Crear una Serie
serie = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'], name='Serie', dtype='int32', copy=True)
print('Serie:')
print(serie, '\n')

# Crear un DataFrame
data = {
    'Nombre': ['Juan', 'Pedro', 'Luis', 'Ana'],
    'Edad': [25, 30, 35, 40],
    'Ciudad': ['Lima', 'Arequipa', 'Cusco', 'Trujillo']
}
df = pd.DataFrame(data)
print('DataFrame:')
print(df, '\n')

# Crear un DataFrame a partir de un archivo CSV
df = pd.read_csv('ventas.csv')
print('DataFrame:')
print(df, '\n')

df.to_csv('ventas2.csv', index=False)
print('Archivo CSV creado')

# Crear un DataFrame a partir de un archivo CSV
df = pd.read_csv('datos.csv')
nombre_inicia_con_j = df['Nombre'].str.startswith('J')
print('Nombre inicia con J:')
print(df[nombre_inicia_con_j], '\n')

# promedio de la columna Edad
promedio_edad = df['Edad'].mean()
print('Promedio de la Edad:', promedio_edad)

# Agrupar por Ciudad
df['Pais'] = 'Mexico'
print(df, '\n')