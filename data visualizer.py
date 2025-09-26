import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
print("Data from CSV:\n", df)

df.to_csv("data_saved.csv", index=False)

random_data = np.random.randint(50, 100, 50)

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].hist(random_data, bins=10, edgecolor='black', color='blue')
axs[0].set_title("Histogram of Random Scores")

# Right: Sine wave
axs[1].plot(x, y, color='red')
axs[1].set_title("Sine Wave")

plt.tight_layout()

plt.savefig("plots/project_plot.png")
plt.show()
plt.close()

print("\nAccess first row using iloc:\n", df.iloc[0])
print("\nAccess 'Name' column using loc:\n", df.loc[:, "Name"])
