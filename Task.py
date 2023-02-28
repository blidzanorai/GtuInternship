import numpy as np
cric_data = np.loadtxt("cric.txt", skiprows = 1)
cric_data

s = cric_data[:,1]
d = cric_data[:,2]
I = cric_data[:,3
             ]
print(s)
print(d)
print(I)

print(np.mean(s))
print(np.mean(d))
print(np.mean(I))

print(np.median(s))
print(np.median(d))
print(np.median(I))

print(np.average(s))
print(np.average(d))
print(np.average(I))
