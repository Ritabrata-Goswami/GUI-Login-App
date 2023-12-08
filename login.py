import sys
import pyodbc 
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtQuick import QQuickWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pathlib import Path



          #Python_GUI
readDbFile = open("dbName.txt", "r")
dbName=readDbFile.read()
conn_mssql = pyodbc.connect('Driver=SQL Server;'
        'Server=ABC\SQLEXPRESS;'
        'Database='+dbName+';'
        'Trusted_Connection=yes;')


class LoginGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(500,500,600,500)

        vertical_layout=QVBoxLayout()
        horizontal_layout = QHBoxLayout()
        form_layout = QFormLayout()
        

        self.iconLabel=QLabel(alignment=Qt.AlignmentFlag.AlignRight)
        self.settingIcon = QPixmap("./image icon/setting.png").scaled(QSize(20, 20))
        self.iconLabel.setPixmap(self.settingIcon)
        self.iconLabel.setObjectName('iconFloatQss')
        self.iconLabel.mousePressEvent = self.settingClicked

        self.settingHeading=QLabel("Setting",
                                   alignment=Qt.AlignmentFlag.AlignHCenter
                                   )
        self.settingHeading.setObjectName("settingHeadingQss")
        self.LoginTabBtn=QPushButton("Login Tab")
        self.LoginTabBtn.setObjectName("LoginTabBtnQss")
        self.LoginTabBtn.clicked.connect(self.LoginTab)

        self.dbName = QLabel("Change Database Name:- ")
        self.dbName.setObjectName("dbNameQss")
        self.EnterdbNameName = QLineEdit(self, 
                                placeholderText="Enter Database Name"
                                )
        self.EnterdbNameName.setObjectName("enterDbNameQss")
        self.EnterdbNameName.setText(dbName)

        self.SaveDbBtn=QPushButton("Save")
        self.SaveDbBtn.setObjectName("SaveDbBtnQss")
        self.SaveDbBtn.clicked.connect(self.SaveDbName)



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

        self.manubarbtn1=QPushButton("Form")
        self.manubarbtn1.setObjectName("FormButtonQss")
        self.manubarbtn1.clicked.connect(self.clickForm)
        self.manubarbtn1.hide()

        self.manubarbtn2=QPushButton("Display")
        self.manubarbtn2.setObjectName("DisplayButtonQss")
        self.manubarbtn2.clicked.connect(self.clickDisplay)
        self.manubarbtn2.hide()


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
        
        self.form_des2=QLabel("Enter Product Name:- ")
        self.form_des2.setObjectName("form_description")
        self.form_entry2=QLineEdit(self, 
                  placeholderText="Enter Product Name"
                )
        self.form_entry2.setObjectName("form_entry")
        
        self.form_des3=QLabel("Enter Product Weight (Kg):- ")
        self.form_des3.setObjectName("form_description")
        self.form_entry3=QLineEdit(self, 
                                placeholderText="Enter Product Weight"
                            )
        self.form_entry3.setObjectName("form_entry")
        
        self.form_entry_btn=QPushButton("Add Data")
        self.form_entry_btn.setObjectName("form_entry_btn")
        
        self.form_entry_btn.clicked.connect(self.sendData)

        self.UserId=QLabel(self)
        self.UserId.hide()


                       #Display table
        self.display_table=QTableWidget(self)
        self.display_description=QLabel("Display Data", 
                                        alignment=Qt.AlignmentFlag.AlignHCenter
                                    )
        self.display_description.setObjectName("display_description")
        self.display_description.hide()

        # self.setCentralWidget(self.display_table)
        self.display_table.setColumnCount(7)
        self.display_table.setColumnWidth(0, 70)
        self.display_table.setColumnWidth(1, 100)
        self.display_table.setColumnWidth(2, 200)
        self.display_table.setColumnWidth(3, 270)
        self.display_table.setColumnWidth(4, 190)
        self.display_table.setColumnWidth(5, 150)
        self.display_table.setColumnWidth(6, 150)
        
        self.display_table.setHorizontalHeaderLabels(["Id", "User Id", "Product Id", "Product Name", "Product Weight", "Edit", "Delete"])
        header_font_1 = QFont("Arial", 14)
        self.display_table.horizontalHeaderItem(0).setFont(header_font_1)
        self.display_table.horizontalHeaderItem(0).setForeground(QColor('#005ce6'))
        self.display_table.horizontalHeaderItem(1).setFont(header_font_1)
        self.display_table.horizontalHeaderItem(1).setForeground(QColor('#005ce6'))
        self.display_table.horizontalHeaderItem(2).setFont(header_font_1)
        self.display_table.horizontalHeaderItem(2).setForeground(QColor('#005ce6'))
        self.display_table.horizontalHeaderItem(3).setFont(header_font_1)
        self.display_table.horizontalHeaderItem(3).setForeground(QColor('#005ce6'))
        self.display_table.horizontalHeaderItem(4).setFont(header_font_1)
        self.display_table.horizontalHeaderItem(4).setForeground(QColor('#005ce6'))
        self.display_table.horizontalHeaderItem(5).setFont(header_font_1)
        self.display_table.horizontalHeaderItem(5).setForeground(QColor('#005ce6'))
        self.display_table.horizontalHeaderItem(6).setFont(header_font_1)
        self.display_table.horizontalHeaderItem(6).setForeground(QColor('#005ce6'))
        self.display_table.setFixedHeight(500)
        self.display_table.hide()


        self.form_des1.hide()
        self.form_entry1.hide()
        self.form_des2.hide()
        self.form_entry2.hide()
        self.form_des3.hide()
        self.form_entry3.hide()
        self.form_entry_btn.hide()

        self.settingHeading.hide()
        self.LoginTabBtn.hide()
        self.dbName.hide()
        self.EnterdbNameName.hide()
        self.SaveDbBtn.hide()

        form_layout.addRow(self.form_des1, self.form_entry1)
        form_layout.addRow(self.form_des2, self.form_entry2)
        form_layout.addRow(self.form_des3, self.form_entry3)
        form_layout.addRow(self.form_entry_btn)

        vertical_layout.addWidget(self.settingHeading)
        vertical_layout.addWidget(self.iconLabel)
        vertical_layout.addWidget(self.LoginTabBtn)
        vertical_layout.addWidget(self.dbName)
        vertical_layout.addWidget(self.EnterdbNameName)
        vertical_layout.addWidget(self.SaveDbBtn)

        vertical_layout.addWidget(self.manubarbtn1)
        vertical_layout.addWidget(self.manubarbtn2)
        vertical_layout.addWidget(self.display_description)
        vertical_layout.addWidget(self.display_table)
        vertical_layout.addStretch()
        vertical_layout.addWidget(self.loginSuccess)
        vertical_layout.addWidget(self.setUserName)
        horizontal_layout.addWidget(self.setUserAge)
        horizontal_layout.addWidget(self.setUserEmail)
        horizontal_layout.addWidget(self.setUserPhone)

        vertical_layout.addWidget(self.line_gap)
        vertical_layout.addLayout(horizontal_layout)
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
            
            try:
                sqlservercursor.execute("SELECT * FROM GUI_APP_LOGIN WHERE userId=? AND pass=?", getUserId, getPass)
                getUserData = sqlservercursor.fetchone()
            except Exception as e:
                QMessageBox.critical(
                    self,
                    'Critical',
                    'Error:- '+str(e)
                )


            if(getUserData):

                self.heading_1.hide()
                self.heading_2.hide()
                self.UserId_txt.hide()
                self.Enter_User_Id.hide()
                self.Password_txt.hide()
                self.Enter_Pass.hide()
                self.LoginBtn.hide()
                self.iconLabel.hide()
                self.LoginTabBtn.hide()
                self.settingHeading.hide()
                self.dbName.hide()
                self.EnterdbNameName.hide()
                self.SaveDbBtn.hide()
                
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
                self.manubarbtn1.show()
                self.manubarbtn2.show()

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

        if (productId!="" and productName!="" and productWeight!=""):

            self.form_entry1.setText("")
            self.form_entry2.setText("")
            self.form_entry3.setText("")

            sqlservercursor = conn_mssql.cursor()

            try:
                sqlservercursor.execute("INSERT INTO GUI_DATA_ENTRY (UserId,Product_Id,Product_Name,Product_Weight) VALUES (?,?,?,?)",userId,productId,productName,productWeight)
                QMessageBox.information(
                        self,
                        'Information',
                        'Data added successfully!'
                    )
                conn_mssql.commit()
            except Exception as e:
                QMessageBox.critical(
                    self,
                    'Critical',
                    'Error:- '+str(e)
                )
            
            sqlservercursor.close()
    

    def clickForm(self):

        self.form_des1.show()
        self.form_entry1.show()
        self.form_des2.show()
        self.form_entry2.show()
        self.form_des3.show()
        self.form_entry3.show()
        self.form_entry_btn.show()
        self.line_gap.show()
        self.loginSuccess.show()
        self.setUserName.show()
        self.setUserAge.show()
        self.setUserEmail.show()
        self.setUserPhone.show()

        self.display_table.hide()
        self.display_description.hide()
        self.iconLabel.hide()
        self.LoginTabBtn.hide()
        self.settingHeading.hide()
        self.dbName.hide()
        self.EnterdbNameName.hide()
        self.SaveDbBtn.hide()

    
    def clickDisplay(self):

        self.display_description.show()
        self.display_table.show()

        self.form_des1.hide()
        self.form_entry1.hide()
        self.form_des2.hide()
        self.form_entry2.hide()
        self.form_des3.hide()
        self.form_entry3.hide()
        self.form_entry_btn.hide()
        self.line_gap.hide()
        self.loginSuccess.hide()
        self.setUserName.hide()
        self.setUserAge.hide()
        self.setUserEmail.hide()
        self.setUserPhone.hide()
        self.iconLabel.hide()
        self.settingHeading.hide()
        self.LoginTabBtn.hide()
        self.dbName.hide()
        self.EnterdbNameName.hide()
        self.SaveDbBtn.hide()

        try:
            sqlservercursor = conn_mssql.cursor()
            sqlservercursor.execute("SELECT * FROM GUI_DATA_ENTRY")
            myresult = sqlservercursor.fetchall()
        except Exception as e:
                QMessageBox.critical(
                    self,
                    'Critical',
                    'Error:- '+str(e)
                )
                

        getAllData=[]
        for res in myresult:
            # print(res)
            getAllData.append(res)
        
        self.display_table.setRowCount(len(getAllData))

        item_font_1 = QFont("Arial", 10)

        r=0
        for data in getAllData:
            self.display_table.setItem(r, 0, QTableWidgetItem(str(r+1)))
            self.display_table.setItem(r, 1, QTableWidgetItem(str(data[1])))
            self.display_table.setItem(r, 2, QTableWidgetItem(data[2]))
            self.display_table.setItem(r, 3, QTableWidgetItem(data[3]))
            self.display_table.setItem(r, 4, QTableWidgetItem(str(data[4])))
            self.btn1=QPushButton(self.display_table)
            self.btn1.setText("Edit")
            self.btn1.setObjectName("EditButtonQss")
            self.btn1.clicked.connect(lambda : self.sendEditId(data[0]))
            self.display_table.setCellWidget(r, 5, self.btn1)

            self.btn2=QPushButton(self.display_table)
            self.btn2.setText("Delete")
            self.btn2.setObjectName("DeleteButtonQss")
            self.btn2.clicked.connect(lambda : self.sendDeleteId(data[0]))
            self.display_table.setCellWidget(r, 6, self.btn2)

            self.display_table.item(r, 0).setFont(item_font_1)
            self.display_table.item(r, 0).setTextAlignment(Qt.AlignCenter)
            self.display_table.item(r, 1).setFont(item_font_1)
            self.display_table.item(r, 1).setTextAlignment(Qt.AlignCenter)
            self.display_table.item(r, 2).setFont(item_font_1)
            self.display_table.item(r, 2).setTextAlignment(Qt.AlignCenter)
            self.display_table.item(r, 3).setFont(item_font_1)
            self.display_table.item(r, 3).setTextAlignment(Qt.AlignCenter)
            self.display_table.item(r, 4).setFont(item_font_1)
            self.display_table.item(r, 4).setTextAlignment(Qt.AlignCenter)

            self.display_table.setRowHeight(r, 35)
            r+=1


    def sendEditId(self, x):
        print(x)
    

    def sendDeleteId(self, y):
        print(y)


    def settingClicked(self, event):
        self.heading_1.hide()
        self.heading_2.hide()
        self.UserId_txt.hide()
        self.Enter_User_Id.hide()
        self.Password_txt.hide()
        self.Enter_Pass.hide()
        self.LoginBtn.hide()
        self.iconLabel.hide()

        self.settingHeading.show()
        self.LoginTabBtn.show()
        self.dbName.show()
        self.EnterdbNameName.show()
        self.SaveDbBtn.show()
    

    def LoginTab(self):
        self.heading_1.show()
        self.heading_2.show()
        self.UserId_txt.show()
        self.Enter_User_Id.show()
        self.Password_txt.show()
        self.Enter_Pass.show()
        self.LoginBtn.show()
        self.iconLabel.show()
        self.settingHeading.hide()
        self.LoginTabBtn.hide()
        self.dbName.hide()
        self.EnterdbNameName.hide()
        self.SaveDbBtn.hide()


    def SaveDbName(self):
        f = open("dbName.txt", "w")
        f.write(self.EnterdbNameName.text())
        f.close()



if __name__=='__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(Path('login.qss').read_text())
    loginapp=LoginGUI()
    sys.exit(app.exec())
