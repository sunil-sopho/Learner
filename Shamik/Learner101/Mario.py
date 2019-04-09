
def pattern1(n):
	#n=input('give a number')
	#n=int(n)
	if n>8 and n<1 :
		print('give valid input')
	else:

		for i in range(0,n):  

			for j in range(n,i,-1): #1
				print(' ',end='')

			for k in range(0,i+1):  #2
				print('#',end='')

			print(' ',end='')

			for p in range(0,i+1):   #3
				print('#',end='')

			print('\n')

	


pattern1(7)
