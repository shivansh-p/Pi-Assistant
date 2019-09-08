import speech_recognition as sr
import platform

r = sr.Recognizer()
platform = platform.system()
if platform == 'Windows':
    print("I'm on Windows!")
    mic = sr.Microphone()
elif platform == 'Linux':
    print("I'm on Pi! Finding mic...")
    mic = sr.Microphone()

with mic as source:
    #r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    snippet = r.recognize_sphinx(audio)
    if "hello pie" in snippet or "hello pi" in snippet:
        print("Hello, David!")
    else:
        print("This is what I heard: ")
        print(snippet)
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
