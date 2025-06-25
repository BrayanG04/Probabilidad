import random
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

# 1. 60 datos para el ejercicio
datos = [10,10,11,11,14,14,14,21,24,26,27,27,29,35,35,
         37,40,41,43,44,48,50,50,51,57,63,72,69,74,63,
         56,61,67,74,71,85,81,98,72,67,91,88,84,76,70,
         71,86,76,92,72,87,95,71,96,82,88,73,86,72,77]

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

# 5. Crear tabla de frecuencias agrupadas
tabla_intervalos = pd.DataFrame({
    "Intervalo": [f"[{int(bins[i])} - {int(bins[i+1])})" for i in range(len(bins)-1)],
    "Frecuencia absoluta": conteo,
})

# 6. Añadir columnas de frecuencia acumulada y relativa
tabla_intervalos["Frecuencia absoluta acumulada"] = tabla_intervalos["Frecuencia absoluta"].cumsum()
tabla_intervalos["Frecuencia relativa"] = tabla_intervalos["Frecuencia absoluta"] / len(datos)
tabla_intervalos["Frecuencia relativa acumulada"] = tabla_intervalos["Frecuencia relativa"].cumsum()

# 7. Calcular xi (promedio del intervalo)
tabla_intervalos["xi"] = [(bins[i] + bins[i+1]) / 2 for i in range(len(bins)-1)]

# 8. Calcular (xi - x_promedio)^2 * ni
promedio = sum(datos) / len(datos)
tabla_intervalos["(xi - x promedio)^2 * ni"] = ((tabla_intervalos["xi"] - promedio) ** 2) * tabla_intervalos["Frecuencia absoluta"]

# 9. Reordenar columnas
tabla_intervalos = tabla_intervalos[[
    "Intervalo",
    "xi",
    "Frecuencia absoluta",
    "Frecuencia absoluta acumulada",
    "Frecuencia relativa",
    "Frecuencia relativa acumulada",
    "(xi - x promedio)^2 * ni"
]]

# 10. Imprimir la tabla final
print("\n=== Tabla de Frecuencia Agrupada con Columnas Adicionales ===\n")
print(tabla_intervalos.to_string(index=False))

# 11. Medidas de tendencia central
media = promedio
datos_ordenados = sorted(datos)
n = len(datos)
mediana = (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2 if n % 2 == 0 else datos_ordenados[n//2]
moda = max(set(datos), key=datos.count)

print("\n=== Medidas de Tendencia Central ===")
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

# 12. Histograma con etiquetas de frecuencia
plt.figure(figsize=(10, 5))
conteo, bins, patches = plt.hist(datos, bins=limites, edgecolor='black')
# 13. Suma de la columna (xi - x promedio)^2 * ni
suma_cuadrados_ni = tabla_intervalos["(xi - x promedio)^2 * ni"].sum()

# 14. Varianza (dividir entre n)
varianza = suma_cuadrados_ni / len(datos)

# 15. Desviación estándar (raíz cuadrada de la varianza)
desviacion_estandar = math.sqrt(varianza)

# 16. Coeficiente de variación (desviación / promedio)
coef_variacion = desviacion_estandar / promedio

# 17. Error estándar (desviación / raíz de n)
error_estandar = desviacion_estandar / math.sqrt(len(datos))

# 18. Mostrar resultados adicionales
print("\n=== Cálculos de Dispersión ===")
print(f"Suma de (xi - x promedio)^2 * ni: {suma_cuadrados_ni:.2f}")
print(f"Varianza: {varianza:.2f}")
print(f"Desviación estándar: {desviacion_estandar:.2f}")
print(f"Coeficiente de variación: {coef_variacion:.4f}")
print(f"Error estándar: {error_estandar:.2f}")

# 19. Datos ordenados
datos_ordenados = sorted(datos)
n = len(datos)

def calcular_percentil(k, etiqueta):
    pos = k * (n) / 100
    if pos.is_integer():
        valor = datos_ordenados[int(pos) - 1]
    else:
        inferior = int(pos)
        fraccion = pos - inferior
        if inferior == 0:
            valor = datos_ordenados[0]
        elif inferior >= n:
            valor = datos_ordenados[-1]
        else:
            valor = datos_ordenados[inferior - 1] + fraccion * (datos_ordenados[inferior] - datos_ordenados[inferior - 1])
    print(f"{etiqueta} ({k}%)")
    print(f"  Posición teórica: {pos:.2f}")
    print(f"  Valor: {valor:.2f}\n")

print("\n=== Estadisticos de posición ===")
calcular_percentil(20, "Percentil 20 (P20)")
calcular_percentil(50, "Cuartil 2 (Q2)")
calcular_percentil(40, "Quintil 2 (K2)")
calcular_percentil(20, "Decil 2 (D2)")

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
