def matrix(m, n, a) : 
	k = 0; l = 0
	while (k < m and l < n) : 
		for i in range(l, n) : 
			print(a[k][i], end = " ") 			
		k += 1
		for i in range(k, m) : 
			print(a[i][n - 1], end = " ") 			
		n -= 1
		if ( k < m) : 			
			for i in range(n - 1, (l - 1), -1) : 
				print(a[m - 1][i], end = " ") 
			m -= 1
		if (l < n) : 
			for i in range(m - 1, k - 1, -1) : 
				print(a[i][l], end = " ") 			
			l += 1


'''R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
matrix = [] 
print("Enter the entries rowwise:") 
for i in range(R):      
    a =[] 
    for j in range(C):      
         a.append(int(input())) 
    matrix.append(a) 
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print()
'''

a = [ [1, 2, 3, 4, 5, 6], 
      [7, 8, 9, 10, 11, 12], 
      [13, 14, 15, 16, 17, 18] ] 
