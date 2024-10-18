import cv2 as cv

class VideoProcessor:
    def __init__(self, video_path):
        self.video_path = video_path

    def process_video(self):
        cap = cv.VideoCapture(self.video_path)

        while cap.isOpened():
            ret, frame = cap.read()

            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            cv.imshow('frame', gray)
            if cv.waitKey(1) == ord('q'):
                break

        cap.release()
        cv.destroyAllWindows()