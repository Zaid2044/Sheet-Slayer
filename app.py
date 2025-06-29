import cv2
import pytesseract
import csv
from tkinter import Tk, filedialog

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def process_image_and_get_data(frame):
    data = pytesseract.image_to_data(frame, output_type=pytesseract.Output.DICT)
    return data

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
        ocr_data = process_image_and_get_data(frame)
    
    if key == ord('c'):
        ocr_data = None
    
    if key == ord('s') and ocr_data:
        extracted_text = []
        n_boxes = len(ocr_data['text'])
        for i in range(n_boxes):
            if int(ocr_data['conf'][i]) > 60:
                extracted_text.append(ocr_data['text'][i])
        
        full_text = " ".join(extracted_text)
        if full_text.strip():
            with open('slayed.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Extracted Text'])
                writer.writerow([full_text])
            
            cv2.putText(frame, "SAVED TO slayed.csv", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow("Sheet Slayer", frame)
            cv2.waitKey(1000)
    
    if key == ord('b'):
        Tk().withdraw()
        filepath = filedialog.askopenfilename()
        if filepath:
            img = cv2.imread(filepath)
            if img is not None:
                img_data = process_image_and_get_data(img)
                
                n_boxes = len(img_data['text'])
                for i in range(n_boxes):
                    if int(img_data['conf'][i]) > 60:
                        x, y, w, h = img_data['left'][i], img_data['top'][i], img_data['width'][i], img_data['height'][i]
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
                cv2.imshow("Processed Image", img)
                cv2.waitKey(0)
                cv2.destroyWindow("Processed Image")

cap.release()
cv2.destroyAllWindows()