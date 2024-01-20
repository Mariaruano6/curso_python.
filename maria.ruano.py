import pandas as pd

# Crear un diccionario con información sobre mascotas y sus dueños
mascotas = {
    "nombre_mascota": ["Firulais", "Pelusa", "Whiskers", "Rocky", "Coco"],
    "edad_mascota": [3, 5, 2, 4, 1],
    "tipo_mascota": ["Perro", "Gato", "Gato", "Hamster", "Perro"]
}

dueños = {
    "nombre_dueño": ["Juan", "María", "Carlos", "Ana", "Pedro"],
    "edad_dueño": [28, 35, 42, 30, 50],
    "mascota_asociada": ["Firulais", "Pelusa", "Whiskers", "Rocky", "Coco"]
}

# Crear un DataFrame para las mascotas y los dueños
df_mascotas = pd.DataFrame(mascotas)
df_dueños = pd.DataFrame(dueños)

# Mostrar la información de las mascotas y los dueños
print("Información de las mascotas:")
print(df_mascotas)

print("\nInformación de los dueños:")
print(df_dueños)

# Realizar una consulta para obtener las mascotas de dueños mayores de 30 años
dueños_mayores_30 = df_dueños[df_dueños['edad_dueño'] > 30]
mascotas_dueños_mayores_30 = pd.merge(dueños_mayores_30, df_mascotas, left_on='mascota_asociada', right_on='nombre_mascota', how='inner')

print("\nMascotas de dueños mayores de 30 años:")
print(mascotas_dueños_mayores_30[["nombre_dueño", "mascota_asociada", "tipo_mascota"]])

# Crear un vector con las edades de las mascotas
edades_mascotas = df_mascotas['edad_mascota'].to_list()

print("\nEdades de las mascotas:")
print(edades_mascotas)

# Crear una tupla con el nombre de la mascota más joven y su tipo
mascota_mas_joven = df_mascotas.loc[df_mascotas['edad_mascota'].idxmin()]
tupla_mascota_mas_joven = (mascota_mas_joven['nombre_mascota'], mascota_mas_joven['tipo_mascota'])

print("\nMascota más joven:")
print(tupla_mascota_mas_joven)

# Crear una matriz con la información de las mascotas y sus dueños
matriz_info = pd.merge(df_mascotas, df_dueños, left_on='nombre_mascota', right_on='mascota_asociada', how='inner').values

print("\nMatriz de información mascotas-dueños:")
print(matriz_info)
