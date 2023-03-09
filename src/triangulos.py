# -*- coding:utf-8 -*-
# triangulos.py

from utils.data_file import Data_File
import var_global

def abrir_triangulos():
    """
    _summary_: Abrir archivo que contiene los datos de figuras anteriores.
    Raises:
        Exception: Error al abrir el archivo.
    """
    f = "../data/triangulos.csv"
    triangulos = ""
    try:
        df = Data_File(f)
        var_global.triangulos = df.load_content()
    except:
        raise Exception("Error en la apertura del archivo de triangulos")

def agregar(nuevo=None):
    """
    _summary_: Agregar una nueva figura a la estructura.
    Args:
        nuevo (_dict_, optional): _description_. Diccionario con los campos a agregar
            a los datos existentes. Defaults to None.
    """
    if nuevo != None:
        var_global.triangulos.append(nuevo)

def modificar(contenido=None,nreg=0):
    """
    _summary_: Modificar una figura existente.
    Args:
        contenido (_dict_, optional): _description_. Diccionario con los valores de campo
            para modificar el registro anterior. Defaults to None.
        nreg (int, optional): _description_. Número de registro a modificar. Defaults to 0.
    """
    if contenido != None and type(contenido) == dict and nreg >= 0:
        for clave in contenido:
            var_global.triangulos[clave] = contenido[clave]

def eliminar(nreg=0):
    """
    _summary_: Eliminar un registro de la tala de figuras.
    Args:
        nreg (int, optional): _description_. Número de registro a eliminar. Defaults to 0.
    """
    if nreg >= 0:
        var_global.triangulos.pop(nreg)
