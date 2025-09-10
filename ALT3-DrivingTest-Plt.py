import csv
import pandas as pd
import matplotlib.pyplot as plt

# Load data with pandas
df = pd.read_csv('drivingtest.csv')
print("info", df.info())
print("shape", df.shape)
print(df.describe())

MyPass = 0
MyFail = 0

# Dictionaries for counts by age
pass_by_age = {}
fail_by_age = {}

with open('drivingtest.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row

    for row in csv_reader:
        age = int(row[2])   # Age column
        outcome = row[6]    # "Pass" or "Fail"

        # Count total passes and fails
        if outcome == "Pass":
            MyPass += 1
            pass_by_age[age] = pass_by_age.get(age, 0) + 1
        else:
            MyFail += 1
            fail_by_age[age] = fail_by_age.get(age, 0) + 1

        # Example of extra logic (optional)
        if row[4] == "None" and int(row[5]) == 0 and age < 18:
            print(age, "Custom Fail condition triggered")

print("MyFail:", MyFail, "MyPass:", MyPass)

# Prepare data for plotting
ages = sorted(set(list(pass_by_age.keys()) + list(fail_by_age.keys())))
pass_counts = [pass_by_age.get(age, 0) for age in ages]
fail_counts = [fail_by_age.get(age, 0) for age in ages]

# Plot using Matplotlib
plt.figure(figsize=(8, 5))
plt.plot(ages, pass_counts, marker='o', label='Pass')
plt.plot(ages, fail_counts, marker='x', label='Fail')
plt.xlabel("Age")
plt.ylabel("Number of Students")
plt.title("Pass vs Fail by Age")
plt.legend()
plt.grid(True)
plt.show()
