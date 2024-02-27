import matplotlib.pyplot as plt
import random


x_data = [random.randint(0,10) for i in range(0, 20)]
y_data = [random.randint(0,10) for i in range(0, 20)]

plt.scatter(x_data, y_data, label="random line")
plt.title("Some random data")
plt.ylabel('random y nums')
plt.xlabel('random x nums')
plt.legend()

plt.show()