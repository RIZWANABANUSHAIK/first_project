def compoundInterest(p,r,t):
	if t==0:
		return principle
	else:
		ci=p*((1+r/100),t)
p=float(input("enter principle amount"))
t=folat(input("enter no.of years"))
r=float(input("enter rate of interest"))
ci=compoundInterest(p,r,t)
print("compound interest :{}".format(ci))
