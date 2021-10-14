import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
  r.adjust_for_ambient_noise(source)  # here
  print("Say something!")
  audio = r.listen(source)
  print(audio)
  print(r.recognize_google(audio))