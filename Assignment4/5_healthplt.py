'''
Health Data Visualization using Pandas and Matplotlib
Reads health_data.csv and creates scatter plots for different relationships
'''

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("health_data.csv")

# Convert gender to numeric for plotting (M=1, F=0)
df["gender_num"] = df["gender"].map({"M": 1, "F": 0})

# 1. Weight vs Height
plt.scatter(df["weight"], df["height"])
plt.title("Weight vs Height")
plt.xlabel("Weight")
plt.ylabel("Height")
plt.show()

# 2. Age vs Weight
plt.scatter(df["age"], df["weight"])
plt.title("Age vs Weight")
plt.xlabel("Age")
plt.ylabel("Weight")
plt.show()

# 3. Height vs Age
plt.scatter(df["height"], df["age"])
plt.title("Height vs Age")
plt.xlabel("Height")
plt.ylabel("Age")
plt.show()

# 4. Gender vs Height
plt.scatter(df["gender_num"], df["height"])
plt.title("Gender vs Height (M=1, F=0)")
plt.xlabel("Gender")
plt.ylabel("Height")
plt.show()

# 5. Gender vs Weight
plt.scatter(df["gender_num"], df["weight"])
plt.title("Gender vs Weight (M=1, F=0)")
plt.xlabel("Gender")
plt.ylabel("Weight")
plt.show()