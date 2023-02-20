# - 터미널에서 'pip install pyqrcode' 명령어를 입력하여 pyqrcode 라이브러리 설치.
# - 터미널에서 'pip install pypng' 명령어를 입력 pypng 라이브러리 설치. (pyqrcode 안에서 쓰이기 때문에 설치.)
# pip install pyqrcode
# pip install pypng

import pyqrcode

qrcode = pyqrcode.create("https://msaischool.kr/")  # - 'qrcode'변수에 QR코드를 생성하는 명령어를 할당.
qrcode.svg("qr_msaischool.svg", scale=8)
qrcode.eps("qr_msaischool.eps", scale=10)
# - QR코드를 svg문서와 eps 파일로 작성.


qrcode = pyqrcode.create("https://msaischool.kr", mode = "binary", encoding = "utf-8")
qrcode.png("qr_msaischool.png", scale = 8, module_color = [0, 0, 0, 255], background =[255, 255, 255, 255])
qrcode.show()
# - 'qr_msaischool.png' png파일이 정상적으로 생성되고 보여짐.
# - 크기를 따로 정해주지 않으면 매우 작게나와서 scale메서드로 크기를 조절.
