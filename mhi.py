import numpy as np
import cv2, time

MHI_DURATION = 50
DEFAULT_THRESHOLD = 32


if __name__ == "__main__":
    video_src = "assets/example.avi"
    cv2.namedWindow("motion-history")
    cv2.namedWindow("raw")

    cam = cv2.VideoCapture(video_src)
    ret, frame = cam.read()
    prev_frame = frame.copy()
    motion_history = np.zeros((frame.shape[0], frame.shape[1]), np.float32)
    timestamp = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            break
        frame_diff = cv2.absdiff(frame, prev_frame)
        gray_diff = cv2.cvtColor(frame_diff, cv2.COLOR_BGR2GRAY)
        ret, fgmask = cv2.threshold(gray_diff, DEFAULT_THRESHOLD, 1, cv2.THRESH_BINARY)
        timestamp += 1

        # update motion history
        cv2.motempl.updateMotionHistory(fgmask, motion_history, timestamp, MHI_DURATION)

        # normalize motion history
        mh = np.uint8(
            np.clip((motion_history - (timestamp - MHI_DURATION)) / MHI_DURATION, 0, 1)
            * 255
        )

        cv2.imshow("motion-history", mh)
        cv2.imshow("raw", frame)

        prev_frame = frame.copy()

        cv2.waitKey(100)

    cv2.destroyAllWindows()