# Reddit Mail Checker For Arduino

Python Script to Check for New Messages on Reddit Account and Output to LED on Arduino

This is a simple script written in Python to check for unread messages on your reddit account and indicate it on an LED on PIN 13 on an Arduino.

The script uses the arudino serial via USB to communicate with the board.

This script was only tested on the Arduino Uno R3

## Installation

### Dependencies
1.) PRAW (Python Reddit API Wrapper)

    Linux: 
       > sudo pip install praw
  
    Windows:
       > pip install praw
  
2.) PySerial

    Linux:
       > sudo pip install pyserial
  
    Windows:
       > pip install pyserial
  

## Usage

  > An LED must be connected to the PIN 13 on the Arduino Board, doesn't have to be an LED in particular, you can connect any thing as long as it's output, like a buzzer.

  > Attach your Arduino board to your computer via USB.

  > Run the reddit_arduino.py script from your shell.

## Note

    The script is set to use the default serial port that the arduino uses based on the OS.

       > On Windows : COM4
    
        > On Linux : /dev/ttyACM0

    In case your arduino uses a different serial port, it can be easily changed in the reddit_arduino.py script
