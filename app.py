import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cap = cv2.VideoCapture(0)
ocr_data = None


while True:
    ret, frame = cap.read()
    if not ret:
        break

    # We need to add the drawing logic here too
    
    cv2.imshow("Sheet Slayer", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    
    if key == ord(' '):
        # The processing logic stays here
        pass

cap.release()
cv2.destroyAllWindows()