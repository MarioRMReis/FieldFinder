# PDF Reader & Text Extractor (GUI-based)

This project is a graphical PDF reader and text extractor built with **OpenCV**, **Tkinter**, and **Tesseract OCR**.
It allows users to load PDF files, define bounding boxes on pages to extract text, save/load configurations, and export extracted text to CSV files.

---

## Features

* Load and display PDF files as images using `pdf2image`
* Draw bounding boxes directly on the PDF to select text regions
* Save and load configurations of selected boxes as `.json` presets
* Extract text from the defined boxes using **Tesseract OCR**
* Export extracted data to `.csv` format
* Navigate between PDF pages using GUI arrows
* Error handling and feedback via OpenCV pop-up overlays

---

## Requirements

Make sure you have the following installed:

```bash
pip install opencv-python pdf2image pytesseract pillow numpy tk
```

### Additional Dependencies

**Tesseract OCR**

* Download: [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
* Default path in code:

  ```python
  pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
  ```
* Update this path if Tesseract is installed elsewhere.

**Poppler for Windows**
Required by `pdf2image` to convert PDF pages to images.
Download and extract from: [https://github.com/oschwartz10612/poppler-windows](https://github.com/oschwartz10612/poppler-windows)

Update this line in `main.py` with your Poppler path:

```python
pdf_png_PIL = convert_from_path(pdf_path, poppler_path="C:\\poppler\\Library\\bin")
```

---

## Usage

1. Run the application:

   ```bash
   python main.py
   ```
2. Load a PDF file using the **Load File** button.
3. Draw boxes with your mouse around text areas you want to extract.
4. Confirm boxes using the **Conf.Box** button.
5. Save configurations (**Save Confg.**) to reuse your selection setup later.
6. Load configurations (**Load Confg.**) to restore saved boxes.
7. Extract text using the **Get Info** button.
   Extracted text is saved as a `.csv` file inside the `information_files/` directory.
8. Navigate pages using the left/right arrow buttons.
9. Quit the program using the **Quit** button or by pressing `ESC`.

---

## Project Structure

```
.
├── main.py               # Core application logic and event loop
├── gui.py                # GUI components (buttons, flash messages)
├── presets/              # (auto-created) stores saved box configurations
└── information_files/    # (auto-created) stores extracted text CSVs
```

---

## GUI Controls Overview

| Button          | Description                         |
| --------------- | ----------------------------------- |
| **Load File**   | Open and display a PDF              |
| **Conf.Box**    | Confirm the current box             |
| **Save Confg.** | Save current boxes to a JSON preset |
| **Load Confg.** | Load a saved JSON preset            |
| **Get Info**    | Run OCR and export text to CSV      |
| **← / →**       | Navigate between pages              |
| **Quit**        | Exit the program                    |

---

## Customization

You can modify:

* Button layout → `gui.py` → `ButtonManager` class
* Poppler and Tesseract paths → `main.py`
* Output directories → change where CSV and JSON files are saved

---

## License

This project is licensed under the **MIT License** — feel free to use and modify it.

---

Would you like me to fill in your **name**, **email**, and **GitHub link** before I save it as a downloadable `README.md` file?
