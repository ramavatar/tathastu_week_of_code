arr = [] 
n = int(input("Enter number of elements : "))  
for i in range(0, n): 
    ele = int(input("Enter "  + str(i) +" th Element :  ")) 
    arr.append(ele)
print("array is :" ,arr)             
flag = 0
i = 1
while i < len(arr): 
    if(arr[i] < arr[i - 1]): 
        flag = 1
    i += 1
      
if (not flag) : 
    print ("Yes, List is sorted.") 
else : 
    print ("No, List is not sorted.") 
