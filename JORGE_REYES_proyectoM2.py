#pedimos al usuario que ingreser dos numeros, uno para el eje x y otro para el y
print("Bienvenido al programa para conocer el cuadrante de algún punto del plano cartesiano")
print()

#Creamos ciclos while para las preguntas con su try
#  y except para validar que el usuario introduzca números solamente


while True:
    try:
        ejeX = int(input("Ingrese un valor para el eje X: ")) 
        break
    except  ValueError:
        print("Error, debe ingresar un número.")

while True:
    try:
        ejeY = int(input("Ingrese un valor para el eje Y: "))
        break  
    except ValueError:
        print("Error, debe ingresar un número.")

if ejeX == 0 and ejeY == 0:
    print("El punto se encuentra en el origen")

elif ejeX == 0:
    print("El punto esta en el eje Y, coordeenadas: (" + str(ejeX) + "," + str(ejeY) + ")")

elif ejeY == 0:
    print("El punto esta en eje X, coordenadas: (" + str(ejeX) + "," + str(ejeY) + ")")    

elif ejeX > 0 and ejeY > 0:
    print("El punto se encuentra en el cuadrante I.")

elif ejeX < 0 and ejeY > 0:
    print("El punto se encuentra en el cuadrante II.")

elif ejeX < 0 and ejeY < 0:
    print("El punto se encuentra en el cuadrante III.")

elif ejeX > 0 and ejeY < 0:
    print("El punto se encuentra en el cuadrante IV.")
