 # XML Extensible Markup Language

 # Tiene caracteres especiales y ciertas reglas de uso

 # Es parecido a html, y agrupa elementos, que se encuentran anidados juntos (nested together)


 # Ej:


 # <people>
 #    <person>
 #        <name>Chuck</name>
 #        <phone>303 4456</phone>
 #    </person>
 #    <person>
 #        <name>Noah</name>
 #        <phone>622 7421</phone>
 #    </person>
 # </people>

 # the primary purpose of XML is to share structured data.

 # It was a simplified subset of this SGML (Standard Generalized Markup Language)
 # , which kind of was the precursor to both XML and HTML.


 # pueden haber atributos

 # <person>
 #    <name>Chuck</name>
 #    <phone type="intl">
 #        +1 734 303 4456
 #    </phone>
 #
 #    <email hide="yes"/>
 # </person>

 # VALIDATION

 # Validation is the act of verifying that the data is in the right format. It's a contract.

# XML validation is the act of taking an document and a Schema Contract, which itself is
 # also an XML document, and then sending to the Validator.

 # Ejemplo:

 # XML Document

 # <person>
 #    <lastname>Severance</lastname>
 #    <age>17<age>
 #    <dateborn>2001-04-17</dateborn>
 # </person>

 # XML Schema Contract (El mas popular tiene extension .xsd)

 # <xs:complexType name="person">
 #    <xs:sequence>
 #       <xs:element name="lastname" type="xs:string"/>
 #       <xs:element name="age" type="xs:integer"/>
 #       <xs:element name="dateborn" type="xs:date"/>
 #    </xs:sequence>
 # </xs:complexType>

 # Como el XML coincide con el contrato, entonces el validador lo valida (valga la redundancia)

 # Los complexType son los que tienen children por dentro, y los simples solo tienen sus valores

 # Cuando deba hacer esto debo leer bastante, porque hay mucha informacion

 # Entonces veamos más a fondo el archivo XMS (El del contrato)

 ##############       XMS

 # <xs:element name="person">
 #    <xs:complexType>
 #       <xs:sequence>
 #          <xs:element name="full_name" type="xs:string"
 #              minOccurs="1" maxOccurs="1"/>    ------->  Significa que debe haber exactamente 1 datos de este tipo, si no arroja error
 #          <xs:element name="child_name" type="xs:string"
 #              minOccurs="0" maxOccurs="10"/>   -------> Esta puede ocurrir de 0 a 10 veces, si no arroja error
 #       </xs:sequence>
 #    </xs:complexType>
 # </xs:element>

 # si el minOccurs es 0 significa que el dato es opcional

 # PARSING XML

import xml.etree.ElementTree as ET

data = ''' <person>
            <name>Chuck</name>
            <phone type="intl">
                +1 734 303 4456
            </phone>
        
            <email hide="yes"/>
         </person> '''

tree = ET.fromstring(data) # Construye como un arbol de datos

print('Name: ', tree.find('name').text)
print('Attr: ', tree.find('email').get('hide'))

# Un ejemplo mas complejo con multiples tags

input = '''
        <stuff>
            <users>
                <user x="2">
                    <id>001</id>
                    <name>Chuck</name>
                </user>
                <user x="7">
                    <id>009</id>
                    <name>Brent</name>
                </user>
            </users>
        </stuff>
        '''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user') # Esto da como una lista de arboles de user
print('User count: ', len(lst))

for item in lst:
    print('Name: ', item.find('name').text)
    print('Id: ', item.find('id').text)
    print('Attribute: ', item.get('x'))