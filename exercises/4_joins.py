# Exercise 4 (Using different "joins")

import pandas as pd

def main() -> int:
    # Emps DATAFRAME
    data = [
        ['9001','Jeff Russel','Sales'],
        ['9002','Jane Boorman','Sales'],
        ['9003','Tom Heints','Sales'],
            ]
    emps = pd.DataFrame(data, columns=["Empno",'Name','Job'])
    emps = emps.astype({'Empno': int, 'Name': str,'Job': str})
    emps = emps.set_index('Empno')

    # Salary DATAFRAME
    data = [
        ['9001','3000'],
        ['9002','2800'],
        ['9003','2500'],
        ['9004','2700']
    ]
    salary = pd.DataFrame(data,columns=['Empno','Salary'])
    salary = salary.astype({'Empno':int,'Salary':float})
    salary = salary.set_index('Empno')

    # Joins
    emps_salary1 = emps.join(salary,how='right')
    emps_salary2 = emps.join(salary,how='inner')
    print(emps_salary1,'\n\n\n',emps_salary2)


if __name__ == "__main__":
    main()