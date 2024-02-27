import pandas as pd
from pandas import DataFrame
import numpy as np

random_data = np.random.randn(10, 5)

columns = ['a', 'b', 'c', 'd', 'e']
my_df = DataFrame(random_data, columns=columns)

print(my_df["a"])