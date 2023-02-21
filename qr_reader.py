import cv2  # - openCV 라이브러리 활용
import pyzbar.pyzbar as pyzbar  # cv2는 인식률이 많이 높지 않기 때문에 pyzbar 라이브러리 함수로 보완

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

def read_qrcode_zbar(opencv_image):
    gray = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)
    decoded = pyzbar.decode(gray)
    for d in decoded:
        x, y, w, h = d.rect
        qrcode_data = d.data.decode("utf-8")
        qrcode_type = d.type
        cv2.rectangle(opencv_image, (x, y), (x + w, y + h), (0, 0, 255), 3)
        text = "{} {}".format(qrcode_data, qrcode_type)
        cv2.putText(opencv_image, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0 ,255), 1, cv2.LINE_AA)
         # - 'putText()를 사용하여 cvimage에 텍스트가 출력되게 한다.
    cv2.imshow("QRimage2", opencv_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # 설정된 'decoded' 변수는 출력시 인식된 모든 QR코드의 데이터를 나열하기 때문에 리스트형으로 출력된다.
filepath = "qr_msaischool.png"   # cv2.imread() 메서드는 변수 'filepath'에 할당된 'png'파일을 읽는다.
cv_image1 = cv2.imread(filepath) 
# read_qrcode_cv2(cv_image1) 
read_qrcode_zbar(cv_image1)
# - 정상적으로 QR코드의 데이터와 QR코드의 위치값을 출력한다.
# - QRimage라는 이름의 이미지파일에 'qr_msaischool.png' 파일의 QR코드를 빨간색 선으로 인식범위가 표시된다.

