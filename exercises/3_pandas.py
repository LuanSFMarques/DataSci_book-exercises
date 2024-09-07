import pandas as pd
import random

# Exercise 3
# Creating a DataFrame with Series

def main() -> None:
    names = ['Victor','Joseph','Robert']
    emails= ['Victor123@gmail.com','Jojo@gmail.com','RobertCool@gmail.com']
    phones = ['47952-8174','46294-8247','93746-9827']

    # Random index 'code'
    t_index = []
    for _ in range(len(names)):
        t_index.append(random.randint(0, (10**3)))

    names = pd.Series(names, name='Names', index=t_index)
    emails = pd.Series(emails, name='Emails', index=t_index)
    phones = pd.Series(phones, name='Phones', index=t_index)

    table = pd.concat([names,emails,phones], axis=1)
    print(table)

if __name__ == "__main__":
    main()