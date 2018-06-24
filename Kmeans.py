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
    summ = np.zeros((7,3), dtype=int)
    num = np.zeros((7,), dtype=int)
    photo = np.zeros((300,450,3), dtype=np.uint8)
    cluster = []
    cluster1 = np.random.random_integers(0, 255, (1, 3))
    cluster2 = np.random.random_integers(0, 255, (1, 3))
    cluster3 = np.random.random_integers(0, 255, (1, 3))
    cluster4 = np.random.random_integers(0, 255, (1, 3))
    cluster5 = np.random.random_integers(0, 255, (1, 3))
    cluster6 = np.random.random_integers(0, 255, (1, 3))
    cluster7 = np.random.random_integers(0, 255, (1, 3))
    cluster.append(cluster1)
    cluster.append(cluster2)
    cluster.append(cluster3)
    cluster.append(cluster4)
    cluster.append(cluster5)
    cluster.append(cluster6)
    cluster.append(cluster7)
    subtract = np.zeros((3,1), dtype=int)
    distance = np.zeros((7,))
    while epoch <= 0 :
        for i in range (300):
            for j in range (450):
                for k in range (7):
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
                if pic [i,j] == 2 :
                    summ[2] += pix[i,j]
                    num[2] += 1
                if pic [i,j] == 3 :
                    summ[3] += pix[i,j]
                    num[3] += 1
                if pic [i,j] == 4 :
                    summ[4] += pix[i,j]
                    num[4] += 1
                if pic [i,j] == 5 :
                    summ[5] += pix[i,j]
                    num[5] += 1
                if pic [i,j] == 6 :
                    summ[6] += pix[i,j]
                    num[6] += 1
        for i in range (7):
            if num[i] != 0 :
                summ[i] = (summ[i]/num[i])
                summ[i] = np.floor(summ[i])
                cluster[i] = summ[i]
        epoch += 1
            
    for i in range (300):
        for j in range (450):
            for k in range (7):
                if pic[i,j] == k:
                    photo [i,j] = cluster[k]
    img = Image.fromarray(photo)
    img.save('myimg.jpeg')
    print ('hello yasi!')

                
def main():
    Kmeans()
    
