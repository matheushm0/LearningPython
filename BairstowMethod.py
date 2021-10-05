import cmath

def quad_root(r, s):
	disc = r**2 + 4*s
	if disc > 0:
		r1 = (r + cmath.sqrt(disc))/2
		r2 = (r - cmath.sqrt(disc))/2
		i1 = 0
		i2 = 0
	else:
		r1 = r/2
		r2 = r1
		i1 = cmath.sqrt(abs(disc))/2
		i2 = -i1
	return complex(r1,i1), complex(r2,i2)

# a = array coeficientes do polinomio
# g = grau do polinomio
# roots = array de raizes
def bairstow(r,s,a,g,roots):
	global iterator
	iterator += 1
	print(f'Iteração = {iterator} \nRaizes={roots}\n\n')
	# print(f'r={r}\ns={s}\na={a}\ng={g}\nroots={roots}\n')
	if g<1: # grau menor que 1 não tem raiz
		return None
	if g==1 and a[0] != 0: # grau 1 ax + b = 0; x = -b/a  
		roots.append(complex(float(-a[0])/float(a[1]), 0))
		return None
	if g==2: # grau 2 calcula bhaskara com cuidado para raizes complexas
		delta = a[1]**2 - 4*a[2]*a[0]
		if delta > 0:
			r1 = (-a[1] + cmath.sqrt(delta))/(2 * a[2])
			r2 = (-a[1] - cmath.sqrt(delta))/(2 * a[2])
			i1 = 0
			i2 = 0
		else:
			r1 = -a[1]/(2 * a[2])
			r2 = r1
			i1 = cmath.sqrt(abs(delta))
			i2 = -i1
		roots.append(complex(r1,i1))
		roots.append(complex(r2,i2))
		return None
	# grau diferente dos anteriores
	# calcula n de termos, que é o grau + 1 basicamente
	n = len(a)
	# definição dos b's
	b = [0] * n # preenche o array com 0
	b[n-1] = a[n-1]
	b[n-2] = a[n-2] + r*b[n-1]
	i = n - 3
	while (i>=0):
		 b[i] = a[i] + r*b[i+1] + s*b[i+2]
		 i -= 1
	# definição dos c's
	c = [0] * n # preenche o array com 0
	c[n-1] = b[n-1]
	c[n-2] = b[n-2] + r*c[n-1]
	i = n - 3
	while(i>=0):
		c[i] = b[i] + r*c[i+1] + s*c[i+2]
		i = i - 1
	# calculo do sistema de equacoes
	det = c[2] * c[2] - c[3] * c[1]
	# cuidado na divisao por 0
	if det != 0:
		dr = (-b[1] * c[2] + b[0] * c[3])/det
		ds = (-b[0] * c[2] + b[1] * c[1])/det
		r = r + dr
		s = s + ds
		if abs(dr/r)*100 > 10 or abs(ds/s)*100 > 10:
			return bairstow(r,s,a,g,roots)
	else: # faz um balanco do r e s caso o det der 0 
		r = r + 1
		s = s + 1
		return bairstow(r,s,a,g,roots)
	if g >= 3: # se grau for maior que 3 pega as raizes a partir de r e s
		r1, r2 = quad_root(r,s)
		roots.append(r1)
		roots.append(r2)
		# aplica a funcao novamente, mas agr os coeficientes são os de b e o polinomio tem 2 graus a menos
		return bairstow(r,s,b[2:], g-2, roots)

print("Bairstow")
iterator = 0
grau = 3
rr = 2.5
ss = 2.6
coefis = [40, 0, 0, 3.5, 1]
roots = []
bairstow(rr, ss, coefis, grau, roots)
k = 1
print(f'Iteração = {iterator+1} \nRaizes={roots}\n\n')