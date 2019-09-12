# healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 liters) - Drank - every 30 minute - log
# Eyes - eyes.mp3 - every 30 min - EyDone - log
# Physical activity - physical.mp3 - every - 435 minutes - ExDone - log
# rules
# Pygame module play audio

from pygame import mixer
def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

if __name__ == '__main__':
    musiconloop("eyes.mp3", "stop")