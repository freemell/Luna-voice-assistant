from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Main GIF Label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1440, 900))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Jarvis/utils/images/home.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        # Push Button 1 (Run)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1180, 790, 101, 51))
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                      "font: 75 18pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")

        # Push Button 2 (Exit)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1310, 790, 101, 51))
        self.pushButton_2.setStyleSheet("background-color:rgb(255, 0, 0);\n"
                                        "font: 75 18pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")

        # Initiating GIF Label
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 401, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Jarvis/utils/images/initiating.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        
        self.textInput = QtWidgets.QLineEdit(self.centralwidget)
        self.textInput.setGeometry(QtCore.QRect(1000, 470, 300, 30))
        self.textInput.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
                                     "background-color:white;\ncolor:black;")
        self.textInput.setPlaceholderText("Type your command here...")
        self.textInput.setObjectName("textInput")

        # Text Browser for Date
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(640, 30, 291, 61))
        self.textBrowser.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
                                       "background-color:transparent;\ncolor:white;"
                                       "border-radius:none;\n")
        self.textBrowser.setObjectName("textBrowser")

        # Text Browser for Time
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(930, 30, 291, 61))
        self.textBrowser_2.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
                                         "background-color:transparent;\ncolor:white;"
                                         "border-radius:none;")
        self.textBrowser_2.setObjectName("textBrowser_2")

        # Command Terminal Text Browser
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(1000, 500, 431, 281))
        self.textBrowser_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
                                         "background-color:transparent;\ncolor:white;")
        self.textBrowser_3.setObjectName("textBrowser_3")

        # Static Images
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 200, 400, 400))
        self.label_3.setPixmap(QtGui.QPixmap("Jarvis/utils/images/static1.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(500, 200, 400, 400))
        self.label_4.setPixmap(QtGui.QPixmap("Jarvis/utils/images/static2.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")

        # New: Text Input Field
        self.textInput = QtWidgets.QLineEdit(self.centralwidget)
        self.textInput.setGeometry(QtCore.QRect(1000, 470, 300, 30))
        self.textInput.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
                                     "background-color:white;\ncolor:black;")
        self.textInput.setPlaceholderText("Type your command here...")
        self.textInput.setObjectName("textInput")

        # New: Command Suggestions
        self.commandSuggestions = QtWidgets.QListWidget(self.centralwidget)
        self.commandSuggestions.setGeometry(QtCore.QRect(1000, 430, 300, 100))
        self.commandSuggestions.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
                                              "background-color:white;\ncolor:black;")
        self.commandSuggestions.setObjectName("commandSuggestions")

        # Populate the command suggestions (Example)
        self.commandSuggestions.addItems([
            "What's the time?",
            "What's the date?",
            "Tell me a joke",
            "Play music",
            "Open Google",
            "Weather in London",
            "Send an email"
        ])

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 26))
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
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))
