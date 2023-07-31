#Utilizamos un ciclo while para crear un ciclo infinito de la pregunta y en caso de que sea correcta 
#esta hara que el programa se detenga
print("Bienvenido al programa para ingresar una palabra entre 4 y 8 letras")
print()
while True:
    palabra = input("Ingrese una palabra entre 4 y 8 letras:")

#hacemos validacion de datos
    
    if palabra.isdigit() == True:
        print("Error,No debes ingresar números")    
    elif palabra.isalpha() == False:
        print("Error no esta permitido ingresar caracteres que no sean letras del alfabeto") 
        
#hacemos la validacion del rango que debe contener la palabra
    elif len(palabra) >= 4 and len(palabra) <= 8:
        print("La palabra es correcta, contiene  una longitud de: " + str(len(palabra)) + ' letras')
        break
    elif len(palabra) < 4:
        print("La palabra es incorrecta tiene una longitud de letras de " + str(len(palabra)) 
              + " que es menor a el número de letras requerido.")
        
    elif len(palabra) > 8:
        print("La palabra es incorrecta tiene una longitud de letras de " + str(len(palabra))
              + " que es mayor al número de letras requerido.")

    