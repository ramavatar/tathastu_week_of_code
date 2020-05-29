def intersection(A, B):
   C = [i for i in A if i in B]
   return C
A=list()
B=list()
m=int(input("Enter size of List: "))
print("Enter Element of list A: ")
for i in range(int(m)):
   ram=int(input(""))
   A.append(ram)
n=int(input("Enter size of List: "))   
print("Enter Element of list B:")
for i in range(int(n)):
   ram=int(input(""))
   B.append(ram)
print("LIST AFTER INTERSECTION: ",intersection(A, B))
