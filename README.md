# Reddit Mail Checker For Arduino

Python Script to Check for New Messages on Reddit Account and Output to LED on Arduino

This is a simple script written in Python to check for unread messages on your reddit account and indicate it on an LED on PIN 13 on an Arduino.

The script uses the arduino serial via USB to communicate with the board.

This script was only tested on the Arduino Uno R3.

## Installation
    
    Linux: 
       > sudo python3 setup.py install
  
    Windows:
       > python setup.py install
       
### Note on Dependencies

These dependencies will be automatically installed, failing which, you can manually install them by typing these commands in your terminal/prompt: 

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
  
      > Open up your Python Console and type:
          >> import arduino_reddit
          >> arduino_reddit.mailcheck("username","password")

      > Alternatively, you can run the checkmail.py script included in the repo which will prompt you for your username and password(which can also be passed as command line arguments depending upon your choice)
         $ python checkmail.py username password
      Additionally, you can manually assign the serial port number your arduino board uses by passing an extra argument:
         $ python checkmail.py username password port
      

## Note

    The script is set to use the default serial port that the arduino uses based on the OS.

       > On Windows : COM4
    
       > On Linux : /dev/ttyACM0

    In case your arduino uses a different serial port, you can manually assign the serial port number your arduino board uses by passing an extra argument:
    
          >> import arduino_reddit
          >> arduino_reddit.mailcheck("username","password","COM4")
        
        
        In Windows, it's this series: COM1, COM2, COM3 ...
        
        In Linux, /dev/ttyACM0, /dev/ttyACM1, /dev/ttyACM2 ...
