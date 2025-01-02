from PyQt6 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow

class MainWindowExt(QtWidgets.QMainWindow, Ui_MainWindow):  # Kế thừa từ QMainWindow và Ui_MainWindow
    def __init__(self):
        super().__init__()  # Khởi tạo QMainWindow trước
        self.setupUi(self)  # Gọi phương thức setup UI từ Ui_MainWindow
        # Gắn các sự kiện cho các nút
        self.pushButtonCheck.clicked.connect(self.check_symmetry)
        self.pushButtonContinue.clicked.connect(self.clear_input)
        self.pushButtonExit.clicked.connect(self.exit_app)

    def check_symmetry(self):
        input_string = self.lineEditString.text().strip()  # Lấy chuỗi nhập vào từ người dùng
        if self.is_symmetric(input_string):
            self.lineEditResult.setText("The string is symmetrical.")
        else:
            self.lineEditResult.setText("The string is not symmetrical.")

    def is_symmetric(self, s):
        """Kiểm tra chuỗi có đối xứng hay không"""
        return s == s[::-1]  # So sánh chuỗi với chuỗi đảo ngược của nó

    def clear_input(self):
        """Xóa chuỗi nhập vào và kết quả"""
        self.lineEditString.clear()
        self.lineEditResult.clear()

    def exit_app(self):
        """Thoát ứng dụng"""
        QtWidgets.QApplication.quit()
