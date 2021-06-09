"""
Author: Mücteba Özcan.
https://github.com/mucozcan/dijkstra-pyqt
"""

# TODO refactor.
# TODO documentation.
# TODO revert edge functionality
# TODO dijkstra typos.

from PyQt5 import QtWidgets
from PyQt5 import QtGui
import sys
import networkx as nx
from utils.dijkstra import Dijkstra
from ui.dijkstra_ui import Ui_Dijkstra
import matplotlib.pyplot as plt

class GUI(QtWidgets.QMainWindow):
    """Main GUI class to handle UI and controller functions.

    Args:
        QtWidgets.QMainWindow()
    """
    def __init__(self):
        """Constructor of GUI.
        """
        super(GUI, self).__init__()
        self.setup_gui()
        

    def setup_gui(self):
        """Initializer of GUI.
        """
        self.form = Ui_Dijkstra()
        self.form.setupUi(self)
        self.G = nx.Graph()
        

        #Controllers
        self.form.addnode_button.clicked.connect(self.add_new_node)
        self.form.connect_button.clicked.connect(self.connect_nodes)
        self.form.run_button.clicked.connect(self.run)
        self.form.resetgraph_button.clicked.connect(self.reset)

    def show_dialog(self, message):
        """Opening a new error window with a given error message.

        Args:
            message (string): error text.
        """
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    def add_new_node(self):
        """ Adding a new node to the Graph. 
        """


        new_node = str(self.form.newnode_text.toPlainText())
        if not new_node:
            self.form.newnode_text.clear()
            self.show_dialog("Empty argument.")
            return
        
        self.form.newnode_text.clear()
        
        if self.G.has_node(new_node):
            self.show_dialog(f"{new_node} is already constructed.")
        
        else:
            self.G.add_node(new_node)
            self.form.plot_canvas.plot(self.G)
       
        

    def connect_nodes(self):
        """Connects two nodes with a given weight. 
        """
        node1 = str(self.form.node1_text.toPlainText())
        node2 = str(self.form.node2_text.toPlainText())
        weight = str(self.form.weight_text.toPlainText())
        self.form.node1_text.clear()
        self.form.node2_text.clear()
        self.form.weight_text.clear()

        if not node1 or not node2 or not weight:      
            self.show_dialog("Empty argument.")
            return
        
        try:
            weight = int(weight)
        except:
            self.show_dialog("Weight should be an integer.")
            return

        if self.G.has_edge(node1, node2):
            self.show_dialog(f"Edge: {node1, node2} is already constructed.")

        else:
            self.G.add_edge(node1, node2, weight=weight)
            self.form.plot_canvas.plot(self.G)

        

    def run(self):
        """Takes source and destination from user and runs the Dijkstra algorithm to calculate shortest path.
        """
        source = str(self.form.source_text.toPlainText())
        dest = str(self.form.destination_text.toPlainText())
        
        self.form.source_text.clear()
        self.form.destination_text.clear()
        
        if not source or not dest:
            self.show_dialog("Empty argument.")
            return 

        
        if self.G.has_node(source) and self.G.has_node(dest):
            if source in nx.algorithms.descendants(self.G, dest):
                graph = nx.to_dict_of_dicts(self.G) # converting to dict based graph.
                dijkstra = Dijkstra(graph)
                parents,  visited = dijkstra.find_route(source, dest)
                shortest_path = dijkstra.generate_path(parents, source, dest)
                shortest_path = " -> ".join(shortest_path)
                result = f"Distance is {visited[dest]} units.\nShortest path from {source} to {dest} is {shortest_path}"
                self.form.result_text.setText(result)
            else:
                self.show_dialog(f"There is no connection between {source} and {dest}.")
        else:
            self.show_dialog(f"Please check source and destination.")
        

    def reset(self):
        """Resets the existing graph.
        """
        self.G = nx.Graph()
        self.form.plot_canvas.plot(self.G)

mainloop = QtWidgets.QApplication([])
run_app = GUI()
run_app.show()
sys.exit(mainloop.exec_())

