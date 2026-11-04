import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# grafico da turma
plt.bar(
    ["ADS", "JAVA", "PYTH"],
    [8.5, 7.0, 9.5],
    color="b",
)
plt.title("GRAFICO DE MÉDIAS")
plt.xlabel("TURMAS")
plt.ylabel("NOTA FINAL")

plt.grid(True, linestyle=':')
plt.show()

plt.savefig("grafico_medias_turmas.png")