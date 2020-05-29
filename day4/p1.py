def count(tuple, x): 
    count = 0
    for i in tuple: 
        if (i == x): 
            count = count + 1
    return count     
tuple = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
ele=int(input("ENTER ELEMENT TO SEARCH:"))
print(ele,"present in list ",count(tuple, ele),"times") 

