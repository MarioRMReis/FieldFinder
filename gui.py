import cv2
import numpy as np
from cv2_gui import create_button_manager, create_toggle_button

class ButtonManager:
    def __init__(self):
        self.buttons = [
            {'name': 'Load', 'pos': (10, 10), 'size': (60, 30), 'label': 'Load'},
            {'name': 'Quit', 'pos': (750, 10), 'size': (60, 30), 'label': 'Quit'},
            {'name': 'Conf.', 'pos': (80, 10), 'size': (90, 30), 'label': 'Confirm'},
        ]
        # Arrow button properties
        self.arrow_size = 40  # Size of the arrow
        self.arrow_margin = 20  # Distance from edge


    def draw_buttons(self, img):
        for btn in self.buttons:
            color = (200, 200, 200) 
            cv2.rectangle(img, btn['pos'],
                          (btn['pos'][0] + btn['size'][0], btn['pos'][1] + btn['size'][1]),
                          color, -1)
            cv2.putText(img, btn['label'],
                        (btn['pos'][0] + 10, btn['pos'][1] + 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
        h, w = img.shape[:2]
        s = self.arrow_size
        m = self.arrow_margin

        # Left arrow (Prev)
        left_center = (m, h // 2)
        left_pts = np.array([
            [left_center[0] + s // 2, left_center[1] - s // 2],
            [left_center[0] + s // 2, left_center[1] + s // 2],
            [left_center[0] - s // 2, left_center[1]]
        ], np.int32)
        cv2.polylines(img, [left_pts.reshape((-1, 1, 2))], True, (0, 0, 0), 2)
        

        # Right arrow (Next)
        right_center = (w - m, h // 2)
        right_pts = np.array([
            [right_center[0] - s // 2, right_center[1] - s // 2],
            [right_center[0] - s // 2, right_center[1] + s // 2],
            [right_center[0] + s // 2, right_center[1]]
        ], np.int32)
        cv2.polylines(img, [right_pts.reshape((-1, 1, 2))], True, (0, 0, 0), 2)

    def check_click(self, x, y, img_shape):
        # Check rectangle buttons
        for btn in self.buttons:
            if (btn['pos'][0] <= x <= btn['pos'][0] + btn['size'][0] and
                btn['pos'][1] <= y <= btn['pos'][1] + btn['size'][1]):
                return btn['name']
        # Check arrow buttons
        h, w = img_shape[:2]
        s = self.arrow_size
        m = self.arrow_margin

        # Left arrow triangle
        left_center = (m, h // 2)
        left_pts = np.array([
            [left_center[0] + s // 2, left_center[1] - s // 2],
            [left_center[0] + s // 2, left_center[1] + s // 2],
            [left_center[0] - s // 2, left_center[1]]
        ], np.int32)
        if cv2.pointPolygonTest(left_pts, (x, y), False) >= 0:
            return 'Prev'

        # Right arrow triangle
        right_center = (w - m, h // 2)
        right_pts = np.array([
            [right_center[0] - s // 2, right_center[1] - s // 2],
            [right_center[0] - s // 2, right_center[1] + s // 2],
            [right_center[0] + s // 2, right_center[1]]
        ], np.int32)
        if cv2.pointPolygonTest(right_pts, (x, y), False) >= 0:
            return 'Next'
        
        