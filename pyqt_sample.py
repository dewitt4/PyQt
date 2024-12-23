from PyQt5.QtWidgets import QApplication, QWidget, QLabel

if __name__ == '__main__':
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle('My PyQt App')
    label = QLabel('Hello from PyQt!', window)
    label.move(50, 50) 
    window.setGeometry(100, 100, 300, 200) 
    window.show()
    app.exec_()
