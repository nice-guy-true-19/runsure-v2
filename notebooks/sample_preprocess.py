import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

df = pd.read_csv("data.csv")

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

X_train, X_test = train_test_split(df_scaled)