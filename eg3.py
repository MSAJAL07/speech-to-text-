import sys
import speech_recognition as sr
import subprocess
command = "ffmpeg -i ./vid2.mp4 -ab 160k -ac 2 -ar 44100 -vn vid_a.wav"
subprocess.call(command, shell=True)
r = sr.Recognizer()
with sr.AudioFile('vid_a.wav') as source:
 audio = r.record(source)

 command = r.recognize_google(audio)
 print(command)
