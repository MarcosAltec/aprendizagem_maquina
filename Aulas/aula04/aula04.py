# import pandas as pd
# a = [1, 7, 2]
# myvar = pd.Series(a)
# print(myvar)
# print(myvar[0])

# import os
# print(os.getcwd())

import pandas as pd
df = pd.read_csv('./dados.csv')
print(df.to_string())