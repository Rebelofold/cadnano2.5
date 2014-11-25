# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow/mainwindow.ui'
#
# Created: Thu Nov 13 14:59:56 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from cadnano.gui.views.pathview.pathtoolbar import PathToolBar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1075, 792)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setStatusTip("")
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.main_splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_splitter.sizePolicy().hasHeightForWidth())
        self.main_splitter.setSizePolicy(sizePolicy)
        self.main_splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_splitter.setFrameShadow(QtWidgets.QFrame.Plain)
        self.main_splitter.setLineWidth(0)
        self.main_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.main_splitter.setOpaqueResize(True)
        self.main_splitter.setHandleWidth(7)
        self.main_splitter.setObjectName("main_splitter")

        self.slice_graphics_view = CustomQGraphicsView(self.main_splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slice_graphics_view.sizePolicy().hasHeightForWidth())
        self.slice_graphics_view.setSizePolicy(sizePolicy)
        self.slice_graphics_view.setMinimumSize(QtCore.QSize(0, 0))
        self.slice_graphics_view.setBaseSize(QtCore.QSize(480, 0))
        self.slice_graphics_view.setMouseTracking(True)
        self.slice_graphics_view.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.slice_graphics_view.setFrameShadow(QtWidgets.QFrame.Plain)
        self.slice_graphics_view.setLineWidth(0)
        self.slice_graphics_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.slice_graphics_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.slice_graphics_view.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.HighQualityAntialiasing|QtGui.QPainter.TextAntialiasing)
        self.slice_graphics_view.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.slice_graphics_view.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.slice_graphics_view.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.slice_graphics_view.setObjectName("slice_graphics_view")

        self.path_splitter = QtWidgets.QSplitter(self.main_splitter)

        self.path_graphics_view = CustomQGraphicsView(self.path_splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path_graphics_view.sizePolicy().hasHeightForWidth())
        self.path_graphics_view.setSizePolicy(sizePolicy)
        self.path_graphics_view.setMinimumSize(QtCore.QSize(0, 0))
        self.path_graphics_view.setMouseTracking(True)
        self.path_graphics_view.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.path_graphics_view.setFrameShadow(QtWidgets.QFrame.Plain)
        self.path_graphics_view.setLineWidth(0)
        self.path_graphics_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.path_graphics_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.path_graphics_view.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.HighQualityAntialiasing|QtGui.QPainter.TextAntialiasing)
        self.path_graphics_view.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.path_graphics_view.setObjectName("path_graphics_view")
        self.gridLayout.addWidget(self.main_splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.topToolBar = QtWidgets.QToolBar(MainWindow)
        self.part_toolbutton = QtWidgets.QToolButton(MainWindow)
        self.part_toolbutton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.part_toolbutton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topToolBar.sizePolicy().hasHeightForWidth())
        self.topToolBar.setSizePolicy(sizePolicy)
        self.topToolBar.setBaseSize(QtCore.QSize(550, 0))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.topToolBar.setFont(font)
        self.topToolBar.setIconSize(QtCore.QSize(24, 24))
        self.topToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.topToolBar.setObjectName("topToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.topToolBar)
        self.rightToolBar = QtWidgets.QToolBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightToolBar.sizePolicy().hasHeightForWidth())
        self.rightToolBar.setSizePolicy(sizePolicy)
        self.rightToolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.rightToolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rightToolBar.setAllowedAreas(QtCore.Qt.LeftToolBarArea|QtCore.Qt.RightToolBarArea|QtCore.Qt.TopToolBarArea)
        self.rightToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.rightToolBar.setObjectName("rightToolBar")
        MainWindow.addToolBar(QtCore.Qt.RightToolBarArea, self.rightToolBar)
        self.leftToolBar = QtWidgets.QToolBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftToolBar.sizePolicy().hasHeightForWidth())
        self.leftToolBar.setSizePolicy(sizePolicy)
        self.leftToolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.leftToolBar.setAllowedAreas(QtCore.Qt.LeftToolBarArea|QtCore.Qt.RightToolBarArea|QtCore.Qt.TopToolBarArea)
        self.leftToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.leftToolBar.setObjectName("leftToolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.leftToolBar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1075, 22))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_edit = QtWidgets.QMenu(self.menubar)
        self.menu_edit.setObjectName("menu_edit")
        self.menu_plugins = QtWidgets.QMenu(self.menubar)
        self.menu_plugins.setObjectName("menu_plugins")
        MainWindow.setMenuBar(self.menubar)
        self.action_new = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/filetools/new"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_new.setIcon(icon)
        self.action_new.setObjectName("action_new")
        self.action_open = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/filetools/open"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_open.setIcon(icon1)
        self.action_open.setObjectName("action_open")
        self.action_close = QtWidgets.QAction(MainWindow)
        self.action_close.setObjectName("action_close")
        self.action_save = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/filetools/save"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_save.setIcon(icon2)
        self.action_save.setObjectName("action_save")
        self.action_save_as = QtWidgets.QAction(MainWindow)
        self.action_save_as.setIcon(icon2)
        self.action_save_as.setObjectName("action_save_as")
        self.action_save_a_copy = QtWidgets.QAction(MainWindow)
        self.action_save_a_copy.setObjectName("action_save_a_copy")
        self.action_print = QtWidgets.QAction(MainWindow)
        self.action_print.setObjectName("action_print")
        self.action_SVG = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/filetools/svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_SVG.setIcon(icon3)
        self.action_SVG.setObjectName("action_SVG")
        self.action_X3D = QtWidgets.QAction(MainWindow)
        self.action_X3D.setObjectName("action_X3D")
        self.action_cut = QtWidgets.QAction(MainWindow)
        self.action_cut.setObjectName("action_cut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionSelect_All = QtWidgets.QAction(MainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.action_new_honeycomb_part = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/parttools/new-honeycomb"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_new_honeycomb_part.setIcon(icon4)
        self.action_new_honeycomb_part.setObjectName("action_new_honeycomb_part")
        self.action_path_break = QtWidgets.QAction(MainWindow)
        self.action_path_break.setCheckable(True)
        self.action_path_break.setChecked(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/pathtools/break"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_path_break.setIcon(icon5)
        self.action_path_break.setObjectName("action_path_break")
        self.action_path_select = QtWidgets.QAction(MainWindow)
        self.action_path_select.setCheckable(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/pathtools/select"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_path_select.setIcon(icon6)
        self.action_path_select.setObjectName("action_path_select")
        self.action_slice_first = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/slicetools/go-first"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_slice_first.setIcon(icon7)
        self.action_slice_first.setObjectName("action_slice_first")
        self.action_slice_last = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/slicetools/go-last"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_slice_last.setIcon(icon8)
        self.action_slice_last.setObjectName("action_slice_last")
        self.action_path_erase = QtWidgets.QAction(MainWindow)
        self.action_path_erase.setCheckable(True)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/pathtools/erase"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_path_erase.setIcon(icon9)
        self.action_path_erase.setObjectName("action_path_erase")
        self.action_path_pencil = QtWidgets.QAction(MainWindow)
        self.action_path_pencil.setCheckable(True)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/pathtools/force"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_path_pencil.setIcon(icon10)
        self.action_path_pencil.setObjectName("action_path_pencil")
        self.action_path_insertion = QtWidgets.QAction(MainWindow)
        self.action_path_insertion.setCheckable(True)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/pathtools/insert"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_path_insertion.setIcon(icon11)
        self.action_path_insertion.setObjectName("action_path_insertion")
        self.action_new_square_part = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/parttools/new-square"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_new_square_part.setIcon(icon12)
        self.action_new_square_part.setObjectName("action_new_square_part")
        self.action_path_skip = QtWidgets.QAction(MainWindow)
        self.action_path_skip.setCheckable(True)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/pathtools/skip"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_path_skip.setIcon(icon13)
        self.action_path_skip.setObjectName("action_path_skip")
        self.action_renumber = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/slicetools/renumber"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_renumber.setIcon(icon14)
        self.action_renumber.setObjectName("action_renumber")
        self.action_path_paint = QtWidgets.QAction(MainWindow)
        self.action_path_paint.setCheckable(True)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/pathtools/paint"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_path_paint.setIcon(icon15)
        self.action_path_paint.setObjectName("action_path_paint")
        self.action_path_add_seq = QtWidgets.QAction(MainWindow)
        self.action_path_add_seq.setCheckable(True)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/pathtools/addseq"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_path_add_seq.setIcon(icon16)
        self.action_path_add_seq.setObjectName("action_path_add_seq")
        self.action_export_staples = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/filetools/csv"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_export_staples.setIcon(icon17)
        self.action_export_staples.setObjectName("action_export_staples")
        self.action_preferences = QtWidgets.QAction(MainWindow)
        self.action_preferences.setObjectName("action_preferences")
        self.action_modify = QtWidgets.QAction(MainWindow)
        self.action_modify.setCheckable(True)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/pathtools/modify"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_modify.setIcon(icon18)
        self.action_modify.setObjectName("action_modify")
        self.action_cadnano_website = QtWidgets.QAction(MainWindow)
        self.action_cadnano_website.setObjectName("action_cadnano_website")
        self.action_feedback = QtWidgets.QAction(MainWindow)
        self.action_feedback.setObjectName("action_feedback")
        self.action_filter_part = QtWidgets.QAction(MainWindow)
        self.action_filter_part.setCheckable(True)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/parttools/filter-part"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_filter_part.setIcon(icon19)
        self.action_filter_part.setObjectName("action_filter_part")
        self.action_filter_endpoint = QtWidgets.QAction(MainWindow)
        self.action_filter_endpoint.setCheckable(True)
        self.action_filter_endpoint.setChecked(True)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/parttools/filter-endpoint"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_filter_endpoint.setIcon(icon20)
        self.action_filter_endpoint.setObjectName("action_filter_endpoint")
        self.action_filter_xover = QtWidgets.QAction(MainWindow)
        self.action_filter_xover.setCheckable(True)
        self.action_filter_xover.setChecked(True)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/parttools/filter-xover"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_filter_xover.setIcon(icon21)
        self.action_filter_xover.setText("")
        self.action_filter_xover.setObjectName("action_filter_xover")
        self.action_filters_label = QtWidgets.QAction(MainWindow)
        self.action_filters_label.setEnabled(False)
        self.action_filters_label.setObjectName("action_filters_label")
        self.action_filter_strand = QtWidgets.QAction(MainWindow)
        self.action_filter_strand.setCheckable(True)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/parttools/filter-strand"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_filter_strand.setIcon(icon22)
        self.action_filter_strand.setObjectName("action_filter_strand")
        self.action_filter_handle = QtWidgets.QAction(MainWindow)
        self.action_filter_handle.setCheckable(True)
        self.action_filter_handle.setChecked(False)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/parttools/filter-handle"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_filter_handle.setIcon(icon23)
        self.action_filter_handle.setObjectName("action_filter_handle")
        self.action_filter_scaf = QtWidgets.QAction(MainWindow)
        self.action_filter_scaf.setCheckable(True)
        self.action_filter_scaf.setChecked(True)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/parttools/filter-scaf"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_filter_scaf.setIcon(icon24)
        self.action_filter_scaf.setObjectName("action_filter_scaf")
        self.action_filter_stap = QtWidgets.QAction(MainWindow)
        self.action_filter_stap.setCheckable(True)
        self.action_filter_stap.setChecked(True)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/parttools/filter-stap"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_filter_stap.setIcon(icon25)
        self.action_filter_stap.setObjectName("action_filter_stap")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_autostaple = QtWidgets.QAction(MainWindow)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(":/pathtools/autostaple"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_autostaple.setIcon(icon26)
        self.action_autostaple.setObjectName("action_autostaple")
        self.action_path_mods = QtWidgets.QAction(MainWindow)
        self.action_path_mods.setCheckable(True)
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(":/pathtools/mods"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_path_mods.setIcon(icon27)
        self.action_path_mods.setObjectName("action_path_mods")
        self.action_new_honeypx_part = QtWidgets.QAction(MainWindow)
        self.action_new_honeypx_part.setIcon(icon4)
        self.action_new_honeypx_part.setObjectName("action_new_honeypx_part")
        self.topToolBar.addAction(self.action_new)
        self.topToolBar.addAction(self.action_open)
        self.topToolBar.addAction(self.action_save)
        self.topToolBar.addAction(self.action_SVG)
        self.topToolBar.addAction(self.action_export_staples)
        self.topToolBar.addSeparator()
        # custom button
        self.topToolBar.addWidget(self.part_toolbutton)
        self.part_toolbutton.setIcon(icon4)
        self.part_toolbutton.addAction(self.action_new_honeycomb_part)
        self.part_toolbutton.addAction(self.action_new_honeypx_part)
        self.part_toolbutton.addAction(self.action_new_square_part)
        self.topToolBar.addSeparator()
        self.topToolBar.addAction(self.action_autostaple)
        self.topToolBar.addAction(self.action_filters_label)
        self.topToolBar.addAction(self.action_filter_scaf)
        self.topToolBar.addAction(self.action_filter_stap)
        self.topToolBar.addAction(self.action_filter_handle)
        self.topToolBar.addAction(self.action_filter_endpoint)
        self.topToolBar.addAction(self.action_filter_xover)
        self.topToolBar.addAction(self.action_filter_strand)
        self.rightToolBar.addAction(self.action_path_select)
        self.rightToolBar.addAction(self.action_path_pencil)
        self.rightToolBar.addAction(self.action_path_break)
        self.rightToolBar.addAction(self.action_path_insertion)
        self.rightToolBar.addAction(self.action_path_skip)
        self.rightToolBar.addAction(self.action_path_paint)
        self.rightToolBar.addAction(self.action_path_add_seq)
        self.rightToolBar.addAction(self.action_path_mods)
        self.leftToolBar.addAction(self.action_slice_first)
        self.leftToolBar.addAction(self.action_slice_last)
        self.leftToolBar.addAction(self.action_renumber)
        self.menu_file.addAction(self.action_about)
        self.menu_file.addAction(self.action_preferences)
        self.menu_file.addAction(self.action_new)
        self.menu_file.addAction(self.action_open)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_close)
        self.menu_file.addAction(self.action_save)
        self.menu_file.addAction(self.action_save_as)
        self.menu_edit.addAction(self.action_modify)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_plugins.menuAction())

        self.retranslateUi(MainWindow)
        self.action_close.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "cadnano"))
        self.topToolBar.setWindowTitle(_translate("MainWindow", "Main Toolbar"))
        self.rightToolBar.setWindowTitle(_translate("MainWindow", "Path Tools"))
        self.leftToolBar.setWindowTitle(_translate("MainWindow", "Slice Tools"))
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.menu_edit.setTitle(_translate("MainWindow", "Edit"))
        self.menu_plugins.setTitle(_translate("MainWindow", "Plugins"))
        self.action_new.setText(_translate("MainWindow", "New..."))
        self.action_new.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_open.setText(_translate("MainWindow", "Open..."))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_close.setText(_translate("MainWindow", "Close"))
        self.action_close.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.action_save.setText(_translate("MainWindow", "Save"))
        self.action_save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_save_as.setText(_translate("MainWindow", "Save As..."))
        self.action_save_as.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.action_save_a_copy.setText(_translate("MainWindow", "Save a Copy..."))
        self.action_print.setText(_translate("MainWindow", "Print..."))
        self.action_SVG.setText(_translate("MainWindow", "SVG"))
        self.action_X3D.setText(_translate("MainWindow", "X3D"))
        self.action_cut.setText(_translate("MainWindow", "Cut"))
        self.action_cut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All"))
        self.actionSelect_All.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.action_new_honeycomb_part.setText(_translate("MainWindow", "Honeycomb"))
        self.action_new_honeycomb_part.setToolTip(_translate("MainWindow", "Click to add new part with honeycomb lattice"))
        self.action_path_break.setText(_translate("MainWindow", "Break Tool"))
        self.action_path_break.setIconText(_translate("MainWindow", "Break"))
        self.action_path_break.setToolTip(_translate("MainWindow", "(B)reak Tool"))
        self.action_path_break.setShortcut(_translate("MainWindow", "B"))
        self.action_path_select.setText(_translate("MainWindow", "Select"))
        self.action_path_select.setIconText(_translate("MainWindow", "Select"))
        self.action_path_select.setToolTip(_translate("MainWindow", "Select Tool (v)"))
        self.action_path_select.setShortcut(_translate("MainWindow", "V"))
        self.action_slice_first.setText(_translate("MainWindow", "First"))
        self.action_slice_first.setToolTip(_translate("MainWindow", "Move the slice bar to the first position."))
        self.action_slice_last.setText(_translate("MainWindow", "Last"))
        self.action_slice_last.setToolTip(_translate("MainWindow", "Move the slice bar to the last position."))
        self.action_path_erase.setText(_translate("MainWindow", "Erase"))
        self.action_path_erase.setToolTip(_translate("MainWindow", "(E)rase Tool"))
        self.action_path_pencil.setText(_translate("MainWindow", "Pencil"))
        self.action_path_pencil.setToolTip(_translate("MainWindow", "Pe(n)cil Tool"))
        self.action_path_pencil.setShortcut(_translate("MainWindow", "N"))
        self.action_path_insertion.setText(_translate("MainWindow", "Insert"))
        self.action_path_insertion.setToolTip(_translate("MainWindow", "(I)nsert Tool"))
        self.action_path_insertion.setShortcut(_translate("MainWindow", "I"))
        self.action_new_square_part.setText(_translate("MainWindow", "Square"))
        self.action_new_square_part.setToolTip(_translate("MainWindow", "Click to add new part with square lattice"))
        self.action_path_skip.setText(_translate("MainWindow", "Skip"))
        self.action_path_skip.setToolTip(_translate("MainWindow", "(S)kip Tool"))
        self.action_path_skip.setShortcut(_translate("MainWindow", "S"))
        self.action_renumber.setText(_translate("MainWindow", "Rnum"))
        self.action_renumber.setToolTip(_translate("MainWindow", "Renumber Slice helices according to helix ordering in Path panel."))
        self.action_path_paint.setText(_translate("MainWindow", "Paint"))
        self.action_path_paint.setToolTip(_translate("MainWindow", "(P)aint Tool"))
        self.action_path_paint.setShortcut(_translate("MainWindow", "P"))
        self.action_path_add_seq.setText(_translate("MainWindow", "Seq"))
        self.action_path_add_seq.setToolTip(_translate("MainWindow", "(A)dd Sequence Tool"))
        self.action_path_add_seq.setShortcut(_translate("MainWindow", "A"))
        self.action_export_staples.setText(_translate("MainWindow", "Export"))
        self.action_export_staples.setToolTip(_translate("MainWindow", "export oligos as *.CSV"))
        self.action_preferences.setText(_translate("MainWindow", "Preferences"))
        self.action_preferences.setShortcut(_translate("MainWindow", "Ctrl+,"))
        self.action_modify.setText(_translate("MainWindow", "Modify mode"))
        self.action_modify.setToolTip(_translate("MainWindow", "Modify mode"))
        self.action_cadnano_website.setText(_translate("MainWindow", "cadnano Website"))
        self.action_feedback.setText(_translate("MainWindow", "Feedback"))
        self.action_filter_part.setText(_translate("MainWindow", "Parts"))
        self.action_filter_part.setToolTip(_translate("MainWindow", "Part-selection mode"))
        self.action_filter_endpoint.setToolTip(_translate("MainWindow", "(E)ndpoints"))
        self.action_filter_endpoint.setShortcut(_translate("MainWindow", "E"))
        self.action_filter_xover.setToolTip(_translate("MainWindow", "(X)overs"))
        self.action_filter_xover.setShortcut(_translate("MainWindow", "X"))
        self.action_filters_label.setText(_translate("MainWindow", "Selectable:"))
        self.action_filters_label.setToolTip(_translate("MainWindow", "Selection Filters"))
        self.action_filter_strand.setToolTip(_translate("MainWindow", "stran(D)s"))
        self.action_filter_strand.setShortcut(_translate("MainWindow", "D"))
        self.action_filter_handle.setToolTip(_translate("MainWindow", "(H)andles"))
        self.action_filter_handle.setShortcut(_translate("MainWindow", "H"))
        self.action_filter_scaf.setToolTip(_translate("MainWindow", "s(C)affold"))
        self.action_filter_scaf.setShortcut(_translate("MainWindow", "C"))
        self.action_filter_stap.setToolTip(_translate("MainWindow", "s(T)aple"))
        self.action_filter_stap.setShortcut(_translate("MainWindow", "T"))
        self.action_about.setText(_translate("MainWindow", "About cadnano"))
        self.action_autostaple.setText(_translate("MainWindow", "AutoStaple"))
        self.action_autostaple.setToolTip(_translate("MainWindow", "Create staple strands complementary to existing scaffold."))
        self.action_path_mods.setText(_translate("MainWindow", "Mod"))
        self.action_path_mods.setToolTip(_translate("MainWindow", "(M)odifer Tool"))
        self.action_path_mods.setShortcut(_translate("MainWindow", "M"))
        self.action_new_honeypx_part.setText(_translate("MainWindow", "Honeycomb PX"))
        self.action_new_honeypx_part.setIconText(_translate("MainWindow", "Honey PX"))
        self.action_new_honeypx_part.setToolTip(_translate("MainWindow", "Add new part honeycomb PX"))
        self.part_toolbutton.setText(_translate("MainWindow", "Add Part "))
        self.part_toolbutton.setToolTip(_translate("MainWindow", "Select a part type"))

from cadnano.gui.views.customqgraphicsview import CustomQGraphicsView
import cadnano.gui.ui.mainwindow.icons_rc
