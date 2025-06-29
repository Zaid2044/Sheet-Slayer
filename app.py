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
        text = pytesseract.image_to_string(frame)
        data = pytesseract.image_to_data(frame, output_type=pytesseract.Output.DICT)
        n_boxes = len(data['text'])
        for i in range(n_boxes):
            if int(data['conf'][i]) > 60:
                x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if text.strip():
            print("--- OCR Result ---")
            print(text)
            print("--------------------")

cap.release()
cv2.destroyAllWindows()