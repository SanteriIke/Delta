import pandas as pd

data = pd.read_csv("lap1.csv")
time = data["time"]
speed = data["speed"] 

print(time)
print(speed) 