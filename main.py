from playsound import playsound
import time
import random as rand


def main():
    while True:
        interval = rand.randint(5, 600)
        time.sleep(interval)
        playsound("calmdown.mp3")


if __name__ == "__main__":
    main()
