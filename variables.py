# STRING

cadena = "Esta es una cadena de texto"
print(type(cadena))


# INTEGER

numero = 250
print(type(numero))


# LISTA

lista1=[1,2,3,4,5,6,7,5]
print(type(lista1))
lista1.append(25)
print(lista1)


# TUPLA

lista2=(1,2,3,4,5,6,7)
print(type(lista2))

x=10
y=30
punto=(x,y)
print(punto[0])
print(punto[1])

# Desempaquetar tupla

fecha = (25, "Diciembre", 2015)
print(fecha)

dd,mm,aa = fecha
print("Dia", dd)
print("Mes", mm)
print("Year", aa)


# SET

lista3={1,2,3,3,9} #set
print(type(lista3))
print(lista3)
lista3.add(50)
lista3.remove(1)
print(lista3)

conjunto=set()
conjunto.add('Pera')
conjunto.add('Manzana')
print((conjunto))


# DICCIONARIOS

casas = {"Harry":"Gryffindor","Draco":"Slytherin"}
print(casas["Harry"])

casas["Hermione"]="Gryffindor"
print(casas["Hermione"])

print(casas.keys())
print(casas.values())
print(casas.get("Hermione"))


gente = {'Pipi':'Calzaslargas', 'Bob':'Esponja','Laura':'Ingalls', 'Sherlock':'Holmes'}

if 'Pedro' in gente:
  print(gente['Pedro'])
else:
  print('Esta clave no existe')
 
nota_alu={"Pedro":7.0,"Noe":8.5,"Mara":6.5}
for alumno in nota_alu:
    print((nota_alu.get(alumno)))

for alumno in nota_alu.items():
    print(alumno)