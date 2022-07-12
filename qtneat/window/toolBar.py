from qtpy.QtWidgets import QToolBar, QWidget, QHBoxLayout, QSizePolicy, QAction, QWidgetAction
from qtpy.QtCore import Qt, QPropertyAnimation, QAbstractAnimation
from pyqt_svg_button import SvgButton


class ToolBar(QToolBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initVal()
        self.__initUi()

    def __initVal(self):
        self.__foldable_flag = False
        self.__foldBtn = SvgButton()
        self.__cornerAction = QWidgetAction(self)
        self.__menuAnimation = QPropertyAnimation(self, b"height")

    def __initUi(self):
        # moving toolbar is not standard nowadays, in my opinion
        # at least I have to polish ugly looking style
        self.setMovable(False)

    def addWidget(self, widget: QWidget) -> QAction:
        self.insertWidget(self.__cornerAction, widget)
        self.__menuAnimation.setStartValue(self.sizeHint().height())

    def setFoldable(self, f: bool):
        self.__foldable_flag = f
        if self.__foldable_flag:
            self.__foldBtn.setIcon('ico/fold.svg')
            self.__foldBtn.setCheckable(True)
            self.__foldBtn.toggled.connect(self.__fold)
            self.__foldBtn.setMaximumWidth(12)

            cornerWidget = QWidget()
            lay = QHBoxLayout()
            lay.addWidget(self.__foldBtn)
            lay.setAlignment(Qt.AlignRight | Qt.AlignBottom)
            lay.setContentsMargins(0, 0, 0, 0)
            cornerWidget.setLayout(lay)
            cornerWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

            self.__cornerAction.setDefaultWidget(cornerWidget)

            self.addAction(self.__cornerAction)

            self.__menuAnimation.valueChanged.connect(self.setFixedHeight)
            self.__menuAnimation.setStartValue(self.sizeHint().height())
            self.__menuAnimation.setDuration(200)  # default duration
            self.__menuAnimation.setEndValue(self.__foldBtn.sizeHint().height())  # default end value
        else:
            # remove fold button or add tack button
            pass

    def __fold(self, f):
        if f:
            self.__menuAnimation.setDirection(QAbstractAnimation.Forward)
            self.__menuAnimation.start()
            self.__foldBtn.setIcon('ico/unfold.svg')
            self.setFixedHeight(self.__foldBtn.sizeHint().height())
        else:
            self.__menuAnimation.setDirection(QAbstractAnimation.Backward)
            self.__menuAnimation.start()
            self.__foldBtn.setIcon('ico/fold.svg')
            self.setFixedHeight(self.sizeHint().height())

