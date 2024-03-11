import tkinter as tk                        # Importing tkinter for GUI building
from PIL import ImageGrab                   # Importing ImageGrab from the Python Imaging Library (PIL). It is used to capture the screen.
import numpy as np                          # Importing numpy library and renaming it as np. It is commonly used for numerical operations in Python.
import cv2                                  # Importing OpenCV library. It is used for computer vision tasks, image processing and video analysis.
from win32api import GetSystemMetrics       # Importing GetSystemMetrics from the win32api module. It's used to get system metrics, like screen width and height for the system in use.
import datetime

# Setting Dimensions:
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

# Giving file name "ASR + Date and Time" at that particular moment:
time_label = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
file_name = f'ASR-{time_label}.mp4'

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = None
recording = False

def start_recording():
    global captured_video, recording
    recording = True
    captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

def stop_recording():
    global captured_video, recording
    recording = False
    cv2.destroyAllWindows()
    if captured_video is not None:
        captured_video.release()

# GUI using tkinter
root = tk.Tk()
root.title("ASM (2024)")

start_button = tk.Button(root, text="Start Recording", command=start_recording)
start_button.pack(pady=30)

stop_button = tk.Button(root, text="Stop Recording", command=stop_recording)
stop_button.pack(pady=30)

def capture_screen():
    global recording, captured_video
    if recording:
        img = ImageGrab.grab(bbox=(0, 0, width, height))
        img_np = np.array(img)
        img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        cv2.imshow('ASM (2024) - by Arcus', img_final)
        captured_video.write(img_final)
        cv2.waitKey(1)

    root.after(10, capture_screen)

# Start capturing screen
capture_screen()
root.state('zoomed')

root.mainloop()
