from Crypto.Util import number
import random

print("Ejercicio 1 - Obtener un numero aleatorio de 256 bits", "\n", random.getrandbits(256), "\n")

# Ejercicio 2
# Obetner un numero primo

i = 0
while(True):
    i = i + 1
    j = random.getrandbits(1024)
    esPrimo = number.isPrime(j)
    if(esPrimo):
        print("Ejercicio 2 - Numero primo de 1024 bits", "\n", j, "\n")
        break

# Ejercicio 3
# Obtener inverso multiplicativo

def inversoMultiplicativo(x, y):
    print("Ejercicio 3 - Inverso multiplicativo de x:","\n", x, "y el numero y:","\n", y, "es:", "\n", number.inverse(x, y), "\n")

a = random.getrandbits(1024)
b = random.getrandbits(1024)

inversoMultiplicativo(a, b)

#Ejercicio 4 Metodos de cifrado
#encontrar la potencia de un numero 2^(e) mod p, donde "e" es un numero de 256 bits y "p" es un primo de 1024 bits

a = 2
b = random.getrandbits(256)
c = j

def potencial(x,y,z):
    print("Ejercicio 4 - la potencia de x a la y mod z es: ", "\n", pow(x,y,z), "\n")

potencial(a,b,c)