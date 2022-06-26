from qtpy.QtWidgets import QPushButton, QWidget
from svgAbstractButton import SvgAbstractButton


class SvgButton(QPushButton, SvgAbstractButton):
    def __init__(self, base_widget: QWidget = None, *args, **kwargs):
        super().__init__(base_widget, *args, **kwargs)