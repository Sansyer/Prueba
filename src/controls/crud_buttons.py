# -*- coding:utf-8 -*-
# reg_window.py

from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QMessageBox

class Crud_Buttons(QVBoxLayout):
    """
    _summary_: Barra de botones CRUD

    Args:
        QVBoxLayout (_type_): _Hereda de plantilla de organización vertical para posición de botones_
    """
    def __init__(self, parent=None, meths=None):
        # Constructor de super clase
        super(Crud_Buttons, self).__init__()
        # Variable de registro actual
        self.actual_act = 0
        self.parent = parent
        self.btnCreate = QPushButton("&Agregar")
        self.btnModify = QPushButton("&Modificar")
        self.btnSearch = QPushButton("&Buscar")
        self.btnDelete = QPushButton("&Eliminar")
        self.btnClose = QPushButton("&Cerrar")
        self.meths = meths
        self.addWidget(self.btnCreate)
        self.addWidget(self.btnModify)
        self.addWidget(self.btnSearch)
        self.addWidget(self.btnDelete)
        self.addWidget(self.btnClose)

        self.btnCreate.clicked.connect(self.set_create)
        self.btnModify.clicked.connect(self.set_modify)
        self.btnDelete.clicked.connect(self.set_delete)
        self.btnClose.clicked.connect(self.set_close)

    def set_create(self):
        total = len(self.parent.datas)
        if self.btnCreate.text == "&Guardar":
            # Guardar el registro
            reg = self.parent.get_fields() # Obtener valores de los campos del formulario
            self.parent.datas.append(reg) # Agregar registro nuevo
            self.parent.btnNav.total = len(self.parent.datas) # Actualizar total de registros
            self.parent.btnNav.actual_reg = 0 # Mover registro actual al principio
            self.parent.set_fields() # Mostrar registro en ventana
            self.parent.set_fields_enabled(False)
            
            self.btnCreate.setText("&Agregar")
            self.btnModify.setEnabled(True)
            self.btnSearch.setEnabled(True)
            self.btnDelete.setEnabled(True)
            self.btnClose.setText("&Cerrar")
        else:
            # Activar el formulario para agregar
            self.btnCreate.setText("&Guardar")
            self.btnModify.setEnabled(False)
            self.btnSearch.setEnabled(False)
            self.btnDelete.setEnabled(False)
            self.btnClose.setText("&Cancelar")
            self.parent.set_fields_clear() # Borrar contenido de los campos
            self.parent.set_fields_enabled(True) # Activar los campos para escribir
            self.parent.fields[0].setEnabled(False) # Suponiendo que el primer campo es ID
            self.parent.fields[0].setText(total) # Siguiente numero en el consecutivo

    def set_modify(self):
        print("Hola mundo")

    def set_search(self):
        print("Hola mundo")

    def set_delete(self):
        btn = QMessageBox.question(self,"Confirmar ...","¿Esta seguro de borrar este regsistro?")

    def set_close(self):
        if self.btnClose.text() == "&Cancelar":
            self.btnCreate.setText("&Agregar")
            self.btnModify.setEnabled(True)
            self.btnSearch.setEnabled(True)
            self.btnDelete.setEnabled(True)
            self.btnClose.setText("&Cerrar")
        else:
            self.parent.hide()