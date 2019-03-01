import matplotlib.pyplot as plt
f = open('./data.txt')
ls = f.read().split('\n')[1:-2]
data = map(float, ls)
print data
plt.scatter(range(len(data)), data)
plt.show()
