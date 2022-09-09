# qtneat
<b>DON'T USE IT. I'M STILL WORKING</b>

don't even care about this. It will take really long time like Toby Fox making Undertale.

Set the Qt frameless titlebar/theme easily

This is for... me.

or someone who want to use this..

## Requirements
* PyQt5 >= 5.8

## Included Packages
* <a href="https://github.com/spyder-ide/qtawesome">qtawesome</a>
* <a href="https://github.com/yjg30737/pyqt-svg-button">pyqt-svg-button</a>
* <a href="https://github.com/yjg30737/pyqt-svg-icon-text-widget">pyqt-svg-icon-text-widget</a>

## Setup
`python -m pip install qtneat`

## Example
```python
from PyQt5.QtWidgets import QApplication
from pyqt_timer.settingsDialog import SettingsDialog

from qtneat import prepareQtApp, QtAppManager

if __name__ == "__main__":
    import sys

    prepareQtApp()
    a = QApplication(sys.argv)
    w = SettingsDialog()
    m = QtAppManager(w)
    m.setTheme(theme='#6f478d')
    m.setTitleBar(icon_filename='settings.svg')
    m.show()
    a.exec()
```

Result

![image](https://user-images.githubusercontent.com/55078043/175795922-2239ee56-b514-46f4-9a2c-849e419a1c8f.png)
