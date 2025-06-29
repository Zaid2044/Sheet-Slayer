# Sheet Slayer 🐍📄🔥


Ever stared into the abyss of a 50-page PDF, a cursed `.jpeg` invoice, or a professor's scanned notes and felt your soul leave your body? The vibe is low. The task is NPC work. The grind is soul-crushing.

**Sheet Slayer** is a weapon against the mundane. It turns your webcam into an AI data entry intern that never sleeps, never complains, and gets it right every time. Point, shoot, and extract. Your boring task just got slayed.

## ✨ Features - The Vibe Check ✨

*   **👁️ The All-Seeing Eye:** A real-time webcam feed that serves as your window into the machine's vision.
*   **🧠 Instantaneous Brain Scan:** Hit `[SPACE]` to perform on-demand OCR on any frame. The AI reads what it sees, instantly.
*   **✅ Visualize the Matrix:** High-confidence text detections are highlighted with satisfying green bounding boxes. See what the AI sees.
*   **💾 The Final Slay:** Hit `[S]` to extract all detected text and forge it into a clean `slayed.csv` file, ready for Excel or your next script.
*   **📂 The Side Quest:** Don't have it live? Hit `[B]` to open a file browser and perform OCR on any static image file (`.png`, `.jpg`, etc.).
*   **🧼 Clean Slate Protocol:** Made a mistake? Hit `[C]` to instantly clear the detected boxes and start fresh.

## 🛠️ The Arsenal - Tech Stack 🛠️

*   **Language:** Python 🐍
*   **Computer Vision:** OpenCV (`opencv-python`)
*   **OCR Engine:** Google's Tesseract (`pytesseract`)
*   **GUI (File Browser):** Tkinter

## 📜 The Ritual - Installation & Setup 📜

Follow the sacred texts to awaken the Slayer on your own machine.

**1. Clone the Lair**
```bash
git clone https://github.com/Zaid2044/Sheet-Slayer.git
cd Sheet-Slayer
```

**2. Install the God Engine (Tesseract)**
*   This is the most critical step. pytesseract is just a wrapper. You need the engine itself.
*   Download the installer from the official Tesseract at UB-Mannheim repo.
*   un the installer. Make sure to check the box to add Tesseract to your system PATH. If you don't, it won't work.

**3. Create the Virtual Soul**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**4. Install the Arcane Libraries**
```bash
pip install -r requirements.txt
```

## ⚔️ How to Wield the Slayer ⚔️
*   Run the main script from your terminal:
```bash
python app.py
```
*    A window will appear with your webcam feed. Use the following controls:
**[SPACE]** - Scan: Captures the current frame and detects text.
**[S]** - Save: Saves the currently displayed text detections to slayed.csv.
**[C]** - Clear: Clears the bounding boxes from the screen.
**[B]** - Browse: Opens a file dialog to process a static image.
**[Q]** - Quit: Closes the application and returns you to the mortal realm.