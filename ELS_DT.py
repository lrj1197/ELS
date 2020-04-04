from PyQt5 import QtWidgets, QtCore, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint
import numpy as np

def lin(m,b,x):
    x = np.array(x)
    return m*x + b

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.btn = QtWidgets.QPushButton("Start", self)
        self.btn.move(100,350)
        self.btn.clicked.connect(self.update_plot_data)

        self.stp = QtWidgets.QPushButton("Stop", self)
        self.stp.move(200,350)
        self.stp.clicked.connect(self.stop_update_plot_data)

        self.btn = QtWidgets.QPushButton("Start", self)
        self.btn.move(350,350)
        self.btn.clicked.connect(self.update_plot_data1)

        self.stp = QtWidgets.QPushButton("Stop", self)
        self.stp.move(450,350)
        self.stp.clicked.connect(self.stop_update_plot_data1)

        self.exit = QtWidgets.QPushButton("Exit", self)
        self.exit.move(250,450)
        self.exit.clicked.connect(self.quit)

        self.graphWidget = pg.PlotWidget(self)
        self.graphWidget.move(0,100)
        self.graphWidget.resize(300,200)

        self.graphWidget1 = pg.PlotWidget(self)
        self.graphWidget1.move(350,100)
        self.graphWidget1.resize(300,200)
        # self.setCentralWidget(self.graphWidget)

        self.x = [0]  # 100 time points
        self.y = [0]  # 100 data points
        self.x1 = [0]  # 100 time points
        self.y1 = [0]  # 100 data points

        self.graphWidget.setBackground('k')
        self.graphWidget1.setBackground('k')
        pen = pg.mkPen(color=(255, 0, 0))
        self.graphWidget.setLabel('left', 'X Outout (°)', color='red', size=10)
        self.graphWidget.setLabel('bottom', 'Minutes (m)', color='red', size=10)
        self.graphWidget1.setLabel('left', 'Y Output (°)', color='red', size=10)
        self.graphWidget1.setLabel('bottom', 'Minutes (m)', color='red', size=10)

        self.pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.graphWidget.plot(self.x, self.y, pen=None,symbol='o',symbolSize=5)
        self.data_line1 =  self.graphWidget1.plot(self.x1, self.y1, pen=None,symbol='o',symbolSize=5)
        self.up_line =  self.graphWidget.plot(self.x, lin(0,50,self.x1), pen=self.pen)
        self.up_line1 =  self.graphWidget1.plot(self.x1, lin(0,50,self.x1), pen=self.pen)
        self.bot_line =  self.graphWidget.plot(self.x, lin(0,25,self.x1), pen=self.pen)
        self.bot_line1 =  self.graphWidget1.plot(self.x1, lin(0,25,self.x1), pen=self.pen)


        self.setGeometry(100,100,700,700)

    def quit(self):
        self.timer.stop()
        self.timer1.stop()
        sys.exit()


    def stop_update_plot_data(self):
        self.timer.stop()


    def update_plot_data(self):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(250)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()        # self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.
        # self.y = self.y[1:]  # Remove the first
        self.y.append( randint(0,100))  # Add a new random value.
        self.up_line.setData(self.x, lin(0,50,self.x))
        self.bot_line.setData(self.x, lin(0,25,self.x))
        self.data_line.setData(self.x, self.y)  # Update the data.

    def stop_update_plot_data1(self):
        self.timer1.stop()


    def update_plot_data1(self):
        self.timer1 = QtCore.QTimer()
        self.timer1.setInterval(250)
        self.timer1.timeout.connect(self.update_plot_data1)
        self.timer1.start()        # self.x = self.x[1:]  # Remove the first y element.
        self.x1.append(self.x1[-1] + 1)  # Add a new value 1 higher than the last.

        # self.y = self.y[1:]  # Remove the first
        self.y1.append( randint(0,100))  # Add a new random value.
        self.up_line1.setData(self.x1, lin(0,50,self.x1))
        self.bot_line1.setData(self.x1, lin(0,25,self.x1))
        self.data_line1.setData(self.x1, self.y1)  # Update the data.

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
