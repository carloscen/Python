#suma de los cubos de n números
#forma de llamar al metodo
#"intervSuma (4)" (es un ejemplo).
def intervSuma(x):      
        vacio=[(conta**3) for conta in range(1,x+1)]        
        print vacio
        return sum(vacio)