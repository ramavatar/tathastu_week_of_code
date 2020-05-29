from operator import itemgetter   
list = [(4, 5, 1), (6, 1, 5), (7, 4, 2), (6, 2, 4)]  
print("The original list is : " + str(list)) 
N =int(input ("Enter Nth Element:"))
list.sort(key = itemgetter(N))  
print("List after sorting tuple by Nth index sort : " + str(list)) 
