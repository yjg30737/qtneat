from qtpy.QtCore import Qt, QCoreApplication
from qtpy.QtGui import QGuiApplication, QFont
from qtpy.QtWidgets import QApplication, QWidget
from pyqt_custom_titlebar_setter import CustomTitlebarSetter
from qt_sass_theme import QtSassTheme

# for pyqt5
from qtneat.window import Window


def prepareQtApp():
    QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)


class QtAppManager:
    def __init__(self, w):
        self.__innerWidget = w
        self.__mainWindow = ''

    def __getStandardWindow(self, main_window: QWidget, title: str = '', icon_filename: str = '',
                                        font: QFont = QFont('Arial', 14), hint: list = ['min', 'max', 'close'],
                                        align=Qt.AlignCenter, bottom_separator: bool = False):
        titleBarWindow = Window(main_window)
        titleBarWindow.setTopTitleBar(title=title, icon_filename=icon_filename, font=font, align=align,
                                      bottom_separator=bottom_separator)
        titleBarWindow.setButtonHint(hint)
        titleBarWindow.setButtons()

        return titleBarWindow

    def setTheme(self, theme: str = 'dark_gray', background_darker=False):
        g = QtSassTheme()
        g.getThemeFiles(theme=theme, background_darker=background_darker)
        g.setThemeFiles(self.__innerWidget)

    def setTitleBar(self, icon_filename: str = '', font: QFont = QFont('Arial', 14),
                    hint: list = ['min', 'max', 'close'], align=Qt.AlignCenter,
                    bottom_separator: bool = False):
        self.__mainWindow = CustomTitlebarSetter.getCustomTitleBarWindow(main_window=self.__innerWidget,
                                                                        title='',
                                                                        icon_filename=icon_filename,
                                                                        font=font,
                                                                        hint=hint,
                                                                        align=align,
                                                                        bottom_separator=bottom_separator)

    def show(self):
        if self.__mainWindow:
            self.__mainWindow.show()
        else:
            self.__innerWidget.show()