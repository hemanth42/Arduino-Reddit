# Reddit Mail Checker For Arduino

Python Script to Check for New Messages on Reddit Account and Output to LED on Arduino

This is a simple script written in Python to check for unread messages on your reddit account and indicate it on an LED on PIN 13 on an Arduino.

The script uses the arduino serial via USB to communicate with the board.

This script was only tested on the Arduino Uno R3.

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
  
      > First and foremost, upload the code in the serial.ino file into your Arduino board
  
      > An LED must be connected to the PIN 13 on the Arduino Board, doesn't have to be an LED in particular, you can connect any thing as long as it's output, like a buzzer.

      > Attach your Arduino board to your computer via USB.
  
      > Go to the reddit_arduino.py script and set your Reddit username and password by editing this line: 
           a = daemon("username", "password")

      > Run the reddit_arduino.py script from your shell.

## Note

    The script is set to use the default serial port that the arduino uses based on the OS.

       > On Windows : COM4
    
       > On Linux : /dev/ttyACM0

    In case your arduino uses a different serial port, it can be easily changed in the reddit_arduino.py script by editing this line:
    
        > self.led = led_controller()
        
        Change that line into:
        
        > self.led = led_controller(port=COM1)
        
        You can pass a the keyword parameter *port* and manually assign the port number
        In Windows, it's this series: COM1, COM2, COM3 ...
        
        In Linux, /dev/ttyACM0, /dev/ttyACM1, /dev/ttyACM2 ...
