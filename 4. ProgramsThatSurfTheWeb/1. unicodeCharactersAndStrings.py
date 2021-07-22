# Para saber cual es el valor real para una letra podemos usar
# Nos devuelve el valor de un caracter en ASCII

print(ord('H')) # Ord significa el ordinal, antes solo se escribia con mayusculas, habian 128 caracteres
# Imprime 72
print(ord('h')) # Ord significa el ordinal, las minusculas tienen mayor valor
# Imprime 104
print(ord('\n')) # Ord significa el ordinal

# LO ANTERIOR EN LOS 60'S 70'S

# Pero después aparecieron distintos tipos de representaciones, y muchas
# veces las computadores japonesas no se podían comunicar con las americanas o europeas,
#
# Pero después se inventó el Unicode

# UNICODE

# Unicode is this universal code for hundreds of millions of different characters and hundreds
# of different character sets. So that instead of saying sorry, you don't fit with your language
# from some South Sea island, it's okay. We've got space in Unicode for that.
# And so Unicode has lots and lots of characters, not 128. Lots and lots of characters.

# Aparecio

# UTF-16 Requiere 2 bytes para cada caracter = 16 bits (Gran cantidad de conjuntos de caracteres)
# UTF-32 Requiere 4 bytes para cada caracter = 32 bits (Todos los caracteres)
# UTF-8 Requiere 1 byte para cada caracter

# Resulta que UTF-8 es el mejor
#   - Se traslapa con ASCII
#   - Deteccion automatica entre ASCII y UTF-8 si uso solo los caracteres en comun
#   - UTF-8 es una practica recomendada para codificar datos que seran intercambiados entres
#     sistemas

#   - UTF-8 tiene como una longitud variable, ya que si lee caracteres "normales"
#     sigue como si nada en ASCII pero si detecta un caracter fuera de lo comun dice "ok, me expando
#     y debo estar en UTF-8"

# Entonces si estoy moviendo datos entre dos sistemas en la red el mundo recomienda que use
# UTF-8

# Dentro de python3 los strings son unicode

x = 'árbiól'
print(type(x)) # imprime str

x = u'árbiól'
print(type(x)) # imprime str

# Sin embargo, en python3 los string normales y los de bits son diferentes

x = b'abc' # Los bytes son raw, crudos, sin codificar, podrian ser UTF-8 UTF-16, ASCII, etc
print(type(x)) # imprime bytes

# Cuando hablamos con un recurso web usando sockets, o hablando a una base de datos
# tenemos que codificar y decodificar datos (usualmente UTF-8)

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysock.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# cmd estaria en bytes ya que lo codificamos con el .encode(), el asume que es UTF-8
# aunque si observamos toda la linea es ASCII

mysock.send(cmd)


# while True:
#     data = mysock.recv(512) -> data estaria en bytes
#     if (len(data) < 1):
#         break
#     mystring = data.decode()) # -> El decode por defecto asume que es UTF-8 o ASCII
                                # mystring estaria en unicode
