import numpy as np
import cv2

MHI_DURATION = 50
DEFAULT_THRESHOLD = 32


def show_mhi_mei(video_src: str) -> None:
    cv2.namedWindow("mhi")
    cv2.namedWindow("mei")
    cv2.namedWindow("raw")
    cv2.moveWindow("mhi", -5000, 5000)
    cv2.moveWindow("mei", 5000, -5000)
    cv2.moveWindow("raw", -5000, -5000)

    cam = cv2.VideoCapture(video_src)
    ret, frame = cam.read()
    h, w = frame.shape[:2]
    prev_frame = frame.copy()
    motion_history = np.zeros((h, w), np.float32)
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

        # mhi
        mhi = np.uint8(np.clip(motion_history, 0, 1) * 255)

        # mei
        mei = np.uint8(
            np.clip((motion_history - (timestamp - MHI_DURATION)) / MHI_DURATION, 0, 1)
            * 255
        )

        cv2.imshow("mhi", mhi)
        cv2.imshow("mei", mei)
        cv2.imshow("raw", frame)

        prev_frame = frame.copy()

        cv2.waitKey(100)

    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    video_src = "assets/example.avi"
    show_mhi_mei(video_src)
