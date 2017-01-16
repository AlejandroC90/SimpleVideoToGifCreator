# SimpleVideoToGifCreator
A Python Script to create high quality gifs "without" so much trouble, works in Linux and Windows and uses ffmpeg.

It uses all the information from here [High Quality Gifs with Ffmpeg](http://blog.pkh.me/p/21-high-quality-gif-with-ffmpeg.html), I just put it an easy way.

## Download

Just download the gifcreator.py file or clone the repository.

## Dependeces

The script needs:
* python 3 [Python 3] (https://www.python.org/downloads/)
* ffmpeg [Ffmpeg Web Page](https://ffmpeg.org/)
* imagemagick (Optional, see "Tumblr Effect" below) [ImageMagick WebPage](https://www.imagemagick.org/script/index.php)


## Usage:

First move the script to the folder where your video is located and the open a terminal or command line.
Script name and then parameters.

    gifcreator.py MyVideoFileName.mkv 00:02 5 myfirstgif

Explanation:
* "MyVideoFileName.mkv", The Video name input
* "00:02", The Start time of the gif
* "5", The duration of the gif in seconds
* "myfirstgif", The gif name without extension

you can use more specific time, like: 01:00:03.15 1.75

And that's it, you get a clean gif with options by default:
![Awww gif](https://k61.kn3.net/1/0/E/0/1/D/42D.gif)

### What are the options by default?
- 12 frames per second
- and 500 px width 

and some filters that are explained in the original link, I'll add some way to change them in the future.


## Creating a swf instead of a gif
Just use the flag -s or --swf, something like this:

    gifcreator.py MyVideoFileName.mkv 00:02 5 mygif --swf

If will create the swf with options by default:

## Creating a gif with subtitles

We can do this by using the -sub or --subtitles flag, **for now only works with mkv files with embeded subtitles**, and it takes some time because it converts the video to a .mp4 with hardcoded subs and then create the gif from the video, so depending of the size of the video and the speed of your cpu it will take some time.
![Good Luck](https://k60.kn3.net/E/4/3/6/F/9/989.gif)

## Creating a swf with subtitles

Use the two flags -sub and -s


## The "Tumblr Effect"
I've seen that the gifs uploaded to tumblr usually get modified by changing the color curves of the image, I tried to replicate this using imagemagick as seen here [Color Modification ImageMagick](http://www.imagemagick.org/Usage/color_mods/)
So when we create a gif (specially from anime):
![Normal](https://k61.kn3.net/B/4/6/7/D/3/9E6.gif)

we can use the flag -tu or --tumblr to modify the colors as seen on the link, the result is something like this (I still need to tune it of find an easier way because **works differently depending of the scene colors**):

![Modified](https://k61.kn3.net/6/2/D/D/3/9/148.gif)

but it does something(I Think).

## Modifying Default Options
By using --help you can get all the info that you need, the most common used are:
- -f or --fps, You can specify the fps of the gif or swf
- -t or -tama, The size in pixeles for the width of the gif or swf
- -c or --calidad, This one is specific for swf files, for the -qscale flag in ffmpeg


# Contributing 

You can comment about everything, give some ideas, changes, improvements without no worries.

# Changing 

I still need to implement some things like adding some watermark to the gifs or being able to select the subtitles, so some things will  be added or changed in the future.

# Why did you did this?

Well, I like to create gifs from anime and movies so was searching for a way to make it simple using the console (I don't know if I made it more complicated), so I decided to try with a script and use some of my novice programming skills.

