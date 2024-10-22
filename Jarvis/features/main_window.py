from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: #000000;")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(20)
        
        # Title Label
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setText("PROGRAM BY MARSHALL")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setStyleSheet("font: 24pt 'MS Shell Dlg 2'; color: #1e90ff;")
        self.verticalLayout.addWidget(self.titleLabel)
        
        # Central Image Container
        self.centralImageContainer = QtWidgets.QWidget(self.centralwidget)
        self.centralImageContainer.setFixedSize(500, 500)
        self.centralImageContainer.setObjectName("centralImageContainer")
        self.centralImageContainer.setStyleSheet("background-color: #000000;")

        self.centralImageLayout = QtWidgets.QVBoxLayout(self.centralImageContainer)
        self.centralImageLayout.setContentsMargins(0, 0, 0, 0)
        self.centralImageLayout.setSpacing(0)

        # Central Image (GIF)
        self.centralImage = QtWidgets.QLabel(self.centralImageContainer)
        self.centralImage.setFixedSize(500, 500)
        self.centralImage.setAlignment(QtCore.Qt.AlignCenter)
        self.centralImage.setObjectName("centralImage")
        self.centralImage.setScaledContents(True)  # Ensure the GIF scales to fit
        self.centralImageLayout.addWidget(self.centralImage)
        self.verticalLayout.addWidget(self.centralImageContainer, alignment=QtCore.Qt.AlignCenter)
        
        # Horizontal layout for buttons
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(20)
        
        # Start Button
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setText("START LUNA")
        self.startButton.setObjectName("startButton")
        self.startButton.setStyleSheet("""
            QPushButton {
                background-color: #1e90ff;
                font: 18pt 'MS Shell Dlg 2';
                color: white;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #4169e1;
            }
        """)
        self.horizontalLayout.addWidget(self.startButton)
        
        # Stop Button
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setText("STOP LUNA")
        self.stopButton.setObjectName("stopButton")
        self.stopButton.setStyleSheet("""
            QPushButton {
                background-color: #ff4500;
                font: 18pt 'MS Shell Dlg 2';
                color: white;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #dc143c;
            }
        """)
        self.horizontalLayout.addWidget(self.stopButton)
        
        # Add horizontal layout to vertical layout
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        # Terminal Text Browser
        self.terminalTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.terminalTextBrowser.setPlaceholderText("Terminal..")
        self.terminalTextBrowser.setObjectName("terminalTextBrowser")
        self.terminalTextBrowser.setStyleSheet("""
            QTextBrowser {
                background-color: #333333;
                color: white;
                border: 1px solid #1e90ff;
                border-radius: 10px;
                padding: 10px;
            }
        """)
        self.verticalLayout.addWidget(self.terminalTextBrowser)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
