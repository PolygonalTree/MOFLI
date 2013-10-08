 #!/usr/bin/env python
 # -*- coding: utf-8 -*-

# simple.py

import sys
from PySide import QtGui

class Incubator(QtGui.QWidget):
	def __init__(self):
		super(Incubator, self).__init__()

		self.initUI()
	def initUI(self):
		QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
		self.setGeometry()

class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('favicon.ico'))        
      	
      	QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn = QtGui.QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)       
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltips')    
        self.statusBar().showMessage('Ready')
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')    
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(exitAction)
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Menubar')    
        sexitAction = QtGui.QAction(QtGui.QIcon('exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.close)
        
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Toolbar')    
        self.show()
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
