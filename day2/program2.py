num=int(input("ENter upto Which Series is Required:"))
a = 0
b = 1
if num < 0: 
        print("Incorrect input") 
else: 
    for i in range(num):
        print(a,end=" ")
        c = a + b 
        a = b 
        b = c 
