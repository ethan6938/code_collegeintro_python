import matplotlib.pyplot as plt

# First 5 cubic numbers
x_values = [1, 2, 3, 4, 5]
y_values = [x**3 for x in x_values]

plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, marker='o', linestyle='-', color='blue')
plt.title("First Five Cubic Numbers")
plt.xlabel("Number")
plt.ylabel("Cube of Number")
plt.grid(True)
plt.show()

# First 5000 cubic numbers with colormap
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.figure(figsize=(10, 6))
plt.scatter(x_values, y_values, c=y_values, cmap='plasma', edgecolor='none', s=1)
plt.colorbar(label="Cubic Value")
plt.title("First 5000 Cubic Numbers with Colormap")
plt.xlabel("Number")
plt.ylabel("Cube of Number")
plt.show()
