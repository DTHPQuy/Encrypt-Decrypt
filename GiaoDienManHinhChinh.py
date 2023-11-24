import sys
sys.path.insert(0,"D:/DeTaiBaoMat/View/Control")
#Chèn đường dẫn để import các file mã hóa trong folder control
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QLabel,QLineEdit, QDialog, QStackedWidget, QVBoxLayout
from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic

#import các class
from mahoaceasar_class import CCeasar
from mahoavignere_class import CVignere
from mahoatrithemius_class import CTrithemius
from mahoabelasco_class import CBelasco
from mahoachuyenvihaidong_class import CChuyenViHaiDong
from mahoachuyenvinhieudong_class import CChuyenViNhieuDong
from mahoaXorCeasar_class import CXORCeasar
from mahoaXorvignere_class import CXORVignere
from mahoaXortrithemius_class import CXORTrithemius
from mahoaXorbelasco_class import CXORBelasco
from mahoaAES_class import CAES
import mahoaRSA
import mahoaSDES
import mahoamd5
import mahoasha3
import mahoasha256


# Import Ui_MainWindow from the generated file
from View.ThietKeManHinhChinh import Ui_MainWindow
class MyMainWindow(QMainWindow):
    data_signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        uic.loadUi('ThietKeManHinhChinh.ui', self)

        #tạo global variable
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.c = ''
        self.k=[]
        self.p = ''
        self.s = ''
        self.ci = ''
        self.VBG = ''
        # Khai báo nút trên main window
        self.MHThayThe_btn_0.clicked.connect(self.Show_Ceasar_Enc)
        self.MHChuyenVi_btn_0.clicked.connect(self.Show_Hai_Dong_Enc)
        self.MHXOR_btn_0.clicked.connect(self.Show_XOR_Ceasar_Enc)
        self.MHHienDai_btn_0.clicked.connect(self.Show_AES_Enc)
        self.MHMotChieu_btn_0.clicked.connect(self.Show_SHA3_Enc)
        self.GMThayThe_btn_0.clicked.connect(self.Show_Ceasar_Dec)
        self.GMChuyenVi_btn_0.clicked.connect(self.Show_Hai_Dong_Dec)
        self.GMXOR_btn_0.clicked.connect(self.Show_XOR_Ceasar_Dec)
        self.GMHienDai_btn_0.clicked.connect(self.Show_AES_Dec)
        
        #Button trong Login
         # Khai báo một biến để theo dõi trạng thái của mật khẩu
        self.password_visible = False
        # Khi nút Đăng nhập được nhấn, kiểm tra tên đăng nhập và mật khẩu
        self.loginButton.clicked.connect(self.check_login)
        # Khi nút "Hiển thị mật khẩu" được nhấn, chuyển đổi echoMode
        self.showPasswordButton.clicked.connect(self.toggle_password_visibility_Login)
        #Button chuyển qua trang SignUp
        self.SignUp_btn.clicked.connect(self.ManHinhDangKy)

        self.cancelButton.clicked.connect(self.close)
        #Các button của các Stacked Widget

        #Button trong Đăng ký
    
        # Khi nút Đăng nhập được nhấn, kiểm tra tên đăng nhập và mật khẩu
        self.signupButton_2.clicked.connect(self.check_signup)
        # Khi nút "Hiển thị mật khẩu" được nhấn, chuyển đổi echoMode
        self.showPasswordButton_2.clicked.connect(self.toggle_password_visibility)
        self.showPasswordButton2_2.clicked.connect(self.toggle_password_visibility)
        self.cancelButton_2.clicked.connect(self.ManHinhDangNhap)

            # Button của Mã Hóa Ceasar
        self.btnClose_1.clicked.connect(self.ManHinhChinh)
        self.MH_Vignere_btn_1.clicked.connect(self.Show_Vignere_Enc)
        self.MH_Trithemius_btn_1.clicked.connect(self.Show_Trithemius_Enc)
        self.MH_Belasco_btn_1.clicked.connect(self.Show_Belasco_Enc)

        self.MHChuyenVi_btn_1.clicked.connect(self.Show_Hai_Dong_Enc)
        self.MHXOR_btn_1.clicked.connect(self.Show_XOR_Ceasar_Enc)
        self.MHHienDai_btn_1.clicked.connect(self.Show_AES_Enc)
        self.MHMotChieu_btn_1.clicked.connect(self.Show_SHA3_Enc)
        
        self.btnMaHoa_1.clicked.connect(self.MaHoa_Ceasar_Enc)
        self.btnOpenFile_1.clicked.connect(self.MoFile_Ceasar_Enc)
        self.btnSaveFile_1.clicked.connect(self.GhiFile_Ceasar_Enc)

            #Button Của Mã hóa Vignere
        self.btnClose_2.clicked.connect(self.ManHinhChinh)
        self.MH_Ceasar_btn_2.clicked.connect(self.Show_Ceasar_Enc)
        self.MH_Trithemius_btn_2.clicked.connect(self.Show_Trithemius_Enc)
        self.MH_Belasco_btn_2.clicked.connect(self.Show_Belasco_Enc)

        self.MHChuyenVi_btn_2.clicked.connect(self.Show_Hai_Dong_Enc)
        self.MHXOR_btn_2.clicked.connect(self.Show_XOR_Ceasar_Enc)
        self.MHHienDai_btn_2.clicked.connect(self.Show_AES_Enc)
        self.MHMotChieu_btn_2.clicked.connect(self.Show_SHA3_Enc)
        
        self.btnMaHoa_2.clicked.connect(self.MaHoa_Vignere_Enc)
        self.btnOpenFile_2.clicked.connect(self.MoFile_Vignere_Enc)
        self.btnSaveFile_2.clicked.connect(self.GhiFile_Vignere_Enc)

                #Button trong Trithemius
        self.btnClose_3.clicked.connect(self.ManHinhChinh)
        self.MH_Ceasar_btn_3.clicked.connect(self.Show_Ceasar_Enc)
        self.MH_Vignere_btn_3.clicked.connect(self.Show_Vignere_Enc)
        self.MH_Belasco_btn_3.clicked.connect(self.Show_Belasco_Enc)

        self.MHChuyenVi_btn_3.clicked.connect(self.Show_Hai_Dong_Enc)
        self.MHXOR_btn_3.clicked.connect(self.Show_XOR_Ceasar_Enc)
        self.MHHienDai_btn_3.clicked.connect(self.Show_AES_Enc)
        self.MHMotChieu_btn_3.clicked.connect(self.Show_SHA3_Enc)

        self.btnMaHoa_3.clicked.connect(self.MaHoa_Trithemius_Enc)
        self.btnOpenFile_3.clicked.connect(self.MoFile_Trithemius_Enc)
        self.btnSaveFile_3.clicked.connect(self.GhiFile_Trithemius_Enc)

                #Button trong Belasco
        self.btnClose_4.clicked.connect(self.ManHinhChinh)
        self.MH_Ceasar_btn_4.clicked.connect(self.Show_Ceasar_Enc)
        self.MH_Vignere_btn_4.clicked.connect(self.Show_Vignere_Enc)
        self.MH_Trithemius_btn_4.clicked.connect(self.Show_Trithemius_Enc)

        self.MHChuyenVi_btn_4.clicked.connect(self.Show_Hai_Dong_Enc)
        self.MHXOR_btn_4.clicked.connect(self.Show_XOR_Ceasar_Enc)
        self.MHHienDai_btn_4.clicked.connect(self.Show_AES_Enc)
        self.MHMotChieu_btn_4.clicked.connect(self.Show_SHA3_Enc)
                
        self.btnMaHoa_4.clicked.connect(self.MaHoa_Belasco_Enc)
        self.btnOpenFile_4.clicked.connect(self.MoFile_Belasco_Enc)
        self.btnSaveFile_4.clicked.connect(self.GhiFile_Belasco_Enc)

                #Button trong Hai Dòng
        self.btnClose_5.clicked.connect(self.ManHinhChinh)
        self.MH_NhieuDong_btn_5.clicked.connect(self.Show_Nhieu_Dong_Enc)

        self.MHThayThe_btn_5.clicked.connect(self.Show_Ceasar_Enc)
        self.MHXOR_btn_5.clicked.connect(self.Show_XOR_Ceasar_Enc)
        self.MHHienDai_btn_5.clicked.connect(self.Show_AES_Enc)
        self.MHMotChieu_btn_5.clicked.connect(self.Show_SHA3_Enc)

        self.btnMaHoa_5.clicked.connect(self.MaHoa_HaiDong_Enc)
        self.btnOpenFile_5.clicked.connect(self.MoFile_HaiDong_Enc)
        self.btnSaveFile_5.clicked.connect(self.GhiFile_HaiDong_Enc)

                #Button trong Nhiều Dòng
        self.btnClose_6.clicked.connect(self.ManHinhChinh)
        self.MH_HaiDong_btn_6.clicked.connect(self.Show_Hai_Dong_Enc)

        self.MHThayThe_btn_6.clicked.connect(self.Show_Ceasar_Enc)
        self.MHXOR_btn_6.clicked.connect(self.Show_XOR_Ceasar_Enc)
        self.MHHienDai_btn_6.clicked.connect(self.Show_AES_Enc)
        self.MHMotChieu_btn_6.clicked.connect(self.Show_SHA3_Enc)

        self.btnMaHoa_6.clicked.connect(self.MaHoa_NhieuDong_Enc)
        self.btnOpenFile_6.clicked.connect(self.MoFile_NhieuDong_Enc)
        self.btnSaveFile_6.clicked.connect(self.GhiFile_NhieuDong_Enc)

                #Button trong XOR_Ceasar_Enc
        self.btnClose_7.clicked.connect(self.ManHinhChinh)
        self.MH_Vignere_btn_7.clicked.connect(self.Show_XOR_Vignere_Enc)
        self.MH_Trithemius_btn_7.clicked.connect(self.Show_XOR_Trithemius_Enc)
        self.MH_Belasco_btn_7.clicked.connect(self.Show_XOR_Belasco_Enc)

        self.MHThayThe_btn_7.clicked.connect(self.Show_Ceasar_Enc)
        self.MHChuyenVi_btn_7.clicked.connect(self.Show_Hai_Dong_Enc)
        self.MHHienDai_btn_7.clicked.connect(self.Show_AES_Enc)
        self.MHMotChieu_btn_7.clicked.connect(self.Show_SHA3_Enc)

        self.btnMaHoa_7.clicked.connect(self.MaHoa_XOR_Ceasar_Enc)
        self.btnOpenFile_7.clicked.connect(self.MoFile_XOR_Ceasar_Enc)
        self.btnSaveFile_7.clicked.connect(self.GhiFile_XOR_Ceasar_Enc)

                #Button trong XOR_Vignere_Enc
        self.btnClose_8.clicked.connect(self.ManHinhChinh)
        self.MH_Ceasar_btn_8.clicked.connect(self.Show_XOR_Ceasar_Enc)
        self.MH_Trithemius_btn_8.clicked.connect(self.Show_XOR_Trithemius_Enc)
        self.MH_Belasco_btn_8.clicked.connect(self.Show_XOR_Belasco_Enc)

        self.MHThayThe_btn_8.clicked.connect(self.Show_Ceasar_Enc)
        self.MHChuyenVi_btn_8.clicked.connect(self.Show_Hai_Dong_Enc)
        self.MHHienDai_btn_8.clicked.connect(self.Show_AES_Enc)
        self.MHMotChieu_btn_8.clicked.connect(self.Show_SHA3_Enc)

        self.btnMaHoa_8.clicked.connect(self.MaHoa_XOR_Vignere_Enc)
        self.btnOpenFile_8.clicked.connect(self.MoFile_XOR_Vignere_Enc)
        self.btnSaveFile_8.clicked.connect(self.GhiFile_XOR_Vignere_Enc)

                #Button Trong XOR_Trithemius_Enc
        self.btnClose_9.clicked.connect(self.ManHinhChinh)
        self.MH_Ceasar_btn_9.clicked.connect(self.Show_XOR_Ceasar_Enc)
        self.MH_Vignere_btn_9.clicked.connect(self.Show_XOR_Vignere_Enc)
        self.MH_Belasco_btn_9.clicked.connect(self.Show_XOR_Belasco_Enc)

        self.MHThayThe_btn_9.clicked.connect(self.Show_Ceasar_Enc)
        self.MHChuyenVi_btn_9.clicked.connect(self.Show_Hai_Dong_Enc)
        self.MHHienDai_btn_9.clicked.connect(self.Show_AES_Enc)
        self.MHMotChieu_btn_9.clicked.connect(self.Show_SHA3_Enc)

        self.btnMaHoa_9.clicked.connect(self.MaHoa_XOR_Trithemius_Enc)
        self.btnOpenFile_9.clicked.connect(self.MoFile_XOR_Trithemius_Enc)
        self.btnSaveFile_9.clicked.connect(self.GhiFile_XOR_Trithemius_Enc)

                #Button trong XOR_Belasco_Enc
        self.btnClose_10.clicked.connect(self.ManHinhChinh)
        self.MH_Ceasar_btn_10.clicked.connect(self.Show_XOR_Ceasar_Enc)
        self.MH_Vignere_btn_10.clicked.connect(self.Show_XOR_Vignere_Enc)
        self.MH_Trithemius_btn_10.clicked.connect(self.Show_XOR_Trithemius_Enc)

        self.MHThayThe_btn_10.clicked.connect(self.Show_Ceasar_Enc)
        self.MHChuyenVi_btn_10.clicked.connect(self.Show_Hai_Dong_Enc)
        self.MHHienDai_btn_10.clicked.connect(self.Show_AES_Enc)
        self.MHMotChieu_btn_10.clicked.connect(self.Show_SHA3_Enc)

        self.btnMaHoa_10.clicked.connect(self.MaHoa_XOR_Belasco_Enc)
        self.btnOpenFile_10.clicked.connect(self.MoFile_XOR_Belasco_Enc)
        self.btnSaveFile_10.clicked.connect(self.GhiFile_XOR_Belasco_Enc)

                #Button trong AES_Enc
        self.btnClose_11.clicked.connect(self.ManHinhChinh)
        self.MH_RSA_btn_11.clicked.connect(self.Show_RSA_Enc)
        self.MH_SDES_btn_11.clicked.connect(self.Show_SDES_Enc)

        self.MHThayThe_btn_11.clicked.connect(self.Show_Ceasar_Enc)
        self.MHChuyenVi_btn_11.clicked.connect(self.Show_Hai_Dong_Enc)
        self.MHXOR_btn_11.clicked.connect(self.Show_XOR_Ceasar_Enc)
        self.MHMotChieu_btn_11.clicked.connect(self.Show_SHA3_Enc)

        self.btnMaHoa_11.clicked.connect(self.MaHoa_AES_Enc)
        self.btnOpenFile_11.clicked.connect(self.MoFile_AES_Enc)
        self.btnSaveFile_11.clicked.connect(self.GhiFile_AES_Enc)

                #Button trong RSA_Dec
        self.btnClose_12.clicked.connect(self.ManHinhChinh)
        self.MH_AES_btn_12.clicked.connect(self.Show_AES_Enc)
        self.MH_SDES_btn_12.clicked.connect(self.Show_SDES_Enc)

        self.MHThayThe_btn_12.clicked.connect(self.Show_Ceasar_Enc)
        self.MHChuyenVi_btn_12.clicked.connect(self.Show_Hai_Dong_Enc)
        self.MHXOR_btn_12.clicked.connect(self.Show_XOR_Ceasar_Enc)
        self.MHMotChieu_btn_12.clicked.connect(self.Show_SHA3_Enc)

        self.btnMaHoa_12.clicked.connect(self.MaHoa_RSA_Enc)
        self.btnOpenFile_12.clicked.connect(self.MoFile_RSA_Enc)
        self.btnSaveFile_12.clicked.connect(self.GhiFile_RSA_Enc)

         #Button Trong SDES_Enc
        self.btnClose_13.clicked.connect(self.ManHinhChinh)
        self.MH_AES_btn_13.clicked.connect(self.Show_AES_Enc)
        self.MH_RSA_btn_13.clicked.connect(self.Show_RSA_Enc)

        self.MHThayThe_btn_13.clicked.connect(self.Show_Ceasar_Enc)
        self.MHChuyenVi_btn_13.clicked.connect(self.Show_Hai_Dong_Enc)
        self.MHXOR_btn_13.clicked.connect(self.Show_XOR_Ceasar_Enc)
        self.MHMotChieu_btn_13.clicked.connect(self.Show_SHA3_Enc)

        self.btnMaHoa_13.clicked.connect(self.MaHoa_SDES_Enc)
        self.btnOpenFile_13.clicked.connect(self.MoFile_SDES_Enc)
        self.btnSaveFile_13.clicked.connect(self.GhiFile_SDES_Enc)
        

        #Button trong SHA3_Enc
        self.btnClose_14.clicked.connect(self.ManHinhChinh)
        self.MH_SHA256_btn_14.clicked.connect(self.Show_SHA256_Enc)
        self.MH_MD5_btn_14.clicked.connect(self.Show_MD5_Enc)

        self.MHThayThe_btn_14.clicked.connect(self.Show_Ceasar_Enc)
        self.MHChuyenVi_btn_14.clicked.connect(self.Show_Hai_Dong_Enc)
        self.MHXOR_btn_14.clicked.connect(self.Show_XOR_Ceasar_Enc)
        self.MHHienDai_btn_14.clicked.connect(self.Show_AES_Enc)

        self.btnMaHoa_14.clicked.connect(self.MaHoa_SHA3_Enc)
        self.btnOpenFile_14.clicked.connect(self.MoFile_SHA3_Enc)
        self.btnSaveFile_14.clicked.connect(self.GhiFile_SHA3_Enc)

                #Button trong SHA256
        self.btnClose_15.clicked.connect(self.ManHinhChinh)
        self.MH_SHA3_btn_15.clicked.connect(self.Show_SHA3_Enc)
        self.MH_MD5_btn_15.clicked.connect(self.Show_MD5_Enc)

        self.MHThayThe_btn_15.clicked.connect(self.Show_Ceasar_Enc)
        self.MHChuyenVi_btn_15.clicked.connect(self.Show_Hai_Dong_Enc)
        self.MHXOR_btn_15.clicked.connect(self.Show_XOR_Ceasar_Enc)
        self.MHHienDai_btn_15.clicked.connect(self.Show_AES_Enc)

        self.btnMaHoa_15.clicked.connect(self.MaHoa_SHA256_Enc)
        self.btnOpenFile_15.clicked.connect(self.MoFile_SHA256_Enc)
        self.btnSaveFile_15.clicked.connect(self.GhiFile_SHA256_Enc)

                #Button trong MD5
        self.btnClose_16.clicked.connect(self.ManHinhChinh)
        self.MH_SHA3_btn_16.clicked.connect(self.Show_SHA3_Enc)
        self.MH_SHA256_btn_16.clicked.connect(self.Show_SHA256_Enc)

        self.MHThayThe_btn_16.clicked.connect(self.Show_Ceasar_Enc)
        self.MHChuyenVi_btn_16.clicked.connect(self.Show_Hai_Dong_Enc)
        self.MHXOR_btn_16.clicked.connect(self.Show_XOR_Ceasar_Enc)
        self.MHHienDai_btn_16.clicked.connect(self.Show_AES_Enc)

        self.btnMaHoa_16.clicked.connect(self.MaHoa_MD5_Enc)
        self.btnOpenFile_16.clicked.connect(self.MoFile_MD5_Enc)
        self.btnSaveFile_16.clicked.connect(self.GhiFile_MD5_Enc)

                #Button Trong Ceasar_Dec
        self.btnClose_18.clicked.connect(self.ManHinhChinh)
        self.GM_Vignere_btn_18.clicked.connect(self.Show_Vignere_Dec)
        self.GM_Trithemius_btn_18.clicked.connect(self.Show_Trithemius_Dec)
        self.GM_Belasco_btn_18.clicked.connect(self.Show_Belasco_Dec)

        self.GMChuyenVi_btn_18.clicked.connect(self.Show_Hai_Dong_Dec)
        self.GMXOR_btn_18.clicked.connect(self.Show_XOR_Ceasar_Dec)
        self.GMHienDai_btn_18.clicked.connect(self.Show_AES_Dec)

        self.btnGiaiMa_18.clicked.connect(self.GiaiMa_Ceasar_Dec) 
        self.btnOpenFile_18.clicked.connect(self.MoFile_Ceasar_Dec)
        self.btnSaveFile_18.clicked.connect(self.GhiFile_Ceasar_Dec)

                #Button Trong Vignere_Dec
        self.btnClose_19.clicked.connect(self.ManHinhChinh)
        self.GM_Ceasar_btn_19.clicked.connect(self.Show_Ceasar_Dec)
        self.GM_Trithemius_btn_19.clicked.connect(self.Show_Trithemius_Dec)
        self.GM_Belasco_btn_19.clicked.connect(self.Show_Belasco_Dec)

        self.GMChuyenVi_btn_19.clicked.connect(self.Show_Hai_Dong_Dec)
        self.GMXOR_btn_19.clicked.connect(self.Show_XOR_Ceasar_Dec)
        self.GMHienDai_btn_19.clicked.connect(self.Show_AES_Dec)

        self.btnGiaiMa_19.clicked.connect(self.GiaiMa_Vignere_Dec)
        self.btnOpenFile_19.clicked.connect(self.MoFile_Vignere_Dec)
        self.btnSaveFile_19.clicked.connect(self.GhiFile_Vignere_Dec)

                #Button trong Trithemius_Dec
        self.btnClose_20.clicked.connect(self.ManHinhChinh)
        self.GM_Ceasar_btn_20.clicked.connect(self.Show_Ceasar_Dec)
        self.GM_Vignere_btn_20.clicked.connect(self.Show_Vignere_Dec)
        self.GM_Belasco_btn_20.clicked.connect(self.Show_Belasco_Dec)

        self.GMChuyenVi_btn_20.clicked.connect(self.Show_Hai_Dong_Dec)
        self.GMXOR_btn_20.clicked.connect(self.Show_XOR_Ceasar_Dec)
        self.GMHienDai_btn_20.clicked.connect(self.Show_AES_Dec)

        self.btnGiaiMa_20.clicked.connect(self.GiaiMa_Trithemius_Dec)
        self.btnOpenFile_20.clicked.connect(self.MoFile_Trithemius_Dec)
        self.btnSaveFile_20.clicked.connect(self.GhiFile_Trithemius_Dec)

                #Button trong Belasco_Dec
        self.btnClose_21.clicked.connect(self.ManHinhChinh)
        self.GM_Ceasar_btn_21.clicked.connect(self.Show_Ceasar_Dec)
        self.GM_Vignere_btn_21.clicked.connect(self.Show_Vignere_Dec)
        self.GM_Trithemius_btn_21.clicked.connect(self.Show_Trithemius_Dec)

        self.GMChuyenVi_btn_21.clicked.connect(self.Show_Hai_Dong_Dec)
        self.GMXOR_btn_21.clicked.connect(self.Show_XOR_Ceasar_Dec)
        self.GMHienDai_btn_21.clicked.connect(self.Show_AES_Dec)

        self.btnGiaiMa_21.clicked.connect(self.GiaiMa_Belasco_Dec)
        self.btnOpenFile_21.clicked.connect(self.MoFile_Belasco_Dec)
        self.btnSaveFile_21.clicked.connect(self.GhiFile_Belasco_Dec)

                #Button Trong Hai Dòng_Dec
        self.btnClose_22.clicked.connect(self.ManHinhChinh)
        self.GM_NhieuDong_btn_22.clicked.connect(self.Show_Nhieu_Dong_Dec)

        self.GMThayThe_btn_22.clicked.connect(self.Show_Ceasar_Dec)
        self.GMXOR_btn_22.clicked.connect(self.Show_XOR_Ceasar_Dec)
        self.GMHienDai_btn_22.clicked.connect(self.Show_AES_Dec)

        self.btnGiaiMa_22.clicked.connect(self.GiaiMa_Hai_Dong_Enc)
        self.btnOpenFile_22.clicked.connect(self.MoFile_Hai_Dong_Enc)
        self.btnSaveFile_22.clicked.connect(self.GhiFile_Hai_Dong_Enc)

                #Button trong Nhiều dòng Dec
        self.btnClose_23.clicked.connect(self.ManHinhChinh)
        self.GM_HaiDong_btn_23.clicked.connect(self.Show_Hai_Dong_Dec)

        self.GMThayThe_btn_23.clicked.connect(self.Show_Ceasar_Dec)
        self.GMXOR_btn_23.clicked.connect(self.Show_XOR_Ceasar_Dec)
        self.GMHienDai_btn_23.clicked.connect(self.Show_AES_Dec)

        self.btnGiaiMa_23.clicked.connect(self.GiaiMa_Nhieu_Dong_Dec)
        self.btnOpenFile_23.clicked.connect(self.MoFile_Nhieu_Dong_Dec)
        self.btnSaveFile_23.clicked.connect(self.GhiFile_Nhieu_Dong_Dec)

                #Button trong XOR_Ceasar_Dec
        self.btnClose_24.clicked.connect(self.ManHinhChinh)
        self.GM_XOR_Vignere_btn_24.clicked.connect(self.Show_XOR_Vignere_Dec)
        self.GM_XOR_Trithemius_btn_24.clicked.connect(self.Show_XOR_Trithemius_Dec)
        self.GM_XOR_Belasco_btn_24.clicked.connect(self.Show_XOR_Belasco_Dec)

        self.GMThayThe_btn_24.clicked.connect(self.Show_Ceasar_Dec)
        self.GMChuyenVi_btn_24.clicked.connect(self.Show_Hai_Dong_Dec)
        self.GMHienDai_btn_24.clicked.connect(self.Show_AES_Dec)

        self.btnGiaiMa_24.clicked.connect(self.GiaiMa_XOR_Ceasar_Dec)
        self.btnOpenFile_24.clicked.connect(self.MoFile_XOR_Ceasar_Dec)
        self.btnSaveFile_24.clicked.connect(self.GhiFile_XOR_Ceasar_Dec)

                #Button trong XOR_Vignere_Dec
        self.btnClose_25.clicked.connect(self.ManHinhChinh)
        self.GM_XOR_Ceasar_btn_25.clicked.connect(self.Show_XOR_Ceasar_Dec)
        self.GM_XOR_Trithemius_btn_25.clicked.connect(self.Show_XOR_Trithemius_Dec)
        self.GM_XOR_Belasco_btn_25.clicked.connect(self.Show_XOR_Belasco_Dec)

        self.GMThayThe_btn_25.clicked.connect(self.Show_Ceasar_Dec)
        self.GMChuyenVi_btn_25.clicked.connect(self.Show_Hai_Dong_Dec)
        self.GMHienDai_btn_25.clicked.connect(self.Show_AES_Dec)
        
        self.btnGiaiMa_25.clicked.connect(self.GiaiMa_XOR_Vignere_Dec)
        self.btnOpenFile_25.clicked.connect(self.MoFile_XOR_Vignere_Dec)
        self.btnSaveFile_25.clicked.connect(self.GhiFile_XOR_Vignere_Dec)

                #Button trong XOR_Trithemius_Dec
        self.btnClose_26.clicked.connect(self.ManHinhChinh)
        self.GM_XOR_Ceasar_btn_26.clicked.connect(self.Show_XOR_Ceasar_Dec)
        self.GM_XOR_Vignere_btn_26.clicked.connect(self.Show_XOR_Vignere_Dec)
        self.GM_XOR_Belasco_btn_26.clicked.connect(self.Show_XOR_Belasco_Dec)

        self.GMThayThe_btn_25.clicked.connect(self.Show_Ceasar_Dec)
        self.GMChuyenVi_btn_25.clicked.connect(self.Show_Hai_Dong_Dec)
        self.GMHienDai_btn_25.clicked.connect(self.Show_AES_Dec)

        self.btnGiaiMa_26.clicked.connect(self.GiaiMa_XOR_Trithemius_Dec)
        self.btnOpenFile_26.clicked.connect(self.MoFile_XOR_Trithemius_Dec)
        self.btnSaveFile_26.clicked.connect(self.GhiFile_XOR_Trithemius_Dec)

                #Button trong XOR_Belasco_Dec
        self.btnClose_27.clicked.connect(self.ManHinhChinh)
        self.GM_XOR_Ceasar_btn_27.clicked.connect(self.Show_XOR_Ceasar_Dec)
        self.GM_XOR_Vignere_btn_27.clicked.connect(self.Show_XOR_Vignere_Dec)
        self.GM_XOR_Trithemius_btn_27.clicked.connect(self.Show_XOR_Trithemius_Dec)

        self.GMThayThe_btn_27.clicked.connect(self.Show_Ceasar_Dec)
        self.GMChuyenVi_btn_27.clicked.connect(self.Show_Hai_Dong_Dec)
        self.GMHienDai_btn_27.clicked.connect(self.Show_AES_Dec)

        self.btnGiaiMa_27.clicked.connect(self.GiaiMa_XOR_Belasco_Dec)
        self.btnOpenFile_27.clicked.connect(self.MoFile_XOR_Belasco_Dec)
        self.btnSaveFile_27.clicked.connect(self.GhiFile_XOR_Belasco_Dec) 

                #Button trong AES_Dec
        self.btnClose_28.clicked.connect(self.ManHinhChinh)
        self.GM_RSA_btn_28.clicked.connect(self.Show_RSA_Dec)
        self.GM_SDES_btn_28.clicked.connect(self.Show_SDES_Dec)

        self.GMThayThe_btn_28.clicked.connect(self.Show_Ceasar_Dec)
        self.GMChuyenVi_btn_28.clicked.connect(self.Show_Hai_Dong_Dec)
        self.GMXOR_btn_28.clicked.connect(self.Show_XOR_Ceasar_Dec)

            #Chức năng
        self.btnGiaiMa_28.clicked.connect(self.GiaiMa_AES_Dec)
        self.btnOpenFile_28.clicked.connect(self.MoFile_AES_Dec)
        self.btnSaveFile_28.clicked.connect(self.GhiFile_AES_Dec)
                
                #Button trong RSA_Dec
        self.btnClose_29.clicked.connect(self.ManHinhChinh)
        self.GM_AES_btn_29.clicked.connect(self.Show_AES_Dec)
        self.GM_SDES_btn_29.clicked.connect(self.Show_SDES_Dec)

        self.GMThayThe_btn_29.clicked.connect(self.Show_Ceasar_Dec)
        self.GMChuyenVi_btn_29.clicked.connect(self.Show_Hai_Dong_Dec)
        self.GMXOR_btn_29.clicked.connect(self.Show_XOR_Ceasar_Dec)
        
        self.btnGiaiMa_29.clicked.connect(self.GiaiMa_RSA_Dec)
        self.btnOpenFile_29.clicked.connect(self.MoFile_RSA_Dec)
        self.btnSaveFile_29.clicked.connect(self.GhiFile_RSA_Dec)

                #Button trong SDES_Dec
        self.btnClose_30.clicked.connect(self.ManHinhChinh)
        self.GM_AES_btn_30.clicked.connect(self.Show_AES_Dec)
        self.GM_RSA_btn_30.clicked.connect(self.Show_RSA_Dec)

        self.GMThayThe_btn_30.clicked.connect(self.Show_Ceasar_Dec)
        self.GMChuyenVi_btn_30.clicked.connect(self.Show_Hai_Dong_Dec)
        self.GMXOR_btn_30.clicked.connect(self.Show_XOR_Ceasar_Dec)

        self.btnGiaiMa_30.clicked.connect(self.GiaiMa_SDES_Dec)
        self.btnOpenFile_30.clicked.connect(self.MoFile_SDES_Dec)
        self.btnSaveFile_30.clicked.connect(self.GhiFile_SDES_Dec)
    #=====================================================================================================================

        #SHOW CÁC MÀN HÌNH
        #Màn Hình chính
    def ManHinhChinh(self):
        self.stackedWidget.setCurrentWidget(self.Main)

    def ManHinhDangNhap(self):
        self.stackedWidget.setCurrentWidget(self.Login)

    def ManHinhDangKy(self):
        self.stackedWidget.setCurrentWidget(self.SignUp)
        #Các màn hình mã hóa
    
    def Show_Ceasar_Enc(self):
        self.stackedWidget.setCurrentWidget(self.Ceasar_Enc)
    
    def Show_Vignere_Enc(self):
        self.stackedWidget.setCurrentWidget(self.Vignere_Enc)
    
    def Show_Trithemius_Enc(self):
        self.stackedWidget.setCurrentWidget(self.Trithemius_Enc)
    
    def Show_Belasco_Enc(self):
        self.stackedWidget.setCurrentWidget(self.Belasco_Enc)
    
    def Show_Hai_Dong_Enc(self):
        self.stackedWidget.setCurrentWidget(self.Hai_Dong_Enc)
    
    def Show_Nhieu_Dong_Enc(self):
        self.stackedWidget.setCurrentWidget(self.Nhieu_Dong_Enc)
    
    def Show_XOR_Ceasar_Enc(self):
        self.stackedWidget.setCurrentWidget(self.XOR_Ceasar_Enc)
    
    def Show_XOR_Vignere_Enc(self):
        self.stackedWidget.setCurrentWidget(self.XOR_Vignere_Enc)
    
    def Show_XOR_Trithemius_Enc(self):
        self.stackedWidget.setCurrentWidget(self.XOR_Trithemius_Enc)

    def Show_XOR_Belasco_Enc(self):
        self.stackedWidget.setCurrentWidget(self.XOR_Belasco_Enc)

    def Show_AES_Enc(self):
        self.stackedWidget.setCurrentWidget(self.AES_Enc)

    def Show_RSA_Enc(self):
        self.stackedWidget.setCurrentWidget(self.RSA_Enc)

    def Show_SDES_Enc(self):
        self.stackedWidget.setCurrentWidget(self.SDES_Enc)

    def Show_SHA3_Enc(self):
        self.stackedWidget.setCurrentWidget(self.SHA3_Enc)

    def Show_SHA256_Enc(self):
        self.stackedWidget.setCurrentWidget(self.SHA256_Enc)

    def Show_MD5_Enc(self):
        self.stackedWidget.setCurrentWidget(self.MD5_Enc)

        #Các màn hình giải mã
    
    def Show_Ceasar_Dec(self):
        self.stackedWidget.setCurrentWidget(self.Ceasar_Dec)

    def Show_Vignere_Dec(self):
        self.stackedWidget.setCurrentWidget(self.Vignere_Dec)
    
    def Show_Trithemius_Dec(self):
        self.stackedWidget.setCurrentWidget(self.Trithemius_Dec)
    
    def Show_Belasco_Dec(self):
        self.stackedWidget.setCurrentWidget(self.Belasco_Dec)
    
    def Show_Hai_Dong_Dec(self):
        self.stackedWidget.setCurrentWidget(self.Hai_Dong_Dec)
    
    def Show_Nhieu_Dong_Dec(self):
        self.stackedWidget.setCurrentWidget(self.Nhieu_Dong_Dec)
    
    def Show_XOR_Ceasar_Dec(self):
        self.stackedWidget.setCurrentWidget(self.XOR_Ceasar_Dec)
    
    def Show_XOR_Vignere_Dec(self):
        self.stackedWidget.setCurrentWidget(self.XOR_Vignere_Dec)
    
    def Show_XOR_Trithemius_Dec(self):
        self.stackedWidget.setCurrentWidget(self.XOR_Trithemius_Dec)

    def Show_XOR_Belasco_Dec(self):
        self.stackedWidget.setCurrentWidget(self.XOR_Belasco_Dec)

    def Show_AES_Dec(self):
        self.stackedWidget.setCurrentWidget(self.AES_Dec)

    def Show_RSA_Dec(self):
        self.stackedWidget.setCurrentWidget(self.RSA_Dec)

    def Show_SDES_Dec(self):
        self.stackedWidget.setCurrentWidget(self.SDES_Dec)

    #=====================================================================================================================
        #Màn hình Mã hóa phương pháp thay thế
            #Màn hình Ceasar
                #Button trong Ceasar
       
        #Chức năng
         #khai báo toàn cục của lớp THIS => datamember
        
    def MaHoa_Ceasar_Enc(self):
        self.textk = self.txtKey_1.toPlainText() #lấy dữ liệu trong text key của ThietKeMaHoaCeasar
        if not self.textk:
            self.show_custom_message( "Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_1.setFocus()
        else:
            textpl = self.txtPlaintext_1.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaCeasar
            if not textpl:
                self.show_custom_message( "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.btnOpenFile_1.setFocus()
            else:
                cCeasar= CCeasar(textpl,int(self.textk)) #khai báo đối tượng của lớp CCeasar
                c = cCeasar.MaHoa() #gọi hàm mã hoá của đối tượng này
                self.txtCiphertext_1.setPlainText(c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaCeasar
    def MoFile_Ceasar_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlaintext_1.setPlainText(fileContent)
    def GhiFile_Ceasar_Enc(self):
        # Lưu file dữ liệu đã mã hoá ciphertext
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Mã hoá", "",
                                                "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtCiphertext_1.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file mã hoá thành công!!!!")

        # Lưu file KEY
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File KEY", "",
                                                "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtKey_1.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file KEY thành công!!!!")
       #=========================================    
    
    def MaHoa_Vignere_Enc(self):
        self.textk = self.txtKey_2.toPlainText() #lấy dữ liệu trong text key của ThietKeMaHoaVignere
        if not self.textk:
            self.show_custom_message("Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_2.setFocus()
        else:
            textpl = self.txtPlaintext_2.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaVignere
            if not textpl:
                self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.btnOpenFile_2.setFocus()
            else:
                cVignere= CVignere(textpl,self.textk) #khai báo đối tượng của lớp CVignere
                self.c = cVignere.MaHoa() #gọi hàm mã hoá của đối tượng này
                self.txtCiphertext_2.setPlainText(self.c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_Vignere_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlaintext_2.setPlainText(fileContent)
    def GhiFile_Vignere_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtCiphertext_2.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file mã hoá thành công!!!!")
                    
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtKey_2.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file KEY thành công!!!!")
        #=========================================    
            #Màn hình Trithemius
                #Chức năng
    
    def MaHoa_Trithemius_Enc(self):
        textpl = self.txtPlaintext_3.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaVignere
        if not textpl:
            self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.btnOpenFile_3.setFocus()
        else:
            cTrithemius= CTrithemius(textpl) #khai báo đối tượng của lớp CVignere
            self.c = cTrithemius.MaHoa() #gọi hàm mã hoá của đối tượng này
            self.txtCiphertext_3.setPlainText(self.c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_Trithemius_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlaintext_3.setPlainText(fileContent)
    def GhiFile_Trithemius_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtCiphertext_3.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file mã hoá thành công!!!!")

        #=========================================    
            #Màn hình Belasco
    
    def MaHoa_Belasco_Enc(self):
        self.textk = self.txtKey_4.toPlainText() #lấy dữ liệu trong text key của ThietKeMaHoaBelasco
        if not self.textk:
            self.show_custom_message("Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_4.setFocus()
        else:
            textpl = self.txtPlaintext_4.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaBelasco
            if not textpl:
                self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.btnOpenFile_4.setFocus()
            else:
                cBelasco= CBelasco(textpl,self.textk) #khai báo đối tượng của lớp CBelasco
                self.c = cBelasco.MaHoa() #gọi hàm mã hoá của đối tượng này
                self.txtCiphertext_4.setPlainText(self.c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaBelasco
    def MoFile_Belasco_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlaintext_4.setPlainText(fileContent)
    def GhiFile_Belasco_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtCiphertext_4.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file mã hoá thành công!!!!")
                
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtKey_4.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file KEY thành công!!!!")
   
    #=====================================================================================================================
        #Màn hình Mã hóa phương pháp chuyển vị
            #Màn hình chuyển vị hai dòng
    def MaHoa_HaiDong_Enc(self):
        textpl = self.txtPlaintext_5.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaVignere
        if not textpl:
            self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.btnOpenFile_5.setFocus()
        else:
            cHaiDong= CChuyenViHaiDong(textpl) #khai báo đối tượng của lớp CVignere
            self.c = cHaiDong.MaHoa() #gọi hàm mã hoá của đối tượng này
            self.txtCiphertext_5.setPlainText(self.c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_HaiDong_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlaintext_5.setPlainText(fileContent)
    def GhiFile_HaiDong_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.c)
            self.show_custom_message("Thông báo", "Lưu file mã hoá thành công!!!!")

        #=========================================    
            #Màn hình chuyển vị nhiều dòng
   
    
    def MaHoa_NhieuDong_Enc(self):
        self.textk = self.txtKey_6.toPlainText() #lấy dữ liệu trong text key của ThietKeMaHoaNhieuDong
        if not self.textk:
            self.show_custom_message("Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_6.setFocus()
        else:
            textpl = self.txtPlaintext_6.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaNhieuDong
            if not textpl:
                self.show_custom_message( "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.btnOpenFile_6.setFocus()
            else:
                cChuyenViNhieuDong= CChuyenViNhieuDong(textpl) #khai báo đối tượng của lớp CNhieuDong
                n = int(self.textk)
                self.k = cChuyenViNhieuDong.CreateKey(n)
                cChuyenViNhieuDong.SetKey(self.k)
                c = cChuyenViNhieuDong.MaHoa() #gọi hàm mã hoá của đối tượng này
                self.txtCiphertext_6.setPlainText(c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaNhieuDong
    def MoFile_NhieuDong_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlaintext_6.setPlainText(fileContent)
    def GhiFile_NhieuDong_Enc(self):
        # Lưu file dữ liệu đã mã hoá ciphertext
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtCiphertext_6.toPlainText())
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
    def MaHoa_XOR_Ceasar_Enc(self):
        self.textk = self.txtKey_7.toPlainText() #lấy dữ liệu trong text key của ThietKeMaHoaCeasar
        if not self.textk:
            self.show_custom_message("Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_7.setFocus()
        else:
            textpl = self.txtPlaintext_7.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaCeasar
            if not textpl:
                self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.btnOpenFile_7.setFocus()
            else:
                cXORCeasar= CXORCeasar() #khai báo đối tượng của lớp CCeasar
                c = cXORCeasar.MaHoa(textpl,int(self.textk)) #gọi hàm mã hoá của đối tượng này
                self.txtCiphertext_7.setPlainText(c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaCeasar
    def MoFile_XOR_Ceasar_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlaintext_7.setPlainText(fileContent)
    def GhiFile_XOR_Ceasar_Enc(self):
        # Lưu file dữ liệu đã mã hoá ciphertext
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtCiphertext_7.toPlainText())
            self.show_custom_message( "Thông báo", "Lưu file mã hoá thành công!!!!")

        # Lưu file KEY
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtKey_7.toPlainText())
            self.show_custom_message( "Thông báo", "Lưu file KEY thành công!!!!")
        #=========================================    
            #Màn hình XOR Vignere
    
    def MaHoa_XOR_Vignere_Enc(self):
        self.textk = self.txtKey_8.toPlainText() #lấy dữ liệu trong text key của ThietKeMaHoaVignere
        if not self.textk:
            self.show_custom_message("Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_8.setFocus()
        else:
            textpl = self.txtPlaintext_8.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaVignere
            if not textpl:
                self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.btnOpenFile_8.setFocus()
            else:
                cVignere= CXORVignere() #khai báo đối tượng của lớp CVignere
                self.c = cVignere.MaHoa(self.p,self.textk) #gọi hàm mã hoá của đối tượng này
                self.txtCiphertext_8.setPlainText(self.c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_XOR_Vignere_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.p = file.read()
                self.txtPlaintext_8.setPlainText(self.p)
    def GhiFile_XOR_Vignere_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtCiphertext_8.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file mã hoá thành công!!!!")
                
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtKey_8.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file KEY thành công!!!!")
        #=========================================    
            #Màn hình XOR Trithemius
    
    def MaHoa_XOR_Trithemius_Enc(self):
        textpl = self.txtPlaintext_9.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaVignere
        if not textpl:
            self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.btnOpenFile_9.setFocus()
        else:
            cTrithemius= CXORTrithemius() #khai báo đối tượng của lớp CVignere
            self.c = cTrithemius.MaHoa(textpl) #gọi hàm mã hoá của đối tượng này
            self.txtCiphertext_9.setPlainText(self.c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_XOR_Trithemius_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlaintext_9.setPlainText(fileContent)
    def GhiFile_XOR_Trithemius_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtCiphertext_9.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file mã hoá thành công!!!!")
        #=========================================
            #Màn hình XOR Belasco
    
    def MaHoa_XOR_Belasco_Enc(self):
        self.textk = self.txtKey_10.toPlainText() #lấy dữ liệu trong text key của ThietKeMaHoaBelasco
        if not self.textk:
            self.show_custom_message("Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_10.setFocus()
        else:
            textpl = self.txtPlaintext_10.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaBelasco
            if not textpl:
                self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.btnOpenFile_10.setFocus()
            else:
                cBelasco= CXORBelasco() #khai báo đối tượng của lớp CBelasco
                self.c = cBelasco.MaHoa(textpl,self.textk) #gọi hàm mã hoá của đối tượng này
                self.txtCiphertext_10.setPlainText(self.c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaBelasco
    def MoFile_XOR_Belasco_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlaintext_10.setPlainText(fileContent)
    def GhiFile_XOR_Belasco_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtCiphertext_10.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file mã hoá thành công!!!!")
                
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtKey_10.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file KEY thành công!!!!")
    
    #=====================================================================================================================
        #Màn hình Mã hóa phương pháp hiện đại
            #Màn hình hiện đại AES
    def MaHoa_AES_Enc(self):
        textpl = self.txtPlaintext_11.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaVignere
        if not textpl:
            self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.btnOpenFile_11.setFocus()
        else:
            cAES = CAES()
            self.c, self.textk = cAES.MaHoa(self.p) #gọi hàm mã hoá của đối tượng này
            self.txtCiphertext_11.setPlainText(self.c.decode('utf-8')) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_AES_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.p = file.read()
                self.txtPlaintext_11.setPlainText(self.p)
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
    
    def MaHoa_RSA_Enc(self):
        self.c = []
        textpl = self.txtPlaintext_12.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaVignere
        if not textpl:
           self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
           self.btnOpenFile_12.setFocus()
        else:
            e=65537
            n=4255903
            self.c = mahoaRSA.MaHoa(textpl,e,n) #gọi hàm mã hoá của đối tượng này
            #print(self.c)
            self.s = ''
            for i in self.c:
                self.s += str(i)+' '
            #print(self.s)
            self.txtCiphertext_12.setPlainText(self.s)
    def MoFile_RSA_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlaintext_12.setPlainText(fileContent)
    def GhiFile_RSA_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w') as file:
                file.write(self.txtCiphertext_12.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file mã hoá thành công!!!!")
                #for i in self.c:
                    #file.write("%d " % i)
         #=========================================    
            #Màn hình hiện đại SDES
    
    def MaHoa_SDES_Enc(self):
        self.textk = self.txtKey_13.toPlainText() #lấy dữ liệu trong text key của ThietKeMaHoaVignere
        if not self.textk:
            self.show_custom_message("Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_13.setFocus()
        else:
            textpl = self.txtPlaintext_13.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaVignere
            if not textpl:
                self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.btnOpenFile_13.setFocus()
            else:
                self.c = mahoaSDES.MaHoa(textpl,self.textk) #gọi hàm mã hoá của đối tượng này
                self.txtCiphertext_13.setPlainText(self.c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_SDES_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlaintext_13.setPlainText(fileContent)
    def GhiFile_SDES_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtCiphertext_13.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file mã hoá thành công!!!!")
                
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtKey_13.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file KEY thành công!!!!")

    #=====================================================================================================================
        #Màn hình Mã hóa phương pháp một chiều
            #Màn hình một chiều SHA3

    def MaHoa_SHA3_Enc(self):
        textpl = self.txtPlaintext_14.toPlainText()
        if not textpl:
            self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.btnOpenFile_14.setFocus()
        else:
            c = mahoasha3.MaHoaSha3(textpl) 
            self.txtCiphertext_14.setPlainText(c) 
    def MoFile_SHA3_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")                                                 
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlaintext_14.setPlainText(fileContent)
    def GhiFile_SHA3_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtCiphertext_14.toPlainText())
         #=========================================    
        #Màn hình Mã hóa phương pháp một chiều
            #Màn hình một chiều SHA256
    
    def MaHoa_SHA256_Enc(self):
        textpl = self.txtPlaintext_15.toPlainText()
        if not textpl:
            self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.btnOpenFile_15.setFocus()
        else:
            c = mahoasha256.MaHoaSha256(textpl) 
            self.txtCiphertext_15.setPlainText(c) 
    def MoFile_SHA256_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")                                                 
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlaintext_15.setPlainText(fileContent)
    def GhiFile_SHA256_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtCiphertext_15.toPlainText())
         #=========================================
        #Màn hình Mã hóa phương pháp một chiều
            #Màn hình một chiều MD5
    
    def MaHoa_MD5_Enc(self):
        textpl = self.txtPlaintext_16.toPlainText()
        if not textpl:
            self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.btnOpenFile_16.setFocus()
        else:
            c = mahoamd5.MaHoaMD5(textpl) 
            self.txtCiphertext_16.setPlainText(c)  
    def MoFile_MD5_Enc(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")                                                 
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlaintext_16.setPlainText(fileContent)
    def GhiFile_MD5_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtCiphertext_16.toPlainText())

   #=====================================================================================================================
        #Màn hình Giải mã phương pháp thay thế
            #Màn hình giải mã Ceasar
    def GiaiMa_Ceasar_Dec(self):
        if not self.textk:
            self.show_custom_message( "Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_18.setFocus()
        else:
            textci = self.txtCiphertext_18.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaCeasar
            if not textci:
                self.show_custom_message( "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.btnOpenFile_18.setFocus()
            else:
                cCeasar= CCeasar("",int(self.textk),textci) #khai báo đối tượng của lớp CCeasar
                s = cCeasar.GiaiMa() #gọi hàm mã hoá của đối tượng này
                self.txtVanBanGoc_18.setPlainText(s) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaCeasar
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
                self.txtCiphertext_18.setPlainText(s)
        # Mở file KEY riêng
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk = file.read()
                self.txtKey_18.setPlainText(self.textk)         
    def GhiFile_Ceasar_Dec(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtVanBanGoc_18.toPlainText())
       #=========================================    
            #Màn hình giải mã Vignere
    
    def GiaiMa_Vignere_Dec(self):
        
        textci = self.txtCiphertext_19.toPlainText() #lấy dữ liệu trong text ciphertext của ThietKeMaHoaVignere
        if not textci:
            self.show_custom_message( "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.btnOpenFile_19.setFocus()
        else:
            cVignere = CVignere("",self.textk, textci)
            c = cVignere.GiaiMa() #gọi hàm mã hoá của đối tượng này
            self.txtVanBanGoc_19.setPlainText(c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
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
                self.txtCiphertext_19.setPlainText(s)
        #Mở file KEY
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk = file.read()
                self.txtKey_19.setText(self.textk)              
    def GhiFile_Vignere_Dec(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtVanBanGoc_19.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file giải mã thành công!!!!")
        
        #=========================================    
            #Màn hình giải mã Trithemius
    
    def GiaiMa_Trithemius_Dec(self):
        textci = self.txtCiphertext_20.toPlainText() #lấy dữ liệu trong text ciphertext của ThietKeMaHoaVignere
        if not textci:
            self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.btnOpenFile_20.setFocus()
        else:
            cTrithemius= CTrithemius("",textci) #khai báo đối tượng của lớp CVignere
            c = cTrithemius.GiaiMa() #gọi hàm mã hoá của đối tượng này
            self.txtVanBanGoc_20.setPlainText(c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
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
                self.txtCiphertext_20.setPlainText(s)            
    def GhiFile_Trithemius_Dec(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtVanBanGoc_20.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file giải mã thành công!!!!")
        #=========================================    
            #Màn hình giải mã Belasco
    
    def GiaiMa_Belasco_Dec(self):
        textci = self.txtCiphertext_21.toPlainText() #lấy dữ liệu trong text ciphertext của ThietKeMaHoaBelasco
        if not textci:
            self.show_custom_message( "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.btnOpenFile_21.setFocus()
        else:
            cBelasco= CBelasco("",self.textk,textci) #khai báo đối tượng của lớp CBelasco
            c = cBelasco.GiaiMa() #gọi hàm mã hoá của đối tượng này
            self.txtVanBanGoc_21.setPlainText(c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaBelasco
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
                self.txtCiphertext_21.setPlainText(s)
        #Mở file KEY
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk = file.read()
                self.txtKey_21.setText(self.textk)            
    def GhiFile_Belasco_Dec(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtVanBanGoc_21.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file giải mã thành công!!!!")
    #=====================================================================================================================
        #Màn hình Giải mã phương pháp Chuyển vị
            #Màn hình giải mã Hai dòng
    def GiaiMa_Hai_Dong_Enc(self):
        textci = self.txtCiphertext_22.toPlainText() #lấy dữ liệu trong text ciphertext của ThietKeMaHoaVignere
        if not textci:
            self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.btnOpenFile_22.setFocus()
        else:
            cHaiDong= CChuyenViHaiDong("",textci) #khai báo đối tượng của lớp CVignere
            c = cHaiDong.GiaiMa() #gọi hàm mã hoá của đối tượng này
            self.txtVanBanGoc_22.setPlainText(c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
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
                self.txtCiphertext_22.setPlainText(s)
    def GhiFile_Hai_Dong_Enc(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtVanBanGoc_22.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file giải mã thành công!!!!")
        #=========================================    
        #Màn hình Giải mã phương pháp Chuyển vị
            #Màn hình giải mã nhiều dòng
    
    def GiaiMa_Nhieu_Dong_Dec(self):
        if not self.textk:
            self.show_custom_message("Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_23.setFocus()
        else:
            textci = self.txtCiphertext_23.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaNhieuDong
            if not textci:
                self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.btnOpenFile_23.setFocus()
            else:
                cChuyenViNhieuDong= CChuyenViNhieuDong("",None,textci) #khai báo đối tượng của lớp CNhieuDong
                k = [ int(item) for item in self.textk.split(' ') ]
                cChuyenViNhieuDong.SetKey(k)
                s = cChuyenViNhieuDong.GiaiMa() #gọi hàm mã hoá của đối tượng này
                self.txtVanBanGoc_23.setPlainText(s) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaNhieuDong
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
                self.txtCiphertext_23.setPlainText(s)
        # Mở file KEY riêng
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk = file.read()
                self.txtKey_23.setPlainText(self.textk)          
    def GhiFile_Nhieu_Dong_Dec(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtVanBanGoc_23.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file giải mã thành công!!!!")
    #=====================================================================================================================
        #Màn hình Giải mã phương pháp XOR
            #Màn hình giải mã XOR Ceasar
    def GiaiMa_XOR_Ceasar_Dec(self):
        if not self.textk:
            self.show_custom_message("Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_24.setFocus()
        else:
            textci = self.txtCiphertext_24.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaCeasar
            if not textci:
                self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.btnOpenFile_24.setFocus()
            else:
                cCeasar= CXORCeasar() #khai báo đối tượng của lớp CCeasar
                s = cCeasar.MaHoa(textci,int(self.textk)) #gọi hàm mã hoá của đối tượng này
                self.txtVanBanGoc_24.setPlainText(s) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaCeasar
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
                self.txtCiphertext_24.setPlainText(s)
        # Mở file KEY riêng
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk = file.read()
                self.txtKey_24.setPlainText(self.textk)           
    def GhiFile_XOR_Ceasar_Dec(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtVanBanGoc_24.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file giải mã thành công!!!!")
        #=========================================
            #Màn hình giải mã XOR Vignere
    

    def GiaiMa_XOR_Vignere_Dec(self):
        self.k = ''
        textci = self.txtCiphertext_25.toPlainText() #lấy dữ liệu trong text ciphertext của ThietKeMaHoaVignere
        if not textci:
            self.show_custom_message( "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.btnOpenFile_25.setFocus()
        else:
            cVignere= CXORVignere() #khai báo đối tượng của lớp CVignere
            self.VBG = cVignere.GiaiMa(self.ci,self.textk) #gọi hàm mã hoá của đối tượng này
            self.txtVanBanGoc_25.setPlainText(self.VBG) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_XOR_Vignere_Dec(self):
        #Mở file dữ liệu đã mã hoá
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.ci= file.read()
                self.txtCiphertext_25.setPlainText(self.ci)
        #Mở file KEY
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk = file.read()
                self.txtKey_25.setText(self.textk)
    def GhiFile_XOR_Vignere_Dec(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.VBG)
            self.show_custom_message("Thông báo", "Lưu file giải mã thành công!!!!")
        #=========================================    
            #Màn hình giải mã XOR Trithemius
    
    def GiaiMa_XOR_Trithemius_Dec(self):
        textci = self.txtCiphertext_26.toPlainText() #lấy dữ liệu trong text ciphertext của ThietKeMaHoaVignere
        if not textci:
            self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.btnOpenFile_26.setFocus()
        else:
            cTrithemius= CXORTrithemius() #khai báo đối tượng của lớp CVignere
            c = cTrithemius.MaHoa(textci) #gọi hàm mã hoá của đối tượng này
            self.txtVanBanGoc_26.setPlainText(c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
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
                self.txtCiphertext_26.setPlainText(s)
    def GhiFile_XOR_Trithemius_Dec(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtVanBanGoc_26.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file giải mã thành công!!!!")
        #=========================================    
            #Màn hình giải mã XOR Belasco
    
    def GiaiMa_XOR_Belasco_Dec(self):

        textci = self.txtCiphertext_27.toPlainText() #lấy dữ liệu trong text ciphertext của ThietKeMaHoaVignere
        if not textci:
            self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.btnOpenFile_27.setFocus()
        else:
            cBelasco= CXORBelasco() #khai báo đối tượng của lớp CVignere
            self.VBG = cBelasco.MaHoa(self.ci,self.textk) #gọi hàm mã hoá của đối tượng này
            self.txtVanBanGoc_27.setPlainText(self.VBG) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_XOR_Belasco_Dec(self):
        #Mở file dữ liệu đã mã hoá
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.ci= file.read()
                self.txtCiphertext_27.setPlainText(self.ci)
        #Mở file KEY
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk = file.read()
                self.txtKey_27.setText(self.textk)          
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
    def GiaiMa_AES_Dec(self):
        self.k = ''
        textci = self.txtCiphertext_28.toPlainText() #lấy dữ liệu trong text ciphertext của ThietKeMaHoaVignere
        if not textci:
            self.show_custom_message( "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.btnOpenFile_28.setFocus()
        else:
            cAES = CAES()
            s = cAES.GiaiMa(self.s,self.k)
            self.txtVanBanGoc_28.setPlainText(s) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_AES_Dec(self):
        #Mở file dữ liệu đã mã hoá
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'rb') as file:
                self.s = file.read()
                self.txtCiphertext_28.setPlainText(self.s.decode('utf-8'))
        #Mở file dữ liệu đã KEY
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'rb') as file:
                self.k = file.read()
                # self.txtCiphertext_28.setPlainText(self.k.decode('utf-8'))
    def GhiFile_AES_Dec(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtVanBanGoc_28.toPlainText())
            #=========================================    
            #Màn hình hiện đại RES
    
    def GiaiMa_RSA_Dec(self):
        textci = self.txtCiphertext_29.toPlainText() #lấy dữ liệu trong text ciphertext của ThietKeMaHoaVignere
        if not textci:
            self.show_custom_message("Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.btnOpenFile_29.setFocus()
        else:
            n=4255903; d=2480777
            ci=[]
            arr_S = self.s.split(" ")
            for i in arr_S:
                ci.append(int(i))
            c = mahoaRSA.GiaiMa(ci,d,n) #gọi hàm mã hoá của đối tượng này
            s = ''
            for i in c:
                s+= str(i)
            self.txtVanBanGoc_29.setPlainText(s) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile_RSA_Dec(self):
        #Mở file dữ liệu đã mã hoá
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r') as file:
                self.s = file.read()
                self.s =self.s.rstrip()
                self.txtCiphertext_29.setPlainText(self.s)
    def GhiFile_RSA_Dec(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtVanBanGoc_29.toPlainText())
            self.show_custom_message("Thông báo", "Lưu file giải mã thành công!!!!")
         #=========================================    
            #Màn hình hiện đại SDES
    
    def GiaiMa_SDES_Dec(self):
        textci = self.txtCiphertext_30.toPlainText() #lấy dữ liệu trong text ciphertext của ThietKeMaHoaVignere
        if not textci:
            self.show_custom_message( "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.btnOpenFile_30.setFocus()
        else:
            c = mahoaSDES.GiaiMa(textci,self.textk ) #gọi hàm mã hoá của đối tượng này
            self.txtVanBanGoc_30.setPlainText(c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
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
                self.txtCiphertext_30.setPlainText(s)
        #Mở file KEY
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk = file.read()
                self.txtKey_30.setText(self.textk)            
    def GhiFile_SDES_Dec(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtVanBanGoc_30.toPlainText())
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
    
    def toggle_password_visibility_Login(self):
        if self.password_visible:
            self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)
            self.password_visible = False
        else:
            self.passwordInput.setEchoMode(QLineEdit.EchoMode.Normal)
            self.password_visible = True

    def check_Account(self,us,ps):
        with open("D:\\detaibaomat\\Data\\account.txt", "r", encoding='utf-8') as file:
            for line in file:
                if line.strip() == us+","+ps:
                    return True
            return False
    
    def check_login(self):
        username = self.usernameInput.text()
        us = mahoasha3.MaHoaSha3(username) 
        password = self.passwordInput.text()
        ps = mahoasha3.MaHoaSha3(password)
        if self.check_Account(us,ps):
            self.openMainWindow()
        else:
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Icon.Information)  # Loại biểu tượng (Information)
            message_box.setWindowTitle('Thông báo')  # Tiêu đề
            message_box.setText('Bạn nhập sai username và password.')  # Nội dung thông báo
            message_box.setStandardButtons(QMessageBox.StandardButton.Ok)  # Các nút (OK)
            result = message_box.exec()  # Hiển thị hộp thoại và chờ đợi phản hồi từ người dùng
            self.usernameInput.setFocus()

    def toggle_password_visibility(self):
        if self.password_visible:
            self.passwordInput_2.setEchoMode(QLineEdit.EchoMode.Password)
            self.passwordInput2_2.setEchoMode(QLineEdit.EchoMode.Password)
            self.password_visible = False
        else:
            self.passwordInput_2.setEchoMode(QLineEdit.EchoMode.Normal)
            self.passwordInput2_2.setEchoMode(QLineEdit.EchoMode.Normal)
            self.password_visible = True
    
         
    def check_signup(self):
        self.username = self.usernameInput_2.text()
        self.password = self.passwordInput_2.text()
        password2 = self.passwordInput2_2.text()
        if(self.password != password2):
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Icon.Information)  # Loại biểu tượng (Information)
            message_box.setWindowTitle('Thông báo')  # Tiêu đề
            message_box.setText('Bạn nhập password lần hai chưa đúng.')  # Nội dung thông báo
            message_box.setStandardButtons(QMessageBox.StandardButton.Ok)  # Các nút (OK)
            result = message_box.exec()  # Hiển thị hộp thoại và chờ đợi phản hồi từ người dùng
            self.passwordInput2_2.setFocus()
        else:
            us = mahoasha3.MaHoaSha3(self.username)
            ps = mahoasha3.MaHoaSha3(self.password)
            
            
            with open("D:\\detaibaomat\\Data\\account.txt", "a", encoding='utf-8') as file:
                file.write(us+","+ps+"\n")
            self.openLoginWindow()

    def openLoginWindow(self):
        self.stackedWidget.setCurrentWidget(self.Login)
        self.usernameInput.setText(self.username)
        self.passwordInput.setText(self.password)

    def openMainWindow(self):
         self.stackedWidget.setCurrentWidget(self.Main)
    
def main():
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec())

    
if __name__ == "__main__":
    main()

