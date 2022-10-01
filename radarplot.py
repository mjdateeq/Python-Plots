import numpy as np
import matplotlib.pyplot as plt
import matplotlib


variables = np.array (['MYCT', 'MMIN', 'MMAX', 'CACH', 'CHMIN', 'CHMAX']);
#centroid =np.array([13.9715, 2.5931, 0.6708, 6.6051, 18.0450, 11.5185, 2.46, 5.46, 6.703, 5.635, 5.9032, 5.9671, 90.9233, 74.0399, 2.0706, 3.8558, 21.3929, 6.7007, 64.03013, 37.33346, 20.0444, 18.7492, 29.68629, 35.40220, 21.0739, 15.1577])

## Low
##centroid =np.array([2, 1, 1, 1, 1, 1])
##centroid_2 =np.array([1, 2, 2, 2, 2, 2])

## Med
##centroid =np.array([1, 2, 1, 2, 1, 2])
##centroid_2 =np.array([2, 1, 1, 2, 1, 1])
## Hi
centroid =np.array([2, 1, 2, 1, 1, 2])
centroid_2 =np.array([1, 2, 1, 2, 2, 1])



courses = np.array(['C++','Python',' AA ',' BB ',' CC ',' DD ',' EE ',' FF '])

scores=np.array([80,95,78,85,45,65,80,60])

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
##plt.plot(angles, centroid_3,'g^:', linewidth=1, label='v3')


plt.thetagrids(np.degrees(angles),variables)
print(" ----- ")

plt.yticks([0.8, 1.7], ["Small", "Large"])


#plt.thetagrids(angles*360/np.pi,variables)
#plt.fill(angles,centroid,facecolor='r',alpha=0.5)
plt.legend(loc=0)
plt.show()




##
##categories = ['X1', 'X2', 'X3', 'X4']
##
##cenX1 = [4, 4, 5, 3]
##cenX2 = [3, 4, 5, 2]
##
##
####label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(cenX1))
##label_loc = np.linspace(start=0, stop=4.7, num=len(cenX1))
##
##
##plt.figure(figsize=(8, 8))
##plt.subplot(polar=True)
##plt.plot(label_loc, cenX1, label='X1 Centers')
##plt.plot(label_loc, cenX2, label='X2 Centers')
##
####plt.plot(label_loc, restaurant_3, label='Restaurant 3')
##plt.title('CFCM comparison', size=20)
####lines, labels = plt.thetagrids(np.degrees(label_loc), labels=categories)
####lines, labels = plt.thetagrids(range(0, 360, 90), ('X1', 'X2', 'X3','X4'))
##lines, labels = plt.thetagrids(range(0, 360, 90), labels=categories)
##
##plt.legend()
##plt.show()


######################################

##categories = ['Food Quality', 'Food Variety', 'Service Quality', 'Ambiance', 'Affordability']
##
##restaurant_1 = [4, 4, 5, 4, 3]
##restaurant_2 = [5, 5, 4, 5, 2]
##restaurant_3 = [3, 4, 5, 3, 5]
##
##label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(restaurant_1))
##
##plt.figure(figsize=(8, 8))
##plt.subplot(polar=True)
##plt.plot(label_loc, restaurant_1, label='Restaurant 1')
##plt.plot(label_loc, restaurant_2, label='Restaurant 2')
##plt.plot(label_loc, restaurant_3, label='Restaurant 3')
##plt.title('Restaurant comparison', size=20)
##lines, labels = plt.thetagrids(np.degrees(label_loc), labels=categories)
##plt.legend()
##plt.show()
