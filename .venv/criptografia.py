# Este código mostrará la criptografía aprendida en clase
# Se utilizará el algoritmo de cifrado César
def cifradoCesar(texto, desplazamiento):#aqui se define la funcion la cual tiene un texto y una desplazamiento especifico 
    textoCifrado = ""
    for letra in texto:
        if letra.isalpha():
            if letra.isupper():
                textoCifrado += chr((ord(letra) - 65 + desplazamiento) % 26 + 65)
            else:
                textoCifrado += chr((ord(letra) - 97 + desplazamiento) % 26 + 97)
        else:
            textoCifrado += letra
    return textoCifrado

# Solicitar información al usuario
mensaje = input("Ingresa el texto a cifrar: ")
desplazamiento = int(input("Ingresa el desplazamiento (número entero): "))

# Cifrar el mensaje
cifrado = cifradoCesar(mensaje, desplazamiento)

# Mostrar resultado
print("Texto cifrado:", cifrado)
