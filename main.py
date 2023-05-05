from playsound import playsound
import time
import random as rand
import os

sounds = list(filter(lambda x: ".mp3" in x, os.listdir("./resources")))
sounds.remove("fuck.mp3") if "fuck.mp3" in sounds else None

file_dir = os.getcwd()
f = []
for sound in sounds:
    f.append(file_dir + "/resources/" + sound)
sounds = f

def main():
    try:
        while True:
            interval = rand.randint(5, 600)
            idx = rand.randint(0, len(sounds))
            time.sleep(interval)
            playsound(sounds[idx])
    except KeyboardInterrupt:
        playsound(file_dir + "/resources/fuck.mp3")
        exit()


if __name__ == "__main__":
    main()
