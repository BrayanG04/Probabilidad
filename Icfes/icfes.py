import pandas as pd

# Ruta al archivo original
archivo = r"C:\Users\Crack\Downloads\datos_saber.xlsx"
df = pd.read_excel(archivo)

# Primero detectamos en cuál columna esta el programa academico 
columna_programa = None
for col in df.columns:
    if  "ESTU_PRGM_ACADEMICO"  in col:
        columna_programa = col
        break

# Lista de palabras clave a buscar
palabras_clave = ["ingenieria"]

# Convertimos a minúsculas para búsqueda más flexible y creamos una copia
df_filtrado = df[df[columna_programa].str.lower().str.contains('|'.join(palabras_clave), na=False)].copy()

# Reemplazar respuestas de sí y no por 1 y 0
df_filtrado.replace({'Sí': 1, 'Si': 1, 'No': 0, 'si': 1, 'no': 0, 'SI': 1, 'NO': 0}, inplace=True)

# Reemplazar valores faltantes con 99
df_filtrado.fillna(99, inplace=True)

# Guardamos el resultado
df_filtrado.to_excel("datos_filtrados_sistemas.xlsx", index=False)

print(f"✅ Se filtraron {len(df_filtrado)} filas relacionadas con Ingeniería de Sistemas. Guardado como 'datos_filtrados_sistemas.xlsx'")
