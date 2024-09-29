import json
import pandas as pd

file = "archive.json"

with open(file,"r") as json_file:
    json_reader = json.load(json_file)

    for each in json_reader['cars']: #iterating inside 'cars'
        formatted_output = "\n".join([f"{key}: {value}" for key, value in each.items()]) #concatenating all items of the list with '\n'
        print(formatted_output+"\n")
    

json_reader = pd.DataFrame(json_reader["cars"]) #transformir the data inside 'cars' in a dataframe
print(json_reader)
