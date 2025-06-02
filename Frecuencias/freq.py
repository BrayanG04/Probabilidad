import random
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. Generar 60 datos aleatorios de 2 dígitos (entre 10 y 99)
datos = [random.randint(10, 99) for _ in range(60)]

# 2. Calcular la frecuencia absoluta usando Counter
frecuencias = Counter(datos)

# 3. Crear tabla de frecuencias con pandas
tabla_frecuencia = pd.DataFrame(sorted(frecuencias.items()), columns=["Dato", "Frecuencia absoluta"])
tabla_frecuencia["Frecuencia relativa"] = tabla_frecuencia["Frecuencia absoluta"] / len(datos)
tabla_frecuencia["Frecuencia acumulada"] = tabla_frecuencia["Frecuencia absoluta"].cumsum()

print("\n=== Tabla de Frecuencia ===\n")
print(tabla_frecuencia.to_string(index=False))

# 5. Medidas de tendencia central
media = sum(datos) / len(datos)
datos_ordenados = sorted(datos)
n = len(datos)
mediana = (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2 if n % 2 == 0 else datos_ordenados[n//2]
moda = tabla_frecuencia.loc[tabla_frecuencia["Frecuencia absoluta"].idxmax(), "Dato"]

print("\n=== Medidas de Tendencia Central ===")
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

# 4. Histograma con etiquetas de frecuencia por intervalo
plt.figure(figsize=(10, 5))
conteo, bins, patches = plt.hist(datos, bins=10, edgecolor='black')

# Añadir etiquetas sobre cada barra
for i in range(len(patches)):
    plt.text(patches[i].get_x() + patches[i].get_width()/2, conteo[i] + 0.5,
             str(int(conteo[i])), ha='center', va='bottom', fontsize=10, color='blue')

plt.title('Histograma con Frecuencias por Intervalo')
plt.xlabel('Intervalos')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.tight_layout()
plt.show()

