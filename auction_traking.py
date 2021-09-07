#!/usr/bin/python3
'''
Módulo de seguimiento de subastas.
'''

# Importaciones
from webdriver import configurar_wd
from connection import agregar_subasta
from datetime import datetime as dt
import sys
import time

# Variables
nombre_usuario = 'Jona0103'
pass_usuario = '7!u?3eT$GLQHphWQ'

# Funciones


def traking(producto: str, url: str):
    wd = configurar_wd()
    wd.get('https://nookazon.com')
    ir_login = wd.find_element_by_xpath('//div[@class="nav-login-btns"]/a[1]')
    ir_login.click()
    wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    entrada_nombre_usuario = wd.find_element_by_name('username')
    entrada_nombre_usuario.send_keys(nombre_usuario)
    entrada_pass_usuario = wd.find_element_by_name('password')
    entrada_pass_usuario.send_keys(pass_usuario)
    boton_login = wd.find_element_by_xpath('//div[@class="login-btn-bar"]/button')
    boton_login.click()
    time.sleep(1)
    while True:
        wd.get(url)
        nombre_subastador = wd.find_element_by_xpath('//div[@class="listing-top"]/div[2]/div[2]/a/span[2]').text
        cantidad_subastada = int(wd.find_element_by_xpath('//div[@class="listing-header-name"]').text.split(' ')[0])
        try:
            while True:
                tiempo_restante = wd.find_element_by_xpath('//div[@class="listing-top"]/div[2]/div[5]').text
                if tiempo_restante != 'AUCTION OVER':
                    time.sleep(1)
                else:
                    time.sleep(2)
                    ofertas = wd.find_elements_by_class_name('listing-bells')
                    precio_base = int(ofertas[0].text.replace('.', ''))
                    ultima_oferta = int(ofertas[1].text.replace('.', ''))
                    fecha = dt.now()
                    fecha_actual = fecha.strftime('%Y-%m-%d')
                    hora_actual = fecha.strftime('%H:%M')
                    agregar_subasta([producto, nombre_subastador, cantidad_subastada, precio_base, ultima_oferta, fecha_actual, hora_actual])
                    time.sleep(5)
                    break
            break
        except:
            pass
        
    
if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2], sys.argv[3])
