from threading import Thread
from time import sleep
from Emotion import Emotion
from signInWin import Ui_firstWindow
from theMainWindow1 import Ui_MainWindow
from computerCam import Camera
from graphics import Graphics
print("starr")
startingWindows = Ui_firstWindow()
print("ended")
mainWindow = Ui_MainWindow()
emotion = Emotion()

cp = Camera(emotion)
camThread = Thread(target=cp.mainProcess)
camThread.start()

gr = Graphics(emotion)
gr.objectsManeger()

camThread.join()

#thread1 = Thread(target=cp.mainProcess)
#thread2 = Thread(target=gr.objectsManeger)
#thread3 = Thread(target=gr.playerManeger(), args=["happy"])
#thread1.start()
#thread2.start()
#thread3.start()