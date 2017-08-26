class dojo:

	def __init__(self, x, y, s):
		self.menor=x
		self.mayor=y
		self.salto=s
		self.rango=range(menor, mayor, salto)


	def sum(self):
		suma = 0
		for i in self.rango:
			suma+=i
		print (suma)
		return suma

print("ingrese menor")
menor = int(input())

print("ingrese mayor")
mayor = int(input())

print("ingrese salto")
salto = int(input())

#rango = range(menor, mayor)
print(menor, mayor)
#print ("la suma es: ", sum(rango))

calcular=dojo(menor, mayor, salto)
calcular.sum()

