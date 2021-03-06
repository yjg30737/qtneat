from qtpy.QtCore import Qt
from qtpy.QtGui import QPalette, QFont, QColor, qGray
from qtpy.QtWidgets import QGridLayout, QWidget, QLabel, QFrame
from pyqt_svg_icon_text_widget import SvgIconTextWidget


class TitleBar(QWidget):
    def __init__(self, base_widget: QWidget, text: str = '', font: QFont = QFont('Arial', 14),
                 icon_filename: str = None,
                 align=Qt.AlignCenter):
        super().__init__()
        self.__baseWidget = base_widget
        self.__initVal()
        self.__initUi(text=text, font=font, icon_filename=icon_filename, align=align)

    def __initVal(self):
        self.__svgIconTitleWidget = ''
        self.__iconLbl = QLabel()
        self.__titleLbl = QLabel()
        self.__cornerWidget = ''
        self.__separator = QFrame()

    def __getTitleTextColor(self, base_color):
        r, g, b = base_color.red() ^ 255, base_color.green() ^ 255, base_color.blue() ^ 255
        if qGray(r, g, b) > 255 // 2:
            text_color = QColor(255, 255, 255)
        else:
            text_color = QColor(0, 0, 0)
        return text_color.name()

    def __initUi(self, text: str, font: QFont = QFont('Arial', 14), icon_filename: str = None, align=Qt.AlignCenter):
        self.__svgIconTitleWidget = SvgIconTextWidget()

        self.__iconLbl = self.__svgIconTitleWidget.getSvgLabel()
        self.__titleLbl = self.__svgIconTitleWidget.getTextLabel()

        if icon_filename:
            self.__svgIconTitleWidget.setSvgFile(icon_filename)
        else:
            self.__iconLbl.setVisible(False)
        self.__svgIconTitleWidget.setText(text)

        self.__titleLbl.setFont(font)

        base_color = self.__baseWidget.palette().color(QPalette.Base)

        self.__titleTextColor = self.__getTitleTextColor(base_color)

        self.setStyleSheet(f'''
                            QWidget
                            {{ 
                            background-color: {base_color.name()};
                            }}
                            QLabel
                            {{
                            color: {self.__titleTextColor};
                            }}
                            '''
                           )

        self.setMinimumHeight(self.sizeHint().height())

        lay = self.__svgIconTitleWidget.layout()
        lay.setContentsMargins(0, 0, 0, 0)

        lay = QGridLayout()
        lay.addWidget(self.__svgIconTitleWidget, 0, 0, 1, 2, alignment=align)
        lay.setContentsMargins(0, 0, 0, 0)
        # todo
        # set the spacing dynamically
        lay.setSpacing(3)
        self.setLayout(lay)

    def setCornerWidget(self, cornerWidget, align=Qt.AlignRight):
        lay = self.layout()
        self.__cornerWidget = cornerWidget
        w = h = self.__titleLbl.fontMetrics().height() * 1.25
        self.__cornerWidget.setButtonSize(w, h)
        if align == Qt.AlignRight:
            lay.addWidget(self.__cornerWidget, 0, 1, 1, 1, alignment=align)
        elif align == Qt.AlignLeft:
            lay.addWidget(self.__cornerWidget, 0, 0, 1, 1, alignment=align)

    def setBottomSeparator(self):
        lay = self.layout()
        self.__separator.setFrameShape(QFrame.HLine)
        self.__separator.setFrameShadow(QFrame.Sunken)
        self.__separator.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.__separator, 1, 0, 1, 2)

    def getIconTitleWidget(self):
        return self.__svgIconTitleWidget

    def getIcon(self):
        return self.__iconLbl

    def getTitle(self):
        return self.__titleLbl

    def getCornerWidget(self):
        return self.__cornerWidget