#calcule la suma de los cuadrados de n números de forma Recursiva.
#forma de llamar al metodo
#"recursivo (5) " (es un ejemplo).
def recursivo (dato, variable=0):
        if(dato>=0):
                variable+=dato**2
                return recursivo(dato-1,variable)
        else:
                print variable