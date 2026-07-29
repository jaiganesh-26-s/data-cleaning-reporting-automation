import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("sample_data.csv")

print("Original Data:")
print(df)

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["City"] = df["City"].fillna("Unknown")
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Save cleaned data
df.to_csv("output/cleaned_data.csv", index=False)

# Create chart
plt.bar(df["Name"], df["Salary"])
plt.title("Employee Salary Report")
plt.xlabel("Name")
plt.ylabel("Salary")
plt.savefig("images/salary_chart.png")

# Create report
summary = df.describe()
summary.to_csv("reports/report.csv")

print("\n✅ Project Completed Successfully!")
