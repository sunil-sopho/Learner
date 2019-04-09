
def credit():
	k=input('enter the number')
	s1,s2=0,0
	for i in k:
		
		if (int(i)%2==0):
			p=int(i)*2
			s1+=(p%10)+(p%100)
		else:
			s2+=int(i)

	a=s1+s2
	if(a%10==0):
		print('valid no.')
	else:
		print('invalid no.')
