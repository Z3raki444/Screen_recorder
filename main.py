import threading

import cv2  # OpenCV library for computer vision tasks such as image and video processing.
import numpy as np  # NumPy library for numerical operations, used here to manipulate arrays.
import pyautogui  # PyAutoGUI library for GUI automation, used here to take screenshots.

# Define the screen resolution for the recording
import tkinter as tk  # Tkinter library for creating GUI elements

# Function to stop the recording
def stop_recording():
    global recording
    recording = False

# Create a Tkinter window
root = tk.Tk()
root.title("Screen Recorder")

# Create a button to stop the recording
stop_button = tk.Button(root, text="Stop Recording", command=stop_recording)
stop_button.pack()

# Variable to control the recording loop
recording = True

# Start the Tkinter main loop in a separate thread
tk_thread = threading.Thread(target=root.mainloop)
tk_thread.start()

# Wait for the Tkinter window to close
tk_thread.join()
resolution = (1920, 1080)

# Specify the codec to be used for the video
codec = cv2.VideoWriter_fourcc(*"XVID")

# Define the filename for the output video
filename = "Recording.avi"

# Set the frames per second (FPS) for the recording
fps = 60.0

# Create a VideoWriter object to save the recording
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Create a window to display the live feed
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)  

# Resize the display window for better visibility
cv2.resizeWindow("Live", 480, 270)

# Infinite loop to capture and process frames
while True:
    # Take a screenshot of the screen
    img = pyautogui.screenshot()

    # Convert the screenshot to a NumPy array
    frame = np.array(img)

    # Convert the color format from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write the frame to the output video file
    out.write(frame)

    # Display the live feed in the resized window
    cv2.imshow('Live', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the VideoWriter object to finalize the video
out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
