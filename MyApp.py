import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from MainWindowExt import MainWindowExt

def main():
    app = QApplication(sys.argv)
    window = MainWindowExt()  # Khởi tạo cửa sổ chính
    window.show()  # Hiển thị cửa sổ
    sys.exit(app.exec())  # Chạy vòng lặp sự kiện của ứng dụng

if __name__ == "__main__":
    main()
