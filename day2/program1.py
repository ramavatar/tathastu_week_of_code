def isodd(num):
    if(num%2==0):
        return False
    return True

def isprime(num):
    a=2
    b=num//2
    while b>=a:
       if(num%a==0):
         return False
       a=a+1
       b=num//a
    return True

def ispalendrome(num):
    rev=0
    temp=num
    while temp>0:
        a=temp%10
        rev=rev*10+a
        temp//=10
    if (num == rev):
        return True
    return False

def isArmstrong(num):
    sum=0
    temp=num
    while temp>0:
        a=temp%10
        sum+=a**3
        temp//=10
    if (num == sum):
        return True
    return False

def check():
    n=int(input("Enter Number:"))
    if(isodd(n)):
        print(n,"is Odd Number")
    else:
        print(n,"is Even Number")
    if(isprime(n)):
        print(n,"is Prime Number")
    if(ispalendrome(n)):
        print(n,"is Palendrome Number")
        
    if(isArmstrong(n)):
        print(n,"is Armstrong Number")    

check()
