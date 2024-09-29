import pandas as pd

letters = ['a','b','c','d','e','f','g','h','i','j','k']
inverse_index = []
for i in range(len(letters)):
    inverse_index.append(len(letters)-1-i)

emps_names = pd.Series(letters, index=inverse_index)
print(emps_names)

print(emps_names.loc[10:8]) #\Equal
print(emps_names[0:3]) #/Equal