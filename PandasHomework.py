import pandas as pd
import numpy as np

data = {
    "Name": ["Pankaj", "Meghna", "David", "Lisa"],
    "Role": ["CEO", np.nan, np.nan, np.nan],
    "Salary": ["100", "200", np.nan, np.nan]
}

df = pd.DataFrame(data, index=["1", "2", "3", "4"])
df["Role"].fillna("Worker")
print(df)