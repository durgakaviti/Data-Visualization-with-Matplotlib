import matplotlib.pyplot as plt
import numpy as np

# Generate random data for the example
categories = ['Python', 'AI & ML', 'Web Development', 'React']
values = np.random.randint(1, 100, size=len(categories))

# Define a list of colors for each category
colors = ['skyblue', 'salmon', 'lightgreen', 'orange']

# Create a bar chart with different colors for each category
plt.bar(categories, values, color=colors)

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example with Different Colors')

# Show the plot
plt.show()
