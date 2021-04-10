from scipy.io import arff
import pandas as pd

data = arff.loadarff('../Data/ThoraricSurgery.arff')
df = pd.DataFrame(data[0])

df.head()