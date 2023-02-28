# - 터미널에서 'pip install pyqrcode' 명령어를 입력하여 pyqrcode 라이브러리 설치.
# - 터미널에서 'pip install pypng' 명령어를 입력 pypng 라이브러리 설치. (pyqrcode 안에서 쓰이기 때문에 설치.)
# pip install pyqrcode
# pip install pypng

import pyqrcode

qrcode = pyqrcode.create("https://msaischool.kr/")
qrcode.svg("qr_msaischool.svg", scale=8)
qrcode.eps("qr_msaischool.eps", scale=10)


qrcode = pyqrcode.create("https://msaischool.kr", mode = "binary", encoding = "utf-8")
qrcode.png("qr_msaischool.png", scale = 8, module_color = [0, 0, 0, 255], background =[255, 255, 255, 255])
qrcode.show()

