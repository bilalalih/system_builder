import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./sample_data/example_data.csv")
numeric_col = df['Salary']

# Distribution plot
plt.hist(numeric_col, bins=30, color='skyblue', edgecolor='black')
plt.title("Distribution Plot")
plt.xlabel("Salary")
plt.savefig("./plots/distribution.png")
plt.show()

# Trend plot
plt.plot(df['Employee_ID'], df['Experience_Years'], color='skyblue')
plt.title("Trend Plot")
plt.ylabel("Salary")
plt.savefig("./plots/trend.png")
plt.show()

# Comparison plot
numeric_col = numeric_col.mean()
categ_col = df['Department']
plt.bar(categ_col, numeric_col, color='skyblue')
plt.title("Comparison Plot")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.savefig("./plots/comparison.png")
plt.show()