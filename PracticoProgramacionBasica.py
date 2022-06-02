from array import array
import os
import sys
# Para limpiar la consola

clear = lambda: os.system('clear')
clear()

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    
"""Ej 1)  Un programa que recibe el sexo de una persona como un char y retorne true si el sexo de la persona es femenino (F) o  masculino (M) o false en cualquier otro caso."""

def masculinoFemenino():
      active = False
      while not active:
            respuesta = input('Ingrese su sexo:> ')
            try :
                  if respuesta == 'F' or respuesta == 'f' or respuesta == 'M' or respuesta == 'm':
                        print(True)
                  else:
                        print(False)
                  active = True
            except:
                  active = False
                  print('Ingrese una opción válida')

"""
Ej 2)  Un programa que recibe la edad de una persona y retorna True si es mayor de 18 años o false si es menor.
"""

def esMayor():
      edad = input('Ingrese su edad:> ')

      try:
            if(int(edad) >= 18):
                  print(True)
            else:
                  print(False)
      
      except:
            print('Ingrese un número')



"""Ej 3) Un programa que reciba una edad y retorne True si es menor a 10 o mayor a 60 en caso contrario retornara False."""

def esMenorOMayor():
      edad = input('Ingrese su edad:> ')

      try:
            if(int(edad) < 10 or int(edad) > 60):
                  print(True)
            else:
                  print(False)
      
      except:
            print('Ingrese un número')

"""Ej 4) Un programa que reciba una temperatura en F° y la convierta a C°."""

#Formula: (75F - 32) x 0.5556

def temperaturaC():
      resultado = input("Ingrese temperatura en F°:> ")
      try:
            c = round((int(resultado) - 32) * 0.5556,1)
            
            print(f"{c}C°")
      except:
            print("Ingrese una temperatura válida")

#temperaturaC()
"""Ej 5) Un programa que retorne true si la suma de los números en las posiciones “2” “3” y “4” de un arreglo de enteros es par, de lo contrario retorna false."""

def esParArray():
      completo = False
      numeros = []
      acumulador = 0
      while not completo:
            try:
                  if acumulador < 6:
                        numIngresado = int(input(f"Ingrese un número para la posición {acumulador}:> "))
                        numeros.append(numIngresado)
                        acumulador = acumulador + 1
                  else:
                        completo = True

            except:
                  print("ingrese un numero válido")
      
      resultado = numeros[2] + numeros[3] + numeros[4]
      if resultado % 2 == 0:
            print(True)
      else:
            print(False)

"""Ej 6) Un programa que retorne true si un arreglo de enteros contiene al menos un número par, de lo contrario retorna false.
"""

arrayPrueba = [1,1,3,5]

def unPar(array):
      resultado = False

      for numero in array:
            if numero % 2 == 0 :
                  resultado = True
                  break

      print(resultado)


"""Ej 7) Un programa que retorne true si dos palabras son iguales entre sí, de lo contrario retorna false."""

def sonIguales():
      palabra1 = input("Ingrese la primer palabra:> ")
      palabra2 = input("Ingrese la segunda palabra:> ")
      if palabra1 == palabra2:
            print(True)
      else:
            print(False)



"""Ej 8) Un programa donde el usuario  ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje."""

def diasDeSemana():
      dia = input("Ingrese el dia:> ")

      if dia == "lunes" or dia == "Lunes" :
            print("Es Lunes...")
      elif dia == "viernes" or dia == "Viernes" :
            print("Hoy es Viernes...")
      elif dia == "Sabado" or dia == "sabado" or dia == "domingo" or dia == "Domingo"  :
            print(f"Hoy es {dia}, fin de semana")
      else:
            print("Hoy no es ni lunes, ni viernes, ni sabado, ni domingo")



"""Ej 9) Un programa que retorne true si un entero es capicúa (ej: 12321), de lo contrario retorna false.
"""


def capicua():
      num = input("Ingrese el número:> ")
      
      string = num[::-1]
      if num == string:
            print(True)
      else:
            print(False)


'''
Ej 10) Un programa que retorne true si el número a es menor que b, de lo contrario retorna false.
'''

def menorB():
      a = int(input("Ingrese A:> "))
      b = int(input("Ingrese B:> "))
      if a < b:
            return print(True)
      else: 
            return print(False)


'''Ej 11) Un programa que retorne true si la multiplicación del número A con el número B es igual a la división del número A con el número B.'''

def esIgualMultiplicarDividir():
      a = int(input("Ingrese A:> "))
      b = int(input("Ingrese B:> "))
      multiplicar = a * b
      dividir = a / b

      if multiplicar == dividir:
            return print(True)
      else:
            return print(False)


'''
Ej 12) Un programa que retorne true si un arreglo de enteros A contiene al menos dos números que también contenga el arreglo de enteros B.'''

def dosNumeros(array1,array2):
      acumulador = 0
      for numero in array1:
            for comparar in array2:
                  if numero == comparar:
                        acumulador = acumulador + 1
      
      if acumulador >= 2:
            return print(True)
      else:
            return print(False)

#arrayUno = [1,2,3,4,5]
#arrayDos = [2,6,7,8]

#dosNumeros(arrayUno,arrayDos)



'''
Ej 13) Un programa que retorne la palabra que recibe pero al revés. (ej: hola, retorno = aloh).
'''

def alReves():
      palabra = input("Ingrese la palabra:> ")
      return print(palabra[::-1])

#alReves('hola')


'''
Ej 14) Un programa que retorne la palabra que recibe cambiando todas sus vocales por x. (Ej: azul, retorno: xzxl).
'''

def vocalX():
      palabra = input("Ingrese la palabra:> ")
      vocales = ['a','e','i','o','u']
      listaPalabra = list(palabra)
      for letra in listaPalabra:
            for vocal in vocales:
                  if letra == vocal:
                        listaPalabra[listaPalabra.index(letra)] = "x"

      listaPalabra = "".join(listaPalabra)
      print(listaPalabra)

# vocalX("azul")


'''
Ej 15) Un programa que busque un string en una oracion y lo cambie por otra palabra.
'''

def cambiarPalabra():
      oracion = input("Ingrese la oración:> ")
      palabra = input("Ingrese la palabra a reemplazar:> ")
      nuevaPalabra = input("Ingrese la nueva palabra:> ")
      resultado = oracion.replace(palabra,nuevaPalabra)
      return print(resultado)

# cambiarPalabra("Hola Mundo","Mundo","Luna")


'''
Ej 16) Un programa que reverse una lista
'''

def reversa(lista):
      lista.reverse()
      print(lista)

# num = [1,2,3,4]
# reversa(num)


'''
Ej 17) Un programa que busque elementos en una lista, el elemento a buscar debe ser pasado como parametro en una funcion.
'''


def buscarElemento(lista):
            elemento = int(input("Ingrese el elemento a buscar:> "))
            if elemento in lista :
                  print(f'El elemento " {elemento} " SI se encuentran en la lista ')
            else:
                  print(f'El elemento " {elemento} " NO se encuentran en la lista ')


# lista = [1,2,3,4,5]
# buscarElemento(lista,1)


'''
Ej 18) Crea un array o arreglo unidimensional donde le indiques el tamaño por teclado y crear una función que rellene el array o arreglo con los múltiplos de un número pedido por teclado. Por ejemplo, si defino un array de tamaño 5 y elijo un 3 en la función, el array contendrá 3, 6, 9, 12, 15. Muestralos por pantalla usando otra función distinta.
'''


def multiplos():
      tamanio = int(input('Ingrese el tamaño del array:> '))
      numero = int(input('Ingrese el numero a procesar:> '))
      lista = []
      bandera = False
      contador = 1
      while not bandera:
            if contador <= tamanio:
                  lista.append(numero * contador)
                  contador += 1
            else:
                  bandera = True
      nuevoArray = array('i',lista)

      sys.stdout.write(str(nuevoArray) + "\n")

# multiplos()

'''
Ej 19) Dado el siguiente arreglo de números:
[1, 2 , 5, 8, 3, 30, 9, 13]
Imprimir en pantalla programáticamente los números impares mayores a 7.
'''

def imprimir(array):
      salida = []
      for elemento in array:
            if elemento > 7 and elemento % 2 != 0:
                  salida.append(elemento)
      
      print(salida)

#imprimir([1, 2 , 5, 8, 3, 30, 9, 13])


'''
Ej 20) Dada las siguientes notas almacenadas en un arreglo:
[20, 15, 12, 11, 8, 4, 1]
Elimine la nota más baja programáticamente sin usar la función (min) y escriba en pantalla. Luego programáticamente calcule el promedio de notas descontando la nota eliminada.
'''

def calcularNotas(array):
      array.sort()
      array.pop(0)
      
      promedio = round(sum(array) / len(array),2)
      print(promedio)

# calcularNotas([20, 15, 12, 11, 8, 4, 1])

def deseaContinuar():
      respuesta = input("Escriba Si para elegir otro ejercicio o NO para salir:> ")
      if respuesta == "Si" or respuesta == "si":
            clear()
            return False
      else:
            return True

def menu():
      global continuar
      
      continuar = False
      
      while not continuar:
            respuesta = int(input('Ingrese el número (1 al 20) del ejercicio a mostrar:> '))
            if respuesta == 1:
                  print(bcolors.OK,"1)  Un programa que recibe el sexo de una persona como un char y retorne true si el sexo de la persona es femenino (F) o  masculino (M) o false en cualquier otro caso")
                  masculinoFemenino()
                  continuar = deseaContinuar()
            elif respuesta == 2:
                  print(bcolors.OK,"2)  Un programa que recibe la edad de una persona y retorna True si es mayor de 18 años o false si es menor")
                  esMayor()     
                  continuar = deseaContinuar()             
            elif respuesta == 3:
                  print(bcolors.OK,"3) Un programa que reciba una edad y retorne True si es menor a 10 o mayor a 60 en caso contrario retornara False")
                  esMenorOMayor()             
                  continuar = deseaContinuar()     
            elif respuesta == 4:
                  print(bcolors.OK,"4) Un programa que reciba una temperatura en F° y la convierta a C°.")
                  temperaturaC()              
                  continuar = deseaContinuar()    
            elif respuesta == 5:
                  print(bcolors.OK,"5) Un programa que retorne true si la suma de los números en las posiciones “2” “3” y “4” de un arreglo de enteros es par, de lo contrario retorna false")
                  esParArray()                
                  continuar = deseaContinuar()  
            elif respuesta == 6:
                  print(bcolors.OK,"6) Un programa que retorne true si un arreglo de enteros contiene al menos un número par, de lo contrario retorna false")
                  print("Arreglo de prueba: ", arrayPrueba)
                  unPar(arrayPrueba)          
                  continuar = deseaContinuar()        
            elif respuesta == 7:
                  print(bcolors.OK,"7) Un programa que retorne true si dos palabras son iguales entre sí, de lo contrario retorna false")
                  sonIguales()                  
                  continuar = deseaContinuar()
            elif respuesta == 8:
                  print(bcolors.OK,"8) Un programa donde el usuario  ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje")
                  diasDeSemana()              
                  continuar = deseaContinuar()    
            elif respuesta == 9:
                  print(bcolors.OK,"9) Un programa que retorne true si un entero es capicúa (ej: 12321), de lo contrario retorna false")
                  capicua()                  
                  continuar = deseaContinuar()
            elif respuesta == 10:
                  print(bcolors.OK,"10) Un programa que retorne true si el número A es menor que B, de lo contrario retorna false")
                  menorB()                  
                  continuar = deseaContinuar()
            elif respuesta == 11:
                  print(bcolors.OK,"11) Un programa que retorne true si la multiplicación del número A con el número B es igual a la división del número A con el número B")
                  esIgualMultiplicarDividir() 
                  continuar = deseaContinuar()                 
            elif respuesta == 12:
                  print(bcolors.OK,"12) Un programa que retorne true si un arreglo de enteros A contiene al menos dos números que también contenga el arreglo de enteros B")
                  arrayUno = [1,2,3,4,5]
                  arrayDos = [2,3,6,7,8]
                  print(f"Arreglos de prueba A: {arrayUno} B: {arrayDos}")
                  dosNumeros(arrayUno,arrayDos)
                  continuar = deseaContinuar()                  
            elif respuesta == 13:
                  print(bcolors.OK,"13) Un programa que retorne la palabra que recibe pero al revés. (ej: hola, retorno = aloh)")
                  alReves()                  
                  continuar = deseaContinuar()
            elif respuesta == 14:
                  print(bcolors.OK,"14) Un programa que retorne la palabra que recibe cambiando todas sus vocales por x. (Ej: azul, retorno: xzxl)")
                  vocalX()                  
                  continuar = deseaContinuar()
            elif respuesta == 15:
                  print(bcolors.OK,"15) Un programa que busque un string en una oracion y lo cambie por otra palabra.")
                  cambiarPalabra()            
                  continuar = deseaContinuar()      
            elif respuesta == 16:
                  num = [1,2,3,4]
                  print(bcolors.OK,"16) Un programa que reverse una lista")
                  print(f'Arreglo a utilizar para la prueba: {num}')
                  reversa(num)                
                  continuar = deseaContinuar()  
            elif respuesta == 17:
                  lista = [1,2,3,4,5]
                  print(bcolors.OK,"17) Un programa que busque elementos en una lista, el elemento a buscar debe ser pasado como parametro en una funcion")
                  print(f"Lista de prueba: {lista}")
                  buscarElemento(lista)       
                  continuar = deseaContinuar()           
            elif respuesta == 18:
                  print(bcolors.OK,"18) Crea un array o arreglo unidimensional donde le indiques el tamaño por teclado y crear una función que rellene el array o arreglo con los múltiplos de un número pedido por teclado. Por ejemplo, si defino un array de tamaño 5 y elijo un 3 en la función, el array contendrá 3, 6, 9, 12, 15. Muestralos por pantalla usando otra función distinta")
                  multiplos()                 
                  continuar = deseaContinuar() 
            elif respuesta == 19:
                  print(bcolors.OK,"19) Dado el siguiente arreglo de números: [1, 2 , 5, 8, 3, 30, 9, 13] Imprimir en pantalla programáticamente los números impares mayores a 7")
                  imprimir([1, 2 , 5, 8, 3, 30, 9, 13])         
                  continuar = deseaContinuar()
            elif respuesta == 20:
                  print(bcolors.OK,"20) Dada las siguientes notas almacenadas en un arreglo: [20, 15, 12, 11, 8, 4, 1] Elimine la nota más baja programáticamente sin usar la función (min) y escriba en pantalla. Luego programáticamente calcule el promedio de notas descontando la nota eliminada")
                  calcularNotas([20, 15, 12, 11, 8, 4, 1])  
                  continuar = deseaContinuar()
                              

menu()