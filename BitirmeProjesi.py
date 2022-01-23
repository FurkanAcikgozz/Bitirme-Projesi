#Tasarım İçin Gerekli Kütüphaneler
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from tkinter import *
from tkinter import filedialog #Dosya Seç için Gerekli Kütüphane
from PIL import Image

#PSNR Değeri için Gerekli Kütüphaneler
from math import log10, sqrt 
import cv2
import numpy as np


import sys


class Pencere(QWidget):
    """Arayüz"""
    def __init__(self):
        super().__init__()
        self.setUI()
    """setUI = Buton ve Labelerin Tanımlanması"""
    def setUI(self):
        self.label3 = QLabel("Resim Sıkıştırma")
        self.label = QLabel("")
        self.label2 = QLabel("")

        button2= QPushButton("Dosya Seç") #Button       
        v_box = QVBoxLayout()
        v_box.addWidget(self.label3)
        v_box.addWidget(self.label)

 
        v_box.addWidget(button2)
        v_box.addWidget(self.label2)
        
        self.setLayout(v_box)
        
        button2.clicked.connect(self.yap2)

        self.show()
        
        
    """yap2: Butona Tıklandığında Yapılan İşlemler"""
    def yap2(self):
            #4 Satır Dosya Seç Butonu
            filepath = filedialog.askopenfilename()
            filee=filedialog.os.path.basename(filepath)
            print(filee)
            print (filepath)
            
            #Resim Sıkıştırma
            dir(Image)

            file_name = filee
            picture = Image.open(filee)
            dim = picture.size
          
            self.label.setText(f"Bu, görüntünün geçerli genişliği ve yüksekliğidir(Çözünürlük): {dim}")

            picture.save("Compressed_"+file_name,optimize=True,quality=30) #Yeni Resim Olarak Kaydetme


            """PSNR = PSNR Değerinin Hesaplanması"""
            def PSNR(original, compressed):
                mse = np.mean((original - compressed) ** 2)
                if(mse == 0):  # MSE is zero means no noise is present in the signal .
                                      # Therefore PSNR have no importance.
                    return 100
                max_pixel = 255.0
                psnr = 20 * log10(max_pixel / sqrt(mse))
                return psnr
                      
                    
            original = cv2.imread(filee)
            compressed = cv2.imread("Compressed_"+filee, 1)
            value = PSNR(original, compressed)
           
            self.label2.setText(f"PSNR değeri: {value} dB")
            
       


if __name__ =="__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())