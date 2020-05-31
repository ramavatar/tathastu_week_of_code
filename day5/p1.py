def replace(number):
    return int(str(number).replace('0','5'))
number = int(input("Enter the number Which contain ) AND 5: "))
print("Number after replacing all 0 with 5 will be", replace(number))
