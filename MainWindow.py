# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main windows for program FTB.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import AddResource

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
#-----------------------------------------------------------
        self.clist=["'","[","]"]
#-----------------------------------------------------------
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1208, 866)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lSearchForResource = QtWidgets.QLabel(self.centralwidget)
        self.lSearchForResource.setGeometry(QtCore.QRect(280, 190, 131, 16))
        self.lSearchForResource.setObjectName("lSearchForResource")
        self.pteSearch = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pteSearch.setGeometry(QtCore.QRect(280, 210, 681, 31))
        self.pteSearch.setObjectName("pteSearch")
        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearch.setGeometry(QtCore.QRect(970, 210, 93, 28))
        self.btnSearch.setObjectName("btnSearch")
        self.btnAddResource = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddResource.setGeometry(QtCore.QRect(870, 250, 91, 31))
        self.btnAddResource.setObjectName("btnAddResource")
        self.lCategories = QtWidgets.QLabel(self.centralwidget)
        self.lCategories.setGeometry(QtCore.QRect(20, 270, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lCategories.setFont(font)
        self.lCategories.setObjectName("lCategories")

#--------------------------------------------------------------------------------------------------------------------    
        self.btnCat1 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat1.setGeometry(QtCore.QRect(10, 310, 191, 28))
        self.btnCat1.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat1.setObjectName("btnCat1")
        self.btnCat1.clicked.connect(self.clickCat1)

        
        self.btnCat2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat2.setGeometry(QtCore.QRect(10, 340, 191, 28))
        self.btnCat2.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat2.setObjectName("btnCat2")
        self.btnCat2.clicked.connect(self.clickCat2)



        self.btnCat3 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat3.setGeometry(QtCore.QRect(10, 370, 191, 28))
        self.btnCat3.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat3.setObjectName("btnCat3")
        self.btnCat3.clicked.connect(self.clickCat3)



        self.btnCat4 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat4.setGeometry(QtCore.QRect(10, 400, 191, 28))
        self.btnCat4.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat4.setObjectName("btnCat4")
        self.btnCat4.clicked.connect(self.clickCat4)



        self.btnCat7 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat7.setGeometry(QtCore.QRect(10, 490, 191, 28))
        self.btnCat7.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat7.setObjectName("btnCat7")
        self.btnCat7.clicked.connect(self.clickCat7)



        self.btnCat5 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat5.setGeometry(QtCore.QRect(10, 430, 191, 28))
        self.btnCat5.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat5.setObjectName("btnCat5")
        self.btnCat5.clicked.connect(self.clickCat5)



        self.btnCat8 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat8.setGeometry(QtCore.QRect(10, 520, 191, 28))
        self.btnCat8.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat8.setObjectName("btnCat8")
        self.btnCat8.clicked.connect(self.clickCat8)



        self.btnCat6 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat6.setGeometry(QtCore.QRect(10, 460, 191, 28))
        self.btnCat6.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat6.setObjectName("btnCat6")
        self.btnCat6.clicked.connect(self.clickCat6)



        self.btnCat11 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat11.setGeometry(QtCore.QRect(10, 610, 191, 28))
        self.btnCat11.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat11.setObjectName("btnCat11")
        self.btnCat11.clicked.connect(self.clickCat11)



        self.btnCat13 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat13.setGeometry(QtCore.QRect(10, 670, 191, 28))
        self.btnCat13.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat13.setObjectName("btnCat13")
        self.btnCat13.clicked.connect(self.clickCat13)



        self.btnCat9 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat9.setGeometry(QtCore.QRect(10, 550, 191, 28))
        self.btnCat9.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat9.setObjectName("btnCat9")
        self.btnCat9.clicked.connect(self.clickCat9)




        self.btnCat14 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat14.setGeometry(QtCore.QRect(10, 700, 191, 28))
        self.btnCat14.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat14.setObjectName("btnCat14")
        self.btnCat14.clicked.connect(self.clickCat14)



        self.btnCat12 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat12.setGeometry(QtCore.QRect(10, 640, 191, 28))
        self.btnCat12.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat12.setObjectName("btnCat12")
        self.btnCat12.clicked.connect(self.clickCat12)



        self.btnCat16 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat16.setGeometry(QtCore.QRect(10, 760, 191, 28))
        self.btnCat16.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat16.setObjectName("btnCat16")
        self.btnCat16.clicked.connect(self.clickCat16)



        self.btnCat15 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat15.setGeometry(QtCore.QRect(10, 730, 191, 28))
        self.btnCat15.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat15.setObjectName("btnCat15")
        self.btnCat15.clicked.connect(self.clickCat15)



        self.btnCat10 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCat10.setGeometry(QtCore.QRect(10, 580, 191, 28))
        self.btnCat10.setStyleSheet("background-color: transparent;\n"
"border-image: url(:off.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;")
        self.btnCat10.setObjectName("btnCat10")
        self.btnCat10.clicked.connect(self.clickCat10)


#--------------------------------------------------------------------------------------------------
        self.lLogo = QtWidgets.QLabel(self.centralwidget)
        self.lLogo.setGeometry(QtCore.QRect(0, 0, 1280, 261))
        self.lLogo.setText("")
        self.lLogo.setPixmap(QtGui.QPixmap("Resources/Thomastown secondary college bannar.png"))
        self.lLogo.setObjectName("lLogo")
        self.lBackground = QtWidgets.QLabel(self.centralwidget)
        self.lBackground.setGeometry(QtCore.QRect(0, 240, 1201, 621))
        self.lBackground.setText("")
        self.lBackground.setPixmap(QtGui.QPixmap("Resources/plain-white-background.jpg"))
        self.lBackground.setObjectName("lBackground")
        self.lBackground.raise_()
        self.lLogo.raise_()
        self.lSearchForResource.raise_()
        self.pteSearch.raise_()
        self.btnSearch.raise_()
        self.btnAddResource.raise_()
        self.lCategories.raise_()

#---------------------------------------------------------------------------------
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(225, 285, 900, 900)) #x,y,w,h
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
#---------------------------------------------------------------------------------------------
        

        self.btnCat1.raise_()
        self.btnCat2.raise_()
        self.btnCat3.raise_()
        self.btnCat4.raise_()
        self.btnCat7.raise_()
        self.btnCat5.raise_()
        self.btnCat8.raise_()
        self.btnCat6.raise_()
        self.btnCat11.raise_()
        self.btnCat13.raise_()
        self.btnCat9.raise_()
        self.btnCat14.raise_()
        self.btnCat12.raise_()
        self.btnCat16.raise_()
        self.btnCat15.raise_()
        self.btnCat10.raise_()

        self.btnAddResource.clicked.connect(self.openSecondWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lSearchForResource.setText(_translate("MainWindow", "Search for resource..."))
        self.btnSearch.setText(_translate("MainWindow", "Search"))
        self.btnAddResource.setText(_translate("MainWindow", "Add Resource"))
        self.lCategories.setText(_translate("MainWindow", "Categories "))
        
        
#--------------------------- Category buttons--------------------------------------------
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

    def openSecondWindow(self):
        self.childWin = QtWidgets.QMainWindow()
        self.childui = AddResource.Ui_MainWindow()
        self.childui.setupUi(self.childWin)
        self.childWin.show()


#-------------------Clicking buttons-------------------

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
                if x[3]=="Educational Resources":
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

#------------------------------------------------------------------




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
