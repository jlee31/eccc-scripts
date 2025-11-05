import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'], gpu=True)

# Open webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Prepare matplotlib window
plt.ion()  # interactive mode on
fig, ax = plt.subplots()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Run OCR on the frame
    results = reader.readtext(frame)

    # Draw bounding boxes and text on the frame
    for (bbox, text, score) in results:
        if score > 0.25:
            top_left = tuple([int(val) for val in bbox[0]])
            bottom_right = tuple([int(val) for val in bbox[2]])
            cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
            cv2.putText(frame, text, (top_left[0], top_left[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

            # Example: detect specific patterns
            if text.startswith('N7'):
                print(f"Detected N7 pattern: {text}")
            elif text.startswith('211'):
                print(f"Detected 211 pattern: {text}")

    # Convert BGR to RGB for Matplotlib
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the frame in the Matplotlib window
    ax.imshow(frame_rgb)
    plt.axis('off')
    plt.pause(0.001)  # short pause for frame update
    ax.clear()

    # Exit if you press Ctrl+C in terminal
    # (matplotlib doesn’t handle key events well for cv2-like behavior)

# Clean up
cap.release()
plt.close()
