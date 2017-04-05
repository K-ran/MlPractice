import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(0,2*np.pi, 100)
points = np.linspace(0,2*np.pi,20)
noise = np.random.normal(2*np.sin(points),.2)+4
plt.plot(x,2*np.sin(x)+4)
plt.plot(points,noise,marker='.',ls='')

# regression codeget_phi(points[i])

learning_rate = 10

def get_phi(inp):
    return np.array([[1 , np.sin(inp)]]).T

def evaluate(inp):
    return w.T.dot(get_phi(inp))
evaluate = np.vectorize(evaluate)

w = np.array([[1,1]]).T

for i in range(0,1000):
    sum=np.array([[0,0]]).T
    for j in range(0,len(noise)):
        sum = sum + (noise[j] - (w.T).dot(get_phi(points[j])))*get_phi(points[j])
    w= w + 0.05*(sum/len(noise))
# j=4
# print (noise[j] - (w.T).dot(get_phi(points[j])))*get_phi(points[j])
print w
plt.plot(x,evaluate(x))
plt.show()