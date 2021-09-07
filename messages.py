#!/usr/bin/python3
'''
Módulo de control de mensajes por consola.
'''

# Importaciones
from connection import promedio_subastas
from colorama.ansi import Style
import colorama
import os

# Funciones
def mensaje(tipo: int, mensaje):
    '''
    Recibe un tipo de mensaje 0:[-] | 1:[INFO] | 2:[ERROR] | 3:[IMPORTANTE] y el mensaje e imprime un mensaje formateado.
    '''
    mensaje = str(mensaje)
    if tipo == 1:
        print(colorama.Fore.YELLOW, ' [INFO] ' + mensaje + Style.RESET_ALL)
    elif tipo == 2:
        print(colorama.Fore.RED, ' [ERROR] ' + mensaje + Style.RESET_ALL)
    elif tipo ==3:
        print(colorama.Fore.CYAN, ' [IMPORTANTE] ' + mensaje + Style.RESET_ALL)
    else:
        print(colorama.Fore.WHITE, ' [-] ' + mensaje + Style.RESET_ALL)


def limpiar_consola(producto:str = 'None'):
    '''
    Limpia la consola e imprime un texto por defecto.
    '''
    comando = 'clear'
    if os.name in ('nt', 'dos'):
        comando = 'cls'
    os.system(comando)
    mensaje(0, 'Producto: ' + producto)
    mensaje(0, 'Precio promedio: ' + promedio_subastas(producto))
