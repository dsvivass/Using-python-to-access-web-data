# Como HTTP es tan comun, hay una libreria que hace todo el trabajo
# del socket por nosotros y hace ver la pagina web como un archivo
# Se llama urllib

import urllib.request, urllib.parse, urllib.error

fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') # aqui ya va metido
    # todo lo del puerto y demas, ya que casi siempre es lo mismo y urllib lo sabe

counter = {}

for line in fhandle:

    words = line\
        .decode()\
        .split()

    for word in words:
        counter[word] = counter.get(word, 0) + 1

print(counter)

