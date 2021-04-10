from scipy.io import arff
import pandas as pd

class Classic:
    data = arff.loadarff('../Data/ThoraricSurgery.arff')
    def Display(self, data):
        for ligne in data:
            print(ligne)
