import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a, index = ["a", "b", None])
print(myvar)
print(myvar["b"])