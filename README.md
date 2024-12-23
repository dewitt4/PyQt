# PyQt
Samples of using PyQt for GUIs for Python 

Here's how to get started with PyQt in Visual Studio Code:

**1. Install PyQt**

* **Open the terminal in VS Code:** View -> Terminal 
* **Install PyQt using pip:** 
   ```bash
   pip install PyQt5 
   ```

**2. Create a Simple PyQt Application**

```python
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
```

**3. Run the Application**

* **Save the code:** Save the file as `my_pyqt_app.py` (or any name you prefer).
* **Run the code:** In the terminal, execute:
   ```bash
   python my_pyqt_app.py
   ```

This will create a simple window with a "Hello from PyQt!" label.

**4. Key PyQt Concepts**

* **QApplication:** The main application object. It handles events and manages the application's resources.
* **QWidget:** The base class for all user interface elements. It represents a rectangular area on the screen.
* **QLabel:** A widget for displaying text.
* **setWindowTitle():** Sets the title of the window.
* **move():** Positions the label within the window.
* **setGeometry():** Sets the size and position of the window.
* **show():** Displays the window on the screen.
* **exec_():** Starts the event loop, which handles user interactions (e.g., mouse clicks, keyboard input).

**5. Exploring PyQt**

* **Layouts:** Use layouts (e.g., `QHBoxLayout`, `QVBoxLayout`, `GridLayout`) to arrange widgets within your application.
* **Widgets:** Explore other PyQt widgets like buttons (`QPushButton`), text boxes (`QLineEdit`), and more.
* **Signals and Slots:** Connect signals (events emitted by widgets) to slots (functions that are executed in response to signals).
* **Styling:** Customize the appearance of your application using stylesheets.

**6. VS Code Integration**

* **Autocompletion:** VS Code's Python extension will provide autocompletion for PyQt classes, methods, and properties.
* **Debugging:** You can debug your PyQt applications within VS Code using the built-in debugger.
* **Linting:** The linter can help identify potential issues in your PyQt code.

This should give you a good starting point with PyQt. Feel free to explore the PyQt documentation and experiment with different widgets and layouts to create more complex applications.
