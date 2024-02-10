import numpy as np
import matplotlib.pyplot as plt

class Curve:
    def __init__(self, start, stop, nbr_points=5432):
        """
        Initialise la courbe avec les paramètres de début, de fin et le nombre de points.
        """
        self.start = start
        self.stop = stop
        self.nbr_points = nbr_points

    def generate_points(self):
        """
        Génère des points aléatoires sur la courbe.
        """
        x = np.random.uniform(self.start, self.stop, self.nbr_points)
        y = np.random.uniform(0, 1.4, self.nbr_points)
        points = np.column_stack((x, y))
        return points

    def plot_curve(self):
        """
        Trace la courbe avec des points colorés en bleu si y > 1, en vert sinon,
        et une ligne rouge à y = 1.
        """
        points = self.generate_points()
        for point in points:
            if point[1] > 1:
                plt.scatter(*point, color='blue', marker='x')
            else:
                plt.scatter(*point, color='green', marker='o')
        plt.plot([self.start, self.stop], [1, 1], color='red')
        plt.show()

# Crée une instance de la classe Curve avec des paramètres spécifiques
curve = Curve(0, 1)

# Appelle la méthode plot_curve pour afficher la courbe
curve.plot_curve()
