def totient(n):
	from sympy import factorint
	fact_dict=factorint(n)
	phi_=1
	for key,val in fact_dict.items():
		phi_*=key**val-key**(val-1)
	return phi_

tot_=totient(240)
print(tot_)