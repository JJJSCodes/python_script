# Two commands to import:
# python3 -m pip install pyserial
# python3 -m pip install pyautogui
# pip install opencv-python

# os is already built into python3

import serial
import pyautogui
import cv2
import os


serialPath = '/dev/cu.usbmodem14101' # Replace this with your arduino usb path. Should tell you on bottom right on arduino IDE if connected.
ser = serial.Serial(serialPath, 9600)
path = '/Users/jasonmei/Downloads' # SAVE THIS TO BE YOUR PATH YOU WANT
images_to_take = 1;
while True:
    reading = ser.readline().decode('utf-8')
    # reading is a string.
    if int(reading) == 1:
        for i in range(images_to_take):
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
            img_name = "capture{}.png".format(i + 1)
            while True:
                cv2.imshow('frame', rgb) # Will display screen showing the image it is going to take.
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("Done")
                    out = cv2.imwrite(os.path.join(path, img_name), frame)
                    break
            cap.release()
            cv2.waitKey(1)
            cv2.destroyAllWindows()
            for s in range(1, 5):
                cv2.waitKey(1)

    if int(reading) == 500:
        print(pyautogui.size())
        # Moves in relation to last position: pyautogui.moveRel(0, 50, duration=1)
        # Click at a position: pyautogui.click(100, 100)
        # Print current position: print(pyautogui.position())
        # Move the mouse absolute: pyautogui.moveTo(100, 100, duration=1)


