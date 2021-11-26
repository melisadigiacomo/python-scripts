# -*- coding: utf-8 -*-

# Seconds lived

import datetime

def segundos_vida(fecha_nacimiento):
    '''A partir de tu fecha de nacimiento 'dd/mm/AAAA', la función devuelve la 
    cantidad de segundos que viviste hasta el momento'''

    # Fecha y hora de nacimiento
    fechayhora_nacimiento = datetime.datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
    # Fecha y hora actual
    fechayhora_actual = datetime.datetime.now()
    
    # Duración de la vida
    vida = fechayhora_actual - fechayhora_nacimiento
    return vida.total_seconds()

segundos = segundos_vida('24/03/1990')
print(segundos)

# Formating the number  

from math import log, floor

def human_format(number):
    units = ['', 'K', 'M', 'G', 'T', 'P']
    k = 1000.0
    magnitude = int(floor(log(number, k)))
    return '%.2f%s' % (number / k**magnitude, units[magnitude])

print(f'You have already lived {human_format(segundos)} seconds')