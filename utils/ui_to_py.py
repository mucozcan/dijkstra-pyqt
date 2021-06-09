from PyQt5 import uic

with open("./dijsktra_ui.py", 'w', encoding="utf-8") as fout:
    uic.compileUi("./MainWindow.ui", fout)
