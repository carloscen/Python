#permite obtener el maximo de 3 números.
#forma de llamar al metodo
#"mayorNum (2,6,3)" (Es un ejemplo).
def mayorNum (x,y,z):
	if x > y and x > z:
		print "Numero Mayor", x
	elif y > x and y > z:
		print "Numero mayor", y
	elif z>x and z>y:
		print "Numero Mayor",z
