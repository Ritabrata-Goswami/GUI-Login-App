import sys
import pyodbc 
from PyQt5 import *
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtQuick import QQuickWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pathlib import Path


class LoginGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(500,500,500,500)

        vertical_layout=QVBoxLayout()
        
        self.heading_1=QLabel("Login",
                        alignment=Qt.AlignmentFlag.AlignHCenter
                        )
        self.heading_1.setObjectName('FirstHeading')
        self.heading_2=QLabel("Enter UserId and Password",
                        alignment=Qt.AlignmentFlag.AlignHCenter
                        )
        self.heading_2.setObjectName('SecondHeading')

        self.UserId_txt=QLabel("User Id:")
        self.UserId_txt.setObjectName("userid")
        self.Enter_User_Id=QLineEdit(self, 
                                placeholderText="Enter Your User Id"
                                )
        self.Enter_User_Id.setObjectName("useridfield")
        self.Password_txt=QLabel("Password:")
        self.Password_txt.setObjectName("password")
        self.Enter_Pass=QLineEdit(self, 
                            placeholderText="Enter Your Password", 
                            echoMode=QLineEdit.EchoMode.Password
                            )
        self.Enter_Pass.setObjectName("passwordfield")

        self.LoginBtn=QPushButton("Login")
        self.LoginBtn.setObjectName("LoginBtn")
        self.LoginBtn.clicked.connect(self.getLogin)


        self.loginSuccess=QLabel("Welcome to Dashboard", 
                                alignment=Qt.AlignmentFlag.AlignHCenter
                                )
        self.loginSuccess.setObjectName("LoginSuccessful")
        self.loginSuccess.hide()

        self.setUserName=QLabel(self)
        self.setUserName.setObjectName("userName")
        self.setUserName.hide()

        self.setUserAge=QLabel(self)
        self.setUserAge.setObjectName("userAge")
        self.setUserAge.hide()

        self.setUserEmail=QLabel(self)
        self.setUserEmail.setObjectName("userEmail")
        self.setUserEmail.hide()

        self.setUserPhone=QLabel(self)
        self.setUserPhone.setObjectName("userPhone")
        self.setUserPhone.hide()

        vertical_layout.addWidget(self.loginSuccess)
        vertical_layout.addWidget(self.setUserName)
        vertical_layout.addWidget(self.setUserAge)
        vertical_layout.addWidget(self.setUserEmail)
        vertical_layout.addWidget(self.setUserPhone)
        
        vertical_layout.addStretch()

        vertical_layout.addWidget(self.heading_1)
        vertical_layout.addWidget(self.heading_2)
        vertical_layout.addWidget(self.UserId_txt)
        vertical_layout.addWidget(self.Enter_User_Id)
        vertical_layout.addWidget(self.Password_txt)
        vertical_layout.addWidget(self.Enter_Pass)
        vertical_layout.addWidget(self.LoginBtn)

        vertical_layout.addStretch()
        self.setLayout(vertical_layout)
        

        self.show()


    def getLogin(self):
        conn_mssql = pyodbc.connect('Driver={SQL Server};'
                'Server=ABC\SQLEXPRESS;'
                'Database=Python_GUI;'
                'Trusted_Connection=yes;')
        
        getUserId=self.Enter_User_Id.text()
        getPass=self.Enter_Pass.text()

        if(getUserId!="" and getPass!=""):
            # print("User Id:- "+getUserId)
            # print("Password:- "+getPass)

            sqlservercursor = conn_mssql.cursor()

            sqlservercursor.execute("SELECT * FROM GUI_APP_LOGIN WHERE userId=? AND pass=?", getUserId, getPass)
            getUserData = sqlservercursor.fetchone()

            if(getUserData):

                self.heading_1.hide()
                self.heading_2.hide()
                self.UserId_txt.hide()
                self.Enter_User_Id.hide()
                self.Password_txt.hide()
                self.Enter_Pass.hide()
                self.LoginBtn.hide()

                self.loginSuccess.show()
                self.setUserName.setText(f"Welcome {getUserData[3]} in dashboard")
                self.setUserName.show()
                self.setUserAge.setText(f"Age:- {getUserData[4]}")
                self.setUserAge.show()
                self.setUserEmail.setText(f"Email:- {getUserData[5]}")
                self.setUserEmail.show()
                self.setUserPhone.setText(f"Phone:- {getUserData[6]}")
                self.setUserPhone.show()

            else:
                print("Login Failed!")

            sqlservercursor.close()
        else:
            QMessageBox.warning(
                self,
                'Warning',
                'User Id and Password Both are mandatory!'
            )


if __name__=='__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(Path('login.qss').read_text())
    loginapp=LoginGUI()
    sys.exit(app.exec())