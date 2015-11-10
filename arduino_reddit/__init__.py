# Author : Hemanth A
# Python Script To Check for New Messages on Reddit Account and Output to LED on Arduino


import os, serial, time, praw

class led_controller:
    def __init__(self, port=None):
        if os.name == 'nt':
            self.port = 'COM4'
        elif os.name == 'posix':
            self.port = '/dev/ttyACM0'

        if port is not None:
            self.port = port

        try:
            self.board = serial.Serial(self.port, 9600)
            time.sleep(2) # 2 second delay to wait for serial to initialize properly
            print("Board Connected Successfully")
        except:
            raise RuntimeError("Could Not Connect To The Arduino Board")

    def led_on(self):
        self.board.write(b'h')

    def led_off(self):
        self.board.write(b'z')

    def led_blink(self):
        self.board.write(b'b')

    def send(self, param):
        if isinstance(param, str):
            self.board.write(bytes(param, encoding='utf-8'))


class Daemon:

    def __init__(self, username=None, password=None, port=None):
        if port is not None:
            self.led = led_controller(port=port)
        else:
            self.led = led_controller()
        self.r = praw.Reddit(user_agent="MSGDaemon/Python")
        self.r.login(username, password, disable_warning=True)

    def get(self):
        msgs = self.r.get_unread(limit=1)
        return msgs

    def check(self):
        while True:
            mail = 0
            msg = self.get()
            for i in msg:
                mail = 1
            if mail == 1:
                print("New Mail!")
                self.led.led_on()
            else:
                print("No Mail")
                self.led.led_off()
            time.sleep(4)

def mailcheck(username=None,password=None, port=None):
    if username is not None and password is not None:
        if port is not None:
            Daemon(username,password, port).check()
        else:
            Daemon(username,password).check()
    else:
        print("Specify the username and password")
    
    

