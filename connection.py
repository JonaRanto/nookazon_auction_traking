#!/usr/bin/python3
'''
Módulo de conexión a la base de datos.
'''

# Importaciones
from babel.numbers import format_currency
import sqlite3
import os

# Variables
nombre_db = os.getcwd() + '\\database.db'

# Funciones


def ejecutar_query(query: str, parametros: list = []):
    '''
    Recibe una consulta y parametros para realizar una conexión a la base dedatos.
    '''
    with sqlite3.connect(nombre_db) as conn:
        cursor = conn.cursor()
        resultado = cursor.execute(query, parametros)
        conn.commit()
    return resultado


def obtener_subastas():
    '''
    Obtiene toda la lista de subastas.
    '''
    query = 'SELECT * FROM subasta'
    filas = ejecutar_query(query)
    resultado = []
    for fila in filas:
        resultado.append(list(fila))
    return resultado


def agregar_subasta(parametros: list = []):
    '''
    Recibe una lista de parametros para añadir una subasta y la añada.
    '''
    query = 'INSERT INTO subasta VALUES(NULL, ?, ?, ?, ?, ?, ? ,?)'
    ejecutar_query(query, parametros)


def promedio_subastas(parametros: str = 'None'):
    '''
    Devuelve el promedio de las subastas formateado.
    '''
    query = 'SELECT AVG(precio_final/cantidad) AS promedio_subastas FROM subasta WHERE producto LIKE "' + parametros + '"'
    filas = ejecutar_query(query)
    try:
        for fila in filas:
            raw_resultado = int(fila[0])
            resultado = str(format_currency(
                raw_resultado, currency='CLP', locale='es_CL'))
    except:
        resultado = 'None'
    return resultado
