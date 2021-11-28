# -*- coding: utf-8 -*-

# Torre de Control

class TorreDeControl:
    '''Modela el trabajo de una torre de control de una aeropuerto, 
    con una pista de aterrizaje.
    Los aviones que están esperando para aterrizar tienen prioridad sobre 
    los que están esperando para despegar.
    '''

    def __init__(self):
        '''Crea una lista vacía para los aviones a aterrizar y otra para los
        aviones a despegar.'''
        self.avion_aterrizar = []
        self.avion_despegar = []


    def nuevo_arribo(self, arribo):
        '''Encola el avion que arriba a la lista avion_aterrizar.'''
        self.avion_aterrizar.append(arribo)


    def nueva_partida(self, partida):
        '''Encola el avion que partirá a la lista avion_despegar.'''
        self.avion_despegar.append(partida)


    def ver_estado(self):
        '''Imprime los aviones en la cola'''
        print('Vuelos esperando para aterrizar: ', end = '')
        print(*self.avion_aterrizar, sep = ', ')
        print('Vuelos esperando para despegar: ', end = '')
        print(*self.avion_despegar, sep = ', ',)


    def asignar_pista(self):
        '''Desencola en primer lugar los aviones a aterrizar. Luego
        desencola los aviones a despegar comenzando desde el primer elemento de 
        la lista avion_despegar. Si las listas están vacía, notifica que no hay vuelos en espera.'''
        # Notificación listas vacías

        # Desencolar
        try:
            if len(self.avion_aterrizar) != 0: #Si hay aviones para aterrizar, aterrizar es prioridad
                print(f'El vuelo {self.avion_aterrizar[0]} aterrizó con éxito')
                self.avion_aterrizar.pop(0)
            else: #Si no hay, despegar
                print(f'El vuelo {self.avion_despegar[0]} despegó con éxito')
                self.avion_despegar.pop(0)
        
        except IndexError:
            print('No hay vuelos en espera')


torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre.ver_estado()
#Vuelos esperando para aterrizar: AR156, AR32
#Vuelos esperando para despegar: KLM1267
torre.asignar_pista()
#El vuelo AR156 aterrizó con éxito.
torre.asignar_pista()
#El vuelo AR32 aterrizó con éxito.
torre.asignar_pista()
#El vuelo KLM1267 despegó con éxito.
torre.asignar_pista()
#No hay vuelos en espera