# -*- coding:utf-8 -*-
# form_window.py

from logging import raiseExceptions
from PyQt6.QtWidgets import (
    QMainWindow, QWidget,
    QFormLayout, QGridLayout,
    QLineEdit, QTextEdit, QListView, QComboBox, QCheckBox, QDateEdit,
    QDateTimeEdit, QRadioButton, QButtonGroup, QSpinBox,
)
from controls.crud_buttons import Crud_Buttons
from controls.reg_navigator import Reg_Navigator

class CRUD_Window(QMainWindow):
    def __init__(self, parent=None, title=None, datas=[], crud_meths={}, fields=[]):
        """
        _summary_: Clase tipo CRUD, para manejo de registros.
        Args:
            parent (_QMainWindow o QWidget_, optional): _description_. Clase padre para compartir
                datos en caso de ser necesario. Defaults to None.
            title (_String_, optional): _description_. Cadena con título de la ventana.
                Defaults to None.
            datas (list, optional): _description_. Arreglo que contiene diccionarios con los
                registros de la tabla a manejar. Defaults to [].
            crud_meths (dict, optional): _description_. Diccionario con las acciones que servirán
                para manejar los registros, agregar, modificar, eliminar. Defaults to {}.
            fields (list, optional): _description_. Arreglo de numeros que indican los tipos
                de campos del formulario, según los tipos de datos. Defaults to [].

        Raises:
            Exception: Se puede presentar error al momento de recibir los datos, ya que puede
                no abrirse correctamente el archivo de origen.
        """
        super(CRUD_Window, self).__init__(parent)
        self.setWindowTitle("Ventana Formulario" if title == None else title)
        # Ventana principal que llamo al formulario
        self.__parent = parent
        ##############################################
        # Tamanio minimo de la ventana
        ##############################################
        self.minimumHeight = 400
        self.minimumWidth = 400
        ##############################################
        # Plantillas principal y secundarias
        ##############################################
        self.glayout = QGridLayout() # Plantilla principal
        self.flayout = QFormLayout() # Plantilla donde estan los campos
        self.btnCrud = Crud_Buttons(parent=self, meths=crud_meths) # Botones de administración de registros
        self.btnNav = Reg_Navigator(parent=parent,total=len(datas), upd=self.set_fields) # Botones de navegación de registros
        ##############################################
        # Manejo de datos del formulario
        ##############################################
        # Campos donde estan los datos del registro
        self.fields = []
        # Validar si la variable contenido tiene el tipo adecuado
        if hasattr(datas, "__len__"):
            if datas != []:
                self.datas = datas
        else:
            raise Exception("No hay contenido para crear la ventana.")
            return
        ##############################################
        # Agregar controles mediante plantillas
        ##############################################
        self.glayout.addLayout(self.flayout,0,0,10,3)
        self.glayout.addLayout(self.btnNav,11,0,1,3)
        self.glayout.addLayout(self.btnCrud,0,3,10,1)
        ##############################################
        # Agregar widget central que contiene plantilla principal
        ##############################################
        widget = QWidget() # Para establecer como central por usar MainWindow
        widget.setLayout(self.glayout) # Plantilla incluida dentro de widget
        self.setCentralWidget(widget)
        #self.setLayout(self.glayout)
        self.mk_fields(fields) # Crear campos solicitados para el formulario
        self.set_fields() # Mostrar valores

    def set_fields(self):
        """
        _summary_: Muestra los valores del registro según el control creado en mk_fields.
        """
        headers = ",".join(self.datas[0])
        headers = headers.split(",")
        i = 0
        for control in self.fields:
            if type(control) == QLineEdit:
                control.setText(self.datas[self.btnNav.actual_reg][headers[i]])
            elif type(control) == QSpinBox:
                control.setValue(int(self.datas[self.btnNav.actual_reg][headers[i]]))
            i = i + 1

    def get_fields(self):
        headers = ",".join(self.datas[0])
        headers = headers.split(",")
        i = 0
        reg = {}
        for control in self.fields:
            if type(control) == QLineEdit:
                reg[headers[i]] = control.text()
            elif type(control) == QSpinBox:
                reg[headers[i]] = control.value()
            i = i + 1
        return reg

    def mk_fields(self, fields):
        """
        _summary_: Crear los controles necesarios para mostrar los datos del registro.
        Args:
            fields (_Int Array_): Arreglo que representa los tipos de controles necesarios
            para mostrar los datos del registro. Deben ser acordes al tipo de datos.
        """
        # Campos incluidos []
        # QRadioButton - QButtonGroup
        headers = ",".join(self.datas[0])
        headers = headers.split(",")
        i = 0
        for field in fields:
            match field:
                case 1: # QLineEdit (1 linea)
                    self.fields.append(QLineEdit())
                case 2: # QTextEdit (Multilinea)
                    self.fields.append(QTextEdit())
                case 3: # QListWidget
                    self.fields.append(QListView())
                case 4: # QComboBox
                    self.fields.append(QComboBox())
                case 5: # QComboBox
                    self.fields.append(QCheckBox())
                case 6: # QDateEdit
                    self.fields.append(QDateEdit())
                case 7: # QDateTimeEdit
                    self.fields.append(QDateTimeEdit())
                case 8: #QSpinBox
                    self.fields.append(QSpinBox())

            self.flayout.addRow(headers[i], self.fields[len(self.fields) - 1]) # Agregar control al layout
            self.fields[len(self.fields) - 1].setEnabled(False) # Descativar control por defecto
            i = i + 1
    
    def set_fields_enabled(self,state=False):
        if type(state) == bool:
            for control in self.fields:
                control.setEnabled(state)
    
    def set_fields_clear(self):
        for control in self.fields:
            if type(control) == QLineEdit:
                control.setText("")
            elif type(control) == QSpinBox:
                control.value(0)
