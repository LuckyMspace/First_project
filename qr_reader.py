import cv2  
import pyzbar.pyzbar as pyzbar 


def read_qrcode_cv2(opencv_image):
    detector = cv2.QRCodeDetector()
    data, rect, _ = detector.detectAndDecode(opencv_image)
    if data:
        print("QRCODE DATA: {}".format(data))
        print("QRCODE LOCATION: {}".format(rect))

        lefttop = (int(rect[0][0][0]), int(rect[0][0][1]))
        rightbottom = (int(rect[0][2][0]), int(rect[0][2][1]))
        cv2.rectangle(opencv_image, lefttop, rightbottom, (0, 0, 255), 5) 
        cv2.imshow("QRimage", opencv_image)
        cv2.waitKey(0)  
        cv2.destroyAllWindows() 

def read_qrcode_zbar(opencv_image):
    gray = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)
    decoded = pyzbar.decode(gray,error_correction = pyzbar.ZBarSymbol.E) 
    for d in decoded:
        x, y, w, h = d.rect
        qrcode_data = d.data.decode("utf-8")
        qrcode_type = d.type
        cv2.rectangle(opencv_image, (x, y), (x + w, y + h), (0, 0, 255), 3) 
        text = "{} {}".format(qrcode_data, qrcode_type)
        cv2.putText(opencv_image, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0 ,255), 1, cv2.LINE_AA)
        
    cv2.imshow("QRimage2", opencv_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    filepath = "qr_msaischool.png"  
    cv_image1 = cv2.imread(filepath) 

    read_qrcode_zbar(cv_image1)


def read_qrcode_webcam():
    cap = cv2.VideoCapture(0) 
    i = 0
    while(cap.isOpened()): 
        ret, img = cap.read()
        if not ret:
            print("ERROR")
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        decoded = pyzbar.decode(gray)
        for d in decoded:
            x, y, w, h = d.rect
            qrcode_data = d.data.decode("utf-8")
            qrcode_type = d.type
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3) 
            text = "{} {}".format(qrcode_data, qrcode_type)
            cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0 ,255), 1, cv2.LINE_AA)
        cv2.imshow("IMG",img)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break
        elif key == ord("s"):
            cv2.imwrite("c_{}.jpg".format(i), img)
            i += 1
    cap.release()
    cv2.destroyAllWindows()

read_qrcode_webcam() 