# import matplotlib.pyplot as plt

# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]

# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth=3)

# # Set chart title and label axes.
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)

# # Set size of tick labels.
# ax.tick_params(labelsize=14)

# plt.show()




import matplotlib.pyplot as plt

# Group members and their values (each one is 1 lower than the previous)
members = ["Ethan", "Marvelous", "Pierre", "Ronny"]
values = [70, 69, 68, 67]  # Descending order for cool effect

# Create an even cooler line graph
plt.figure(figsize=(10, 6))
plt.plot(members, values, marker="o", linestyle="-", color="#FF4500", linewidth=4, 
         markersize=12, markerfacecolor="black", markeredgewidth=2, markeredgecolor="yellow")

# Add title and labels with more dramatic styling
plt.title("⚡ 404 Avengers - Power Levels ⚡", fontsize=20, fontweight="bold", color="purple")
plt.xlabel("Members", fontsize=14, fontweight="bold", color="darkred")
plt.ylabel("Score", fontsize=14, fontweight="bold", color="darkblue")

# Add value labels with cooler styling
for i, v in enumerate(values):
    plt.text(i, v + 1, str(v), ha="center", fontsize=14, fontweight="bold", color="white",
             bbox=dict(facecolor="blue", edgecolor="white", boxstyle="round,pad=0.5"))

# Enhanced grid with neon-style glow
plt.grid(axis="y", linestyle="--", alpha=0.3, color="cyan")

# Dark background for a futuristic feel
plt.gca().set_facecolor("#222222")

# Show the graph
plt.show()
