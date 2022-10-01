import numpy as np
import matplotlib.pyplot as plt

## part of this code is used in my paper [Concept Discovery in Data: A Design and Interpretation Framework of Conditional Clustering and Logic Networks]
##########


variables = np.array (['MYCT', 'MMIN', 'MMAX', 'CACH', 'CHMIN', 'CHMAX']);
## Hi
centroid =np.array([2, 1, 2, 1, 1, 2])
centroid_2 =np.array([1, 2, 1, 2, 2, 1])


datalength = len(centroid)

angles = np.linspace(0, 2*np.pi, datalength, endpoint=False) #     

#centroid = np.concatenate((centroid,[centroid[0]]))
#centroid_2 = np.concatenate((centroid_2,[centroid_2[0]]))
##centroid_3 = np.concatenate((centroid_3,[centroid_3[0]]))

#angles = np.concatenate((angles,[angles[0]]))

plt.figure(figsize=(4, 4))

print(angles)
print('='*20)
print(centroid)
plt.polar(angles, centroid,'rx--', linewidth=1, label='v1')
plt.plot(angles, centroid_2,'bo-', linewidth=1, label='v2')

plt.thetagrids(np.degrees(angles),variables)
print(" ----- ")

plt.yticks([0.8, 1.7], ["Small", "Large"])

plt.legend(loc=0)
plt.show()
