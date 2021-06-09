# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import networkx as nx
import matplotlib.pyplot as plt
class Ui_Dijkstra(object):
    """Main UI class of app.

    """
    def setupUi(self, Dijsktra):
        """Rendering UI elements.

        """
        Dijsktra.setObjectName("Dijsktra")
        Dijsktra.resize(827, 720)
        self.centralwidget = QtWidgets.QWidget(Dijsktra)
        self.centralwidget.setObjectName("centralwidget")
        self.node1_text = QtWidgets.QTextEdit(self.centralwidget)
        self.node1_text.setGeometry(QtCore.QRect(280, 430, 71, 41))
        self.node1_text.setObjectName("node1_text")
        self.node2_text = QtWidgets.QTextEdit(self.centralwidget)
        self.node2_text.setGeometry(QtCore.QRect(370, 430, 71, 41))
        self.node2_text.setObjectName("node2_text")
        self.addnode_button = QtWidgets.QPushButton(self.centralwidget)
        self.addnode_button.setGeometry(QtCore.QRect(80, 480, 91, 31))
        self.addnode_button.setObjectName("addnode_button")
        self.newnode_text = QtWidgets.QTextEdit(self.centralwidget)
        self.newnode_text.setGeometry(QtCore.QRect(90, 430, 71, 41))
        self.newnode_text.setObjectName("newnode_text")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 400, 101, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 360, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 360, 121, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 410, 71, 19))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(370, 410, 71, 19))
        self.label_5.setObjectName("label_5")
        self.weight_text = QtWidgets.QTextEdit(self.centralwidget)
        self.weight_text.setGeometry(QtCore.QRect(460, 430, 71, 41))
        self.weight_text.setObjectName("weight_text")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(460, 410, 79, 19))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(390, 10, 51, 19))
        self.label_7.setObjectName("label_7")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(223, 380, 41, 161))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(570, 380, 41, 161))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(620, 360, 191, 21))
        self.label_8.setObjectName("label_8")
        self.source_text = QtWidgets.QTextEdit(self.centralwidget)
        self.source_text.setGeometry(QtCore.QRect(630, 430, 61, 41))
        self.source_text.setObjectName("source_text")
        self.destination_text = QtWidgets.QTextEdit(self.centralwidget)
        self.destination_text.setGeometry(QtCore.QRect(730, 430, 61, 41))
        self.destination_text.setObjectName("destination_text")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(630, 410, 61, 19))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(730, 410, 91, 20))
        self.label_10.setObjectName("label_10")
        self.run_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_button.setGeometry(QtCore.QRect(670, 490, 100, 27))
        self.run_button.setObjectName("run_button")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(50, 340, 721, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(40, 550, 731, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(380, 560, 51, 19))
        self.label_11.setObjectName("label_11")
        self.result_text = QtWidgets.QTextEdit(self.centralwidget)
        self.result_text.setGeometry(QtCore.QRect(180, 580, 461, 91))
        self.result_text.setReadOnly(True)
        self.result_text.setObjectName("result_text")
        self.connect_button = QtWidgets.QPushButton(self.centralwidget)
        self.connect_button.setGeometry(QtCore.QRect(360, 490, 100, 27))
        self.connect_button.setObjectName("connect_button")
        self.resetgraph_button = QtWidgets.QPushButton(self.centralwidget)
        self.resetgraph_button.setGeometry(QtCore.QRect(699, 600, 111, 41))
        self.resetgraph_button.setObjectName("resetgraph_button")
        Dijsktra.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Dijsktra)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 827, 24))
        self.menubar.setObjectName("menubar")
        Dijsktra.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Dijsktra)
        self.statusbar.setObjectName("statusbar")
        Dijsktra.setStatusBar(self.statusbar)
        self.error_dialog = QtWidgets.QErrorMessage()


        # self.G = nx.Graph()
        self.plot_canvas = PlotCanvas(self.centralwidget)
        self.plot_canvas.setGeometry(QtCore.QRect(190, 30, 461, 301))
        self.plot_canvas.setObjectName("plot_canvas")

        self.retranslateUi(Dijsktra)
        QtCore.QMetaObject.connectSlotsByName(Dijsktra)

    def retranslateUi(self, Dijsktra):
        _translate = QtCore.QCoreApplication.translate
        Dijsktra.setWindowTitle(_translate("Dijsktra", "Dijkstra"))
        self.addnode_button.setText(_translate("Dijsktra", "Add Node"))
        self.newnode_text.setHtml(_translate("Dijsktra", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("Dijsktra", "Node Name"))
        self.label_2.setText(_translate("Dijsktra", "New Node"))
        self.label_3.setText(_translate("Dijsktra", "Connect Nodes"))
        self.label_4.setText(_translate("Dijsktra", "Node 1"))
        self.label_5.setText(_translate("Dijsktra", "Node 2"))
        self.label_6.setText(_translate("Dijsktra", "Weight"))
        self.label_7.setText(_translate("Dijsktra", "Graph"))
        self.label_8.setText(_translate("Dijsktra", "Calculate Shortest Path"))
        self.label_9.setText(_translate("Dijsktra", "Source"))
        self.label_10.setText(_translate("Dijsktra", "Destination"))
        self.run_button.setText(_translate("Dijsktra", "Run"))
        self.label_11.setText(_translate("Dijsktra", "Result"))
        self.connect_button.setText(_translate("Dijsktra", "Connect"))
        self.resetgraph_button.setText(_translate("Dijsktra", "Reset Graph"))


class PlotCanvas(FigureCanvas): # By inheriting the FigureCanvas class, this class is both a PyQt5 Qwidget and a Matplotlib FigureCanvas, which is the key to connecting pyqt5 and matplotlib
    """A UI element to plotting networkx graph on window.
    """
    def __init__(self, parent=None):
        """Constructor of PlotCanvas class.

        Args:
            parent (optional): Parent should be Qt widget. Defaults to None.
        """
        FigureCanvas.__init__(self)
        self.setParent(parent)
        self.figure = plt.figure()
        FigureCanvas.updateGeometry(self)
       

    def plot(self, G):
        """Plotting all nodes and edges of graph with labels.

        Args:
            G (nx.Graph): Graph.
        """
        self.figure.clf()
        pos=nx.spring_layout(G, seed=42)

        #Drawing graph on canvas in UI.
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        nx.draw(G, pos, with_labels=True, font_size=11, node_size=150, node_color="r", font_color="w")
        self.draw_idle()