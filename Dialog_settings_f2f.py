# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\Dialog_settings_f2f.ui'
#
# Created: Sat Dec 22 11:35:12 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(663, 280)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Dialog.setPalette(palette)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.chb_semicolon = QtGui.QCheckBox(self.groupBox)
        self.chb_semicolon.setObjectName(_fromUtf8("chb_semicolon"))
        self.gridLayout.addWidget(self.chb_semicolon, 1, 1, 1, 1)
        self.chb_tab = QtGui.QCheckBox(self.groupBox)
        self.chb_tab.setChecked(True)
        self.chb_tab.setObjectName(_fromUtf8("chb_tab"))
        self.gridLayout.addWidget(self.chb_tab, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.chb_pattern = QtGui.QCheckBox(self.groupBox)
        self.chb_pattern.setObjectName(_fromUtf8("chb_pattern"))
        self.horizontalLayout_2.addWidget(self.chb_pattern)
        self.txt_pattern = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_pattern.sizePolicy().hasHeightForWidth())
        self.txt_pattern.setSizePolicy(sizePolicy)
        self.txt_pattern.setObjectName(_fromUtf8("txt_pattern"))
        self.horizontalLayout_2.addWidget(self.txt_pattern)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        self.chb_whitespace = QtGui.QCheckBox(self.groupBox)
        self.chb_whitespace.setChecked(True)
        self.chb_whitespace.setObjectName(_fromUtf8("chb_whitespace"))
        self.gridLayout.addWidget(self.chb_whitespace, 1, 0, 1, 1)
        self.chb_space = QtGui.QCheckBox(self.groupBox)
        self.chb_space.setChecked(True)
        self.chb_space.setObjectName(_fromUtf8("chb_space"))
        self.gridLayout.addWidget(self.chb_space, 0, 1, 1, 1)
        self.chb_comma = QtGui.QCheckBox(self.groupBox)
        self.chb_comma.setObjectName(_fromUtf8("chb_comma"))
        self.gridLayout.addWidget(self.chb_comma, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_3.addWidget(self.label_6)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_5)
        self.spb_col_y = QtGui.QSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spb_col_y.sizePolicy().hasHeightForWidth())
        self.spb_col_y.setSizePolicy(sizePolicy)
        self.spb_col_y.setMinimum(1)
        self.spb_col_y.setProperty("value", 2)
        self.spb_col_y.setObjectName(_fromUtf8("spb_col_y"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.spb_col_y)
        self.gridLayout_3.addLayout(self.formLayout_3, 0, 1, 1, 1)
        self.chb_has_z = QtGui.QCheckBox(self.groupBox)
        self.chb_has_z.setObjectName(_fromUtf8("chb_has_z"))
        self.gridLayout_3.addWidget(self.chb_has_z, 0, 3, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.spb_col_x = QtGui.QSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spb_col_x.sizePolicy().hasHeightForWidth())
        self.spb_col_x.setSizePolicy(sizePolicy)
        self.spb_col_x.setMinimum(1)
        self.spb_col_x.setProperty("value", 1)
        self.spb_col_x.setObjectName(_fromUtf8("spb_col_x"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.spb_col_x)
        self.gridLayout_3.addLayout(self.formLayout, 0, 0, 1, 1)
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.spb_col_z = QtGui.QSpinBox(self.groupBox)
        self.spb_col_z.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spb_col_z.sizePolicy().hasHeightForWidth())
        self.spb_col_z.setSizePolicy(sizePolicy)
        self.spb_col_z.setMinimum(1)
        self.spb_col_z.setProperty("value", 3)
        self.spb_col_z.setObjectName(_fromUtf8("spb_col_z"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.spb_col_z)
        self.gridLayout_3.addLayout(self.formLayout_4, 0, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QObject.connect(self.chb_whitespace, QtCore.SIGNAL(_fromUtf8("pressed()")), self.chb_space.click)
        QtCore.QObject.connect(self.chb_has_z, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.spb_col_z.setEnabled)
        QtCore.QObject.connect(self.chb_whitespace, QtCore.SIGNAL(_fromUtf8("pressed()")), self.chb_tab.click)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "File2File settings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "TextDriver", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Format for text driver:  field1 <sep_char> field2 <sep_char> field3 <sep_char> .....", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Column separators:", None, QtGui.QApplication.UnicodeUTF8))
        self.chb_semicolon.setText(QtGui.QApplication.translate("Dialog", "; Semicolon ", None, QtGui.QApplication.UnicodeUTF8))
        self.chb_tab.setText(QtGui.QApplication.translate("Dialog", "Tab", None, QtGui.QApplication.UnicodeUTF8))
        self.chb_pattern.setText(QtGui.QApplication.translate("Dialog", "Specify sep chars", None, QtGui.QApplication.UnicodeUTF8))
        self.chb_whitespace.setWhatsThis(QtGui.QApplication.translate("Dialog", "<html><head/><body><p>Default: Use all whitespace as field separator.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.chb_whitespace.setText(QtGui.QApplication.translate("Dialog", "All whitespace", None, QtGui.QApplication.UnicodeUTF8))
        self.chb_space.setText(QtGui.QApplication.translate("Dialog", "Space", None, QtGui.QApplication.UnicodeUTF8))
        self.chb_comma.setText(QtGui.QApplication.translate("Dialog", ", Comma", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Geometry columns:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Y column", None, QtGui.QApplication.UnicodeUTF8))
        self.chb_has_z.setText(QtGui.QApplication.translate("Dialog", "Has z", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "X column", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Z column", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

