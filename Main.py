import pandas as pd 

l1 = pd.read_csv("lap1.csv")
l2 = pd.read_csv("lap2.csv")

print("Previous Lap:\n", l1.head())
print("Recent Lap:\n", l2.head())