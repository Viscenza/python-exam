from matplotlib import pyplot as plt
import numpy as np

# Définition d'une équation avec 0.5 pts de décalage
def equation(x):
    return x**5 + 0.5

# Définition des échelles
y_ticks = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4]
x_ticks = [0, 0.2, 0.4, 0.6, 0.8, 1.0]

# Création d'un tableau de valeurs x
x_values = np.linspace(0, 1, 1000)

# Courbe
plt.plot(x_values, equation(x_values), label=r'$x^5$')

# Définition des échelles des axes 
plt.xticks(np.arange(0, 1.1, 0.2)) 
plt.yticks(y_ticks)

# Labels et légende
plt.xlabel('x')
plt.ylabel(r'$x^5$')
plt.legend()
plt.grid()

# Affichage du graphique
plt.show()
