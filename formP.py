# Form implementation generated from reading ui file 'c:\Users\Genesis\Documents\Progra2\ProyectoEDD\formP.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ventana(object):
    def setupUi(self, ventana):
        ventana.setObjectName("ventana")
        ventana.resize(400, 166)
        self.label = QtWidgets.QLabel(parent=ventana)
        self.label.setGeometry(QtCore.QRect(30, 70, 131, 16))
        self.label.setObjectName("label")
        self.txt_Contrasena = QtWidgets.QLineEdit(parent=ventana)
        self.txt_Contrasena.setGeometry(QtCore.QRect(120, 70, 271, 22))
        self.txt_Contrasena.setObjectName("txt_Contrasena")
        self.txt_Archivo = QtWidgets.QLineEdit(parent=ventana)
        self.txt_Archivo.setGeometry(QtCore.QRect(120, 30, 271, 22))
        self.txt_Archivo.setObjectName("txt_Archivo")
        self.label_2 = QtWidgets.QLabel(parent=ventana)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 131, 16))
        self.label_2.setObjectName("label_2")
        self.btn_Aceptar = QtWidgets.QPushButton(parent=ventana)
        self.btn_Aceptar.setGeometry(QtCore.QRect(40, 130, 75, 24))
        self.btn_Aceptar.setObjectName("btn_Aceptar")
        self.btn_cancelar = QtWidgets.QPushButton(parent=ventana)
        self.btn_cancelar.setGeometry(QtCore.QRect(290, 130, 75, 24))
        self.btn_cancelar.setObjectName("btn_cancelar")

        self.retranslateUi(ventana)
        QtCore.QMetaObject.connectSlotsByName(ventana)

    def retranslateUi(self, ventana):
        _translate = QtCore.QCoreApplication.translate
        ventana.setWindowTitle(_translate("ventana", "Dialog"))
        self.label.setText(_translate("ventana", "Contraseña:"))
        self.label_2.setText(_translate("ventana", "Archivo:"))
        self.btn_Aceptar.setText(_translate("ventana", "Aceptar"))
        self.btn_cancelar.setText(_translate("ventana", "Cancelar"))