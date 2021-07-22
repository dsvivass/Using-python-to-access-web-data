# AN HTTP REQUEST IN PYTHON

# application protocol
# HTTP - Hypertext transport protocol

# Es la capa dominante en internet, es un conjunto de reglas que permiten a los browsers
# traer documentos web de servidores en la internet

# Es como un formulario de estandares para trabajar

# Una de las cosas que estandariza HTTP es la URL (Uniform resource locaters)
#
# Ej: http://www.dr-daniel.com/page.htm
#
# http://      www.dr-daniel.com      /page.htm
#
# protocol            host             document

# Antes en los 90 se tenian que conocer estas cosas por separado, pero con el URL ahora
# todo se puede concatenar

# EJEMPLO:

import socket # Es como un tubo de conexion

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Es como crear una puerta,
                                # pero la puerta aun no esta abierta, ni conectada aun

mysock.connect(('data.pr4e.org', 80)) # Va y encuentra el webserver y se conecta en el puerto 80 (Esto puede fallar)

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() # esto es un request, asi se hace con el
                                                                    # protocolo HTTP
                                                                    # \r\n\r\n esto es como un enter enter que se debe hacer
                                                                    # como se hace en telnet

# En HTTP nosotros enviamos primero y el servidor recibe, entonces:

mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

mysock.close() # Cerramos el socket, ya que todo lo que hicimos anteriormente consume muchos recursos tanto de mi computador
# como del otro computador# .

# lo que imprime son los header, metadatos y luego imprime el texto

