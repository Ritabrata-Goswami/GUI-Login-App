import sys
import pyodbc 
from PyQt5 import *
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtQuick import QQuickWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pathlib import Path



conn_mssql = pyodbc.connect('Driver={SQL Server};'
        'Server=ABC\SQLEXPRESS;'
        'Database=Python_GUI;'
        'Trusted_Connection=yes;')

class LoginGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(500,500,600,500)

        vertical_layout=QVBoxLayout()
        horizontal_layout = QHBoxLayout()
        form_layout = QFormLayout()
        

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

        self.setUserName=QLabel(self,
                                alignment=Qt.AlignmentFlag.AlignHCenter
                                )
        self.setUserName.setObjectName("userName")
        self.setUserName.hide()

        self.setUserAge=QLabel(self,
                                alignment=Qt.AlignmentFlag.AlignHCenter
                               )
        self.setUserAge.setObjectName("userAge")
        self.setUserAge.hide()

        self.setUserEmail=QLabel(self)
        self.setUserEmail.setObjectName("userEmail")
        self.setUserEmail.hide()

        self.setUserPhone=QLabel(self,
                                alignment=Qt.AlignmentFlag.AlignHCenter
                                )
        self.setUserPhone.setObjectName("userPhone")
        self.setUserPhone.hide()

        vertical_layout.addWidget(self.loginSuccess)
        vertical_layout.addWidget(self.setUserName)
        horizontal_layout.addWidget(self.setUserAge)
        horizontal_layout.addWidget(self.setUserEmail)
        horizontal_layout.addWidget(self.setUserPhone)
        

        self.line_gap=QLabel("Enter Data Below",
                                alignment=Qt.AlignmentFlag.AlignHCenter
                            )
        self.line_gap.setObjectName("line_gap")
        self.line_gap.hide()

        self.form_des1=QLabel("Enter ProductId:- ")
        self.form_des1.setObjectName("form_description")
        self.form_entry1=QLineEdit(self, 
                  placeholderText="Enter Product Id"
                )
        self.form_entry1.setObjectName("form_entry")
        form_layout.addRow(self.form_des1, self.form_entry1)

        self.form_des2=QLabel("Enter Product Name:- ")
        self.form_des2.setObjectName("form_description")
        self.form_entry2=QLineEdit(self, 
                  placeholderText="Enter Product Name"
                )
        self.form_entry2.setObjectName("form_entry")
        form_layout.addRow(self.form_des2, self.form_entry2)

        self.form_des3=QLabel("Enter Product Weight (Kg):- ")
        self.form_des3.setObjectName("form_description")
        self.form_entry3=QLineEdit(self, 
                                placeholderText="Enter Product Weight"
                            )
        self.form_entry3.setObjectName("form_entry")
        form_layout.addRow(self.form_des3, self.form_entry3)

        self.form_entry_btn=QPushButton("Add Data")
        self.form_entry_btn.setObjectName("form_entry_btn")
        form_layout.addRow(self.form_entry_btn)
        self.form_entry_btn.clicked.connect(self.sendData)

        self.UserId=QLabel(self)
        self.UserId.hide()

        self.form_des1.hide()
        self.form_entry1.hide()
        self.form_des2.hide()
        self.form_entry2.hide()
        self.form_des3.hide()
        self.form_entry3.hide()
        self.form_entry_btn.hide()


        vertical_layout.addLayout(horizontal_layout)
        vertical_layout.addWidget(self.line_gap)
        vertical_layout.addLayout(form_layout)

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
        

        self.show()     #display GUI.


    def getLogin(self):
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
                
                self.UserId.setText(str(getUserData[0]))
                self.loginSuccess.show()
                self.setUserName.setText(f"Welcome {getUserData[3]} in dashboard")
                self.setUserName.show()
                self.setUserAge.setText(f"Age:- {getUserData[4]}")
                self.setUserAge.show()
                self.setUserEmail.setText(f"Email:- {getUserData[5]}")
                self.setUserEmail.show()
                self.setUserPhone.setText(f"Phone:- {getUserData[6]}")
                self.setUserPhone.show()

                self.form_des1.show()
                self.form_entry1.show()
                self.form_des2.show()
                self.form_entry2.show()
                self.form_des3.show()
                self.form_entry3.show()
                self.form_entry_btn.show()
                self.line_gap.show()

            else:
                print("Login Failed!")

            sqlservercursor.close()
        else:
            QMessageBox.warning(
                self,
                'Warning',
                'User Id and Password Both are mandatory!'
            )
    

    def sendData(self):
        productId=self.form_entry1.text()
        productName=self.form_entry2.text()
        productWeight=self.form_entry3.text()
        userId=self.UserId.text()

        self.form_entry1.setText("")
        self.form_entry2.setText("")
        self.form_entry3.setText("")

        sqlservercursor = conn_mssql.cursor()
        sqlservercursor.execute("INSERT INTO GUI_DATA_ENTRY (UserId,Product_Id,Product_Name,Product_Weight) VALUES (?,?,?,?)",userId,productId,productName,productWeight)
        QMessageBox.information(
                self,
                'Information',
                'Data added successfully!'
            )
        conn_mssql.commit()
        sqlservercursor.close()


if __name__=='__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(Path('login.qss').read_text())
    loginapp=LoginGUI()
    sys.exit(app.exec())
