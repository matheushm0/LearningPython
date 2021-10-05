import math

def get_next(x0, x1, x2):
	h0, h1 = x1-x0,	x2-x1
	if h0 == 0: return x2
	d0, d1 = (f(x1) - f(x0))/h0, (f(x2) - f(x1))/h1
	a = (d1-d0)/(h1+h0)
	b, c = a*h1 + d1, f(x2)
	if (b >= 0):
		return x2 + (-2*c)/(b+math.sqrt(b*b - 4*a*c))
	else:
		return x2 + (-2*c)/(b-math.sqrt(b*b - 4*a*c))

# criteria = 0 max_interaction
# criteria = 1 min_error
def check_criteria(old, new, criteria, criteria_value, iterator):
	if criteria == 0:
		return iterator<criteria_value
	elif criteria == 1:
		return abs(((new-old)/new)) * 100 >= criteria_value

def muller_method(x0, x1, x2, criteria = 0, criteria_value=10):
	iterator = 0
	check = True
	while(check):
		x0, x1, x2 = x1, x2, get_next(x0, x1, x2)
		iterator += 1
		check = check_criteria(x1, x2, criteria, criteria_value, iterator)
		print(f'Iteração = {iterator} | Xr = {x2} | Ea(%) = {abs(((x2-x1)/x2)) * 100}')

# target function
def f(x):
	return (x**3 + x**2 - 3 * x - 5)
	
print("Müller")
muller_method(0, 0.5, 1, 1, 10)