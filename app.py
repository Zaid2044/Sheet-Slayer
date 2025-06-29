import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Sheet Slayer", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    
    if key == ord(' '):
        print("Frame captured!")

cap.release()
cv2.destroyAllWindows()