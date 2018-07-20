from PyQt4 import QtCore, QtGui
#-------------------------------------------------------------------------------------------------
import subprocess
#-------------------------------------------------------------------------------------------------

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainWindow(object):
#-------------------------------------------------------------------------------------------------
    count = 0
    classSet = []

    def count_class(self,state):
        if state == QtCore.Qt.Checked:
            self.count = self.count + 1
        else:
            self.count = self.count - 1
        #print(self.count)
        self.lcdNumber.display(self.count)

    def train_cmd(self):
        self.class_sub()

        string = ''
        for c in self.classSet:
            string = string+str(c)+' '
        string = string[:-1]

        class_update_cmd = "python GUI/updateClasses.py "+str( len(self.classSet) )+' '+string
        subprocess.call(class_update_cmd,shell=True)

        train_cmd_str = './darknet detector train modified/voc_gui.data modified/yolov3-voc_gui.cfg darknet53.conv.74 -gpus 0'
        #train_cmd_str = './darknet detector train modified/voc_gui.data cfg/yolov3-voc_gui.cfg backup/yolov3-voc_gui.backup -gpus 0,1'
        subprocess.call(train_cmd_str,shell=True)

    def class_sub(self):

        self.classSet = []
        if self.aeroplane.isChecked(): 
            self.classSet.append( str(self.aeroplane.objectName()) )

        if self.bicycle.isChecked(): 
            self.classSet.append( str(self.bicycle.objectName()) )

        if self.bird.isChecked(): 
            self.classSet.append( str(self.bird.objectName()) )

        if self.boat.isChecked(): 
            self.classSet.append( str(self.boat.objectName()) )

        if self.bottle.isChecked(): 
            self.classSet.append( str(self.bottle.objectName()) )

        if self.bus.isChecked(): 
            self.classSet.append( str(self.bus.objectName()) )

        if self.cat.isChecked(): 
            self.classSet.append( str(self.cat.objectName()) )

        if self.car.isChecked(): 
            self.classSet.append( str(self.car.objectName()) )

        if self.chair.isChecked(): 
            self.classSet.append( str(self.chair.objectName()) )

        if self.cow.isChecked(): 
            self.classSet.append( str(self.cow.objectName()) )

        if self.dog.isChecked(): 
            self.classSet.append( str(self.dog.objectName()) )

        if self.diningtable.isChecked(): 
            self.classSet.append( str(self.diningtable.objectName()) )

        if self.horse.isChecked(): 
            self.classSet.append( str(self.horse.objectName()) )

        if self.motorbike.isChecked(): 
            self.classSet.append( str(self.motorbike.objectName()) )

        if self.person.isChecked(): 
            self.classSet.append( str(self.person.objectName()) )

        if self.pottedplant.isChecked(): 
            self.classSet.append( str(self.pottedplant.objectName()) )

        if self.sheep.isChecked(): 
            self.classSet.append( str(self.sheep.objectName()) )

        if self.sofa.isChecked(): 
            self.classSet.append( str(self.sofa.objectName()) )

        if self.train.isChecked(): 
            self.classSet.append( str(self.train.objectName()) )

        if self.tvmonitor.isChecked(): 
            self.classSet.append( str(self.tvmonitor.objectName()) )

#-------------------------------------------------------------------------------------------------

    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(281, 531)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.TrainWigLabel = QtGui.QLabel(self.centralwidget)
        self.TrainWigLabel.setObjectName(_fromUtf8("TrainWigLabel"))
        self.gridLayout.addWidget(self.TrainWigLabel, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(288, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(20, 258, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.classGrid = QtGui.QGridLayout()
        self.classGrid.setObjectName(_fromUtf8("classGrid"))
        self.sofa = QtGui.QCheckBox(self.centralwidget)
        self.sofa.setObjectName(_fromUtf8("sofa"))
        self.classGrid.addWidget(self.sofa, 8, 1, 1, 1)
        self.tvmonitor = QtGui.QCheckBox(self.centralwidget)
        self.tvmonitor.setObjectName(_fromUtf8("tvmonitor"))
        self.classGrid.addWidget(self.tvmonitor, 9, 1, 1, 1)
        self.pottedplant = QtGui.QCheckBox(self.centralwidget)
        self.pottedplant.setObjectName(_fromUtf8("pottedplant"))
        self.classGrid.addWidget(self.pottedplant, 7, 1, 1, 1)
        self.horse = QtGui.QCheckBox(self.centralwidget)
        self.horse.setObjectName(_fromUtf8("horse"))
        self.classGrid.addWidget(self.horse, 6, 0, 1, 1)
        self.bird = QtGui.QCheckBox(self.centralwidget)
        self.bird.setObjectName(_fromUtf8("bird"))
        self.classGrid.addWidget(self.bird, 1, 0, 1, 1)
        self.aeroplane = QtGui.QCheckBox(self.centralwidget)
        self.aeroplane.setObjectName(_fromUtf8("aeroplane"))
        self.classGrid.addWidget(self.aeroplane, 0, 0, 1, 1)
        self.boat = QtGui.QCheckBox(self.centralwidget)
        self.boat.setObjectName(_fromUtf8("boat"))
        self.classGrid.addWidget(self.boat, 1, 1, 1, 1)
        self.person = QtGui.QCheckBox(self.centralwidget)
        self.person.setObjectName(_fromUtf8("person"))
        self.classGrid.addWidget(self.person, 7, 0, 1, 1)
        self.bicycle = QtGui.QCheckBox(self.centralwidget)
        self.bicycle.setObjectName(_fromUtf8("bicycle"))
        self.classGrid.addWidget(self.bicycle, 0, 1, 1, 1)
        self.dog = QtGui.QCheckBox(self.centralwidget)
        self.dog.setObjectName(_fromUtf8("dog"))
        self.classGrid.addWidget(self.dog, 5, 1, 1, 1)
        self.diningtable = QtGui.QCheckBox(self.centralwidget)
        self.diningtable.setObjectName(_fromUtf8("diningtable"))
        self.classGrid.addWidget(self.diningtable, 5, 0, 1, 1)
        self.cow = QtGui.QCheckBox(self.centralwidget)
        self.cow.setObjectName(_fromUtf8("cow"))
        self.classGrid.addWidget(self.cow, 4, 1, 1, 1)
        self.train = QtGui.QCheckBox(self.centralwidget)
        self.train.setObjectName(_fromUtf8("train"))
        self.classGrid.addWidget(self.train, 9, 0, 1, 1)
        self.cat = QtGui.QCheckBox(self.centralwidget)
        self.cat.setObjectName(_fromUtf8("cat"))
        self.classGrid.addWidget(self.cat, 3, 1, 1, 1)
        self.chair = QtGui.QCheckBox(self.centralwidget)
        self.chair.setObjectName(_fromUtf8("chair"))
        self.classGrid.addWidget(self.chair, 4, 0, 1, 1)
        self.car = QtGui.QCheckBox(self.centralwidget)
        self.car.setObjectName(_fromUtf8("car"))
        self.classGrid.addWidget(self.car, 3, 0, 1, 1)
        self.bus = QtGui.QCheckBox(self.centralwidget)
        self.bus.setObjectName(_fromUtf8("bus"))
        self.classGrid.addWidget(self.bus, 2, 1, 1, 1)
        self.bottle = QtGui.QCheckBox(self.centralwidget)
        self.bottle.setObjectName(_fromUtf8("bottle"))
        self.classGrid.addWidget(self.bottle, 2, 0, 1, 1)
        self.motorbike = QtGui.QCheckBox(self.centralwidget)
        self.motorbike.setObjectName(_fromUtf8("motorbike"))
        self.classGrid.addWidget(self.motorbike, 6, 1, 1, 1)
        self.sheep = QtGui.QCheckBox(self.centralwidget)
        self.sheep.setObjectName(_fromUtf8("sheep"))
        self.classGrid.addWidget(self.sheep, 8, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.classGrid)
        spacerItem2 = QtGui.QSpacerItem(20, 258, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(288, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.NumClassLabel = QtGui.QLabel(self.centralwidget)
        self.NumClassLabel.setObjectName(_fromUtf8("NumClassLabel"))
        self.horizontalLayout_4.addWidget(self.NumClassLabel)
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setMinimumSize(QtCore.QSize(50, 50))
        self.lcdNumber.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdNumber.setFrameShadow(QtGui.QFrame.Plain)
        self.lcdNumber.setNumDigits(2)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.horizontalLayout_4.addWidget(self.lcdNumber)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.weight_display_text = QtGui.QLabel(self.centralwidget)
        self.weight_display_text.setObjectName(_fromUtf8("weight_display_text"))
        self.horizontalLayout_3.addWidget(self.weight_display_text)
        self.lcdNumber_weight = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber_weight.setMinimumSize(QtCore.QSize(50, 50))
        self.lcdNumber_weight.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdNumber_weight.setFrameShadow(QtGui.QFrame.Plain)
        self.lcdNumber_weight.setObjectName(_fromUtf8("lcdNumber_weight"))
        self.horizontalLayout_3.addWidget(self.lcdNumber_weight)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.trainButton = QtGui.QPushButton(self.centralwidget)
        self.trainButton.setMaximumSize(QtCore.QSize(127, 24))
        self.trainButton.setObjectName(_fromUtf8("trainButton"))
        self.horizontalLayout.addWidget(self.trainButton)
        self.cancelButton = QtGui.QPushButton(self.centralwidget)
        self.cancelButton.setMaximumSize(QtCore.QSize(127, 24))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 4, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 281, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuTRAIN = QtGui.QMenu(self.menubar)
        self.menuTRAIN.setObjectName(_fromUtf8("menuTRAIN"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)
        self.actionTest = QtGui.QAction(mainWindow)
        self.actionTest.setObjectName(_fromUtf8("actionTest"))
        self.menubar.addAction(self.menuTRAIN.menuAction())
#-------------------------------------------------------------------------------------------------
        self.aeroplane.stateChanged.connect(self.count_class)
        self.bicycle.stateChanged.connect(self.count_class)
        self.bird.stateChanged.connect(self.count_class)
        self.boat.stateChanged.connect(self.count_class)
        self.bottle.stateChanged.connect(self.count_class)
        self.bus.stateChanged.connect(self.count_class)
        self.car.stateChanged.connect(self.count_class)
        self.cat.stateChanged.connect(self.count_class)
        self.chair.stateChanged.connect(self.count_class)
        self.cow.stateChanged.connect(self.count_class)
        self.diningtable.stateChanged.connect(self.count_class)
        self.dog.stateChanged.connect(self.count_class)
        self.horse.stateChanged.connect(self.count_class)
        self.motorbike.stateChanged.connect(self.count_class)
        self.person.stateChanged.connect(self.count_class)
        self.pottedplant.stateChanged.connect(self.count_class)
        self.sheep.stateChanged.connect(self.count_class)
        self.sofa.stateChanged.connect(self.count_class)
        self.train.stateChanged.connect(self.count_class)
        self.tvmonitor.stateChanged.connect(self.count_class)
        #QtCore.QObject.connect(self.trainButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.train_cmd)
        self.trainButton.clicked.connect(self.train_cmd)
        self.cancelButton.clicked.connect(QtCore.QCoreApplication.instance().quit)        
#------------------------------------------------------------------------------------------------- 

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "YOLO GUI", None))
        self.TrainWigLabel.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline; color:#161616;\">Choose classes to Train Data</span></p></body></html>", None))
        self.sofa.setText(_translate("mainWindow", "sofa", None))
        self.tvmonitor.setText(_translate("mainWindow", "tv monitor", None))
        self.pottedplant.setText(_translate("mainWindow", "potted plant", None))
        self.horse.setText(_translate("mainWindow", "horse", None))
        self.bird.setText(_translate("mainWindow", "bird", None))
        self.aeroplane.setText(_translate("mainWindow", "aeroplane", None))
        self.boat.setText(_translate("mainWindow", "boat", None))
        self.person.setText(_translate("mainWindow", "person", None))
        self.bicycle.setText(_translate("mainWindow", "bicycle", None))
        self.dog.setText(_translate("mainWindow", "dog", None))
        self.diningtable.setText(_translate("mainWindow", "dining table", None))
        self.cow.setText(_translate("mainWindow", "cow", None))
        self.train.setText(_translate("mainWindow", "train", None))
        self.cat.setText(_translate("mainWindow", "cat", None))
        self.chair.setText(_translate("mainWindow", "chair", None))
        self.car.setText(_translate("mainWindow", "car", None))
        self.bus.setText(_translate("mainWindow", "bus", None))
        self.bottle.setText(_translate("mainWindow", "bottle", None))
        self.motorbike.setText(_translate("mainWindow", "motorbike", None))
        self.sheep.setText(_translate("mainWindow", "sheep", None))
        self.NumClassLabel.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#005500;\">Number of classes selected</span></p></body></html>", None))
        self.weight_display_text.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#00007f;\">Weight of model (MB)</span></p></body></html>", None))
        self.trainButton.setText(_translate("mainWindow", "Train", None))
        self.cancelButton.setText(_translate("mainWindow", "Cancel", None))
        self.menuTRAIN.setTitle(_translate("mainWindow", "Train", None))
        self.actionTest.setText(_translate("mainWindow", "Test", None))

