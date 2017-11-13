list1=[5,10,15,20,25]
def exercise1():
	newlist=[list1[0],list1[-1]]
	return(newlist)
print(exercise1())


list2=[1,2,3,4,5,6]
def exercise2():
	thislist=[]
	for index in range(len(list2)):
		if(list2[index]<5):
			thislist.append(list2[index])
	return(thislist)
print(exercise2())


list3=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list4= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]