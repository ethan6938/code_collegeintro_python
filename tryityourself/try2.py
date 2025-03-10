import matplotlib.pyplot as plt
from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            self.x_values.append(self.x_values[-1] + x_step)
            self.y_values.append(self.y_values[-1] + y_step)

    def get_step(self):
        """Determine the direction and distance for a step."""
        direction = choice([1, -1])  # Can remove -1 for one-directional movement
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])  # Extended range
        return direction * distance


# Create a Random Walk instance with 5,000 points
rw = RandomWalk(5000)
rw.fill_walk()

# Plot the random walk using a line instead of scatter (molecular motion)
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(rw.x_values, rw.y_values, linewidth=1, color='blue')

# Emphasize the start and end points
ax.scatter(0, 0, c='green', edgecolors='black', s=100, label="Start")
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='black', s=100, label="End")

# Hide axes for better presentation
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.title("Molecular Motion - Random Walk", fontsize=14)
plt.legend()
plt.show()
