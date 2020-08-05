# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Adding a resource window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import csv 

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.clist=["'","[","]"]
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1196, 869)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.btnCat9 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat9.setGeometry(QtCore.QRect(10, 540, 191, 28))
        self.btnCat9.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat9.setObjectName("btnCat9")
        self.btnCat9.clicked.connect(self.clickCat9)
        self.btnCat9.clicked.connect(self.hideAll)



        self.btnCat15 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat15.setGeometry(QtCore.QRect(10, 720, 191, 28))
        self.btnCat15.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat15.setObjectName("btnCat15")
        self.btnCat15.clicked.connect(self.clickCat15)
        self.btnCat15.clicked.connect(self.hideAll)



        self.btnCat16 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat16.setGeometry(QtCore.QRect(10, 750, 191, 28))
        self.btnCat16.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat16.setObjectName("btnCat16")
        self.btnCat16.clicked.connect(self.clickCat16)
        self.btnCat16.clicked.connect(self.hideAll)



        self.btnCat1 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat1.setGeometry(QtCore.QRect(10, 300, 191, 28))
        self.btnCat1.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat1.setObjectName("btnCat1")
        self.btnCat1.clicked.connect(self.clickCat1)
        self.btnCat1.clicked.connect(self.hideAll)



        self.btnCat13 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat13.setGeometry(QtCore.QRect(10, 660, 191, 28))
        self.btnCat13.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat13.setObjectName("btnCat13")
        self.btnCat13.clicked.connect(self.clickCat13)
        self.btnCat13.clicked.connect(self.hideAll)




        self.btnCat4 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat4.setGeometry(QtCore.QRect(10, 390, 191, 28))
        self.btnCat4.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat4.setObjectName("btnCat4")
        self.btnCat4.clicked.connect(self.clickCat4)
        self.btnCat4.clicked.connect(self.hideAll)



        self.lBackground = QtWidgets.QLabel(self.centralwidget)
        self.lBackground.setGeometry(QtCore.QRect(0, 230, 1201, 621))
        self.lBackground.setText("")
        self.lBackground.setPixmap(QtGui.QPixmap("Resources/plain-white-background.jpg"))
        self.lBackground.setObjectName("lBackground")




        self.btnCat3 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat3.setGeometry(QtCore.QRect(10, 360, 191, 28))
        self.btnCat3.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat3.setObjectName("btnCat3")
        self.btnCat3.clicked.connect(self.hideAll)



        self.btnCat8 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat8.setGeometry(QtCore.QRect(10, 510, 191, 28))
        self.btnCat8.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat8.setObjectName("btnCat8")
        self.btnCat8.clicked.connect(self.hideAll)



        self.lCategories = QtWidgets.QLabel(self.centralwidget)
        self.lCategories.setGeometry(QtCore.QRect(20, 260, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lCategories.setFont(font)
        self.lCategories.setObjectName("lCategories")
        self.btnCat14 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat14.setGeometry(QtCore.QRect(10, 690, 191, 28))
        self.btnCat14.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat14.setObjectName("btnCat14")
        self.btnCat14.clicked.connect(self.hideAll)



        self.btnCat11 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat11.setGeometry(QtCore.QRect(10, 600, 191, 28))
        self.btnCat11.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat11.setObjectName("btnCat11")
        self.btnCat11.clicked.connect(self.hideAll)



        self.btnCat6 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat6.setGeometry(QtCore.QRect(10, 450, 191, 28))
        self.btnCat6.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat6.setObjectName("btnCat6")
        self.btnCat6.clicked.connect(self.hideAll)



        self.btnCat12 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat12.setGeometry(QtCore.QRect(10, 630, 191, 28))
        self.btnCat12.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat12.setObjectName("btnCat12")
        self.btnCat12.clicked.connect(self.clickCat12)
        self.btnCat12.clicked.connect(self.hideAll)


        self.btnCat7 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat7.setGeometry(QtCore.QRect(10, 480, 191, 28))
        self.btnCat7.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat7.setObjectName("btnCat7")
        self.btnCat7.clicked.connect(self.clickCat7)
        self.btnCat7.clicked.connect(self.hideAll)


        self.lLogo = QtWidgets.QLabel(self.centralwidget)
        self.lLogo.setGeometry(QtCore.QRect(0, -10, 1280, 261))
        self.lLogo.setText("")
        self.lLogo.setPixmap(QtGui.QPixmap("Resources/Thomastown secondary college bannar.png"))
        self.lLogo.setObjectName("lLogo")



        self.btnCat10 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat10.setGeometry(QtCore.QRect(10, 570, 191, 28))
        self.btnCat10.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat10.setObjectName("btnCat10")
        self.btnCat10.clicked.connect(self.clickCat10)
        self.btnCat10.clicked.connect(self.hideAll)


        self.btnCat2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat2.setGeometry(QtCore.QRect(10, 330, 191, 28))
        self.btnCat2.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat2.setObjectName("btnCat2")
        self.btnCat2.clicked.connect(self.clickCat2)
        self.btnCat2.clicked.connect(self.hideAll)


        self.btnCat5 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat5.setGeometry(QtCore.QRect(10, 420, 191, 28))
        self.btnCat5.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat5.setObjectName("btnCat5")
        self.btnCat5.clicked.connect(self.clickCat5)
        self.btnCat5.clicked.connect(self.hideAll)


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 380, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 460, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(290, 520, 160, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(380, 370, 251, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(380, 450, 251, 31))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(700, 370, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(700, 410, 251, 141))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 260, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.plainTextEdit_4 = QtWidgets.QLabel(self.centralwidget)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(280, 580, 671, 61))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(860, 670, 93, 28))
        self.pushButton.setObjectName("pushButton")
#------------------------------saving---------------------------------
        self.pushButton.clicked.connect(self.saving)

#-----------------------------------------------------------------------------------------------------
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(225, 285, 900, 900)) #x,y,w,h
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
#----------------------------------------------------------------------------------------------------



        self.lBackground.raise_()
        self.btnCat9.raise_()
        self.btnCat15.raise_()
        self.btnCat16.raise_()
        self.btnCat1.raise_()
        self.btnCat13.raise_()
        self.btnCat4.raise_()
        self.btnCat3.raise_()
        self.btnCat8.raise_()
        self.lCategories.raise_()
        self.btnCat14.raise_()
        self.btnCat11.raise_()
        self.btnCat6.raise_()
        self.btnCat12.raise_()
        self.btnCat7.raise_()
        self.lLogo.raise_()
        self.btnCat10.raise_()
        self.btnCat2.raise_()
        self.btnCat5.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.comboBox.raise_()
        self.plainTextEdit.raise_()
        self.plainTextEdit_2.raise_()
        self.label_3.raise_()
        self.plainTextEdit_3.raise_()
        self.label_4.raise_()
        self.plainTextEdit_4.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1196, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

#---------------------------------category buttons (left hand side)-------------------
        self.btnCat1.setText(_translate("MainWindow", "Audiobooks"))
        self.btnCat2.setText(_translate("MainWindow", "Novels"))
        self.btnCat3.setText(_translate("MainWindow", "Mathematics"))
        self.btnCat4.setText(_translate("MainWindow", "English"))
        self.btnCat7.setText(_translate("MainWindow", "Creative Subjects"))
        self.btnCat5.setText(_translate("MainWindow", "Economics"))
        self.btnCat8.setText(_translate("MainWindow", "Accounting"))
        self.btnCat6.setText(_translate("MainWindow", "Legal Studies"))
        self.btnCat11.setText(_translate("MainWindow", "History"))
        self.btnCat13.setText(_translate("MainWindow", "Geography"))
        self.btnCat9.setText(_translate("MainWindow", "Science Subjects"))
        self.btnCat14.setText(_translate("MainWindow", "LOTE"))
        self.btnCat12.setText(_translate("MainWindow", "EBOOKS"))
        self.btnCat16.setText(_translate("MainWindow", "Educational Resources"))
        self.btnCat15.setText(_translate("MainWindow", "Other resources"))
        self.btnCat10.setText(_translate("MainWindow", "Movies"))

#-------------------------------Items in combo box-----------------------------
        self.label.setText(_translate("MainWindow", "Title:"))
        self.label_2.setText(_translate("MainWindow", "Author:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Audiobooks"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Novels"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Mathematics"))
        self.comboBox.setItemText(3, _translate("MainWindow", "English"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Creative subjects"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Economics"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Accounting"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Legal Studies"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Hisotry"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Geography"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Science Subjects"))
        self.comboBox.setItemText(11, _translate("MainWindow", "LOTE"))
        self.comboBox.setItemText(12, _translate("MainWindow", "EBOOKS"))
        self.comboBox.setItemText(13, _translate("MainWindow", "Educational resources"))
        self.comboBox.setItemText(14, _translate("MainWindow", "Other resources"))
        self.comboBox.setItemText(15, _translate("MainWindow", "Movies"))

        self.label_3.setText(_translate("MainWindow", "Description:"))
        self.label_4.setText(_translate("MainWindow", "Adding New Resource:"))
        self.plainTextEdit_4.setText(_translate("MainWindow", "Instructions:\n Add the the required information that is needed on the right-hand side of the heading.\nOnce the user clicks the \'add resource\' button, the information will be stored within the program."))
        self.pushButton.setText(_translate("MainWindow", "Add Resource"))


    def saving(self):
            Title = ""
            Author = ""
            Description = ""
            Category = ""

            Title = self.plainTextEdit.toPlainText()
            Author = self.plainTextEdit_2.toPlainText()
            Description = self.plainTextEdit_3.toPlainText()
            Category = self.comboBox.currentText()

            print(type(Title), type(Author), type(Description), type(Category))
            file = open ("C:\\Users\\mcurci20\\OneDrive - Ivanhoe Grammar School\\Documents\\GitHub\\SearchingResourceApp\\Resource list.csv","a")
            file.writelines(Title + ',' + Author + ',' + Description + ',' + Category + '\n' )
            file.close ()

#-------------------Clicking buttons-------------------
    def hideAll(self):
        self.plainTextEdit.setHidden(True)
        self.plainTextEdit_2.setHidden(True)
        self.plainTextEdit_3.setHidden(True)
        self.plainTextEdit_4.setHidden(True)
        self.label_2.setHidden(True)
        self.label_3.setHidden(True)
        self.label_4.setHidden(True)
        self.comboBox.setHidden(True)
        self.pushButton.setHidden(True)
#------------------------------------------------------------
    def clickCat1(self): #Audiobooks
        templist=[]
        tempstr=""
        tempstr2=""
        csvFile=open("Resource list.csv")
        for x in csvFile:
                x=x.rstrip("\n")
                x=x.split(",")
                if x[3]=="Audiobooks":
                        templist2=[x[0],x[1],x[2]]
                        templist.append(templist2)
        for y in templist:
                print(y)
                y=str(y)
                for z in y:
                        print(z)
                        if z in self.clist:
                                z=""
                        tempstr2+=z
                tempstr=tempstr+tempstr2+"\n"
                tempstr2=""
        self.label.setText(tempstr)

        

    def clickCat2(self):
        templist=[]
        tempstr=""
        tempstr2=""
        csvFile=open("Resource list.csv")
        for x in csvFile:
                x=x.rstrip("\n")
                x=x.split(",")
                if x[3]=="Novels":
                        templist2=[x[0],x[1],x[2]]
                        templist.append(templist2)
        for y in templist:
                print(y)
                y=str(y)
                for z in y:
                        print(z)
                        if z in self.clist:
                                z=""
                        tempstr2+=z
                tempstr=tempstr+tempstr2+"\n"
                tempstr2=""
        self.label.setText(tempstr)

    def clickCat3(self):
        templist=[]
        tempstr=""
        tempstr2=""
        csvFile=open("Resource list.csv")
        for x in csvFile:
                x=x.rstrip("\n")
                x=x.split(",")
                if x[3]=="Mathematics":
                        templist2=[x[0],x[1],x[2]]
                        templist.append(templist2)
        for y in templist:
                print(y)
                y=str(y)
                for z in y:
                        print(z)
                        if z in self.clist:
                                z=""
                        tempstr2+=z
                tempstr=tempstr+tempstr2+"\n"
                tempstr2=""
        self.label.setText(tempstr)

    def clickCat4(self):
        templist=[]
        tempstr=""
        tempstr2=""
        csvFile=open("Resource list.csv")
        for x in csvFile:
                x=x.rstrip("\n")
                x=x.split(",")
                if x[3]=="English":
                        templist2=[x[0],x[1],x[2]]
                        templist.append(templist2)
        for y in templist:
                print(y)
                y=str(y)
                for z in y:
                        print(z)
                        if z in self.clist:
                                z=""
                        tempstr2+=z
                tempstr=tempstr+tempstr2+"\n"
                tempstr2=""
        self.label.setText(tempstr)

    def clickCat5(self):
        templist=[]
        tempstr=""
        tempstr2=""
        csvFile=open("Resource list.csv")
        for x in csvFile:
                x=x.rstrip("\n")
                x=x.split(",")
                if x[3]=="Economics":
                        templist2=[x[0],x[1],x[2]]
                        templist.append(templist2)
        for y in templist:
                print(y)
                y=str(y)
                for z in y:
                        print(z)
                        if z in self.clist:
                                z=""
                        tempstr2+=z
                tempstr=tempstr+tempstr2+"\n"
                tempstr2=""
        self.label.setText(tempstr)

    def clickCat6(self):
        templist=[]
        tempstr=""
        tempstr2=""
        csvFile=open("Resource list.csv")
        for x in csvFile:
                x=x.rstrip("\n")
                x=x.split(",")
                if x[3]=="Legal Studies":
                        templist2=[x[0],x[1],x[2]]
                        templist.append(templist2)
        for y in templist:
                print(y)
                y=str(y)
                for z in y:
                        print(z)
                        if z in self.clist:
                                z=""
                        tempstr2+=z
                tempstr=tempstr+tempstr2+"\n"
                tempstr2=""
        self.label.setText(tempstr)

    def clickCat7(self):
        templist=[]
        tempstr=""
        tempstr2=""
        csvFile=open("Resource list.csv")
        for x in csvFile:
                x=x.rstrip("\n")
                x=x.split(",")
                if x[3]=="Creative Subjects":
                        templist2=[x[0],x[1],x[2]]
                        templist.append(templist2)
        for y in templist:
                print(y)
                y=str(y)
                for z in y:
                        print(z)
                        if z in self.clist:
                                z=""
                        tempstr2+=z
                tempstr=tempstr+tempstr2+"\n"
                tempstr2=""
        self.label.setText(tempstr)

    def clickCat8(self):
        templist=[]
        tempstr=""
        tempstr2=""
        csvFile=open("Resource list.csv")
        for x in csvFile:
                x=x.rstrip("\n")
                x=x.split(",")
                if x[3]=="Accounting":
                        templist2=[x[0],x[1],x[2]]
                        templist.append(templist2)
        for y in templist:
                print(y)
                y=str(y)
                for z in y:
                        print(z)
                        if z in self.clist:
                                z=""
                        tempstr2+=z
                tempstr=tempstr+tempstr2+"\n"
                tempstr2=""
        self.label.setText(tempstr) 

    def clickCat9(self):
        templist=[]
        tempstr=""
        tempstr2=""
        csvFile=open("Resource list.csv")
        for x in csvFile:
                x=x.rstrip("\n")
                x=x.split(",")
                if x[3]=="Science Subjects":
                        templist2=[x[0],x[1],x[2]]
                        templist.append(templist2)
        for y in templist:
                print(y)
                y=str(y)
                for z in y:
                        print(z)
                        if z in self.clist:
                                z=""
                        tempstr2+=z
                tempstr=tempstr+tempstr2+"\n"
                tempstr2=""
        self.label.setText(tempstr)      

    def clickCat10(self):
        templist=[]
        tempstr=""
        tempstr2=""
        csvFile=open("Resource list.csv")
        for x in csvFile:
                x=x.rstrip("\n")
                x=x.split(",")
                if x[3]=="Movies":
                        templist2=[x[0],x[1],x[2]]
                        templist.append(templist2)
        for y in templist:
                print(y)
                y=str(y)
                for z in y:
                        print(z)
                        if z in self.clist:
                                z=""
                        tempstr2+=z
                tempstr=tempstr+tempstr2+"\n"
                tempstr2=""
        self.label.setText(tempstr)      

    def clickCat11(self):
        templist=[]
        tempstr=""
        tempstr2=""
        csvFile=open("Resource list.csv")
        for x in csvFile:
                x=x.rstrip("\n")
                x=x.split(",")
                if x[3]=="History":
                        templist2=[x[0],x[1],x[2]]
                        templist.append(templist2)
        for y in templist:
                print(y)
                y=str(y)
                for z in y:
                        print(z)
                        if z in self.clist:
                                z=""
                        tempstr2+=z
                tempstr=tempstr+tempstr2+"\n"
                tempstr2=""
        self.label.setText(tempstr)

    def clickCat12(self):
        templist=[]
        tempstr=""
        tempstr2=""
        csvFile=open("Resource list.csv")
        for x in csvFile:
                x=x.rstrip("\n")
                x=x.split(",")
                if x[3]=="EBOOKS":
                        templist2=[x[0],x[1],x[2]]
                        templist.append(templist2)
        for y in templist:
                print(y)
                y=str(y)
                for z in y:
                        print(z)
                        if z in self.clist:
                                z=""
                        tempstr2+=z
                tempstr=tempstr+tempstr2+"\n"
                tempstr2=""
        self.label.setText(tempstr)

    def clickCat13(self):
        templist=[]
        tempstr=""
        tempstr2=""
        csvFile=open("Resource list.csv")
        for x in csvFile:
                x=x.rstrip("\n")
                x=x.split(",")
                if x[3]=="Geography":
                        templist2=[x[0],x[1],x[2]]
                        templist.append(templist2)
        for y in templist:
                print(y)
                y=str(y)
                for z in y:
                        print(z)
                        if z in self.clist:
                                z=""
                        tempstr2+=z
                tempstr=tempstr+tempstr2+"\n"
                tempstr2=""
        self.label.setText(tempstr)

    def clickCat14(self):
        templist=[]
        tempstr=""
        tempstr2=""
        csvFile=open("Resource list.csv")
        for x in csvFile:
                x=x.rstrip("\n")
                x=x.split(",")
                if x[3]=="LOTE":
                        templist2=[x[0],x[1],x[2]]
                        templist.append(templist2)
        for y in templist:
                print(y)
                y=str(y)
                for z in y:
                        print(z)
                        if z in self.clist:
                                z=""
                        tempstr2+=z
                tempstr=tempstr+tempstr2+"\n"
                tempstr2=""
        self.label.setText(tempstr)

    def clickCat15(self):
        templist=[]
        tempstr=""
        tempstr2=""
        csvFile=open("Resource list.csv")
        for x in csvFile:
                x=x.rstrip("\n")
                x=x.split(",")
                if x[3]=="Other resources":
                        templist2=[x[0],x[1],x[2]]
                        templist.append(templist2)
        for y in templist:
                print(y)
                y=str(y)
                for z in y:
                        print(z)
                        if z in self.clist:
                                z=""
                        tempstr2+=z
                tempstr=tempstr+tempstr2+"\n"
                tempstr2=""
        self.label.setText(tempstr)

    def clickCat16(self):
        templist=[]
        tempstr=""
        tempstr2=""
        csvFile=open("Resource list.csv")
        for x in csvFile:
                x=x.rstrip("\n")
                x=x.split(",")
                if x[3]=="Educational resources":
                        templist2=[x[0],x[1],x[2]]
                        templist.append(templist2)
        for y in templist:
                print(y)
                y=str(y)
                for z in y:
                        print(z)
                        if z in self.clist:
                                z=""
                        tempstr2+=z
                tempstr=tempstr+tempstr2+"\n"
                tempstr2=""
        self.label.setText(tempstr)            
            
 #------------------------------------------------------------------------------
                                 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
