# -*- coding:utf-8 -*-
# data_file.py

from os import path

class Data_File():
    def __init__(self,file=""):
        if file != "" and type(file) == str:
            if path.exists(file):
                self.file = file
            else:
                raise Exception("El archivo no existe")
        else:
            raise Exception("No es un nombre de archivo válido")

    def load_content(self):
        """
        _summary_: Carga el contenido de una archivo separado por comas y lo almacena
            en un arreglo de diccionarios. De la forma:
            [
                {
                    Campo: valor
                }
            ]
            NOTA: El archivo debe tener en cabezado.

        Returns:
            _type_: _array[ dict{} ]_
        """
        # Cargar encabezado
        file = open(self.file,"r")
        header = file.readline() # leer línea del archivo
        header = header.split(",") # Cortarla cada que haya coma
        datas = []  # Arreglo que guardara los registros
        #first = True # Variable para evitar que se cargue como registro el encabezado
        for line in file:
            data = {} # Diccionario que almacena un registro
         #   if first == True:
                # Evitar la primera linea por ser encabezado
         #       first = False
         #   else:
            register = line.split(",") # Separa la línea por comas
            for i in list(range(0, len(header))):
                # Según la cantidad de encabezados, cargar cada valor y crear n registro
                header[i] = header[i].replace("\n", "") # Remover el salto de línea
                data[header[i]] = register[i].replace("\n", "") # Remover el salto de línea
            datas.append(data) # Almacenar el registro en el arreglo luego de crear el diccionario
        return datas # Retornar el arreglo con los registros

    def save_content(self, datas):
        file = open(file, "w") # Escribir sin tener en cuenta contenido anterior
        # file.truncate(0) # Sería parta borrar contenido anterior si fuera necesario
        claves = ",".join(datas[0]) #Unir en un String todos los encabezados
        try:
            file.write(claves + "\n")
            for reg in datas:
                valores = ",".join(reg.values())
                file.write(valores + "\n")
            file.close()
        except:
            file.close()
            raise Exception("Hubo un error en la escritura del archivo")