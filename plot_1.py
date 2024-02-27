# import matplotlib's pyplot
import matplotlib.pyplot as plt

# grab a bit of data
my_data = [i for i in range(0,10)]
my_data_2 = [i*2 for i in range(0,10)]

plt.plot(my_data, label="firstline")
plt.plot(my_data_2, label="secondline")

plt.title("A couple of lines")
plt.ylabel("made up number")
plt.xlabel('index of made up number')
plt.legend()

# plt.show()
plt.savefig("first_fig.pdf")