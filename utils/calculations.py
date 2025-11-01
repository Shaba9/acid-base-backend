import numpy as np

def calculate_pH(bicarbonate, pco2):
    return round(6.1 + np.log10(bicarbonate / (0.03 * pco2)), 2)
