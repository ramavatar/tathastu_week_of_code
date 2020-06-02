def array(arr, n, k): 
    arr.sort()  
    return arr[k-1]  


arr = [] 
n = int(input("Enter number of elements : "))  
for i in range(0, n): 
    ele = int(input("Enter " + str(i) + " th element  ")) 
    arr.append(ele)
print("array is :" ,arr) 
l = len(arr) 
k = int(input("ENTER  VALUE OF K: "))
print(str(k)+"th smallest element is", array(arr, n, k)) 

