import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 26
dataset_size = 100
frame_width = 640
frame_height = 480

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

for j in range(number_of_classes):
    class_symbol = chr(ord('A') + j)  # A-Z
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print('Collecting data for class {}'.format(class_symbol))

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to capture frame. Exiting...")
            break

        # Resize the frame
        frame = cv2.resize(frame, (frame_width, frame_height))

        # Show the class symbol (on a copy)
        display_frame = frame.copy()
        cv2.putText(display_frame, f'Symbol: {class_symbol}', (frame_width - 250, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2, cv2.LINE_AA)

        cv2.putText(display_frame, 'Press "Q" to start saving imgs', (50, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('frame', display_frame)

        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to capture frame. Exiting...")
            break

        frame = cv2.resize(frame, (frame_width, frame_height))

        display_frame = frame.copy()
        cv2.putText(display_frame, f'Symbol: {class_symbol}', (frame_width - 250, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow('frame', display_frame)
        cv2.waitKey(25)

        cv2.imwrite(os.path.join(class_dir, f'{counter}.jpg'), frame)
        counter += 1

cap.release()
cv2.destroyAllWindows()
