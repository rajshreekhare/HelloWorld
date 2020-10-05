################################################################ FILES USED ##########################################################################
f1=open("/home/rajshreekhare/Desktop/IIITD_Study/sem_1/CF_(CSE640)/Assignments/1/ml-100k/u5.base","r")
f2=open("/home/rajshreekhare/Desktop/IIITD_Study/sem_1/CF_(CSE640)/Assignments/1/ml-100k/u5.test","r")
#f3 = open("/home/rajshreekhare/Desktop/a.txt", "w")
#f4 = open("/home/rajshreekhare/Desktop/b.txt", "w")
#f5 = open("/home/rajshreekhare/Desktop/c.txt", "w")
#f6 = open("/home/rajshreekhare/Desktop/d.txt", "w")
#f7 = open("/home/rajshreekhare/Desktop/PrdeictedRatings.txt", "r+")

# import SDKs
import math
import numpy as np

def cosine_similarity(v1,v2):
	a = np.dot(v1, v2)
	b = np.linalg.norm(v1)
	c = np.linalg.norm(v2)

	return (a / b) / c

'''compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
	z=(math.sqrt(sumxx)*math.sqrt(sumyy))
	if(z==0):
		return 0
	else:
		return sumxy/z

	#v1,v2 = [3, 45, 7, 2], [2, 54, 13, 15]
	#print(v1, v2, cosine_similarity(v1,v2))'''


##################################################################### INPUT file #####################################################################

w1, h1 = 1683,944
input = [[0 for x in range(w1)] for y in range(h1)]

print ("START: making of user-item matrix (INPUT)")
for lines in range(1,80001):

	i = f1.readline().split("\t")
	Uid1=int(i[0])
	Iid1=int(i[1])
	rating1=int(i[2])
	input[Uid1][Iid1]=rating1

f1.close()
print ("END: making of user-item matrix (INPUT)")

######################################################### COSINE SIMILARITY calculation #############################################################

w3, h3 = 944,944
cs = [[0 for x in range(w3)] for y in range(h3)]

print ("START: making of cosine matrix (CS)")

v1 = []
v2 = []
for i in range(1, 943):
	for j in range(i+1, 944):
		for k in range(1, 1683):
			if( i!=j and (input[i][k]!=0 and input[j][k]!=0)):
				v1.append(input[i][k])
				v2.append(input[j][k])
		if(len(v1)!=0 and len(v2)!=0):
			similarity = cosine_similarity(v1, v2)
		del v1[:]
		del v2[:]
		cs[i][j] = cs[j][i] = similarity

print ("END: making of cosine matrix (CS)")

##################################################### FILE BASED Approach #####################################

print ("START: predicting ratings (USER-USER) and NMAE")

s1=[]
error=[]
l = 1
while l < 20001:
	lines = f2.readline().split("\t")

	x = int(lines[0])		#Uid
	y = int(lines[1])		#Iid
	r2 = int(lines[2])
	r=0
	s=0
	for i in range(1, 944):
		if (i!=x and input[i][y] != 0):
			r += float(input[i][y] * cs[x][i])		#summation of ratings * similarities
			s += cs[x][i]					#summation of similarities
	c=0
	if (s != 0):
		preR= r/s
	else:
		preR=0
		c=c+1

	error.append(abs(r2-preR))
	l += 1

sum1 = sum(error)
length = len(error)
mae = sum1/length
print ("MAE = ", mae)
nmae= mae/4
print ("NMAE = ", nmae)

print ("END: predicting ratings (USER-USER) and NMAE")
######################################################################################
