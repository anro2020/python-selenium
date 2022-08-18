from queue import Empty
from selenium.webdriver.common.by import By
from selenium import webdriver

class Acciones(object):
    accion:str
    path:str
    valor:str
    pagina_actual:str
    pagina_siguiente:str
    texto:str
    th:str
    td:str
    driver:webdriver

    def __init__(self):
        self.accion = Empty
        self.path = Empty
        self.pagina_actual = Empty
        self.pagina_siguiente = Empty
        self.valor = Empty
        self.texto = Empty
        self.th = Empty
        self.td = Empty

    def buscarPath(self, path):
        if path == "XPATH":
            return By.XPATH

        if path == "CLASS_NAME":
            return By.CLASS_NAME

        if path == "CSS_SELECTOR":
            return By.CSS_SELECTOR

        if path == "ID":
            return By.ID

        if path == "LINK_TEXT":
            return By.LINK_TEXT

        if path == "NAME":
            return By.NAME

        if path == "TAG_NAME":
            return By.TAG_NAME

        if path == "PARTIAL_LINK_TEXT":
            return By.PARTIAL_LINK_TEXT






