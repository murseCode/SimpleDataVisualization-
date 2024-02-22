import pandas as pd
import matplotlib.pyplot as plt


width = 10
height = 5
columns = 1
rows = 2
csv_file = 'sample_data.csv' # Replace with your CSV file path

# Step 1: Read the CSV file
data = pd.read_csv(csv_file)

# Step 2: Display the data (here, we're assuming the CSV has columns 'A' and 'B')
plt.figure(figsize=(width, height))

# Creating a bar plot
plt.subplot(columns, rows, 1)
plt.bar(data['A'], data['B'], color='blue')
plt.xlabel('Column A')
plt.ylabel('Column B')
plt.title('Bar Plot of A vs B')

# Creating a line plot
plt.subplot(columns, rows, 2)
plt.plot(data['A'], data['B'], color='red')
plt.xlabel('Column A')
plt.ylabel('Column B')
plt.title('Line Plot of A vs B')

# Display the dashboard
plt.tight_layout()
plt.show()
