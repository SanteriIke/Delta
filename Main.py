from pdb import run

import pandas as pd #only works in visual studio code, tried in normal visual studio.

#Just to make sure, I'll print out both files by themselves before comparing. Since this works we can continue
l1 = pd.read_csv("lap1.csv")
l2 = pd.read_csv("lap2.csv")
print("Previous Lap:\n", l1.head())
print("Recent Lap:\n", l2.head()) 

def highlight_differences(df):
    # currently trying to highlight differences
    def highlight(val):
        color = 'red' if val else ''
        return f'background-color: {color}'

    return df.applymap(highlight)

#here is where the comparison will happen. For now it uses static information from the current CSV files
#At some point I will make it possible to compare files that are not hard coded in, but for now this is just to get the function working.
print("Comparing Laps...")
delta = l1.compare(l2)
print("Comparison:\n", delta) 

