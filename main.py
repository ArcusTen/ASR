import cv2
import datetime
import numpy as np
import tkinter as tk
from PIL import ImageGrab
from win32api import GetSystemMetrics

# Setting Dimensions:
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

# Giving file name "ASR + Date and Time" at that particular moment:
time_label = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
file_name = f'ASR-{time_label}.mp4'

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
capturedVideo = None
recording = False

def startRecording():
    global capturedVideo, recording
    recording = True
    capturedVideo = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

def stopRecording():
    global capturedVideo, recording
    recording = False
    if capturedVideo is not None:
        capturedVideo.release()

# GUI 
root = tk.Tk()
root.title("ASR v2024.1.0.0 - Beta")
# root.iconbitmap("./assets/favicon.ico")
root.configure(bg="#8e929c")


def createButton(parent, text, command):
    button = tk.Button(root,
                       text=text, 
                       fg="white", 
                       bg="#13eb74" if text == "Start Recording" else "#b01c12",
                    #    command=command, font=("Segoe Script", 30, "bold"))
                       command=command, font=("Poppins", 30, "bold"))
    button.pack(pady=50)


createButton(root, "Start Recording", startRecording)
createButton(root, "Stop Recording", stopRecording)

def captureScreen():
    global recording, capturedVideo
    if recording:
        img = ImageGrab.grab(bbox=(0, 0, width, height))
        img_np = np.array(img)
        img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        capturedVideo.write(img_final)

    root.after(10, captureScreen)

if __name__ == "__main__":
    captureScreen()
    root.state('zoomed')
    root.mainloop()
