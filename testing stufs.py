import cv2

camera_indexes = [0, 1, 2, 3, 4]
backends = [cv2.CAP_DSHOW, cv2.CAP_MSMF]

for backend in backends:
    print(f"Testing backend: {backend}")
    for index in camera_indexes:
        cap = cv2.VideoCapture(index, backend)
        if cap.isOpened():
            print(f"✅ Camera accessed at index {index} with backend {backend}")
            ret, frame = cap.read()
            if ret:
                cv2.imshow('Test Frame', frame)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            cap.release()
            break
        else:
            print(f"❌ Failed to access camera at index {index} with backend {backend}")
