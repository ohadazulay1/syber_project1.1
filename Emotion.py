class Emotion:

    HAPPY = 'happy'
    SAD = "sad"
    INITIAL_STATE = HAPPY

    def __init__(self):
        self.emotion = self.INITIAL_STATE

    def setHappy(self):
        self.emotion = self.HAPPY


    def setSad(self):
        self.emotion = self.SAD


    def setEmotion(self, emotion: str):
        self.emotion = emotion

    def getEmotion(self) -> str:
        return self.emotion