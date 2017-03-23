#permite rotar una lista.
#rotar la lista una pocicion 
#"rotarL  [4,5,6]" (Es un ejemplo)solo funciona una vez cada que se inicia.
def rotar(lista):
	lista.append(lista[0])
	lista.remove(lista[0])
	print lista
rotar(input('rotarL '))
