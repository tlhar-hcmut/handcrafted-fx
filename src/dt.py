# Gunner Farneback’s algorithm

import cv2
import numpy as np


def show_dense_track(video_src: str) -> None:
    cap = cv2.VideoCapture(video_src)

    ret, frame1 = cap.read()
    prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    hsv = np.zeros_like(frame1)
    hsv[..., 1] = 255

    while 1:
        ret, frame2 = cap.read()
        if not ret:
            break

        next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

        flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)

        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        hsv[..., 0] = ang * 180 / np.pi / 2
        hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
        rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

        cv2.imshow("frame2", rgb)

        k = cv2.waitKey(100) & 0xFF
        if k == 27:
            break
        elif k == ord("s"):
            cv2.imwrite("opticalfb.png", frame2)
            cv2.imwrite("opticalhsv.png", rgb)
        prvs = next

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    show_dense_track("assets/example.avi")
