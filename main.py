import speech_recognition as sr
import asyncio


class MainRobow:
    def __init__(self) -> None:
        self.filter_words = ["follow me", "give me the cup", "give me the ball", ]

    async def speechRecognition(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            while True:
                print("Say something ... ")
                try:
                    audio = r.listen(source)
                    text = self.filterSpeech(r.recognize_google(audio))
                    if text is None:
                        print("Say somthing again, I can't recognize voice as valid Voice ...")
                        continue
                    elif text == "follow me":
                        pass
                    else:
                        pass
                    print("you say: ", text)

                except:
                    continue


    def filterSpeech(self, text):
        if text in self.filter_words:
            return text
        return None

    

if __name__ == "__main__":  
    robo = MainRobow()
    asyncio.run(robo.speechRecognition())