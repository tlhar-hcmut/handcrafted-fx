import cv2


def show_sift(video_src: str) -> None:
    cap = cv2.VideoCapture(video_src)
    sift = cv2.xfeatures2d.SIFT_create()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        keypoints = sift.detect(gray, None)

        img = cv2.drawKeypoints(gray, keypoints, frame)

        cv2.imshow("sift", img)

        cv2.waitKey(100)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    video_src = "assets/example.avi"
    show_sift(video_src)