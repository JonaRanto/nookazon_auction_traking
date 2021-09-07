#!/usr/bin/python3
'''
Bot de seguimiento de subastas en Nookazon.
'''

# Importaciones
from messages import limpiar_consola, mensaje
from webdriver import configurar_wd
import subprocess
import time
import os

# Variables
#url_subasta = input('Ingresar url: ')
url_subasta = r'https://nookazon.com/product/1689860200/auctions?priceMin=0&priceMax=50000000&priceType=bells&orderBy=endtime-asc'
minuto_ejecucion = 5

# Código
os.system('mode con: cols=50 lines=10')
limpiar_consola()
wd = configurar_wd()
while True:
    wd.get(url_subasta)
    nombre_producto = str(wd.find_element_by_xpath(
                '//div[@class="product-name"]').text)
    grilla_subastas = wd.find_element_by_xpath('//div[@class="row"]')
    lista_subastas = grilla_subastas.find_elements_by_class_name(
        'listing-product-info')
    while True:
        limpiar_consola(nombre_producto)
        mensaje(1, 'Esperando...')
        try:
            hay_subastas = False
            for subasta in lista_subastas:
                if subasta.text.split('\n')[-1].split(' ')[-3] == '0h':
                    minuto = int(subasta.text.split('\n')
                                [-1].split(' ')[-2].replace('m', ''))
                    segundo = int(subasta.text.split(
                        '\n')[-1].split(' ')[-1].replace('s', ''))
                    mensaje(1, str(minuto) + ':' + str(segundo))
                    hay_subastas = True
                    if minuto == minuto_ejecucion and segundo <= 3:
                        url = str(subasta.find_element_by_tag_name(
                            'a').get_attribute('href'))
                        subprocess.Popen(
                            ['python', 'auction_traking.py', 'traking', nombre_producto, url])
                        time.sleep(5)
                        break
            if not hay_subastas:
                mensaje(1, 'No hay subastas actualmente. Recargando...')
                time.sleep(30)
                break
            time.sleep(1)
        except:
            break
