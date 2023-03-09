import sys

from PyQt6.QtWidgets import QApplication
from ui.main_window import Main_Window
from ui.crud_window import CRUD_Window
import triangulos
import var_global

def w_triangulos():
    triangulos.abrir_triangulos()
    acciones = {
        "agregar"   : triangulos.agregar,
        "modificar" : triangulos.modificar,
        "eliminar"  : triangulos.eliminar,
    }
    campos = [1 ,8, 8, 8, 8, 8, 8] #Campos de formulario segun tipo de control

    frmCrud = CRUD_Window(var_global.window, # Parent
        "CRUD - Triangulos", # Titulo
        var_global.triangulos, # Datos []
        acciones, # Funciones {} sobre los registros
        campos # Tipos [] de control por campo
        )
    frmCrud.show()

def w_cuadrado(window):
    print("Hola")

if __name__ == "__main__":
    ventanas = {
        "&Triangulos": w_triangulos,
        "&Cuadrados" : w_cuadrado,
        "-" : None,
        "--" : None,
        "---" : None,
        "----" : None,
    }
    app = QApplication([])
    var_global.window = Main_Window(title="Bienvenidos a mi programa :D",datas=ventanas)
    var_global.window.show()
    sys.exit(app.exec())