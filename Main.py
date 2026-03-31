import pandas as pd #pandas... doesn't work. still figuring it out

#This part imports the 2 .csv file so that everything isn't inline scripted
l1 = pd.read_csv("lap1.csv")
l2 = pd.read_csv("lap2.csv")

#Just to make sure, I'll print out both files by themselves before comparing. Since this works we can contineu
print("Previous Lap:\n", l1.head())
print("Recent Lap:\n", l2.head()) 

#compare in table 

l2.compare(l1, keep_shape=False, keep_equal=True)
((l1.fillna(1) == l2.fillna(1)).melt()['value'] == 0).sum()