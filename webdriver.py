#!/usr/bin/python3
'''
Módulo de configuración de WebDriver.
'''

# Importaciones
from messages import mensaje
import os

# Variables
chromedriver_file = os.getcwd() + '\\chromedriver.exe'
addblock_file = os.getcwd() + '\\uBlock_origin_1.37.2.crx'

# Funciones


def configurar_wd():
    '''
    Realizar la configuración del webdriver.
    '''
    from selenium import webdriver as wd
    config_chrome = wd.ChromeOptions()
    # Forzar el inicio de la web para un dispositivo compatible.
    config_chrome.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
    config_chrome.add_argument('--disable-notifications')
    config_chrome.add_experimental_option(
        'excludeSwitches', ['enable-logging'])
    config_chrome.add_extension(addblock_file)
    try:
        # Ejecuta el controlador de chrome ubicado en la raiz y le pasa las opciones configuradas
        wd = wd.Chrome(executable_path=chromedriver_file,
                       options=config_chrome)
    except Exception as e:
        mensaje(2, e)
    wd.implicitly_wait(10)
    return wd
