import random
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

# 1. Generar 60 datos aleatorios de 2 dígitos (entre 10 y 99)
datos = [random.randint(10, 99) for _ in range(60)]

# 2. Parámetros para intervalos
valor_min = min(datos)
valor_max = max(datos)
amplitud_total = valor_max - valor_min
num_clases = math.ceil(math.sqrt(len(datos)))  # redondear raíz de n
extension_intervalo = math.ceil(amplitud_total / num_clases)

print("\n=== Parámetros para Agrupación ===")
print(f"Valor mínimo: {valor_min}")
print(f"Valor máximo: {valor_max}")
print(f"Amplitud total: {amplitud_total}")
print(f"Número de clases: {num_clases}")
print(f"Extensión del intervalo: {extension_intervalo}")

# 3. Crear los límites de los intervalos
limites = [valor_min + i * extension_intervalo for i in range(num_clases + 1)]

# 4. Agrupar los datos en intervalos
conteo, bins = np.histogram(datos, bins=limites)

# 5. Crear tabla de frecuencias agrupadas con columnas ordenadas
tabla_intervalos = pd.DataFrame({
    "Intervalo": [f"[{int(bins[i])} - {int(bins[i+1])})" for i in range(len(bins)-1)],
    "Frecuencia absoluta": conteo,
})

# Añadir columnas en orden solicitado
tabla_intervalos["Frecuencia absoluta acumulada"] = tabla_intervalos["Frecuencia absoluta"].cumsum()
tabla_intervalos["Frecuencia relativa"] = tabla_intervalos["Frecuencia absoluta"] / len(datos)
tabla_intervalos["Frecuencia relativa acumulada"] = tabla_intervalos["Frecuencia relativa"].cumsum()

# Reordenar columnas si no quedaron en orden
tabla_intervalos = tabla_intervalos[[
    "Intervalo",
    "Frecuencia absoluta",
    "Frecuencia absoluta acumulada",
    "Frecuencia relativa",
    "Frecuencia relativa acumulada"
]]

print("\n=== Tabla de Frecuencia Agrupada ===\n")
print(tabla_intervalos.to_string(index=False))

# 6. Medidas de tendencia central
media = sum(datos) / len(datos)
datos_ordenados = sorted(datos)
n = len(datos)
mediana = (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2 if n % 2 == 0 else datos_ordenados[n//2]
moda = max(set(datos), key=datos.count)

print("\n=== Medidas de Tendencia Central ===")
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

# 7. Histograma con etiquetas de frecuencia por intervalo
plt.figure(figsize=(10, 5))
conteo, bins, patches = plt.hist(datos, bins=limites, edgecolor='black')

# Añadir etiquetas sobre cada barra
for i in range(len(patches)):
    plt.text(patches[i].get_x() + patches[i].get_width()/2, conteo[i] + 0.5,
             str(int(conteo[i])), ha='center', va='bottom', fontsize=10, color='blue')

plt.title('Histograma con Frecuencias Agrupadas')
plt.xlabel('Intervalos')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.tight_layout()
plt.show()