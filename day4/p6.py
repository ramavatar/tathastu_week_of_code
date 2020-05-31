size = int(input("Enter Size dictonary: "))
dict = []
for i in range(size):
    dict.append(input("Enter the word " + str(i + 1) + ": "))
size = int(input("Enter Size of array: "))
array = []
result = []
print("Enter",str(size), " the characters in array: ")
for i in range(size):
    array.append(input())
for word in dict: 
    if set(word).issubset(set(array)):
        result.append(word)
print(", ".join(result) + ".")
