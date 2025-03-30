name = ("santiago")
print (name)

#forzamos el tipo
address: str = "avenida 123"
address = 32
print (type(address)) #mirar el tipo de una variable

print(type("soy un dato str"))#dato string
print(type(5))#dato tipo int
print(type(1.5))#dato tipo float

#operadores aritmeticos 

print (5 + 3) #suma
print (5 - 3) #resta
print (5 * 3) #multiplicacion
print (5 / 3) #division
print (10 % 3) #modulo es una divisio y muestra el multiplo
print (10 // 3) #esta divisoon por mas que de decimal aproxima a un numero entero
print (5 ** 3) #exponente


print ("Hola " + "mundo") #concatenacion de strings # no se puede concatnear strings con enteros
print ("hola " + str(5)) #str transforma lo que sea a string 
#print (5 + "hola") #no se puede sumar string con enteros
print ("hola " * 5) #multiplicacion de strings multiplico hola 5 veces
print ("hola " * 5 + "mundo") #multiplicacion de strings 
print ("hola " * (5 + 3)) #multiplicacion de strings 

my_int = 2.5 * 2
print ("hola " * int(my_int))#no se puede multiplicar por float pero si se puede transformar por entero igual que con str

#operadores comparativos
print (3 > 4)
print (3 < 4)
print (3 <= 4)
print (3 >= 4)
print (3 == 4) #igualdad
print (3 != 4) #diferencia
print (3 == 3.0) #igualdad entre float y entero
print ("hola" < "zython") #compara las letras de cada palabra #compara una ordenacion alfabetica
print (len("holass") < len( "zython"))  # con len si cuenta las letras de las palabras


#operadores logicos
print (3 > 4 and "hola">"python") #FALSE Y FALSE = FALSE
print (3 > 4 or "hola">"python") #FALSE Y TRUE = FALSE
print (3 < 4 or "hola"<"python") #TRUE Y TRUE = TRUE

#print (3 > 4 not "hola">"python") #no se puede usar not con strings
print (not (3 > 4)) #negar una condicion si algo es verdadero dentro de la condicion y pongo not sera falso

#strings


