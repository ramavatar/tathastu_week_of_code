def Rev(data, i, length):
    if i==length:
        print("PERMUTATION OF STRING:",''.join(data) )
    else: 
        for j in range(i,length): 
            data[i], data[j] = data[j], data[i] 
            Rev(data, i+1, length) 
            data[i], data[j] = data[j], data[i]  


string =input("Enter String: ")
n = len(string) 
data = list(string) 
Rev(data, 0, n)
