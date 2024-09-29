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

    # Orders DATAFRAME
    data = [
        [2608, 9001, 35],
        [2617, 9001, 35],
        [2620, 9001, 139],
        [2621, 9002, 95],
        [2626, 9002, 218],
    ]
    orders = pd.DataFrame(data,columns=['Pono','Empno','Total'])
    orders = orders.astype({'Pono':int,'Empno':int,'Total':int})

    # Joins and Merge
    emps_salary1 = emps.join(salary,how='right')
    emps_salary2 = emps.join(salary,how='inner')
    emps_orders = emps.merge(orders,how='inner', left_on='Empno', right_on='Empno').set_index('Pono')

    # Mean using groupby()
    mean_total = orders.groupby(['Empno'])['Total'].mean()

    
    #print(emps_salary1)
    #print(emps_salary2)
    #print(orders)
    #print(emps_orders)
    #print(mean_total)

    return 0


if __name__ == "__main__":
    main()