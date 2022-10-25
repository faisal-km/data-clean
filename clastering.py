import pandas as pd
data = pd.read_csv(
    'data.csv'
)

print(data.isnull().sum())
print("--------------")
data.dropna(0, "any", inplace=True)