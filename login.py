from PyQt5 import QtCore, QtGui, QtWidgets
import style
import sys

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.setFixedSize(638, 680)
        Login.setStyleSheet(style.style)
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.contenedor = QtWidgets.QFrame(self.centralwidget)
        self.contenedor.setGeometry(QtCore.QRect(160, 70, 331, 501))
        self.contenedor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contenedor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contenedor.setObjectName("contenedor")
        self.labelUsuario = QtWidgets.QLabel(self.contenedor)
        self.labelUsuario.setGeometry(QtCore.QRect(40, 140, 91, 31))
        self.labelUsuario.setObjectName("labelUsuario")
        self.label = QtWidgets.QLabel(self.contenedor)
        self.label.setGeometry(QtCore.QRect(40, 260, 161, 31))
        self.label.setObjectName("label")
        self.contrasenia = QtWidgets.QLineEdit(self.contenedor)
        self.contrasenia.setGeometry(QtCore.QRect(40, 300, 261, 28))
        self.contrasenia.setEchoMode(QtWidgets.QLineEdit.Password)
        self.contrasenia.setObjectName("contrasenia")
        self.Iniciar = QtWidgets.QPushButton(self.contenedor)
        self.Iniciar.setGeometry(QtCore.QRect(90, 390, 131, 41))
        self.Iniciar.setObjectName("Iniciar")
        self.labelLogin = QtWidgets.QLabel(self.contenedor)
        self.labelLogin.setGeometry(QtCore.QRect(140, 40, 71, 51))
        self.labelLogin.setText("")
        self.labelLogin.setObjectName("labelLogin")
        self.lineEdit = QtWidgets.QLineEdit(self.contenedor)
        self.lineEdit.setGeometry(QtCore.QRect(40, 180, 261, 28))
        self.lineEdit.setObjectName("lineEdit")
        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.labelUsuario.setText(_translate("Login", "EMAIL"))
        self.label.setText(_translate("Login", "PASSWORD"))
        self.Iniciar.setText(_translate("Login", "Iniciar Sesión"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
