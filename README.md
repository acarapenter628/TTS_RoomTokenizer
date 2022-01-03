# TTS_RoomTokenizer
A GIMP plugin for generating map tokens for use in Tabletop Simulator

## General Info

TTS_RoomTokenizer is a tool created to improve the experience of playing tabletop roleplaying games (such as Dungeons and Dragons or Pathinder) over the internet.  It is a plugin for GIMP (GNU Image Manipulation Program) written in Python that can be used to extract images of individual rooms from a larger game map.  Those extracted images can then be imported into the Tabletop Simulator software by Berserk Games and revealed as players discover them.

An [example image](https://i.imgur.com/4FDoNpw.jpg) of the output was provided by a Reddit user who tested the initial version of the script.

TTS_RoomTokenizer is only intended to be used on legally acquired digital maps.

## Installation and Usage Instructions
Instructions were written using GIMP v2.8.16 on Windows and may vary with other versions.  It has also been tested with v2.10.14 on Windows.

This has not been tested on OSX or Linux.  It is expected to work (with an additional manual step for OSX users in the instructions below), but it has not been confirmed.

* Copy RoomTokenizer.py your GIMP install directory.  On Windows, this is most likely C:\Program Files\GIMP 2.  It needs to go a few subfolders down, so for me, the full path is C:\Program Files\GIMP 2\lib\gimp\2.0\plug-ins.  If GIMP was already running, you'll need to restart it, and you should see a new option at the bottom of your Edit menu: "Export Selection"

* Open up your (legally acquired) map in GIMP and convert it to single layer image of just the rooms and the walls surrounding them with a transparent background.  There's not really a good way to automate this - you'll have to do it manually.  The Quick Mask (Shift + Q) and a large eraser are your friends here.  Save it as an xcf file (GIMP's default file format).
  * Depending on your map and your level of effort, you may also want to edit out any traps or hidden doors included on your map
  * You can use File -> Open to import a single page of a PDF file with a configurable resolution.  It defaults to 100 pixels per inch, which is probably lower resolution than you want.  I'm not sure the best way to find the native resolution of a PDF, so just increase the resolution by 100 until you start seeing diminishing returns.

* Next, you'll probably want to assign the script to a hotkey so you don't have to click through menus too many times (Edit -> Preferences -> Interface -> Configure Keyboard Shortcuts.  Search for "Export Selection" and assign it a hotkey)

* Now we can get started:  select the first room you want to export. Quick Mask and Rectangle Select (R) are your main tools here.  With the Rectangle Select, you can add to your current selection by holding Shift or subtract from it by holding Ctrl (on Windows, probably Command or whatever on Mac)

* **OSX Users:** In the same folder where you saved your xcf file earlier, create a folder with the same filename with "rooms" appended to the end.  For example, if you saved the xcf file as ExampleFile.xcf, create a subfolder called ExampleFilerooms.  This folder is generated automatically in Windows and Linux (untested on Linux)

* Hit that hotkey you selected earlier, and if we're on the right track, your selection should disappear.  In the folder where you saved your xcf file earlier, there should now be a folder with the same name as your xcf file with "rooms" appended to the end.  Rour room image is now inside that folder, titled room00000.png

* Repeat the process for every room

* Import the images into TTS as custom tokens.  Unfortunately, this must be done one by one.

* Put all your tokens into a hidden area, drag them out onto the main table when your players get to that room, and scale them to size (+/- keys).

## Caveats
* The XCF file must be a single layer when using this script (see issue #4)
* It is surprisingly difficult to find clear, concise documentation on GIMP scripting, so there is a nonzero amount of cargo cult code with some of the GIMP functions.  Specific examples are called out in issue #1
