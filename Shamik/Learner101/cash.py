def cash():
	k=int(input('amount'))
	n1,r1,n2,r2,n3,r3,n4=0,0,0,0,0,0,0
	if k%0.25==0:
		n1=k/0.25
		r1=k%0.25

	if r1%0.10==0:
		n2=r1/0.10
		r2=r1%0.10

	if r2%0.05==0:
		n3=r2/0.05
		r3=r1%0.05

	if r3%0.01==0:
		n4=r3/0.01
		return n1+n2+n3+n4

	print(n1+n2+n3+n4)




#cash(0.88)
