# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\Tab_bshlm.ui'
#
# Created: Tue May 28 11:30:21 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_tab_bshlm(object):
    def setupUi(self, tab_bshlm):
        tab_bshlm.setObjectName(_fromUtf8("tab_bshlm"))
        tab_bshlm.resize(884, 575)
        self.verticalLayout_27 = QtGui.QVBoxLayout(tab_bshlm)
        self.verticalLayout_27.setContentsMargins(25, 15, 25, 30)
        self.verticalLayout_27.setObjectName(_fromUtf8("verticalLayout_27"))
        self.gb_bshlm_3 = QtGui.QGroupBox(tab_bshlm)
        self.gb_bshlm_3.setObjectName(_fromUtf8("gb_bshlm_3"))
        self.verticalLayout_25 = QtGui.QVBoxLayout(self.gb_bshlm_3)
        self.verticalLayout_25.setObjectName(_fromUtf8("verticalLayout_25"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_25.addItem(spacerItem)
        self.gridLayout_27 = QtGui.QGridLayout()
        self.gridLayout_27.setObjectName(_fromUtf8("gridLayout_27"))
        self.label_21 = QtGui.QLabel(self.gb_bshlm_3)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_27.addWidget(self.label_21, 0, 0, 1, 1)
        self.lbl_bshlm_description = QtGui.QLabel(self.gb_bshlm_3)
        self.lbl_bshlm_description.setObjectName(_fromUtf8("lbl_bshlm_description"))
        self.gridLayout_27.addWidget(self.lbl_bshlm_description, 1, 0, 1, 1)
        self.verticalLayout_25.addLayout(self.gridLayout_27)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_25.addItem(spacerItem1)
        self.gridLayout_28 = QtGui.QGridLayout()
        self.gridLayout_28.setObjectName(_fromUtf8("gridLayout_28"))
        self.label_22 = QtGui.QLabel(self.gb_bshlm_3)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_28.addWidget(self.label_22, 2, 1, 1, 1)
        self.cb_bshlm_system = QtGui.QComboBox(self.gb_bshlm_3)
        self.cb_bshlm_system.setEditable(True)
        self.cb_bshlm_system.setObjectName(_fromUtf8("cb_bshlm_system"))
        self.gridLayout_28.addWidget(self.cb_bshlm_system, 2, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_28.addItem(spacerItem2, 2, 6, 1, 1)
        self.verticalLayout_25.addLayout(self.gridLayout_28)
        self.chb_bshlm_custom_ellipsoid = QtGui.QCheckBox(self.gb_bshlm_3)
        self.chb_bshlm_custom_ellipsoid.setEnabled(True)
        self.chb_bshlm_custom_ellipsoid.setObjectName(_fromUtf8("chb_bshlm_custom_ellipsoid"))
        self.verticalLayout_25.addWidget(self.chb_bshlm_custom_ellipsoid)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_25.addItem(spacerItem3)
        self.gridLayout_29 = QtGui.QGridLayout()
        self.gridLayout_29.setObjectName(_fromUtf8("gridLayout_29"))
        self.lbl_bshlm_ellipsoid_3 = QtGui.QLabel(self.gb_bshlm_3)
        self.lbl_bshlm_ellipsoid_3.setObjectName(_fromUtf8("lbl_bshlm_ellipsoid_3"))
        self.gridLayout_29.addWidget(self.lbl_bshlm_ellipsoid_3, 1, 0, 1, 1)
        self.label_23 = QtGui.QLabel(self.gb_bshlm_3)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_29.addWidget(self.label_23, 1, 2, 1, 1)
        self.label_24 = QtGui.QLabel(self.gb_bshlm_3)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_29.addWidget(self.label_24, 1, 1, 1, 1)
        self.txt_bshlm_ellipsoid = QtGui.QLineEdit(self.gb_bshlm_3)
        self.txt_bshlm_ellipsoid.setEnabled(False)
        self.txt_bshlm_ellipsoid.setReadOnly(False)
        self.txt_bshlm_ellipsoid.setObjectName(_fromUtf8("txt_bshlm_ellipsoid"))
        self.gridLayout_29.addWidget(self.txt_bshlm_ellipsoid, 2, 0, 1, 1)
        self.txt_bshlm_flattening = QtGui.QLineEdit(self.gb_bshlm_3)
        self.txt_bshlm_flattening.setEnabled(False)
        self.txt_bshlm_flattening.setReadOnly(False)
        self.txt_bshlm_flattening.setObjectName(_fromUtf8("txt_bshlm_flattening"))
        self.gridLayout_29.addWidget(self.txt_bshlm_flattening, 2, 2, 1, 1)
        self.txt_bshlm_axis = QtGui.QLineEdit(self.gb_bshlm_3)
        self.txt_bshlm_axis.setEnabled(False)
        self.txt_bshlm_axis.setReadOnly(False)
        self.txt_bshlm_axis.setObjectName(_fromUtf8("txt_bshlm_axis"))
        self.gridLayout_29.addWidget(self.txt_bshlm_axis, 2, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_29.addItem(spacerItem4, 1, 3, 1, 1)
        self.verticalLayout_25.addLayout(self.gridLayout_29)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_25.addItem(spacerItem5)
        self.gridLayout_30 = QtGui.QGridLayout()
        self.gridLayout_30.setObjectName(_fromUtf8("gridLayout_30"))
        self.txt_bshlm_x1 = QtGui.QLineEdit(self.gb_bshlm_3)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(220, 252, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 252, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.txt_bshlm_x1.setPalette(palette)
        self.txt_bshlm_x1.setObjectName(_fromUtf8("txt_bshlm_x1"))
        self.gridLayout_30.addWidget(self.txt_bshlm_x1, 1, 2, 1, 1)
        self.txt_bshlm_y1 = QtGui.QLineEdit(self.gb_bshlm_3)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(220, 252, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 252, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.txt_bshlm_y1.setPalette(palette)
        self.txt_bshlm_y1.setObjectName(_fromUtf8("txt_bshlm_y1"))
        self.gridLayout_30.addWidget(self.txt_bshlm_y1, 1, 3, 1, 1)
        self.label_25 = QtGui.QLabel(self.gb_bshlm_3)
        self.label_25.setText(_fromUtf8(""))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_30.addWidget(self.label_25, 0, 1, 1, 1)
        self.lbl_bshlm_x = QtGui.QLabel(self.gb_bshlm_3)
        self.lbl_bshlm_x.setObjectName(_fromUtf8("lbl_bshlm_x"))
        self.gridLayout_30.addWidget(self.lbl_bshlm_x, 0, 2, 1, 1)
        self.lbl_bshlm_y = QtGui.QLabel(self.gb_bshlm_3)
        self.lbl_bshlm_y.setObjectName(_fromUtf8("lbl_bshlm_y"))
        self.gridLayout_30.addWidget(self.lbl_bshlm_y, 0, 3, 1, 1)
        self.lbl_bshlm_station1_3 = QtGui.QLabel(self.gb_bshlm_3)
        self.lbl_bshlm_station1_3.setObjectName(_fromUtf8("lbl_bshlm_station1_3"))
        self.gridLayout_30.addWidget(self.lbl_bshlm_station1_3, 1, 0, 1, 1)
        self.lbl_bshlm_station2_3 = QtGui.QLabel(self.gb_bshlm_3)
        self.lbl_bshlm_station2_3.setObjectName(_fromUtf8("lbl_bshlm_station2_3"))
        self.gridLayout_30.addWidget(self.lbl_bshlm_station2_3, 2, 0, 1, 1)
        self.txt_bshlm_x2 = QtGui.QLineEdit(self.gb_bshlm_3)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(220, 252, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 252, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.txt_bshlm_x2.setPalette(palette)
        self.txt_bshlm_x2.setObjectName(_fromUtf8("txt_bshlm_x2"))
        self.gridLayout_30.addWidget(self.txt_bshlm_x2, 2, 2, 1, 1)
        self.txt_bshlm_y2 = QtGui.QLineEdit(self.gb_bshlm_3)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(220, 252, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 252, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.txt_bshlm_y2.setPalette(palette)
        self.txt_bshlm_y2.setObjectName(_fromUtf8("txt_bshlm_y2"))
        self.gridLayout_30.addWidget(self.txt_bshlm_y2, 2, 3, 1, 1)
        self.txt_bshlm_lon1 = QtGui.QLineEdit(self.gb_bshlm_3)
        self.txt_bshlm_lon1.setEnabled(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.txt_bshlm_lon1.setPalette(palette)
        self.txt_bshlm_lon1.setReadOnly(True)
        self.txt_bshlm_lon1.setObjectName(_fromUtf8("txt_bshlm_lon1"))
        self.gridLayout_30.addWidget(self.txt_bshlm_lon1, 1, 4, 1, 1)
        self.txt_bshlm_lat1 = QtGui.QLineEdit(self.gb_bshlm_3)
        self.txt_bshlm_lat1.setEnabled(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.txt_bshlm_lat1.setPalette(palette)
        self.txt_bshlm_lat1.setReadOnly(True)
        self.txt_bshlm_lat1.setObjectName(_fromUtf8("txt_bshlm_lat1"))
        self.gridLayout_30.addWidget(self.txt_bshlm_lat1, 1, 5, 1, 1)
        self.txt_bshlm_lon2 = QtGui.QLineEdit(self.gb_bshlm_3)
        self.txt_bshlm_lon2.setEnabled(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.txt_bshlm_lon2.setPalette(palette)
        self.txt_bshlm_lon2.setReadOnly(True)
        self.txt_bshlm_lon2.setObjectName(_fromUtf8("txt_bshlm_lon2"))
        self.gridLayout_30.addWidget(self.txt_bshlm_lon2, 2, 4, 1, 1)
        self.txt_bshlm_lat2 = QtGui.QLineEdit(self.gb_bshlm_3)
        self.txt_bshlm_lat2.setEnabled(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.txt_bshlm_lat2.setPalette(palette)
        self.txt_bshlm_lat2.setReadOnly(True)
        self.txt_bshlm_lat2.setObjectName(_fromUtf8("txt_bshlm_lat2"))
        self.gridLayout_30.addWidget(self.txt_bshlm_lat2, 2, 5, 1, 1)
        self.lbl_bshlm_lon = QtGui.QLabel(self.gb_bshlm_3)
        self.lbl_bshlm_lon.setObjectName(_fromUtf8("lbl_bshlm_lon"))
        self.gridLayout_30.addWidget(self.lbl_bshlm_lon, 0, 4, 1, 1)
        self.lbl_bshlm_lat = QtGui.QLabel(self.gb_bshlm_3)
        self.lbl_bshlm_lat.setObjectName(_fromUtf8("lbl_bshlm_lat"))
        self.gridLayout_30.addWidget(self.lbl_bshlm_lat, 0, 5, 1, 1)
        self.verticalLayout_25.addLayout(self.gridLayout_30)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_25.addItem(spacerItem6)
        self.horizontalLayout_25 = QtGui.QHBoxLayout()
        self.horizontalLayout_25.setObjectName(_fromUtf8("horizontalLayout_25"))
        self.gridLayout_31 = QtGui.QGridLayout()
        self.gridLayout_31.setObjectName(_fromUtf8("gridLayout_31"))
        self.txt_bshlm_distance = QtGui.QLineEdit(self.gb_bshlm_3)
        self.txt_bshlm_distance.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_bshlm_distance.sizePolicy().hasHeightForWidth())
        self.txt_bshlm_distance.setSizePolicy(sizePolicy)
        self.txt_bshlm_distance.setObjectName(_fromUtf8("txt_bshlm_distance"))
        self.gridLayout_31.addWidget(self.txt_bshlm_distance, 0, 1, 1, 1)
        self.txt_bshlm_azimuth1 = QtGui.QLineEdit(self.gb_bshlm_3)
        self.txt_bshlm_azimuth1.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_bshlm_azimuth1.sizePolicy().hasHeightForWidth())
        self.txt_bshlm_azimuth1.setSizePolicy(sizePolicy)
        self.txt_bshlm_azimuth1.setObjectName(_fromUtf8("txt_bshlm_azimuth1"))
        self.gridLayout_31.addWidget(self.txt_bshlm_azimuth1, 1, 1, 1, 1)
        self.txt_bshlm_azimuth2 = QtGui.QLineEdit(self.gb_bshlm_3)
        self.txt_bshlm_azimuth2.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_bshlm_azimuth2.sizePolicy().hasHeightForWidth())
        self.txt_bshlm_azimuth2.setSizePolicy(sizePolicy)
        self.txt_bshlm_azimuth2.setObjectName(_fromUtf8("txt_bshlm_azimuth2"))
        self.gridLayout_31.addWidget(self.txt_bshlm_azimuth2, 2, 1, 1, 1)
        self.label_26 = QtGui.QLabel(self.gb_bshlm_3)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_31.addWidget(self.label_26, 0, 0, 1, 1)
        self.label_27 = QtGui.QLabel(self.gb_bshlm_3)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_31.addWidget(self.label_27, 1, 0, 1, 1)
        self.label_28 = QtGui.QLabel(self.gb_bshlm_3)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_31.addWidget(self.label_28, 2, 0, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_31.addItem(spacerItem7, 0, 2, 1, 1)
        self.horizontalLayout_25.addLayout(self.gridLayout_31)
        self.txt_bshlm_log = QtGui.QTextEdit(self.gb_bshlm_3)
        self.txt_bshlm_log.setReadOnly(True)
        self.txt_bshlm_log.setObjectName(_fromUtf8("txt_bshlm_log"))
        self.horizontalLayout_25.addWidget(self.txt_bshlm_log)
        self.verticalLayout_25.addLayout(self.horizontalLayout_25)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_25.addItem(spacerItem8)
        self.groupBox_12 = QtGui.QGroupBox(self.gb_bshlm_3)
        self.groupBox_12.setObjectName(_fromUtf8("groupBox_12"))
        self.verticalLayout_26 = QtGui.QVBoxLayout(self.groupBox_12)
        self.verticalLayout_26.setObjectName(_fromUtf8("verticalLayout_26"))
        self.rdobt_bshlm_mode1 = QtGui.QRadioButton(self.groupBox_12)
        self.rdobt_bshlm_mode1.setChecked(True)
        self.rdobt_bshlm_mode1.setObjectName(_fromUtf8("rdobt_bshlm_mode1"))
        self.verticalLayout_26.addWidget(self.rdobt_bshlm_mode1)
        self.rdobt_bshlm_mode2 = QtGui.QRadioButton(self.groupBox_12)
        self.rdobt_bshlm_mode2.setObjectName(_fromUtf8("rdobt_bshlm_mode2"))
        self.verticalLayout_26.addWidget(self.rdobt_bshlm_mode2)
        self.verticalLayout_25.addWidget(self.groupBox_12)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_25.addItem(spacerItem9)
        self.verticalLayout_27.addWidget(self.gb_bshlm_3)

        self.retranslateUi(tab_bshlm)
        QtCore.QObject.connect(self.rdobt_bshlm_mode1, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.txt_bshlm_x2.setEnabled)
        QtCore.QObject.connect(self.rdobt_bshlm_mode1, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.txt_bshlm_y2.setEnabled)
        QtCore.QObject.connect(self.rdobt_bshlm_mode2, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.txt_bshlm_azimuth1.setEnabled)
        QtCore.QObject.connect(self.rdobt_bshlm_mode2, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.txt_bshlm_distance.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(tab_bshlm)

    def retranslateUi(self, tab_bshlm):
        tab_bshlm.setWindowTitle(_translate("tab_bshlm", "Form", None))
        self.gb_bshlm_3.setTitle(_translate("tab_bshlm", "Bessel Helmert", None))
        self.label_21.setText(_translate("tab_bshlm", "Description:", None))
        self.lbl_bshlm_description.setText(_translate("tab_bshlm", "system info", None))
        self.label_22.setText(_translate("tab_bshlm", "Coordinate system:", None))
        self.cb_bshlm_system.setWhatsThis(_translate("tab_bshlm", "Minilabel describing the input srs (2D only).", None))
        self.chb_bshlm_custom_ellipsoid.setToolTip(_translate("tab_bshlm", "Check this to use a custom ellipsoid.", None))
        self.chb_bshlm_custom_ellipsoid.setWhatsThis(_translate("tab_bshlm", "Check this to use a custom ellipsoid and define parameters (axis, flattening) yourself.", None))
        self.chb_bshlm_custom_ellipsoid.setText(_translate("tab_bshlm", "Custom Ellipsoid", None))
        self.lbl_bshlm_ellipsoid_3.setText(_translate("tab_bshlm", "Ellipsoid:", None))
        self.label_23.setText(_translate("tab_bshlm", "Inverse flattening:", None))
        self.label_24.setText(_translate("tab_bshlm", "Semi-major axis:", None))
        self.txt_bshlm_flattening.setWhatsThis(_translate("tab_bshlm", "Inverse flattening of used ellipsoid.", None))
        self.txt_bshlm_axis.setWhatsThis(_translate("tab_bshlm", "Major axis of used ellipsoid.", None))
        self.txt_bshlm_x1.setWhatsThis(_translate("tab_bshlm", "Input coordinate for first station/point.", None))
        self.txt_bshlm_y1.setWhatsThis(_translate("tab_bshlm", "Input coordinate for first station/point.", None))
        self.lbl_bshlm_x.setText(_translate("tab_bshlm", "Easting:", None))
        self.lbl_bshlm_y.setText(_translate("tab_bshlm", "Northing:", None))
        self.lbl_bshlm_station1_3.setText(_translate("tab_bshlm", "Station 1 ", None))
        self.lbl_bshlm_station2_3.setText(_translate("tab_bshlm", "Station 2", None))
        self.txt_bshlm_x2.setWhatsThis(_translate("tab_bshlm", "Input coordinate for second station/point.", None))
        self.txt_bshlm_y2.setWhatsThis(_translate("tab_bshlm", "Input coordinate for second station/point.", None))
        self.lbl_bshlm_lon.setText(_translate("tab_bshlm", "Longitude:", None))
        self.lbl_bshlm_lat.setText(_translate("tab_bshlm", "Latitude:", None))
        self.txt_bshlm_distance.setWhatsThis(_translate("tab_bshlm", "Calculated distance between points.", None))
        self.txt_bshlm_azimuth1.setWhatsThis(_translate("tab_bshlm", "Calculated azimuth (distance to geometrical north).", None))
        self.label_26.setText(_translate("tab_bshlm", "Distance:", None))
        self.label_27.setText(_translate("tab_bshlm", "Forward Azimuth:", None))
        self.label_28.setText(_translate("tab_bshlm", "Backwards Azimuth:", None))
        self.txt_bshlm_log.setWhatsThis(_translate("tab_bshlm", "Text field for logging error messages.", None))
        self.groupBox_12.setTitle(_translate("tab_bshlm", "Calculation mode", None))
        self.rdobt_bshlm_mode1.setWhatsThis(_translate("tab_bshlm", "In this mode distance and azimuths are calculated based on locations of two input points.", None))
        self.rdobt_bshlm_mode1.setText(_translate("tab_bshlm", "Find distance and azimuth from positions of station1 and  station2.", None))
        self.rdobt_bshlm_mode2.setWhatsThis(_translate("tab_bshlm", "In this mode the position of the second point is calculated based on input distance and azimuth.", None))
        self.rdobt_bshlm_mode2.setText(_translate("tab_bshlm", "Find position of station2 based on distance and azimuth from station1. ", None))

