from os.path import abspath, dirname, join
import sys

# Lấy đường dẫn của thư mục chứa file hiện tại
current_dir = dirname(abspath(__file__))

# Thêm đường dẫn của thư mục Control vào sys.path
sys.path.insert(0, join(current_dir, 'Control'))
#Chèn đường dẫn để import các file mã hóa trong folder control
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QLabel,QLineEdit, QDialog
from PyQt6.uic import ui_file
from PyQt6.QtGui import QFontMetrics, QFont
from PyQt6.QtCore import pyqtSignal
from View.loginDialog import Ui_Dialog as Ui_Login

#import các class
from View.Control.mahoaceasar_class import CCeasar
from View.Control.mahoavignere_class import CVignere
from View.Control.mahoatrithemius_class import CTrithemius
from View.Control.mahoabelasco_class import CBelasco
from View.Control.mahoachuyenvihaidong_class import CChuyenViHaiDong
from View.Control.mahoachuyenvinhieudong_class import CChuyenViNhieuDong
from View.Control.mahoaXorCeasar_class import CXORCeasar
from View.Control.mahoaXorvignere_class import CXORVignere
from View.Control.mahoaXortrithemius_class import CXORTrithemius
from View.Control.mahoaXorbelasco_class import CXORBelasco
from View.Control.mahoaAES_class import CAES
import View.Control.mahoaRSA
import View.Control.mahoaSDES
import View.Control.mahoamd5
import View.Control.mahoasha3
import View.Control.mahoasha256


# Import Ui_MainWindow from the generated file
from View.ThietKeManHinhChinh import Ui_MainWindow
class MyMainWindow(QMainWindow):
    data_signal = pyqtSignal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        font = QFont("Arial", 12)

        # Load the UI from Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Chỉnh sửa chữ và font của QMessageBox
        self.login_dialog = Ui_Login()
        self.login_dialog.setupUi(ui.login_dialog)
        # Khai báo nút trên main window
        self.ui.MHThayThe_btn_0.clicked.connect(self.Ceasar_Enc)
        self.ui.MHChuyenVi_btn_0.clicked.connect(self.Hai_Dong_Enc)
        self.ui.MHXOR_btn_0.clicked.connect(self.XOR_Ceasar_Enc)
        self.ui.MHHienDai_btn_0.clicked.connect(self.AES_Enc)
        self.ui.MHMotChieu_btn_0.clicked.connect(self.SHA3_Enc)
        self.ui.GMThayThe_btn_0.clicked.connect(self.Ceasar_Dec)
        self.ui.GMChuyenVi_btn_0.clicked.connect(self.Hai_Dong_Dec)
        self.ui.GMXOR_btn_0.clicked.connect(self.XOR_Ceasar_Dec)
        self.ui.GMHienDai_btn_0.clicked.connect(self.AES_Dec)
        
        #Dialog
    def DangNhap(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.GiaoDienLoginDialog)
        # Trang Đăng nhập
        # Khai báo một biến để theo dõi trạng thái của mật khẩu
        self.password_visible = False
        # Khi nút Đăng nhập được nhấn, kiểm tra tên đăng nhập và mật khẩu
       # Kết nối nút từ dialog với các hàm xử lý
        self.login_dialog.loginButton.clicked.connect(self.check_login)
        self.login_dialog.showPasswordButton.clicked.connect(self.toggle_password_visibility)

    def toggle_password_visibility(self):
        if self.password_visible:
            self.login_dialog.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)
            self.password_visible = False
        else:
            self.login_dialog.passwordInput.setEchoMode(QLineEdit.EchoMode.Normal)
            self.password_visible = True

    def check_Account(self,us,ps):
        with open("D:\\DeTaiBaoMat\\Data\\account.txt", "r", encoding='utf-8') as file:
            for line in file:
                if line.strip() == us+","+ps:
                    return True
            return False
    def send_data_to_main_window(self):
        
        data = "ok"
        self.data_signal.emit(data)
        
    def check_login(self):
        username = self.login_dialog.usernameInput.text()
        us = View.Control.mahoasha3.MaHoaSha3(username) 
        password = self.login_dialog.passwordInput.text()
        ps = View.Control.mahoasha3.MaHoaSha3(password)
        if self.check_Account(us,ps):
            self.send_data_to_main_window()
            self.close()
        else:
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Icon.Information)  # Loại biểu tượng (Information)
            message_box.setWindowTitle('Thông báo')  # Tiêu đề
            message_box.setText('Bạn nhập sai username và password.')  # Nội dung thông báo
            message_box.setStandardButtons(QMessageBox.StandardButton.Ok)  # Các nút (OK)
            result = message_box.exec()  # Hiển thị hộp thoại và chờ đợi phản hồi từ người dùng
            self.login_dialog.usernameInput.setFocus()

    #=====================================================================================================================
        #Màn hình chính
    def ManHinhChinh(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Main)
        
    #=====================================================================================================================
        #Màn hình Mã hóa phương pháp thay thế
            #Màn hình Ceasar
    def Ceasar_Enc(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Ceasar_Enc)
                #Button trong Ceasar
        self.ui.btnClose_1.clicked.connect(self.ManHinhChinh)
        self.ui.MH_Vignere_btn_1.clicked.connect(self.Vignere_Enc)
        self.ui.MH_Trithemius_btn_1.clicked.connect(self.Trithemius_Enc)
        self.ui.MH_Belasco_btn_1.clicked.connect(self.Belasco_Enc)

        self.ui.MHChuyenVi_btn_1.clicked.connect(self.Hai_Dong_Enc)
        self.ui.MHXOR_btn_1.clicked.connect(self.XOR_Ceasar_Enc)
        self.ui.MHHienDai_btn_1.clicked.connect(self.AES_Enc)
        self.ui.MHMotChieu_btn_1.clicked.connect(self.SHA3_Enc)
        font = QFont("Arial", 12)
        #Chức năng
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.ui.btnMaHoa_1.clicked.connect(self.MaHoa_Ceasar_Enc)
        self.ui.btnOpenFile_1.clicked.connect(self.MoFile_Ceasar_Enc)
        self.ui.btnSaveFile_1.clicked.connect(self.GhiFile_Ceasar_Enc)
    def MaHoa_Ceasar_Enc(self):
        self.textk = self.ui.txtKey_1.toPlainText() #lấy dữ liệu trong text key của ThietKeMaHoaCeasar
        if not self.textk:
            self.show_custom_message( "Thông báo", "Bạn chưa nhập key!!!!")
            self.ui.txtKey_1.setFocus()
        else:
            textpl = self.ui.txtPlaintext_1.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaCeasar
            if not textpl:
                self.show_custom_message( "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.ui.btnOpenFile_1.setFocus()
            else:
                cCeasar= CCeasar(textpl,int(self.textk)) #khai báo đối tượng của lớp CCeasar
                c = cCeasar.MaHoa() #gọi hàm mã hoá của đối tượng này
                self.ui.txtCiphertext_1.setPlainText(c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaCeasar
    def MoFile_Ceasar_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.ui.txtPlaintext_1.setPlainText(fileContent)
    def GhiFile_Ceasar_Enc(self):
        # Lưu file dữ liệu đã mã hoá ciphertext
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Mã hoá", "",
                                                "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtCiphertext_1.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file mã hoá thành công!!!!")

        # Lưu file KEY
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File KEY", "",
                                                "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtKey_1.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file KEY thành công!!!!")
       #=========================================    
            #Màn hình Vignere
    def Vignere_Enc(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Vignere_Enc)
                #Button trong Vignere
        self.ui.btnClose_2.clicked.connect(self.ManHinhChinh)
        self.ui.MH_Ceasar_btn_2.clicked.connect(self.Ceasar_Enc)
        self.ui.MH_Trithemius_btn_2.clicked.connect(self.Trithemius_Enc)
        self.ui.MH_Belasco_btn_2.clicked.connect(self.Belasco_Enc)

        self.ui.MHChuyenVi_btn_2.clicked.connect(self.Hai_Dong_Enc)
        self.ui.MHXOR_btn_2.clicked.connect(self.XOR_Ceasar_Enc)
        self.ui.MHHienDai_btn_2.clicked.connect(self.AES_Enc)
        self.ui.MHMotChieu_btn_2.clicked.connect(self.SHA3_Enc)
        font = QFont("Arial", 12)
                #Chức năng
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.c = ''
        self.ui.btnMaHoa_2.clicked.connect(self.MaHoa_Vignere_Enc)
        self.ui.btnOpenFile_2.clicked.connect(self.MoFile_Vignere_Enc)
        self.ui.btnSaveFile_2.clicked.connect(self.GhiFile_Vignere_Enc)

    def MaHoa_Vignere_Enc(self):
        self.textk = self.ui.txtKey_2.toPlainText() #lấy dữ liệu trong text key của ThietKeMaHoaVignere
        if not self.textk:
            self.show_custom_message("Thông báo", "Bạn chưa nhập key!!!!")
            self.ui.txtKey_2.setFocus()
        else:
            textpl = self.ui.txtPlaintext_2.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaVignere
            if not textpl:
                self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.ui.btnOpenFile_2.setFocus()
            else:
                cVignere= CVignere(textpl,self.textk) #khai báo đối tượng của lớp CVignere
                self.c = cVignere.MaHoa() #gọi hàm mã hoá của đối tượng này
                self.ui.txtCiphertext_2.setPlainText(self.c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_Vignere_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.ui.txtPlaintext_2.setPlainText(fileContent)
    def GhiFile_Vignere_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtCiphertext_2.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file mã hoá thành công!!!!")
                    
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtKey_2.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file KEY thành công!!!!")
        #=========================================    
            #Màn hình Trithemius
    def Trithemius_Enc(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Trithemius_Enc)
                #Button trong Trithemius
        self.ui.btnClose_3.clicked.connect(self.ManHinhChinh)
        self.ui.MH_Ceasar_btn_3.clicked.connect(self.Ceasar_Enc)
        self.ui.MH_Vignere_btn_3.clicked.connect(self.Vignere_Enc)
        self.ui.MH_Belasco_btn_3.clicked.connect(self.Belasco_Enc)

        self.ui.MHChuyenVi_btn_3.clicked.connect(self.Hai_Dong_Enc)
        self.ui.MHXOR_btn_3.clicked.connect(self.XOR_Ceasar_Enc)
        self.ui.MHHienDai_btn_3.clicked.connect(self.AES_Enc)
        self.ui.MHMotChieu_btn_3.clicked.connect(self.SHA3_Enc)
        font = QFont("Arial", 12)
                #Chức năng
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.c = ''
        self.ui.btnMaHoa_3.clicked.connect(self.MaHoa_Trithemius_Enc)
        self.ui.btnOpenFile_3.clicked.connect(self.MoFile_Trithemius_Enc)
        self.ui.btnSaveFile_3.clicked.connect(self.GhiFile_Trithemius_Enc)
    def MaHoa_Trithemius_Enc(self):
        textpl = self.ui.txtPlaintext_3.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaVignere
        if not textpl:
            self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.ui.btnOpenFile_3.setFocus()
        else:
            cTrithemius= CTrithemius(textpl) #khai báo đối tượng của lớp CVignere
            self.c = cTrithemius.MaHoa() #gọi hàm mã hoá của đối tượng này
            self.ui.txtCiphertext_3.setPlainText(self.c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_Trithemius_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.ui.txtPlaintext_3.setPlainText(fileContent)
    def GhiFile_Trithemius_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtCiphertext_3.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file mã hoá thành công!!!!")

        #=========================================    
            #Màn hình Belasco
    def Belasco_Enc(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Belasco_Enc)
                #Button trong Belasco
        self.ui.btnClose_4.clicked.connect(self.ManHinhChinh)
        self.ui.MH_Ceasar_btn_4.clicked.connect(self.Ceasar_Enc)
        self.ui.MH_Vignere_btn_4.clicked.connect(self.Vignere_Enc)
        self.ui.MH_Trithemius_btn_4.clicked.connect(self.Trithemius_Enc)

        self.ui.MHChuyenVi_btn_4.clicked.connect(self.Hai_Dong_Enc)
        self.ui.MHXOR_btn_4.clicked.connect(self.XOR_Ceasar_Enc)
        self.ui.MHHienDai_btn_4.clicked.connect(self.AES_Enc)
        self.ui.MHMotChieu_btn_4.clicked.connect(self.SHA3_Enc)
                
                #Chức năng
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.c = ''
        self.ui.btnMaHoa_4.clicked.connect(self.MaHoa_Belasco_Enc)
        self.ui.btnOpenFile_4.clicked.connect(self.MoFile_Belasco_Enc)
        self.ui.btnSaveFile_4.clicked.connect(self.GhiFile_Belasco_Enc)
    def MaHoa_Belasco_Enc(self):
        self.textk = self.ui.txtKey_4.toPlainText() #lấy dữ liệu trong text key của ThietKeMaHoaBelasco
        if not self.textk:
            self.show_custom_message("Thông báo", "Bạn chưa nhập key!!!!")
            self.ui.txtKey_4.setFocus()
        else:
            textpl = self.ui.txtPlaintext_4.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaBelasco
            if not textpl:
                self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.ui.btnOpenFile_4.setFocus()
            else:
                cBelasco= CBelasco(textpl,self.textk) #khai báo đối tượng của lớp CBelasco
                self.c = cBelasco.MaHoa() #gọi hàm mã hoá của đối tượng này
                self.ui.txtCiphertext_4.setPlainText(self.c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaBelasco
    def MoFile_Belasco_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.ui.txtPlaintext_4.setPlainText(fileContent)
    def GhiFile_Belasco_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtCiphertext_4.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file mã hoá thành công!!!!")
                
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtKey_4.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file KEY thành công!!!!")
    #=====================================================================================================================
        #Màn hình Mã hóa phương pháp chuyển vị
            #Màn hình chuyển vị hai dòng
    def Hai_Dong_Enc(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Hai_Dong_Enc)

                #Button trong Hai Dòng
        self.ui.btnClose_5.clicked.connect(self.ManHinhChinh)
        self.ui.MH_NhieuDong_btn_5.clicked.connect(self.Nhieu_Dong_Enc)

        self.ui.MHThayThe_btn_5.clicked.connect(self.Ceasar_Enc)
        self.ui.MHXOR_btn_5.clicked.connect(self.XOR_Ceasar_Enc)
        self.ui.MHHienDai_btn_5.clicked.connect(self.AES_Enc)
        self.ui.MHMotChieu_btn_5.clicked.connect(self.SHA3_Enc)

                #Chức năng
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.c = ''
        self.ui.btnMaHoa_5.clicked.connect(self.MaHoa_HaiDong_Enc)
        self.ui.btnOpenFile_5.clicked.connect(self.MoFile_HaiDong_Enc)
        self.ui.btnSaveFile_5.clicked.connect(self.GhiFile_HaiDong_Enc)
    def MaHoa_HaiDong_Enc(self):
        textpl = self.ui.txtPlaintext_5.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaVignere
        if not textpl:
            self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.ui.btnOpenFile_5.setFocus()
        else:
            cHaiDong= CChuyenViHaiDong(textpl) #khai báo đối tượng của lớp CVignere
            self.c = cHaiDong.MaHoa() #gọi hàm mã hoá của đối tượng này
            self.ui.txtCiphertext_5.setPlainText(self.c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_HaiDong_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.ui.txtPlaintext_5.setPlainText(fileContent)
    def GhiFile_HaiDong_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.c)
            self.show_custom_message("Thông báo", "Lưu file mã hoá thành công!!!!")

        #=========================================    
            #Màn hình chuyển vị nhiều dòng
    def Nhieu_Dong_Enc(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Nhieu_Dong_Enc)
                #Button
        self.ui.btnClose_6.clicked.connect(self.ManHinhChinh)
        self.ui.MH_HaiDong_btn_6.clicked.connect(self.Hai_Dong_Enc)

        self.ui.MHThayThe_btn_6.clicked.connect(self.Ceasar_Enc)
        self.ui.MHXOR_btn_6.clicked.connect(self.XOR_Ceasar_Enc)
        self.ui.MHHienDai_btn_6.clicked.connect(self.AES_Enc)
        self.ui.MHMotChieu_btn_6.clicked.connect(self.SHA3_Enc)

                #Chức năng
        # Thêm xử lý sự kiện và tuỳ chỉnh giao diện người dùng tại đây
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.k=[]
        self.ui.btnMaHoa_6.clicked.connect(self.MaHoa_NhieuDong_Enc)
        self.ui.btnOpenFile_6.clicked.connect(self.MoFile_NhieuDong_Enc)
        self.ui.btnSaveFile_6.clicked.connect(self.GhiFile_NhieuDong_Enc)
    def MaHoa_NhieuDong_Enc(self):
        self.textk = self.ui.txtKey_6.toPlainText() #lấy dữ liệu trong text key của ThietKeMaHoaNhieuDong
        if not self.textk:
            self.show_custom_message("Thông báo", "Bạn chưa nhập key!!!!")
            self.ui.txtKey_6.setFocus()
        else:
            textpl = self.ui.txtPlaintext_6.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaNhieuDong
            if not textpl:
                self.show_custom_message( "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.ui.btnOpenFile_6.setFocus()
            else:
                cChuyenViNhieuDong= CChuyenViNhieuDong(textpl) #khai báo đối tượng của lớp CNhieuDong
                n = int(self.textk)
                self.k = cChuyenViNhieuDong.CreateKey(n)
                cChuyenViNhieuDong.SetKey(self.k)
                c = cChuyenViNhieuDong.MaHoa() #gọi hàm mã hoá của đối tượng này
                self.ui.txtCiphertext_6.setPlainText(c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaNhieuDong
    def MoFile_NhieuDong_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.ui.txtPlaintext_6.setPlainText(fileContent)
    def GhiFile_NhieuDong_Enc(self):
        # Lưu file dữ liệu đã mã hoá ciphertext
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtCiphertext_6.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file mã hoá thành công!!!!")

        # Lưu file KEY
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                s = ''
                for item in self.k:
                    s += str(item) + " "
                s = s.rstrip()  # Loại bỏ dấu cách cuối cùng
                print(s)
                file.write(s)
            self.show_custom_message("Thông báo", "Lưu file KEY thành công!!!!")
    #=====================================================================================================================
        #Màn hình Mã hóa phương pháp XOR
            #Màn hình XOR Ceasar
    def XOR_Ceasar_Enc(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.XOR_Ceasar_Enc)
                #Button trong XOR_Ceasar_Enc
        self.ui.btnClose_7.clicked.connect(self.ManHinhChinh)
        self.ui.MH_Vignere_btn_7.clicked.connect(self.XOR_Vignere_Enc)
        self.ui.MH_Trithemius_btn_7.clicked.connect(self.XOR_Trithemius_Enc)
        self.ui.MH_Belasco_btn_7.clicked.connect(self.XOR_Belasco_Enc)

        self.ui.MHThayThe_btn_7.clicked.connect(self.Ceasar_Enc)
        self.ui.MHChuyenVi_btn_7.clicked.connect(self.Hai_Dong_Enc)
        self.ui.MHHienDai_btn_7.clicked.connect(self.AES_Enc)
        self.ui.MHMotChieu_btn_7.clicked.connect(self.SHA3_Enc)

                #Chức năng
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.ui.btnMaHoa_7.clicked.connect(self.MaHoa_XOR_Ceasar_Enc)
        self.ui.btnOpenFile_7.clicked.connect(self.MoFile_XOR_Ceasar_Enc)
        self.ui.btnSaveFile_7.clicked.connect(self.GhiFile_XOR_Ceasar_Enc)

    def MaHoa_XOR_Ceasar_Enc(self):
        self.textk = self.ui.txtKey_7.toPlainText() #lấy dữ liệu trong text key của ThietKeMaHoaCeasar
        if not self.textk:
            self.show_custom_message("Thông báo", "Bạn chưa nhập key!!!!")
            self.ui.txtKey_7.setFocus()
        else:
            textpl = self.ui.txtPlaintext_7.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaCeasar
            if not textpl:
                self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.ui.btnOpenFile_7.setFocus()
            else:
                cXORCeasar= CXORCeasar() #khai báo đối tượng của lớp CCeasar
                c = cXORCeasar.MaHoa(textpl,int(self.textk)) #gọi hàm mã hoá của đối tượng này
                self.ui.txtCiphertext_7.setPlainText(c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaCeasar
    def MoFile_XOR_Ceasar_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.ui.txtPlaintext_7.setPlainText(fileContent)
    def GhiFile_XOR_Ceasar_Enc(self):
        # Lưu file dữ liệu đã mã hoá ciphertext
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtCiphertext_7.toPlainText())
            self.show_custom_message( "Thông báo", "Lưu file mã hoá thành công!!!!")

        # Lưu file KEY
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtKey_7.toPlainText())
            self.show_custom_message( "Thông báo", "Lưu file KEY thành công!!!!")
        #=========================================    
            #Màn hình XOR Vignere
    def XOR_Vignere_Enc(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.XOR_Vignere_Enc)
                #Button trong XOR_Vignere_Enc
        self.ui.btnClose_8.clicked.connect(self.ManHinhChinh)
        self.ui.MH_Ceasar_btn_8.clicked.connect(self.XOR_Ceasar_Enc)
        self.ui.MH_Trithemius_btn_8.clicked.connect(self.XOR_Trithemius_Enc)
        self.ui.MH_Belasco_btn_8.clicked.connect(self.XOR_Belasco_Enc)

        self.ui.MHThayThe_btn_8.clicked.connect(self.Ceasar_Enc)
        self.ui.MHChuyenVi_btn_8.clicked.connect(self.Hai_Dong_Enc)
        self.ui.MHHienDai_btn_8.clicked.connect(self.AES_Enc)
        self.ui.MHMotChieu_btn_8.clicked.connect(self.SHA3_Enc)

        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.c = ''
        self.p = ''
        self.ui.btnMaHoa_8.clicked.connect(self.MaHoa_XOR_Vignere_Enc)
        self.ui.btnOpenFile_8.clicked.connect(self.MoFile_XOR_Vignere_Enc)
        self.ui.btnSaveFile_8.clicked.connect(self.GhiFile_XOR_Vignere_Enc)
    def MaHoa_XOR_Vignere_Enc(self):
        self.textk = self.ui.txtKey_8.toPlainText() #lấy dữ liệu trong text key của ThietKeMaHoaVignere
        if not self.textk:
            self.show_custom_message("Thông báo", "Bạn chưa nhập key!!!!")
            self.ui.txtKey_8.setFocus()
        else:
            textpl = self.ui.txtPlaintext_8.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaVignere
            if not textpl:
                self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.ui.btnOpenFile_8.setFocus()
            else:
                cVignere= CXORVignere() #khai báo đối tượng của lớp CVignere
                self.c = cVignere.MaHoa(self.p,self.textk) #gọi hàm mã hoá của đối tượng này
                self.ui.txtCiphertext_8.setPlainText(self.c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_XOR_Vignere_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.p = file.read()
                self.ui.txtPlaintext_8.setPlainText(self.p)
    def GhiFile_XOR_Vignere_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtCiphertext_8.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file mã hoá thành công!!!!")
                
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtKey_8.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file KEY thành công!!!!")
        #=========================================    
            #Màn hình XOR Trithemius
    def XOR_Trithemius_Enc(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.XOR_Trithemius_Enc)
        self.ui.btnClose_9.clicked.connect(self.ManHinhChinh)
        self.ui.MH_Ceasar_btn_9.clicked.connect(self.XOR_Ceasar_Enc)
        self.ui.MH_Vignere_btn_9.clicked.connect(self.XOR_Vignere_Enc)
        self.ui.MH_Belasco_btn_9.clicked.connect(self.XOR_Belasco_Enc)

        self.ui.MHThayThe_btn_9.clicked.connect(self.Ceasar_Enc)
        self.ui.MHChuyenVi_btn_9.clicked.connect(self.Hai_Dong_Enc)
        self.ui.MHHienDai_btn_9.clicked.connect(self.AES_Enc)
        self.ui.MHMotChieu_btn_9.clicked.connect(self.SHA3_Enc)

                #Chức năng
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.c = ''
        self.ui.btnMaHoa_9.clicked.connect(self.MaHoa_XOR_Trithemius_Enc)
        self.ui.btnOpenFile_9.clicked.connect(self.MoFile_XOR_Trithemius_Enc)
        self.ui.btnSaveFile_9.clicked.connect(self.GhiFile_XOR_Trithemius_Enc)
    def MaHoa_XOR_Trithemius_Enc(self):
        textpl = self.ui.txtPlaintext_9.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaVignere
        if not textpl:
            self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.ui.btnOpenFile_9.setFocus()
        else:
            cTrithemius= CXORTrithemius() #khai báo đối tượng của lớp CVignere
            self.c = cTrithemius.MaHoa(textpl) #gọi hàm mã hoá của đối tượng này
            self.ui.txtCiphertext_9.setPlainText(self.c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_XOR_Trithemius_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.ui.txtPlaintext_9.setPlainText(fileContent)
    def GhiFile_XOR_Trithemius_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtCiphertext_9.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file mã hoá thành công!!!!")
        #=========================================
            #Màn hình XOR Belasco
    def XOR_Belasco_Enc(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.XOR_Belasco_Enc)
        self.ui.btnClose_10.clicked.connect(self.ManHinhChinh)
        self.ui.MH_Ceasar_btn_10.clicked.connect(self.XOR_Ceasar_Enc)
        self.ui.MH_Vignere_btn_10.clicked.connect(self.XOR_Vignere_Enc)
        self.ui.MH_Trithemius_btn_10.clicked.connect(self.XOR_Trithemius_Enc)

        self.ui.MHThayThe_btn_10.clicked.connect(self.Ceasar_Enc)
        self.ui.MHChuyenVi_btn_10.clicked.connect(self.Hai_Dong_Enc)
        self.ui.MHHienDai_btn_10.clicked.connect(self.AES_Enc)
        self.ui.MHMotChieu_btn_10.clicked.connect(self.SHA3_Enc)

        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.c = ''
        self.ui.btnMaHoa_10.clicked.connect(self.MaHoa_XOR_Belasco_Enc)
        self.ui.btnOpenFile_10.clicked.connect(self.MoFile_XOR_Belasco_Enc)
        self.ui.btnSaveFile_10.clicked.connect(self.GhiFile_XOR_Belasco_Enc)
    def MaHoa_XOR_Belasco_Enc(self):
        self.textk = self.ui.txtKey_10.toPlainText() #lấy dữ liệu trong text key của ThietKeMaHoaBelasco
        if not self.textk:
            self.show_custom_message("Thông báo", "Bạn chưa nhập key!!!!")
            self.ui.txtKey_10.setFocus()
        else:
            textpl = self.ui.txtPlaintext_10.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaBelasco
            if not textpl:
                self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.ui.btnOpenFile_10.setFocus()
            else:
                cBelasco= CXORBelasco() #khai báo đối tượng của lớp CBelasco
                self.c = cBelasco.MaHoa(textpl,self.textk) #gọi hàm mã hoá của đối tượng này
                self.ui.txtCiphertext_10.setPlainText(self.c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaBelasco
    def MoFile_XOR_Belasco_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.ui.txtPlaintext_10.setPlainText(fileContent)
    def GhiFile_XOR_Belasco_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtCiphertext_10.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file mã hoá thành công!!!!")
                
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtKey_10.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file KEY thành công!!!!")
    #=====================================================================================================================
        #Màn hình Mã hóa phương pháp hiện đại
            #Màn hình hiện đại AES
    def AES_Enc(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.AES_Enc)
        self.ui.btnClose_11.clicked.connect(self.ManHinhChinh)
        self.ui.MH_RSA_btn_11.clicked.connect(self.RSA_Enc)
        self.ui.MH_SDES_btn_11.clicked.connect(self.SDES_Enc)

        self.ui.MHThayThe_btn_11.clicked.connect(self.Ceasar_Enc)
        self.ui.MHChuyenVi_btn_11.clicked.connect(self.Hai_Dong_Enc)
        self.ui.MHXOR_btn_11.clicked.connect(self.XOR_Ceasar_Enc)
        self.ui.MHMotChieu_btn_11.clicked.connect(self.SHA3_Enc)

            #Chức năng
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.c = ''
        self.p = ''
        self.ui.btnMaHoa_11.clicked.connect(self.MaHoa_AES_Enc)
        self.ui.btnOpenFile_11.clicked.connect(self.MoFile_AES_Enc)
        self.ui.btnSaveFile_11.clicked.connect(self.GhiFile_AES_Enc)
    def MaHoa_AES_Enc(self):
        textpl = self.ui.txtPlaintext_11.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaVignere
        if not textpl:
            self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.ui.btnOpenFile_11.setFocus()
        else:
            cAES = CAES()
            self.c, self.textk = cAES.MaHoa(self.p) #gọi hàm mã hoá của đối tượng này
            self.ui.txtCiphertext_11.setPlainText(self.c.decode('utf-8')) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_AES_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.p = file.read()
                self.ui.txtPlaintext_11.setPlainText(self.p)
    def GhiFile_AES_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'wb') as file:
                file.write(self.c)
            self.show_custom_message("Thông báo","Lưu file mã hoá thành công")
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'wb') as file:
                file.write(self.textk)
            self.show_custom_message("Thông Báo","Lưu file Key thành công")
        #=========================================    
            #Màn hình hiện đại RSA
    def RSA_Enc(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.RSA_Enc)
        self.ui.btnClose_12.clicked.connect(self.ManHinhChinh)
        self.ui.MH_AES_btn_12.clicked.connect(self.AES_Enc)
        self.ui.MH_SDES_btn_12.clicked.connect(self.SDES_Enc)

        self.ui.MHThayThe_btn_12.clicked.connect(self.Ceasar_Enc)
        self.ui.MHChuyenVi_btn_12.clicked.connect(self.Hai_Dong_Enc)
        self.ui.MHXOR_btn_12.clicked.connect(self.XOR_Ceasar_Enc)
        self.ui.MHMotChieu_btn_12.clicked.connect(self.SHA3_Enc)

            #Chức năng
        self.c = []
        self.s = ''
        self.ui.btnMaHoa_12.clicked.connect(self.MaHoa_RSA_Enc)
        self.ui.btnOpenFile_12.clicked.connect(self.MoFile_RSA_Enc)
        self.ui.btnSaveFile_12.clicked.connect(self.GhiFile_RSA_Enc)
    def MaHoa_RSA_Enc(self):
        textpl = self.ui.txtPlaintext_12.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaVignere
        if not textpl:
           self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
           self.ui.btnOpenFile_12.setFocus()
        else:
            e=65537
            n=4255903
            self.c = View.Control.mahoaRSA.MaHoa(textpl,e,n) #gọi hàm mã hoá của đối tượng này
            #print(self.c)
            self.s = ''
            for i in self.c:
                self.s += str(i)+' '
            #print(self.s)
            self.ui.txtCiphertext_12.setPlainText(self.s)
    def MoFile_RSA_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.ui.txtPlaintext_12.setPlainText(fileContent)
    def GhiFile_RSA_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w') as file:
                file.write(self.ui.txtCiphertext_12.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file mã hoá thành công!!!!")
                #for i in self.c:
                    #file.write("%d " % i)
         #=========================================    
            #Màn hình hiện đại SDES
    def SDES_Enc(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.SDES_Enc)
        self.ui.btnClose_13.clicked.connect(self.ManHinhChinh)
        self.ui.MH_AES_btn_13.clicked.connect(self.AES_Enc)
        self.ui.MH_RSA_btn_13.clicked.connect(self.RSA_Enc)

        self.ui.MHThayThe_btn_13.clicked.connect(self.Ceasar_Enc)
        self.ui.MHChuyenVi_btn_13.clicked.connect(self.Hai_Dong_Enc)
        self.ui.MHXOR_btn_13.clicked.connect(self.XOR_Ceasar_Enc)
        self.ui.MHMotChieu_btn_13.clicked.connect(self.SHA3_Enc)

            #Chức năng
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.c = ''
        self.ui.btnMaHoa_13.clicked.connect(self.MaHoa_SDES_Enc)
        self.ui.btnOpenFile_13.clicked.connect(self.MoFile_SDES_Enc)
        self.ui.btnSaveFile_13.clicked.connect(self.GhiFile_SDES_Enc)
    def MaHoa_SDES_Enc(self):
        self.textk = self.ui.txtKey_13.toPlainText() #lấy dữ liệu trong text key của ThietKeMaHoaVignere
        if not self.textk:
            self.show_custom_message("Thông báo", "Bạn chưa nhập key!!!!")
            self.ui.txtKey_13.setFocus()
        else:
            textpl = self.ui.txtPlaintext_13.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaVignere
            if not textpl:
                self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.ui.btnOpenFile_13.setFocus()
            else:
                self.c = View.Control.mahoaSDES.MaHoa(textpl,self.textk) #gọi hàm mã hoá của đối tượng này
                self.ui.txtCiphertext_13.setPlainText(self.c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_SDES_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.ui.txtPlaintext_13.setPlainText(fileContent)
    def GhiFile_SDES_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtCiphertext_13.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file mã hoá thành công!!!!")
                
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtKey_13.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file KEY thành công!!!!")

    #=====================================================================================================================
        #Màn hình Mã hóa phương pháp một chiều
            #Màn hình một chiều SHA3
    def SHA3_Enc(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.SHA3_Enc)
        self.ui.btnClose_14.clicked.connect(self.ManHinhChinh)
        self.ui.MH_SHA256_btn_14.clicked.connect(self.SHA256_Enc)
        self.ui.MH_MD5_btn_14.clicked.connect(self.MD5_Enc)

        self.ui.MHThayThe_btn_14.clicked.connect(self.Ceasar_Enc)
        self.ui.MHChuyenVi_btn_14.clicked.connect(self.Hai_Dong_Enc)
        self.ui.MHXOR_btn_14.clicked.connect(self.XOR_Ceasar_Enc)
        self.ui.MHHienDai_btn_14.clicked.connect(self.AES_Enc)

        self.ui.btnMaHoa_14.clicked.connect(self.MaHoa_SHA3_Enc)
        self.ui.btnOpenFile_14.clicked.connect(self.MoFile_SHA3_Enc)
        self.ui.btnSaveFile_14.clicked.connect(self.GhiFile_SHA3_Enc)
    def MaHoa_SHA3_Enc(self):
        textpl = self.ui.txtPlaintext_14.toPlainText()
        if not textpl:
            self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.ui.btnOpenFile_14.setFocus()
        else:
            c = View.Control.mahoasha3.MaHoaSha3(textpl) 
            self.ui.txtCiphertext_14.setPlainText(c) 

    def MoFile_SHA3_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")                                                 
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.ui.txtPlaintext_14.setPlainText(fileContent)
    def GhiFile_SHA3_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtCiphertext_14.toPlainText())
         #=========================================    
        #Màn hình Mã hóa phương pháp một chiều
            #Màn hình một chiều SHA256
    def SHA256_Enc(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.SHA256_Enc)
        self.ui.btnClose_15.clicked.connect(self.ManHinhChinh)
        self.ui.MH_SHA3_btn_15.clicked.connect(self.SHA3_Enc)
        self.ui.MH_MD5_btn_15.clicked.connect(self.MD5_Enc)

        self.ui.MHThayThe_btn_15.clicked.connect(self.Ceasar_Enc)
        self.ui.MHChuyenVi_btn_15.clicked.connect(self.Hai_Dong_Enc)
        self.ui.MHXOR_btn_15.clicked.connect(self.XOR_Ceasar_Enc)
        self.ui.MHHienDai_btn_15.clicked.connect(self.AES_Enc)

        self.ui.btnMaHoa_15.clicked.connect(self.MaHoa_SHA256_Enc)
        self.ui.btnOpenFile_15.clicked.connect(self.MoFile_SHA256_Enc)
        self.ui.btnSaveFile_15.clicked.connect(self.GhiFile_SHA256_Enc)
    def MaHoa_SHA256_Enc(self):
        textpl = self.ui.txtPlaintext_15.toPlainText()
        if not textpl:
            self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.ui.btnOpenFile_15.setFocus()
        else:
            c = View.Control.mahoasha256.MaHoaSha256(textpl) 
            self.ui.txtCiphertext_15.setPlainText(c) 

    def MoFile_SHA256_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")                                                 
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.ui.txtPlaintext_15.setPlainText(fileContent)
    def GhiFile_SHA256_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtCiphertext_15.toPlainText())
         #=========================================
        #Màn hình Mã hóa phương pháp một chiều
            #Màn hình một chiều MD5
    def MD5_Enc(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.MD5_Enc)
        self.ui.btnClose_16.clicked.connect(self.ManHinhChinh)
        self.ui.MH_SHA3_btn_16.clicked.connect(self.SHA3_Enc)
        self.ui.MH_SHA256_btn_16.clicked.connect(self.SHA256_Enc)

        self.ui.MHThayThe_btn_16.clicked.connect(self.Ceasar_Enc)
        self.ui.MHChuyenVi_btn_16.clicked.connect(self.Hai_Dong_Enc)
        self.ui.MHXOR_btn_16.clicked.connect(self.XOR_Ceasar_Enc)
        self.ui.MHHienDai_btn_16.clicked.connect(self.AES_Enc)

        self.ui.btnMaHoa_16.clicked.connect(self.MaHoa_MD5_Enc)
        self.ui.btnOpenFile_16.clicked.connect(self.MoFile_MD5_Enc)
        self.ui.btnSaveFile_16.clicked.connect(self.GhiFile_MD5_Enc)

    def MaHoa_MD5_Enc(self):
        textpl = self.ui.txtPlaintext_16.toPlainText()
        if not textpl:
            self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.ui.btnOpenFile_16.setFocus()
        else:
            c = View.Control.mahoamd5.MaHoaMD5(textpl) 
            self.ui.txtCiphertext_16.setPlainText(c)  

    def MoFile_MD5_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")                                                 
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.ui.txtPlaintext_16.setPlainText(fileContent)
    def GhiFile_MD5_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtCiphertext_16.toPlainText())


   #=====================================================================================================================
        #Màn hình Giải mã phương pháp thay thế
            #Màn hình giải mã Ceasar
    def Ceasar_Dec(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Ceasar_Dec)
        self.ui.btnClose_18.clicked.connect(self.ManHinhChinh)
        self.ui.GM_Vignere_btn_18.clicked.connect(self.Vignere_Dec)
        self.ui.GM_Trithemius_btn_18.clicked.connect(self.Trithemius_Dec)
        self.ui.GM_Belasco_btn_18.clicked.connect(self.Belasco_Dec)

        self.ui.GMChuyenVi_btn_18.clicked.connect(self.Hai_Dong_Dec)
        self.ui.GMXOR_btn_18.clicked.connect(self.XOR_Ceasar_Dec)
        self.ui.GMHienDai_btn_18.clicked.connect(self.AES_Dec)

            #Chức năng
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.ui.btnGiaiMa_18.clicked.connect(self.GiaiMa_Ceasar_Dec) #????????????????????????
        self.ui.btnOpenFile_18.clicked.connect(self.MoFile_Ceasar_Dec)
        self.ui.btnSaveFile_18.clicked.connect(self.GhiFile_Ceasar_Dec)
    def GiaiMa_Ceasar_Dec(self):
        if not self.textk:
            self.show_custom_message( "Thông báo", "Bạn chưa nhập key!!!!")
            self.ui.txtKey_18.setFocus()
        else:
            textci = self.ui.txtCiphertext_18.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaCeasar
            if not textci:
                self.show_custom_message( "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.ui.btnOpenFile_18.setFocus()
            else:
                cCeasar= CCeasar("",int(self.textk),textci) #khai báo đối tượng của lớp CCeasar
                s = cCeasar.GiaiMa() #gọi hàm mã hoá của đối tượng này
                self.ui.txtVanBanGoc_18.setPlainText(s) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaCeasar
    def MoFile_Ceasar_Dec(self):
        # Mở file đã mã hoá riêng
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                s=''
                line = file.readline()
                while line:
                    s+=line
                    line = file.readline()
                self.ui.txtCiphertext_18.setPlainText(s)
        # Mở file KEY riêng
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk = file.read()
                self.ui.txtKey_18.setPlainText(self.textk)
                
    def GhiFile_Ceasar_Dec(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtVanBanGoc_18.toPlainText())
       #=========================================    
            #Màn hình giải mã Vignere
    def Vignere_Dec(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Vignere_Dec)
        self.ui.btnClose_19.clicked.connect(self.ManHinhChinh)
        self.ui.GM_Ceasar_btn_19.clicked.connect(self.Ceasar_Dec)
        self.ui.GM_Trithemius_btn_19.clicked.connect(self.Trithemius_Dec)
        self.ui.GM_Belasco_btn_19.clicked.connect(self.Belasco_Dec)

        self.ui.GMChuyenVi_btn_19.clicked.connect(self.Hai_Dong_Dec)
        self.ui.GMXOR_btn_19.clicked.connect(self.XOR_Ceasar_Dec)
        self.ui.GMHienDai_btn_19.clicked.connect(self.AES_Dec)

        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.ui.btnGiaiMa_19.clicked.connect(self.GiaiMa_Vignere_Dec)
        self.ui.btnOpenFile_19.clicked.connect(self.MoFile_Vignere_Dec)
        self.ui.btnSaveFile_19.clicked.connect(self.GhiFile_Vignere_Dec)
    def GiaiMa_Vignere_Dec(self):
        textci = self.ui.txtCiphertext_19.toPlainText() #lấy dữ liệu trong text ciphertext của ThietKeMaHoaVignere
        if not textci:
            self.show_custom_message( "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.ui.btnOpenFile_19.setFocus()
        else:
            cVignere = CVignere("",self.textk, textci)
            c = cVignere.GiaiMa() #gọi hàm mã hoá của đối tượng này
            self.ui.txtVanBanGoc_19.setPlainText(c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_Vignere_Dec(self):
        #Mở file dữ liệu đã mã hoá
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                s=''
                line = file.readline()
                while line:
                    s+=line
                    line = file.readline()
                self.ui.txtCiphertext_19.setPlainText(s)
        #Mở file KEY
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk = file.read()
                self.ui.txtKey_19.setText(self.textk)
                
    def GhiFile_Vignere_Dec(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtVanBanGoc_19.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file giải mã thành công!!!!")
        
        #=========================================    
            #Màn hình giải mã Trithemius
    def Trithemius_Dec(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Trithemius_Dec)
        self.ui.btnClose_20.clicked.connect(self.ManHinhChinh)
        self.ui.GM_Ceasar_btn_20.clicked.connect(self.Ceasar_Dec)
        self.ui.GM_Vignere_btn_20.clicked.connect(self.Vignere_Dec)
        self.ui.GM_Belasco_btn_20.clicked.connect(self.Belasco_Dec)

        self.ui.GMChuyenVi_btn_20.clicked.connect(self.Hai_Dong_Dec)
        self.ui.GMXOR_btn_20.clicked.connect(self.XOR_Ceasar_Dec)
        self.ui.GMHienDai_btn_20.clicked.connect(self.AES_Dec)

            #Chức năng
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.ui.btnGiaiMa_20.clicked.connect(self.GiaiMa_Trithemius_Dec)
        self.ui.btnOpenFile_20.clicked.connect(self.MoFile_Trithemius_Dec)
        self.ui.btnSaveFile_20.clicked.connect(self.GhiFile_Trithemius_Dec)
    def GiaiMa_Trithemius_Dec(self):
        textci = self.ui.txtCiphertext_20.toPlainText() #lấy dữ liệu trong text ciphertext của ThietKeMaHoaVignere
        if not textci:
            self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.ui.btnOpenFile_20.setFocus()
        else:
            cTrithemius= CTrithemius("",textci) #khai báo đối tượng của lớp CVignere
            c = cTrithemius.GiaiMa() #gọi hàm mã hoá của đối tượng này
            self.ui.txtVanBanGoc_20.setPlainText(c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_Trithemius_Dec(self):
        #Mở file dữ liệu đã mã hoá
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                s=''
                line = file.readline()
                while line:
                    s+=line
                    line = file.readline()
                self.ui.txtCiphertext_20.setPlainText(s)
                
    def GhiFile_Trithemius_Dec(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtVanBanGoc_20.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file giải mã thành công!!!!")
        #=========================================    
            #Màn hình giải mã Belasco
    def Belasco_Dec(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Belasco_Dec)
        self.ui.btnClose_21.clicked.connect(self.ManHinhChinh)
        self.ui.GM_Ceasar_btn_21.clicked.connect(self.Ceasar_Dec)
        self.ui.GM_Vignere_btn_21.clicked.connect(self.Vignere_Dec)
        self.ui.GM_Trithemius_btn_21.clicked.connect(self.Trithemius_Dec)

        self.ui.GMChuyenVi_btn_21.clicked.connect(self.Hai_Dong_Dec)
        self.ui.GMXOR_btn_21.clicked.connect(self.XOR_Ceasar_Dec)
        self.ui.GMHienDai_btn_21.clicked.connect(self.AES_Dec)

            #Chức năng
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.ui.btnGiaiMa_21.clicked.connect(self.GiaiMa_Belasco_Dec)
        self.ui.btnOpenFile_21.clicked.connect(self.MoFile_Belasco_Dec)
        self.ui.btnSaveFile_21.clicked.connect(self.GhiFile_Belasco_Dec)
    def GiaiMa_Belasco_Dec(self):
        textci = self.ui.txtCiphertext_21.toPlainText() #lấy dữ liệu trong text ciphertext của ThietKeMaHoaBelasco
        if not textci:
            self.show_custom_message( "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.ui.btnOpenFile_21.setFocus()
        else:
            cBelasco= CBelasco("",self.textk,textci) #khai báo đối tượng của lớp CBelasco
            c = cBelasco.GiaiMa() #gọi hàm mã hoá của đối tượng này
            self.ui.txtVanBanGoc_21.setPlainText(c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaBelasco
    def MoFile_Belasco_Dec(self):
        #Mở file dữ liệu đã mã hoá
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                s=''
                line = file.readline()
                while line:
                    s+=line
                    line = file.readline()
                self.ui.txtCiphertext_21.setPlainText(s)
        #Mở file KEY
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk = file.read()
                self.ui.txtKey_21.setText(self.textk)
                
    def GhiFile_Belasco_Dec(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtVanBanGoc_21.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file giải mã thành công!!!!")
    #=====================================================================================================================
        #Màn hình Giải mã phương pháp Chuyển vị
            #Màn hình giải mã Hai dòng
    def Hai_Dong_Dec(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Hai_Dong_Dec)
        self.ui.btnClose_22.clicked.connect(self.ManHinhChinh)
        self.ui.GM_NhieuDong_btn_22.clicked.connect(self.Nhieu_Dong_Dec)

        self.ui.GMThayThe_btn_22.clicked.connect(self.Ceasar_Dec)
        self.ui.GMXOR_btn_22.clicked.connect(self.XOR_Ceasar_Dec)
        self.ui.GMHienDai_btn_22.clicked.connect(self.AES_Dec)

            #Chức năng
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.ui.btnGiaiMa_22.clicked.connect(self.GiaiMa_Hai_Dong_Enc)
        self.ui.btnOpenFile_22.clicked.connect(self.MoFile_Hai_Dong_Enc)
        self.ui.btnSaveFile_22.clicked.connect(self.GhiFile_Hai_Dong_Enc)
    def GiaiMa_Hai_Dong_Enc(self):
        textci = self.ui.txtCiphertext_22.toPlainText() #lấy dữ liệu trong text ciphertext của ThietKeMaHoaVignere
        if not textci:
            self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.ui.btnOpenFile_22.setFocus()
        else:
            cHaiDong= CChuyenViHaiDong("",textci) #khai báo đối tượng của lớp CVignere
            c = cHaiDong.GiaiMa() #gọi hàm mã hoá của đối tượng này
            self.ui.txtVanBanGoc_22.setPlainText(c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_Hai_Dong_Enc(self):
        #Mở file dữ liệu đã mã hoá
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                s=''
                line = file.readline()
                while line:
                    s+=line
                    line = file.readline()
                self.ui.txtCiphertext_22.setPlainText(s)
    def GhiFile_Hai_Dong_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtVanBanGoc_22.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file giải mã thành công!!!!")
        #=========================================    
        #Màn hình Giải mã phương pháp Chuyển vị
            #Màn hình giải mã nhiều dòng
    def Nhieu_Dong_Dec(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Nhieu_Dong_Dec)
        self.ui.btnClose_23.clicked.connect(self.ManHinhChinh)
        self.ui.GM_HaiDong_btn_23.clicked.connect(self.Hai_Dong_Dec)

        self.ui.GMThayThe_btn_23.clicked.connect(self.Ceasar_Dec)
        self.ui.GMXOR_btn_23.clicked.connect(self.XOR_Ceasar_Dec)
        self.ui.GMHienDai_btn_23.clicked.connect(self.AES_Dec)

            #Chức năng
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.ui.btnGiaiMa_23.clicked.connect(self.GiaiMa_Nhieu_Dong_Dec) #????????????????????????
        self.ui.btnOpenFile_23.clicked.connect(self.MoFile_Nhieu_Dong_Dec)
        self.ui.btnSaveFile_23.clicked.connect(self.GhiFile_Nhieu_Dong_Dec)
    def GiaiMa_Nhieu_Dong_Dec(self):
        if not self.textk:
            self.show_custom_message("Thông báo", "Bạn chưa nhập key!!!!")
            self.ui.txtKey_23.setFocus()
        else:
            textci = self.ui.txtCiphertext_23.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaNhieuDong
            if not textci:
                self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.ui.btnOpenFile_23.setFocus()
            else:
                cChuyenViNhieuDong= CChuyenViNhieuDong("",None,textci) #khai báo đối tượng của lớp CNhieuDong
                k = [ int(item) for item in self.textk.split(' ') ]
                cChuyenViNhieuDong.SetKey(k)
                s = cChuyenViNhieuDong.GiaiMa() #gọi hàm mã hoá của đối tượng này
                self.ui.txtVanBanGoc_23.setPlainText(s) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaNhieuDong
    def MoFile_Nhieu_Dong_Dec(self):
        # Mở file đã mã hoá riêng
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                s=''
                line = file.readline()
                while line:
                    s+=line
                    line = file.readline()
                self.ui.txtCiphertext_23.setPlainText(s)
        # Mở file KEY riêng
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk = file.read()
                self.ui.txtKey_23.setPlainText(self.textk)
                
    def GhiFile_Nhieu_Dong_Dec(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtVanBanGoc_23.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file giải mã thành công!!!!")
    #=====================================================================================================================
        #Màn hình Giải mã phương pháp XOR
            #Màn hình giải mã XOR Ceasar
    def XOR_Ceasar_Dec(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.XOR_Ceasar_Dec)
        self.ui.btnClose_24.clicked.connect(self.ManHinhChinh)
        self.ui.GM_XOR_Vignere_btn_24.clicked.connect(self.XOR_Vignere_Dec)
        self.ui.GM_XOR_Trithemius_btn_24.clicked.connect(self.XOR_Trithemius_Dec)
        self.ui.GM_XOR_Belasco_btn_24.clicked.connect(self.XOR_Belasco_Dec)

        self.ui.GMThayThe_btn_24.clicked.connect(self.Ceasar_Dec)
        self.ui.GMChuyenVi_btn_24.clicked.connect(self.Hai_Dong_Dec)
        self.ui.GMHienDai_btn_24.clicked.connect(self.AES_Dec)

            #Chức năng
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.ui.btnGiaiMa_24.clicked.connect(self.GiaiMa_XOR_Ceasar_Dec) #????????????????????????
        self.ui.btnOpenFile_24.clicked.connect(self.MoFile_XOR_Ceasar_Dec)
        self.ui.btnSaveFile_24.clicked.connect(self.GhiFile_XOR_Ceasar_Dec)
    def GiaiMa_XOR_Ceasar_Dec(self):
        if not self.textk:
            self.show_custom_message("Thông báo", "Bạn chưa nhập key!!!!")
            self.ui.txtKey_24.setFocus()
        else:
            textci = self.ui.txtCiphertext_24.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaCeasar
            if not textci:
                self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.ui.btnOpenFile_24.setFocus()
            else:
                cCeasar= CXORCeasar() #khai báo đối tượng của lớp CCeasar
                s = cCeasar.MaHoa(textci,int(self.textk)) #gọi hàm mã hoá của đối tượng này
                self.ui.txtVanBanGoc_24.setPlainText(s) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaCeasar
    def MoFile_XOR_Ceasar_Dec(self):
        # Mở file đã mã hoá riêng
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                s=''
                line = file.readline()
                while line:
                    s+=line
                    line = file.readline()
                self.ui.txtCiphertext_24.setPlainText(s)
        # Mở file KEY riêng
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk = file.read()
                self.ui.txtKey_24.setPlainText(self.textk)
                
    def GhiFile_XOR_Ceasar_Dec(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtVanBanGoc_24.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file giải mã thành công!!!!")
        #=========================================
            #Màn hình giải mã XOR Vignere
    def XOR_Vignere_Dec(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.XOR_Vignere_Dec)
        self.ui.btnClose_25.clicked.connect(self.ManHinhChinh)
        self.ui.GM_XOR_Ceasar_btn_25.clicked.connect(self.XOR_Ceasar_Dec)
        self.ui.GM_XOR_Trithemius_btn_25.clicked.connect(self.XOR_Trithemius_Dec)
        self.ui.GM_XOR_Belasco_btn_25.clicked.connect(self.XOR_Belasco_Dec)

        self.ui.GMThayThe_btn_25.clicked.connect(self.Ceasar_Dec)
        self.ui.GMChuyenVi_btn_25.clicked.connect(self.Hai_Dong_Dec)
        self.ui.GMHienDai_btn_25.clicked.connect(self.AES_Dec)

        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.ci = ''
        self.VBG = ''
        self.ui.btnGiaiMa_25.clicked.connect(self.GiaiMa_XOR_Vignere_Dec)
        self.ui.btnOpenFile_25.clicked.connect(self.MoFile_XOR_Vignere_Dec)
        self.ui.btnSaveFile_25.clicked.connect(self.GhiFile_XOR_Vignere_Dec)

    def GiaiMa_XOR_Vignere_Dec(self):
        textci = self.ui.txtCiphertext_25.toPlainText() #lấy dữ liệu trong text ciphertext của ThietKeMaHoaVignere
        if not textci:
            self.show_custom_message( "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.ui.btnOpenFile_25.setFocus()
        else:
            cVignere= CXORVignere() #khai báo đối tượng của lớp CVignere
            self.VBG = cVignere.GiaiMa(self.ci,self.textk) #gọi hàm mã hoá của đối tượng này
            self.ui.txtVanBanGoc_25.setPlainText(self.VBG) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_XOR_Vignere_Dec(self):
        #Mở file dữ liệu đã mã hoá
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.ci= file.read()
                self.ui.txtCiphertext_25.setPlainText(self.ci)
        #Mở file KEY
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk = file.read()
                self.ui.txtKey_25.setText(self.textk)
    def GhiFile_XOR_Vignere_Dec(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.VBG)
            self.show_custom_message("Thông báo", "Lưu file giải mã thành công!!!!")
        #=========================================    
            #Màn hình giải mã XOR Trithemius
    def XOR_Trithemius_Dec(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.XOR_Trithemius_Dec)
        self.ui.btnClose_26.clicked.connect(self.ManHinhChinh)
        self.ui.GM_XOR_Ceasar_btn_26.clicked.connect(self.XOR_Ceasar_Dec)
        self.ui.GM_XOR_Vignere_btn_26.clicked.connect(self.XOR_Vignere_Dec)
        self.ui.GM_XOR_Belasco_btn_26.clicked.connect(self.XOR_Belasco_Dec)

        self.ui.GMThayThe_btn_25.clicked.connect(self.Ceasar_Dec)
        self.ui.GMChuyenVi_btn_25.clicked.connect(self.Hai_Dong_Dec)
        self.ui.GMHienDai_btn_25.clicked.connect(self.AES_Dec)

            #Chức năng
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.ui.btnGiaiMa_26.clicked.connect(self.GiaiMa_XOR_Trithemius_Dec)
        self.ui.btnOpenFile_26.clicked.connect(self.MoFile_XOR_Trithemius_Dec)
        self.ui.btnSaveFile_26.clicked.connect(self.GhiFile_XOR_Trithemius_Dec)
    def GiaiMa_XOR_Trithemius_Dec(self):
        textci = self.ui.txtCiphertext_26.toPlainText() #lấy dữ liệu trong text ciphertext của ThietKeMaHoaVignere
        if not textci:
            self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.ui.btnOpenFile_26.setFocus()
        else:
            cTrithemius= CXORTrithemius() #khai báo đối tượng của lớp CVignere
            c = cTrithemius.MaHoa(textci) #gọi hàm mã hoá của đối tượng này
            self.ui.txtVanBanGoc_26.setPlainText(c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_XOR_Trithemius_Dec(self):
        #Mở file dữ liệu đã mã hoá
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                s=''
                line = file.readline()
                while line:
                    s+=line
                    line = file.readline()
                self.ui.txtCiphertext_26.setPlainText(s)
                
    def GhiFile_XOR_Trithemius_Dec(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtVanBanGoc_26.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file giải mã thành công!!!!")
        #=========================================    
            #Màn hình giải mã XOR Belasco
    def XOR_Belasco_Dec(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.XOR_Belasco_Dec)
        self.ui.btnClose_27.clicked.connect(self.ManHinhChinh)
        self.ui.GM_XOR_Ceasar_btn_27.clicked.connect(self.XOR_Ceasar_Dec)
        self.ui.GM_XOR_Vignere_btn_27.clicked.connect(self.XOR_Vignere_Dec)
        self.ui.GM_XOR_Trithemius_btn_27.clicked.connect(self.XOR_Trithemius_Dec)

        self.ui.GMThayThe_btn_27.clicked.connect(self.Ceasar_Dec)
        self.ui.GMChuyenVi_btn_27.clicked.connect(self.Hai_Dong_Dec)
        self.ui.GMHienDai_btn_27.clicked.connect(self.AES_Dec)

        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.ci = ''
        self.VBG = ''
        self.ui.btnGiaiMa_27.clicked.connect(self.GiaiMa_XOR_Belasco_Dec)
        self.ui.btnOpenFile_27.clicked.connect(self.MoFile_XOR_Belasco_Dec)
        self.ui.btnSaveFile_27.clicked.connect(self.GhiFile_XOR_Belasco_Dec)
    def GiaiMa_XOR_Belasco_Dec(self):
        textci = self.ui.txtCiphertext_27.toPlainText() #lấy dữ liệu trong text ciphertext của ThietKeMaHoaVignere
        if not textci:
            self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.ui.btnOpenFile_27.setFocus()
        else:
            cBelasco= CXORBelasco() #khai báo đối tượng của lớp CVignere
            self.VBG = cBelasco.MaHoa(self.ci,self.textk) #gọi hàm mã hoá của đối tượng này
            self.ui.txtVanBanGoc_27.setPlainText(self.VBG) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_XOR_Belasco_Dec(self):
        #Mở file dữ liệu đã mã hoá
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.ci= file.read()
                self.ui.txtCiphertext_27.setPlainText(self.ci)
        #Mở file KEY
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk = file.read()
                self.ui.txtKey_27.setText(self.textk)
                
    def GhiFile_XOR_Belasco_Dec(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.VBG)
            self.show_custom_message("Thông báo", "Lưu file giải mã thành công!!!!")
        
    #=====================================================================================================================
        #Màn hình Giải mã phương pháp hiện đại
            #Màn hình giải mã AES
    def AES_Dec(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.AES_Dec)
        self.ui.btnClose_28.clicked.connect(self.ManHinhChinh)
        self.ui.GM_RSA_btn_28.clicked.connect(self.RSA_Dec)
        self.ui.GM_SDES_btn_28.clicked.connect(self.SDES_Dec)

        self.ui.GMThayThe_btn_28.clicked.connect(self.Ceasar_Dec)
        self.ui.GMChuyenVi_btn_28.clicked.connect(self.Hai_Dong_Dec)
        self.ui.GMXOR_btn_28.clicked.connect(self.XOR_Ceasar_Dec)

            #Chức năng
        self.s = '' #khai báo toàn cục của lớp THIS => datamember
        self.k = ''
        self.ui.btnGiaiMa_28.clicked.connect(self.GiaiMa_AES_Dec)
        self.ui.btnOpenFile_28.clicked.connect(self.MoFile_AES_Dec)
        self.ui.btnSaveFile_28.clicked.connect(self.GhiFile_AES_Dec)
    def GiaiMa_AES_Dec(self):
        textci = self.ui.txtCiphertext_28.toPlainText() #lấy dữ liệu trong text ciphertext của ThietKeMaHoaVignere
        if not textci:
            self.show_custom_message( "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.ui.btnOpenFile_28.setFocus()
        else:
            cAES = CAES()
            s = cAES.GiaiMa(self.s,self.k)
            self.ui.txtVanBanGoc_28.setPlainText(s) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_AES_Dec(self):
        #Mở file dữ liệu đã mã hoá
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'rb') as file:
                self.s = file.read()
                self.ui.txtCiphertext_28.setPlainText(self.s.decode('utf-8'))
        #Mở file dữ liệu đã KEY
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'rb') as file:
                self.k = file.read()
                # self.ui.txtCiphertext_28.setPlainText(self.k.decode('utf-8'))

    def GhiFile_AES_Dec(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtVanBanGoc_28.toPlainText())
            #=========================================    
            #Màn hình hiện đại RES
    def RSA_Dec(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.RSA_Dec)
        self.ui.btnClose_29.clicked.connect(self.ManHinhChinh)
        self.ui.GM_AES_btn_29.clicked.connect(self.AES_Dec)
        self.ui.GM_SDES_btn_29.clicked.connect(self.SDES_Dec)

        self.ui.GMThayThe_btn_29.clicked.connect(self.Ceasar_Dec)
        self.ui.GMChuyenVi_btn_29.clicked.connect(self.Hai_Dong_Dec)
        self.ui.GMXOR_btn_29.clicked.connect(self.XOR_Ceasar_Dec)
        
        self.s = '' #khai báo toàn cục của lớp THIS => datamember
        self.ui.btnGiaiMa_29.clicked.connect(self.GiaiMa_RSA_Dec)
        self.ui.btnOpenFile_29.clicked.connect(self.MoFile_RSA_Dec)
        self.ui.btnSaveFile_29.clicked.connect(self.GhiFile_RSA_Dec)
    def GiaiMa_RSA_Dec(self):
        textci = self.ui.txtCiphertext_29.toPlainText() #lấy dữ liệu trong text ciphertext của ThietKeMaHoaVignere
        if not textci:
            self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.ui.btnOpenFile_29.setFocus()
        else:
            n=4255903; d=2480777
            ci=[]
            arr_S = self.s.split(" ")
            for i in arr_S:
                ci.append(int(i))
            c = View.Control.mahoaRSA.GiaiMa(ci,d,n) #gọi hàm mã hoá của đối tượng này
            s = ''
            for i in c:
                s+= str(i)
            self.ui.txtVanBanGoc_29.setPlainText(s) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_RSA_Dec(self):
        #Mở file dữ liệu đã mã hoá
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r') as file:
                self.s = file.read()
                self.s =self.s.rstrip()
                self.ui.txtCiphertext_29.setPlainText(self.s)

    def GhiFile_RSA_Dec(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtVanBanGoc_29.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file giải mã thành công!!!!")
         #=========================================    
            #Màn hình hiện đại SDES
    def SDES_Dec(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.SDES_Dec)
        self.ui.btnClose_30.clicked.connect(self.ManHinhChinh)
        self.ui.GM_AES_btn_30.clicked.connect(self.AES_Dec)
        self.ui.GM_RSA_btn_30.clicked.connect(self.RSA_Dec)

        self.ui.GMThayThe_btn_30.clicked.connect(self.Ceasar_Dec)
        self.ui.GMChuyenVi_btn_30.clicked.connect(self.Hai_Dong_Dec)
        self.ui.GMXOR_btn_30.clicked.connect(self.XOR_Ceasar_Dec)

            #Chức năng
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.ui.btnGiaiMa_30.clicked.connect(self.GiaiMa_SDES_Dec)
        self.ui.btnOpenFile_30.clicked.connect(self.MoFile_SDES_Dec)
        self.ui.btnSaveFile_30.clicked.connect(self.GhiFile_SDES_Dec)
    def GiaiMa_SDES_Dec(self):
        textci = self.ui.txtCiphertext_30.toPlainText() #lấy dữ liệu trong text ciphertext của ThietKeMaHoaVignere
        if not textci:
            self.show_custom_message( "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.ui.btnOpenFile_30.setFocus()
        else:
            c = View.Control.mahoaSDES.GiaiMa(textci,self.textk ) #gọi hàm mã hoá của đối tượng này
            self.ui.txtVanBanGoc_30.setPlainText(c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_SDES_Dec(self):
        #Mở file dữ liệu đã mã hoá
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                s=''
                line = file.readline()
                while line:
                    s+=line
                    line = file.readline()
                self.ui.txtCiphertext_30.setPlainText(s)
        #Mở file KEY
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk = file.read()
                self.ui.txtKey_30.setText(self.textk)
                
    def GhiFile_SDES_Dec(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.ui.txtVanBanGoc_30.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file giải mã thành công!!!!")
    #=====================================================================================================================
    def show_custom_message(self, title, content):
        # Tạo đối tượng QMessageBox
        msg_box = QMessageBox()

        # Thiết lập màu chữ và font cho QMessageBox
        msg_box.setStyleSheet("QMessageBox { background-color: " + "#040222" + ";}")
        
        # Thiết lập các thuộc tính khác của QMessageBox

        # Thiết lập các thuộc tính khác của QMessageBox
        msg_box.setWindowTitle(title)
        msg_box.setText(content)
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setText(content)
        for label in msg_box.findChildren(QLabel):
            label.setStyleSheet("color: " + "#1AF5B9" + ";")
        # Hiển thị MessageBox
        msg_box.exec()
def main():
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()



'''

'''
