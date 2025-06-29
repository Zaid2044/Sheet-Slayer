import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cap = cv2.VideoCapture(0)
ocr_data = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if ocr_data:
        n_boxes = len(ocr_data['text'])
        for i in range(n_boxes):
            if int(ocr_data['conf'][i]) > 60:
                x, y, w, h = ocr_data['left'][i], ocr_data['top'][i], ocr_data['width'][i], ocr_data['height'][i]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Sheet Slayer", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    
    if key == ord(' '):
        ocr_data = pytesseract.image_to_data(frame, output_type=pytesseract.Output.DICT)
    
    if key == ord('c'):
        ocr_data = None

cap.release()
cv2.destroyAllWindows()