import numpy as np

# Exercise 2
# Find the higher monthly payments and calculate the average between them

# Salary Grid
salary1 = [2700,3000,3000]
salary2 = [2600,2800,2800]
salary3 = [2300,2500,2500]

salary = np.array([salary1,salary2,salary3])


# Bonus Grid
bonus1 = [500,400,400]
bonus2 = [600,300,400]
bonus3 = [200,500,400]

bonus = np.array([bonus1,bonus2,bonus3])

salary_bonus = salary + bonus

def main():
    # Finding the max monthly payment
    month_max = np.amax(salary_bonus,0)
    print(month_max)

    # Fingind the average between this values
    m_max_av = round(np.average(month_max), 2)
    print(m_max_av)

if __name__ == "__main__":
    main()