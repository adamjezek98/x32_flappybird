from pythonosc import udp_client
import time
import math
import random

client = udp_client.SimpleUDPClient("192.168.100.20", 10023)


def ch_floating_zero(ch):
    return ("0" + str(ch))[-2:]


def set_ch_on(ch, on):
    ch = ch_floating_zero(ch)
    client.send_message("/ch/" + ch + "/mix/on", "OFF" if on else "ON")


def set_fader(ch, val):
    ch = ch_floating_zero(ch)
    client.send_message("/ch/" + ch + "/mix/fader", val)


def set_ch_color(ch, col):
    ch = ch_floating_zero(ch)
    client.send_message("/ch/" + ch + "/config/color", col)


def set_ch_name(ch, name):
    ch = ch_floating_zero(ch)
    client.send_message("/ch/" + ch + "/config/name", name)


colors = ["OFF", "GN", "RD", "YE", "BL", "MG", "CY", "WH", "OFFi"]
remapper = {0: 0, 199: 1, 391: 2, 568: 3, 724: 4, 851: 5, 946: 6, 1004: 7, 1024: 8}

map = [0] * 15
lastMove = 0
moveDelay = 1
MAX_HEIGHT = 1024

global bird, lastBird

bird = 2024
lastBird = 0
lastBirdFall = 0

score = 0


def moveMap():
    global score

    if map[0]:
        print("crash", bird, map[0])
        if (map[0] - 200 < bird and map[0] + 200 > bird):
            score += 1
        else:
            gameOver()
            a = 1 / 0

    for i in range(len(map) - 1):
        map[i] = map[i + 1]
    map[-1] = 0


def addHole():
    if map[-1] + map[-2] + map[-3] == 0:
        map[-1] = int((MAX_HEIGHT / 8) * random.randint(2, 8))
        # print("adding hole")


def drawMap():
    # print(map)
    for i in range(len(map)):
        set_fader(i + 2, map[i])
        set_ch_on(i + 2, map[i])


def drawBird():
    set_fader(1, bird)


def drawScore():
    global score

    scorestring = ("0" * 17) + "{0:b}".format(score)
    for i in range(1, 17):
        set_ch_color(i, colors[int(scorestring[-i])])


def checkButton():
    client.send_message("/xremote", 0)
    global bird, lastBird
    while 1:
        try:
            msg = client._sock.recv(1024)

            if str(msg, "utf8").startswith("/ch/01/mix/on"):
                if not msg[-1]:
                    # print("bird should go up", lastBird, time.time())
                    # if lastBird + 0.01 < time.time():
                    # print("bird up")
                    bird += 150
                    if bird > MAX_HEIGHT:
                        bird = MAX_HEIGHT
                    drawBird()
                    set_ch_on(1, 0)
                    lastBird = time.time()

        except(BlockingIOError, UnicodeDecodeError):
            break


def gameOver():
    for i in range(1, 17):
        set_fader(i, 0)
    for _i in range(5):
        for i in range(1, 17):
            set_ch_on(i, 1)
        drawScore()
        time.sleep(0.2)
        for i in range(1, 17):
            set_ch_on(i, 0)
            set_ch_color(i, colors[0])
        time.sleep(0.2)


for i in range(16):
    set_ch_name(i + 1, str(2 ** i))

while 1:
    if lastMove + moveDelay < time.time():
        moveMap()
        lastMove = time.time()
        addHole()
        drawMap()
        drawScore()
    if lastBird + 0.1 < time.time():
        bird -= 20
        if bird < 0:
            gameOver()
            a = 1 / 0
    drawBird()
    checkButton()
    time.sleep(0.05)
