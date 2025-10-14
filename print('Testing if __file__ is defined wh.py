import matplotlib.pyplot as plt



x=[i for i in range(10) if i%2==0]
y=[i**2 for i in x]
plt.plot(x,y)
plt.show()


