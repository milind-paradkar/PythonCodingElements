import pandas as pd

df = pd.read_csv("mckinsey.csv")
print("df:\n", df)
print("df.size:", df.size)
print("df.shape (a tuple):", df.shape)
print("df.shape[0] (rows) * df.shape[1] (columns) :", df.shape[0] * df.shape[1],"= df.size:", df.size)






