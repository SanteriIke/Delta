from pdb import run

import pandas as pd #pandas... doesn't work. still figuring it out

l1 = pd.read_csv("lap1.csv")
l2 = pd.read_csv("lap2.csv")

#Just to make sure, I'll print out both files by themselves before comparing. Since this works we can continue

print("Previous Lap:\n", l1.head())
print("Recent Lap:\n", l2.head()) 

#here is where the comparison will happen. For now it uses static information from the current CSV files
#At some point I will make it possible to compare files that are not hard coded in, but for now this is just to get the function working.
print("Comparing Laps...")

def compare():
    pd.merge(l1, l2, on='speed', how='left', indicator=True).query("_merge == 'left_only'")
    pd.merge(l1, l2, on='speed', how='right', indicator=True).query("_merge == 'right_only'")

print(compare())