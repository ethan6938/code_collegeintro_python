import random
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Task 1: Two D8s - Sum of two 8-sided dice (1000 rolls)
rolls_two_d8 = [random.randint(1, 8) + random.randint(1, 8) for _ in range(1000)]

# Task 2: Three D6 Dice - Sum of three 6-sided dice (1000 rolls)
rolls_three_d6 = [random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) for _ in range(1000)]

# Task 3: Multiplication of two D8 rolls (1000 rolls)
rolls_multiply_d8 = [random.randint(1, 8) * random.randint(1, 8) for _ in range(1000)]

# Task 4: Random Walk using Plotly
steps = [random.choice([-1, 1]) for _ in range(1000)]
position = [sum(steps[:i+1]) for i in range(len(steps))]

# Plotting for Task 1 - Two D8s
plt.figure(figsize=(10, 6))
plt.hist(rolls_two_d8, bins=range(2, 17), edgecolor='black', align='left')
plt.title('Histogram of Rolling Two 8-Sided Dice (1000 Rolls)')
plt.xlabel('Sum of Rolls')
plt.ylabel('Frequency')
plt.xticks(range(2, 17))
plt.show()

# Plotting for Task 2 - Three D6 Dice
plt.figure(figsize=(10, 6))
plt.hist(rolls_three_d6, bins=range(3, 19), edgecolor='black', align='left')
plt.title('Histogram of Rolling Three 6-Sided Dice (1000 Rolls)')
plt.xlabel('Sum of Rolls')
plt.ylabel('Frequency')
plt.xticks(range(3, 19))
plt.show()

# Plotting for Task 3 - Multiplication of Two D8 Rolls
plt.figure(figsize=(10, 6))
plt.hist(rolls_multiply_d8, bins=range(1, 65), edgecolor='black', align='left')
plt.title('Histogram of Multiplying Two 8-Sided Dice (1000 Rolls)')
plt.xlabel('Product of Rolls')
plt.ylabel('Frequency')
plt.xticks(range(1, 65, 5))
plt.show()

# Plotting for Task 4 - Random Walk using Plotly
fig = go.Figure(data=go.Scatter(x=list(range(1000)), y=position, mode='lines'))
fig.update_layout(title="Random Walk (1000 Steps)",
                  xaxis_title="Step Number",
                  yaxis_title="Position")
fig.show()
