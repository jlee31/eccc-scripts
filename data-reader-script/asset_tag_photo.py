import cv2 as cv
import easyocr
import os

reader = easyocr.Reader(['en'], gpu=False)

i = 41

while i > 34:
    image_path = f'images/10-27/{i}.png'
    result_file = f'pile5.txt'
    if not os.path.exists(image_path):
        print(f"No more images found after index {i-1}. Exiting.")
        break
    
    print(f"\nProcessing: {image_path}")

    image = cv.imread(image_path)
    if image is None:
        print(f"Could not read {image_path}. Skipping.")
        i += 1
        continue

    text_blocks = reader.readtext(image)
    
    # Read res.txt once per image
    if os.path.exists(result_file):
        with open(result_file, 'r') as f:
            existing_lines = {line.strip() for line in f}
    else:
        existing_lines = set()

    new_entries = []

    for _, (bbox, text, score) in enumerate(text_blocks):
        text = text.strip()

        if text.startswith('N7'):
            print(f"Detected N7 pattern: {text}")
            if text not in existing_lines:
                new_entries.append(text)
                print("Asset Tag added to file")
            else:
                print("Asset Tag already found")

        elif text.startswith('211') or text.startswith('910') or text.startswith('120') or text.startswith('Serial'):
            print(f"Detected pattern: {text}")
            if text not in existing_lines:
                new_entries.append(text)
                new_entries.append('')
                print("Serial num added to file")
            else:
                print("Serial num already found")

    with open(result_file, 'a') as f:
        f.write(str(i) + '\n')
    # Append new entries (if any)
    if new_entries:
        with open(result_file, 'a') as f:
            for entry in new_entries:
                f.write(entry + '\n')

    i -= 1