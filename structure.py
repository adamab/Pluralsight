from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys





app = QApplication(sys.argv)
dialog = QDialog()
dialog.show()
app.exec_() # can also use sys.exit(app.exec_()) will give a specific exit code

