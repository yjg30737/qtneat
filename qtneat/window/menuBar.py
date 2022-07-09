from pyqt_svg_button import SvgButton
from pyqt_svg_label import SvgLabel
from qtpy import QtWidgets, QtCore, QtGui


class MenuBar(QtWidgets.QMenuBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initVal()
        self.__initUi()

    def __initVal(self):
        self.__isHidable = False
        self.__isHiding = False
        self.__iconLbl = SvgLabel()
        self.__titleLbl = QtWidgets.QLabel()

    def __initUi(self):
        pass

    def __showMenu(self):
        self.__menuAnimation.setDirection(QtCore.QAbstractAnimation.Backward)
        self.__menuAnimation.start()
        self.__isHiding = False

    def __hideMenu(self):
        self.__menuAnimation.setDirection(QtCore.QAbstractAnimation.Forward)
        self.__menuAnimation.start()
        self.__isHiding = True

    def setTitle(self, title: str, font: QtGui.QFont = QtGui.QFont('Arial', 9)):
        self.__titleLbl.setText(title)
        self.__titleLbl.setFont(font)
        self.__titleLbl.setMinimumHeight(self.sizeHint().height())
        cornerWidget = self.cornerWidget()
        if cornerWidget:
            lay = cornerWidget.layout()
            if lay:
                lay.insertWidget(0, self.__titleLbl)
        else:
            cornerWidget = QtWidgets.QWidget()
            lay = QtWidgets.QHBoxLayout()
            lay.addWidget(self.__titleLbl)
            lay.setContentsMargins(0, 0, 2, 0)
            cornerWidget.setLayout(lay)
            self.setCornerWidget(cornerWidget, QtCore.Qt.TopRightCorner)

    def setIcon(self, icon: str):
        self.__iconLbl.setSvgFile(icon)
        self.setCornerWidget(self.__iconLbl, QtCore.Qt.TopLeftCorner)

    def getTitle(self) -> QtWidgets.QLabel:
        return self.__titleLbl

    def getIcon(self) -> SvgLabel:
        return self.__iconLbl

    def setHidable(self, flag: bool):
        self.__isHidable = flag
        self.setMouseTracking(True)
        self.setHideButton()

    def setHideButton(self):
        tool_button = self.findChild(QtWidgets.QToolButton)
        tool_button.setArrowType(QtCore.Qt.RightArrow)

        self.__showToggleBtn = SvgButton(self)
        self.__showToggleBtn.clicked.connect(self.__hideMenu)
        self.__showToggleBtn.setToolTip('Hide the menu bar')
        self.__showToggleBtn.setIcon('close.svg')

        height = self.sizeHint().height()
        # button should be square
        width = height
        self.__showToggleBtn.setFixedSize(width, height)

        cornerWidget = self.cornerWidget(QtCore.Qt.TopRightCorner)
        if cornerWidget:
            print(cornerWidget)
            # cornerWidget.layout().addWidget(self.__showToggleBtn)

        self.__menuAnimation = QtCore.QPropertyAnimation(self, b"height")
        self.__menuAnimation.valueChanged.connect(self.setFixedHeight)

        self.__menuAnimation.setStartValue(height)
        self.__menuAnimation.setDuration(200)  # default duration
        self.__menuAnimation.setEndValue(1)  # default end value

    def enterEvent(self, e):
        if self.__isHidable and self.__isHiding:
            self.__showMenu()
        return super().enterEvent(e)

