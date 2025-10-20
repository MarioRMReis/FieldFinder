import cv2
import gui
from pdf2image import convert_from_path
import tkinter as tk
import numpy as np
from tkinter import filedialog
from tkinter import simpledialog

#! Buttons____________________________________________________________
def Load_pdf_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
   
    return file_path

def Load_pdf(pdf_path):
    global boxes
    pdf_png_PIL = convert_from_path(pdf_path, poppler_path="C:\\poppler\\Library\\bin")
    return pdf_png_PIL

def Quit_program():
    cv2.destroyAllWindows()
    exit()

def get_text_input(prompt="Enter text:"):
    root = tk.Tk()
    root.withdraw()
    user_input = simpledialog.askstring("Input", prompt)
    root.destroy()
    return user_input

def mouse_callback(event, x, y, flags, param):
    global boxes, pending_box, drawing, x_start, y_start, pdf_PIL, current_page, num_pages
    if event == cv2.EVENT_LBUTTONDOWN:
        btn = button_manager.check_click(x, y, pdf_png.shape)
        if btn == 'Conf.':
            if pending_box is not None:
                boxes[current_page].append(pending_box)
                pending_box = None
        elif btn == 'Quit':
            Quit_program()
        elif btn == 'Load':
            pdf_path = Load_pdf_path()
            current_page  = 0
            pdf_PIL = Load_pdf(pdf_path)
            num_pages = len(pdf_PIL)
            boxes = [[] for _ in range(num_pages)]
        elif btn == 'Prev':
            if current_page == 0:
                current_page = 0
            else:
                current_page -= 1
        elif btn == 'Next':
            if current_page == num_pages-1:
                current_page = num_pages-1
            else:
                current_page += 1     
        elif btn == 'Save_config':
            pass
        elif btn == 'Load_config':
            pass
        else:
            # Not a button: start drawing rectangle
            drawing = True
            x_start, y_start = x, y
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        img = pdf_png.copy()
        for box in boxes[current_page]:
            cv2.rectangle(img, box[0], box[1], (0, 255, 0), 2)
        cv2.rectangle(img, (x_start, y_start), (x, y), (0, 255, 0), 2)
        pending_box = ((x_start, y_start), (x, y))
    elif event == cv2.EVENT_LBUTTONUP and drawing:
        drawing = False
        pending_box = ((x_start, y_start), (x, y))

def main():
    global boxes, pdf_png, drawing, button_manager, pending_box, pdf_PIL, current_page, num_pages
    
    pdf_path = Load_pdf_path()
    drawing = False
    current_page  = 0
    pdf_PIL = Load_pdf(pdf_path)
    num_pages = len(pdf_PIL)
    boxes = [[] for _ in range(num_pages)]
    pending_box = None
    
    while True:
        pdf_png = cv2.cvtColor(np.array(pdf_PIL[current_page]), cv2.COLOR_RGB2BGR)
        if pdf_png.shape[1] > 1080:
            img_height, img_width = pdf_png.shape[:2]
            scale = 1080 / img_height
            new_width = int(img_width * scale)
            pdf_png = cv2.resize(pdf_png, (new_width, 1080), interpolation=cv2.INTER_AREA)
            
        cv2.namedWindow('PDF Reader', cv2.WINDOW_NORMAL)
        cv2.setMouseCallback('PDF Reader', mouse_callback)
        button_manager = gui.ButtonManager()   

        display_img = pdf_png.copy()
        # Draw confirmed rectangles
        for box in boxes[current_page]:
            cv2.rectangle(display_img, box[0], box[1], (0, 255, 0), 2)
        # Draw pending box (not yet confirmed)
        if pending_box is not None:
            cv2.rectangle(display_img, pending_box[0], pending_box[1], (0, 255, 255), 2)  # Yellow for pending
        # Draw buttons
        gui.ButtonManager.draw_buttons(button_manager, display_img)
        cv2.imshow('PDF Reader', display_img)
        if cv2.waitKey(20) & 0xFF == 27:  # ESC to exit
            break
    cv2.destroyAllWindows()
    
def files_init_():
    pass

if __name__ == "__main__":
    files_init_()
    main()
    