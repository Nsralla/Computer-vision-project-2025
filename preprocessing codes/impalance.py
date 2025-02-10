import pandas as pd

# Load the CSV file
csv_path = "validation_split.csv"
data = pd.read_csv(csv_path)

# Count the number of images per class
class_counts = data['User ID'].value_counts()

# Print the counts
print("Class Distribution:")
print(class_counts)

# Save the counts to a new CSV file for reference
class_counts.to_csv("class_distribution.csv", header=["count"], index_label="class")

