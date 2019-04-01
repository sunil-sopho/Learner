import sys
def ceasar(k):
	s=input("Enter the string")
	#print(ord(k))
	#s="power"
	a=[]
	if isinstance(k,int)==True:

		for i in range(len(s)):
			p=ord(s[i])+k
			if (p<123 and p>96) or (p<91 and p>64):
				a.append(chr(p))
			else:
				a.append(chr(p-26))


			#if :
			#	a.append(chr(p))
			#else:
			#	a.append(chr(p-26))
		
		s1="".join(a)	
			#print(chr((ord(s[i])+k)))
		return s1

	else:
		print('Invalid')
		


print(ceasar(2))
