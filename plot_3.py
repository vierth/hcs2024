import matplotlib.pyplot as plt
import random
import seaborn as sns

sns.set_theme()
x_data = [random.randint(0,10) for _ in range(0, 20)]
y_data = [random.randint(0,10) for _ in range(0, 20)]

sizes = [random.randint(2,100) for _ in range(0,20)]
colors = ["magenta" for _ in range(0,20)]
colors[8] = "cyan"


plt.scatter(x_data, y_data, s=sizes, c=colors, label="random line")
plt.title("Some random data")
plt.ylabel('random y nums')
plt.xlabel('random x nums')
plt.legend()

plt.show()