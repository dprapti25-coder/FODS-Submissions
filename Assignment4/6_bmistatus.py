'''
BMI Calculation and Health Status Classification
Adds BMI and Health_Status columns to dataset using conditions.
'''

import pandas as pd

# Load dataset
df = pd.read_csv("health_data.csv")

# Calculate BMI
df["BMI"] = df["weight"] / (df["height"] ** 2)

# Function to classify health status
def get_health_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Healthy range"
    elif 25 <= bmi <= 29.9:
        return "Overweight risk"
    elif 30 <= bmi <= 34.9:
        return "High risk"
    else:
        return "Critical condition"

# Apply function to create new column
df["Health_Status"] = df["BMI"].apply(get_health_status)

# Display updated dataset
print(df)

# Save new file
df.to_csv("updated_health_data.csv", index=False)

print("\nUpdated file saved as updated_health_data.csv")