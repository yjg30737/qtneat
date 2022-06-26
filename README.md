# qtneat
<b>DON'T USE IT</b>

Set the Qt frameless titlebar/theme easily

There is qtmodern, qtawesome, i chose the word "<b>neat</b>".

Tell me that naming is nice.

I'll make this usable not only for PyQt5, but also for PyQt6 and PySide6.

## Requirements
* PyQt5 >= 5.8

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
