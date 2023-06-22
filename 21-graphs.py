"""
Graficos con los modulos (seaborn) y (matplotlib)
Ejemplos:
"""

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("graph\\data.csv")

sns.lineplot(x="date", y="points", data=df)  ## creo el grafico lineal
# sns.barplot(x="date", y="points", data=df)  ## creo el grafico de barras
# sns.scatterplot(x="date", y="points", data=df)  ## creo el grafico de puntos
# sns.boxplot(x="date", y="points", data=df)  ## creo el grafico de cajas
# sns.violinplot(x="date", y="points", data=df)  ## creo el grafico de violin

plt.plot("01/10/2023", 100, "o")  ## creo un punto en el grafico lineal

plt.show()  ## muestro el grafico
