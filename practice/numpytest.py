import numpy as np

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

# Salary and Bonus matrix sum
salary_bonus = salary+bonus
print(salary_bonus)

# Max value in salary_bonus
print(salary_bonus.max())

# Max Value in each month
print(np.amax(salary_bonus, 0)) # 0 -> Vertical, 1 -> Horizontal

