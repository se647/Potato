import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
class MainWindow(QMainWindow):
    def _init_(self):
        super().__init__()
        self.setWindowTitle("Hello PyQt")
        self.setGeometry(100, 100, 600, 400)
        self.label = QLabel("Hello PyQt!", self)
        self.label.setGeometry(50, 50, 200, 50)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
        