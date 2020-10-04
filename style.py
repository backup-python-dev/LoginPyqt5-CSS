style="""
*{
    font-family :: century gothic;
}
QWidget{
    background-image: url("fondo.jpg");
}
QFrame#contenedor{
    width: 260px;
    height: 260px;
    border-radius: 15px;
    background: rgba(3,3,3,0.25);
    display: none;
}
QLabel#labelLogin{
  background: transparent;
  image: url("bloquear.png");
}
QLabel{
  background: transparent;
  color:rgb(255, 255, 255);
  font-family:Dyuthi;
  font-size: 22px;
  text-align: center;
}
QLabel:hover{
  background: transparent;
  font-family: -apple-system;
  color: rgb(209, 207, 214);
}
QLineEdit{
  background: transparent;
  border: none;
  border-bottom: 1px solid white;
  font-size: 18px;
  color:white;
  font-weight: bold;
  font-family:Chilanka;
}
QLineEdit#contrasenia{
  background: transparent;
  border: none;
  border-bottom: 1px solid white;
}
QPushButton{
  background: rgb(12, 73, 171);
  border-radius: 18px;
  color:white;
  font-family: 'Open Sans', sans-serif;
  font-weight: bold;
}
QPushButton:hover{
  background: rgb(41, 137, 255);
  border-radius: 18px;
  color:white;
  font-family: 'Open Sans', sans-serif;
  font-weight: bold;
}
"""