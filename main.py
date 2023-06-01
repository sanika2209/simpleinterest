#PYTHON program for calculating simple interest
gender = input("Enter your gender (M/F): ")
age = int(input("Enter your age: "))
amount = float(input("Enter the fixed deposit amount: "))
years = int(input("Enter the number of years for fixed deposit: "))

if gender == 'F' and age >= 60:
    rate = 0.08
elif gender == 'F' and age < 60:
    rate = 0.06
elif gender == 'M' and age >= 60:
    rate = 0.07
else:
    rate = 0.05

interest = amount * rate * years
total_amount = amount + interest

print("Simple interest: ", interest)
print("Total amount after interest: ", total_amount)
