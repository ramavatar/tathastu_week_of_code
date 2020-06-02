def Prefix(str1, str2): 

	result = ""; 
	n1 = len(str1) 
	n2 = len(str2) 
	i = 0
	j = 0
	while i <= n1 - 1 and j <= n2 - 1: 
	
		if (str1[i] != str2[j]): 
			break
			
		result += str1[i] 
		i += 1
		j += 1

	return (result) 

def common(arr, n): 

	prefix = arr[0] 

	for i in range (1, n): 
		prefix = Prefix(prefix, arr[i]) 

	return (prefix) 


arr = ["Ram", "RamAvatar","Ramayan"] 
n = len(arr) 
ans = common(arr, n) 
if (len(ans)): 
	print ("The longest common prefix is -", ans);
else: 
	print("There is no common prefix") 
