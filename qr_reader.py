import cv2  # - openCV 라이브러리 활용

def read_qrcode_cv2(opencv_image):
    detector = cv2.QRCodeDetector()
    data, rect, _ = detector.detectAndDecode(opencv_image)
    if data:
        print("QRCODE DATA: {}".format(data))
        print("QRCODE LOCATION: {}".format(rect))

        lefttop = (int(rect[0][0][0]), int(rect[0][0][1]))
        rightbottom = (int(rect[0][2][0]), int(rect[0][2][1]))
        cv2.rectangle(opencv_image, lefttop, rightbottom, (0, 0, 255), 5) 
        # - color값이 입력되는 자리에 (0,0,255)는 RGB 순서가 아니라 BGR순서다.
        # - 빨간색으로 표시하기 위해 R값에 255를 입력했다.
        cv2.imshow("QRimage", opencv_image)
        cv2.waitKey(0)  # - 이걸 안하면 창이 떴다가 바로 사라진다. 키 입력이 될때까지는 꺼지지 않는다.
        cv2.destroyAllWindows()


filepath = "qr_msaischool.png"   # cv2.imread() 메서드는 변수 'filepath'에 할당된 'png'파일을 읽는다.
cv_image1 = cv2.imread(filepath) 
read_qrcode_cv2(cv_image1) 
# - 정상적으로 QR코드의 데이터와 QR코드의 위치값을 출력한다.
# - QRimage라는 이름의 이미지파일에 'qr_msaischool.png' 파일의 QR코드를 빨간색 선으로 인식범위가 표시된다.

