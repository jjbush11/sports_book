import login, homepage, mybets
import sys
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = login.StartWindow()
    window.showFullScreen()  # Show the window in fullscreen mode
    sys.exit(app.exec())
