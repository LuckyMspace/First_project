import cv2  # - openCV 라이브러리 활용

def read_qrcode_cv2(opencv_image):
    detector = cv2.QRCodeDetector()
    data, rect, _ = detector.detectAndDecode(opencv_image)
    if data:
        print("QRCODE DATA: {}".format(data))
        print("QRCODE LOCATION: {}".format(rect))

filepath = "qr_msaischool.png"   # cv2.imread() 메서드는 변수 'filepath'에 할당된 'png'파일을 읽는다.
cv_image1 = cv2.imread(filepath) 
read_qrcode_cv2(cv_image1) 
# 여기까지 정상적으로 QR코드의 데이터와 QR코드의 위치값을 출력한다.

