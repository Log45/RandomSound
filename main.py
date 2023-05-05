from playsound import playsound
import time
import random as rand
import os

sounds = list(filter(lambda x: ".mp3" in x, os.listdir(".")))
sounds.remove("fuck.mp3") if "fuck.mp3" in sounds else None

file_dir = os.getcwd
fuck = []
for sound in sounds:
    file_dir = os.getcwd()
    fuck.append(file_dir + "/" + sound)

sounds = fuck

def main():
    try:
        while True:
            interval = rand.randint(5, 15)
            idx = rand.randint(0, len(sounds))
            time.sleep(interval)
            playsound(sounds[idx])
    except KeyboardInterrupt:
        playsound(file_dir + "/fuck.mp3")
        exit()


if __name__ == "__main__":
    main()
