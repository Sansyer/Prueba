# -*- coding:utf-8 -*-
# reg_window.py

from PyQt6.QtWidgets import QHBoxLayout, QPushButton, QLabel
import qtawesome

class Reg_Navigator(QHBoxLayout):
    """
    _summary_: Barra de navegación de registros

    Args:
        QHBoxLayout (_type_): _Hereda de plantilla de organización horizonal para posición de botones_
    """
    def __init__(self, parent=None, total=0, upd=None):
        """
        _summary_: Control con botones de navegación por registros.
        Args:
            parent (_type_, optional): _description_. Ventana contenedora para intercambio de datos.
                Defaults to None.
            total (int, optional): _description_. Total de registros.
                Defaults to 0.
            upd (_type_, optional): _description_. Metodo de actualización de datos.
                Defaults to None.
        """
        # Constructor de super clase
        super(Reg_Navigator, self).__init__()
        # Variable de registro actual
        self.actual_reg = 0
        # Validar que el numero total de registros sea valido
        if type(total) == int:
            self.total = total
        else:
            self.total = 0
        self.parent = parent
        self.btn1 = QPushButton(qtawesome.icon("fa5s.step-backward"), "")
        self.btn2 = QPushButton(qtawesome.icon("fa5s.backward"), "")
        self.btn3 = QPushButton(qtawesome.icon("fa5s.forward"), "")
        self.btn4 = QPushButton(qtawesome.icon("fa5s.step-forward"), "")
        self.lblReg = QLabel("Reg .. de ..")
        self.upd_method = upd
        self.addWidget(self.btn1)
        self.addWidget(self.btn2)
        self.addWidget(self.lblReg)
        self.addWidget(self.btn3)
        self.addWidget(self.btn4)
        self.btn1.clicked.connect(self.set_aback)
        self.btn2.clicked.connect(self.set_back)
        self.btn3.clicked.connect(self.set_forw)
        self.btn4.clicked.connect(self.set_aforw)

    def set_aback(self):
        self.actual_reg = 0
        self.upd_method()
        self.update_reg()

    def set_back(self):
        if self.actual_reg <= 0:
            self.actual_reg = self.total - 1
        else:
            self.actual_reg -= 1
        self.upd_method()
        self.update_reg()

    def set_forw(self):
        if self.actual_reg >= (self.total - 1):
            self.actual_reg = 0
        else:
            self.actual_reg += 1
        self.upd_method()
        self.update_reg()

    def set_aforw(self):
        self.actual_reg = self.total - 1
        self.upd_method()
        self.update_reg()

    def update_reg(self):
        """
        _summary_ : Actualizar registro mostrado actualmente
        """
        self.lblReg.setText("Reg " + str(self.actual_reg + 1) + " de " + str(self.total))