# -*- coding:utf-8 -*-
# main_window.py

"""Main window-style application."""

from PyQt6.QtWidgets import (
    QLabel,
    QPushButton,
    QMainWindow,
    QWidget,
    QStatusBar,
    QToolBar,
    QGridLayout,
    QVBoxLayout,
)
from ui.crud_window import CRUD_Window

class Main_Window(QMainWindow):
    """
    _summary_: Ventana principal de aplicación.

    Args:
        QMainWindow (_type_): _Hereda de ventana principal de QT._
    """

    def __init__(self, parent=None, title=None, datas=None):
        """
        _summary_: Ventana principal de aplicación.
        Args:
            parent (_QMainWindow o QWidget_, optional): _description_. Ventana padre para intercambio de datos.
                Defaults to None.
            title (_String_, optional): _description_. Título de la ventana o aplicación.
                Defaults to None.
            datas (_dict_, optional): _description_. Diccionario con las ventanas a trabajar.
                Defaults to None.
        """
        super().__init__(parent=parent)
        self.setWindowTitle(title if title != None else "Ventana") # Titulo de ventana
        self.setMinimumSize(800,600) # Tamanio minimo
        self.btns = []
        layout = QGridLayout() # Plantilla de espacios externos (Margin)
        layout1 = QVBoxLayout() # Plantilla para organizar botones
        layout.addWidget(QLabel("-"),0,0,1,3) # Organizar la plantilla para que el botón quede en el centro
        layout.addWidget(QLabel("-"),1,0,3,1)
         ##############################################
        # Agregar botones para abrir ventanas de CRUD
        ##############################################
        for key in datas:
            btn = QPushButton(key)
            layout1.addWidget(btn) # Widget para agregar en el centro
            if datas[key] == None:
                btn.setEnabled(False)  # Si la funcion esta vacia, desactivar boton
            else:
                btn.clicked.connect(datas[key]) # Conectar evento click de boton a slot
        layout.addLayout(layout1,1,1)
        layout.addWidget(QLabel("-"),1,2,3,1)
        layout.addWidget(QLabel("-"),2,0,1,3)
         ##############################################
        # Widget Central
        ##############################################
        widget = QWidget() # Para establecer como central por usar MainWindow
        widget.setLayout(layout) # Plantilla incluida dentro de widget
        self.setCentralWidget(widget)
        self._createMenu(datas) # Crear menu
        self._createToolBar(datas) # Crear barra de herramientas
        self._createStatusBar() # Crear barra de status

    def _createMenu(self, datas):
        menu = self.menuBar().addMenu("&Menu")
        for key in datas:
            if datas[key] != None:
                menu.addAction(key, datas[key])

        menu.addAction("&Exit", self.close)

    def _createToolBar(self, datas):
        tools = QToolBar()
        for key in datas:
            if datas[key] != None:
                tools.addAction(key, datas[key])
        tools.addAction("Exit", self.close)
        self.addToolBar(tools)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)

    def hola(self):
        print("Hola mundo")