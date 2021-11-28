class Cliente:
    suspendidos=[] #Variable de Clase
    
    def __init__(self,codigo,nombre):
        self.codigo=codigo #Variable de Instancia
        self.nombre=nombre #Variable de Instancia

    def imprimir(self):
        print("Codigo: {}".format(self.codigo))
        print("Nombre: {}".format(self.nombre))
        self.esta_suspendido()
    
    def suspender(self):
        Cliente.suspendidos.append(self.codigo)
    
    def esta_suspendido(self):
        if self.codigo in Cliente.suspendidos:
            print("Esta suspendido")
            print("_____________________________")
        else:
            print("No esta suspendido")
            print("_____________________________")


cliente1=Cliente(1,"Juan")
cliente2=Cliente(2,"Ana")
cliente3=Cliente(3,"Diego")
cliente4=Cliente(4,"Pedro")
cliente3.suspender()
cliente4.suspender()

cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()

'''
Codigo: 1
Nombre: Juan
No esta suspendido
_____________________________
Codigo: 2
Nombre: Ana
No esta suspendido
_____________________________
Codigo: 3
Nombre: Diego
Esta suspendido
_____________________________
Codigo: 4
Nombre: Pedro
Esta suspendido
_____________________________
'''

##

class Operacion:
    def __init__(self):
        self.valor1=int(input("Ingrese primer valor:"))
        self.valor2=int(input("Ingrese segundo valor:"))
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()

    def __del__(self):
        print('Método delete llamado')

    def sumar(self):
        suma=self.valor1+self.valor2
        print("La suma es: {}".format(suma))

    def restar(self):
        resta=self.valor1-self.valor2
        print("La resta es: {}".format(resta))

    def multiplicar(self):
        producto=self.valor1*self.valor2
        print("El producto es: {}".format(producto))

    def dividir(self):
        division=self.valor1/self.valor2
        print("La division es: {}".format(division))

operacion1 = Operacion()

