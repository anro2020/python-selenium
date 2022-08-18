from queue import Empty
from selenium import webdriver

class Datos(object):
    ruta_driver:str
    navegador:str
    pagina_web:str
    driver:str
    tabla_datos:Empty
    nombre_csv:str
    eje_x:str
    eje_y:str
    kind:str

    def __init__(self):
        self.ruta_driver = Empty
        self.navegador = Empty
        self.pagina_web = Empty
        self.driver = webdriver
        self.tabla_datos = []
        self.nombre_csv = Empty
        self.eje_x = Empty
        self.eje_y = Empty
        self.kind = Empty

    def crearTabla(self, x, y):
        self.tabla_datos = [[x,y]]





