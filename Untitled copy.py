from PIL import Image
import numpy as np
import math
import random
import sys

im = Image.open('segmentation.jpg') 
pix = im.load()

def Kmeans():
    epoch = 0
    pic = np.zeros((300,450), dtype=int)
    summ = np.zeros((2,3), dtype=int)
    num = np.zeros((2,), dtype=int)
    photo = np.zeros((300,450,3), dtype=np.uint8)
    cluster = []
    cluster1 = np.random.random_integers(0, 255, (1, 3))
    cluster2 = np.random.random_integers(0, 255, (1, 3))
 


    cluster.append(cluster1)
    cluster.append(cluster2)

    subtract = np.zeros((3,1), dtype=int)
    distance = np.zeros((3,))
    while epoch <= 1 :
        for i in range (300):
            for j in range (450):
                for k in range (2):
                    subtract =  np.subtract(pix[i,j], cluster[k])
                    distance[k] = np.inner(subtract,subtract)
                d = distance.argmin()
                pic[i,j] = d
        for i in range (300):
            for j in range (450):
                if pic [i,j] == 0 :
                    summ[0] += pix[i,j]
                    num[0] += 1
                if pic [i,j] == 1 :
                    summ[1] += pix[i,j]
                    num[1] += 1

        for i in range (2):
            if num[i] != 0 :
                summ[i] = (summ[i]/num[i])
                summ[i] = np.floor(summ[i])
                cluster[i] = summ[i]
        epoch += 1
            
    for i in range (300):
        for j in range (450):
            for k in range (2):
                if pic[i,j] == k:
                    photo [i,j] = cluster[k]
    img = Image.fromarray(photo)
    img.save('myimg.jpeg')
    print ('hello yasi!')

                
def main():
    Kmeans()
    
