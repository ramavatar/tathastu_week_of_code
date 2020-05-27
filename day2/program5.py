rows = int(input("Enter rows"))
for i in range(rows):
        print((str(rows-i)+"*")*(rows-1-i)+str(rows-i))
for i in range(2,rows+1):
        print((str(i)+"*")*(i-1)+str(i))    

