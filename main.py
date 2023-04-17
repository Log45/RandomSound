from playsound import playsound
import time
import random as rand
import os

sounds = list(filter(lambda x: ".mp3" in x, os.listdir(".")))
print(sounds)
def main():
    playsound("pipe.mp3")
    try:
        while True:
            interval = rand.randint(5, 600)
            idx = rand.randint(0, len(sounds))
            playsound(sounds[idx])
            time.sleep(interval)
    except KeyboardInterrupt:
        playsound()
        exit()


if __name__ == "__main__":
    main()
