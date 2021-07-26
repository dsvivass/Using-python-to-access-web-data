import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = "http://py4e-data.dr-chuck.net/comments_1308009.xml"

uh = urllib.request.urlopen(url)

data = uh.read()
tree = ET.fromstring(data)

results = tree.findall('.//count') # Podemos buscar elementos con la XPath syntax
                                    # supremamente util para localizar elementos de manera
                                    # dinamica. Informacion que servia para la tesis de
                                    # pregrado

                                    # ej: root.findall(".//year/..[@name='Singapore']")
                                    # Cada parte tiene su razon de ser, leer

                                    # https://docs.python.org/3/library/xml.etree.elementtree.html#elementtree-xpath

print(sum([int(res.text) for res in results]))
