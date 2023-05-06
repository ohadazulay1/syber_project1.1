
from cv2 import *
import cv2
import time
from faceRecognition import Facial
from Emotion import Emotion

class Camera:
    filePlace = "C:/python/photos/test1.jpg"

    def __init__(self, emotion: Emotion):
        self.emotion = emotion

    def retFilePlace(self):
        return self.filePlace

    def mainProcess(self):
        lastEmotion = "start"
        print("starting...")
        fr = Facial()
        # cv2.namedWindow("preview")
        vc = cv2.VideoCapture(0)

        if vc.isOpened():  # try to get the first frame
            rval, frame = vc.read()
            # cv2.imshow("preview", frame)
        else:
            rval = False

        i = 0
        while rval:
            i = i + 1
            rval, frame = vc.read()
            cv2.imwrite(self.filePlace, frame)
            self.emotion.setEmotion(fr.whatFacialExpression(self.filePlace, frame, lastEmotion))

            print("cam emotion --> " + self.emotion.getEmotion())
            if self.emotion.getEmotion() != lastEmotion:
                print("cam emotion changed to --> " + self.emotion.getEmotion())
                lastEmotion = self.emotion.getEmotion()

            key = cv2.waitKey(500)
            if key == 27:  # exit on ESC
                break

    def finish(self):
        self.vc.release()
        cv2.destroyWindow("preview")

# if _name_ == "_main_":
    #   c = Camera()
    #  c.mainProcess()
    # c.finish()