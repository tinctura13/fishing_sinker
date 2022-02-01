"""
Sinker provides functionality to calculate the actual size of spherical fishing
sinkers depending on their weight.

use Sinker.calculate_diameter to calculate the diameter of the sinker
"""

import math


class Sinker:
    def __init__(self):
        """Fishing sinker calculator

        Usage example
        _____________
        sinker = Sinker()
        weights = [2, 5, 8, 12, 15, 20, 25, 30, 35] #(grams)
        p = 11.34 #density of the material (gram/cm^3)
        sinker.calculate_diameters(weights, p)
        """
        self.volumes = []
        self.diameters = []

    def calculate_diameters(self, weights, p):
        """Calculate the diameter of the sphere for fishing sinker
        depending on it weight.

        Parameters
        __________
        weights : list
            Python list with the actual weights of the fishing sinkers.(grams)
        p : int
            Actual density of the material for sinkers.(gram/cm^3)

        Returns
        _______
        dict.key : int
            Actual weight of the sinker. (grams)
        dict.value : int
            Actual diameter of the sinker sphere. (centimeters)
        """
        for weight in weights:
            volume = weight / p
            self.volumes.append(volume)

        for volume in self.volumes:
            radius = (((3 * volume) / (4 * math.pi)) ** (1. / 3))
            self.diameters.append(round((radius * 2), 2))

        return dict(zip(weights, self.diameters))

