# x32_flappybird
## Flappybird game on Behringer X32 digital mixer

Simple python script, that connects to X32 and turns it into Flappy Bird game console! (yeah, I was bored).
It started as a joke after friend showed me "Mardi Gras" Mode on StudioLive32 and I was like "I can do it on our X32" (show below),
and when I saw how simple it is to talk with the mixer, I was like "Do you want to play Flappy Bird on $2,000 mixer?".


Channel 1 mute button is used to jump up. Channel 1 fader represents the bird. 
Channels 2-15 represents map. Because it is hard to make two pipes (one from bottom and second from top) with one fader, the fader shows the gap between them you have to fly into.
There is one pipe every three faders, with mute used to indicate pipe.
Channel displays are used as binary score counter. Each time you fly through pipe, you get 1 point. If you hit the pipe or ground, game is over.


[![Behriinger X32 Flappy Bird](http://img.youtube.com/vi/ODJc2xbhxbE/0.jpg)](http://www.youtube.com/watch?v=ODJc2xbhxbE "Behriinger X32 Flappy Bird")

[Behringer X32 Flappy Bird on YoutTube](http://www.youtube.com/watch?v=ODJc2xbhxbE)


If you are worried about your faders, you can play the game on [Mixing Station](https://play.google.com/store/apps/details?id=com.davidgiga1993.mixingstation&hl=en)

[![Behringer X32 Flappy Bird in Mixing Station](http://img.youtube.com/vi/9u2JLGnquyg/0.jpg)](http://www.youtube.com/watch?v=9u2JLGnquyg "Behringer X32 Flappy Bird in Mixing Station")

[Behringer X32 Flappy Bird in Mixing Station on YouTube](http://www.youtube.com/watch?v=9u2JLGnquyg "Behringer X32 Flappy Bird in Mixing Station")


# X32 Waves
This just makes moving waves over the faders and does fancy stuff with displays. All channels and busses are affected. 
If you are running X32Edit on your PC, I reccomend to kill it. It likes to freeze once I run this.
[![Behringer X32 Waves](http://img.youtube.com/vi/a8QgwBLrPfk/0.jpg)](http://www.youtube.com/watch?v=a8QgwBLrPfk "Behringer X32 Waves")

[Behringer X32 Waves on YouTube](http://www.youtube.com/watch?v=a8QgwBLrPfk "Behringer X32 Waves")

# Requirements:
[python-osc](https://pypi.org/project/python-osc/)

# How to run it:
There are two files, one will make waves over the faders, second will run the flappy bird. Mixers IP is hard-writtend in the begging of the file, you can either edit it, or set your mixer to be at 192.168.100.20. 
Once you have python3 and python-osc installed, simply run `python 32flappybird.py`.
All the code was written fast, with no intention to share it, or use it again in the future. It is kinda sh*tty, but works. 
Did you heard about the sys.exit() command? 
Neither did I. So at game over, the script is terminated by throwing ZeroDivisionError exception. God help us all.
