import json
import csv
import pandas as pd
import matplotlib.pyplot as plt

from queue import Empty
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Clases.Navegador import Navegador
from Clases.Datos import Datos
from Clases.Acciones import Acciones

def siguientePagina():
    for c in data[2]['siguientePagina']:
        objetoAcciones.pagina_actual = c['pagina_actual']
        objetoAcciones.pagina_siguiente = c['pagina_siguiente']
        objetoAcciones.path = objetoAcciones.buscarPath(c['path'])

    paginaSiguiente = objetoDatos.driver.find_elements(objetoAcciones.path, objetoAcciones.pagina_siguiente)
    paginaActual =  objetoDatos.driver.find_element(objetoAcciones.path, objetoAcciones.pagina_actual)

    for i in paginaSiguiente:
        if (i.text == '←'):
            continue
        if (int(i.text) > int(paginaActual.text)):
            objetoDatos.driver.execute_script("arguments[0].click();", i)
            break

def abrirPaginaWeb():
    objetoDatos.driver.get(objetoDatos.pagina_web)

def maximizarVentana():
    objetoDatos.driver.maximize_window()

def crearTabla():
    for c in data[1]['tabla']:
        objetoDatos.nombre_csv = c['nombre_csv']
        objetoDatos.eje_x = c['x']
        objetoDatos.eje_y = c['y']
        objetoDatos.kind = c['kind']
        objetoDatos.crearTabla(c['x'], c['y'])

def navegarPagina():
        for c in data[5]['navegarPagina']:
            objetoAcciones.path = objetoAcciones.buscarPath(c['path'])
            objetoAcciones.valor = c['valor']
        
        scroll = objetoDatos.driver.find_element(objetoAcciones.path, objetoAcciones.valor)
        scroll.send_keys(Keys.END)

def darClicInput():
    for c in data[3]['escribirInput']:
        objetoAcciones.valor = c['valor']
        objetoAcciones.texto = c['texto']
        objetoAcciones.path = objetoAcciones.buscarPath(c['path'])

    input = objetoDatos.driver.find_element(objetoAcciones.path, objetoAcciones.valor)
    input.click()
    input.send_keys(objetoAcciones.texto)
    input.send_keys(Keys.ENTER)

def crearCSV():
    datos = objetoDatos.tabla_datos
    archivo = open(objetoDatos.nombre_csv, 'w')
    with archivo:
        writer = csv.writer(archivo)
        writer.writerows(datos)
    print("archivo creado")

def cerrarPaginaWeb():
    objetoDatos.driver.quit()

def crearGrafica():
    grafica = pd.read_csv(objetoDatos.nombre_csv, encoding='ISO-8859-1')
    grafica.plot(objetoDatos.eje_x, objetoDatos.eje_y, kind = objetoDatos.kind)
    plt.show()

def recolectarDatos():
    for c in data[4]['obtenerDatosTabla']:
        objetoAcciones.th = c['th']
        objetoAcciones.td = c['td']
        objetoAcciones.path = objetoAcciones.buscarPath(c['path'])

    listaElementos_titulos = objetoDatos.driver.find_elements(objetoAcciones.path, objetoAcciones.th)
    listaElementos_descripcion = objetoDatos.driver.find_elements(objetoAcciones.path, objetoAcciones.td)

    for i, c in zip(listaElementos_titulos, listaElementos_descripcion):
       objetoDatos.tabla_datos.append([i.text, c.text])

objetoNavegador = Navegador()
objetoDatos = Datos()
objetoAcciones = Acciones()

data = Empty

#Primera configuracion - Web
with open('./Configuracion/configuracion.json') as archivo:
    data = json.load(archivo)

    for i in data[0]['web']:
        objetoDatos.navegador = i['navegador']
        objetoDatos.ruta_driver = i['ruta_driver']
        objetoDatos.pagina_web = i['pagina_web']

if objetoNavegador.navegadores(objetoDatos.navegador) == 1:
    objetoDatos.driver = webdriver.Edge(objetoDatos.ruta_driver)

if objetoNavegador.navegadores(objetoDatos.navegador) == 2:
   objetoDatos.driver = webdriver.Chrome(objetoDatos.ruta_driver)

if objetoNavegador.navegadores(objetoDatos.navegador) == 3:
   objetoDatos.driver = webdriver.Firefox(objetoDatos.ruta_driver)


abrirPaginaWeb()
maximizarVentana()
darClicInput()
crearTabla()
for i in range(3):
    navegarPagina()
    siguientePagina()
    recolectarDatos()
crearCSV()
crearGrafica()
cerrarPaginaWeb()