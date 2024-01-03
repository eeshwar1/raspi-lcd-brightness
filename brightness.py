#!/usr/bin/python
import npyscreen
import os
import sys

class BrightnessForm(npyscreen.ActionPopup):

    FILE="/sys/class/backlight/rpi_backlight/brightness"
    def create(self):
        bf = open(self.FILE,"r")
        brighness_value = int(bf.readline())
        bf.close()
        self.brightness = self.add(npyscreen.TitleSlider, name = 'Brightness', out_of = 255, lowest=1, step=10, value=brighness_value)

    def on_ok(self):
        bf = open(self.FILE,"w")
        bf.write(str(int(self.brightness.value)))
        bf.close()
        self.parentApp.switchForm(None)

    def on_cancel(self):
        self.parentApp.switchForm(None)

class MyApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', BrightnessForm, name='Brightness', lines=5, columns=50)


def running_as_root() -> bool:
    return os.getuid() == 0



if __name__ == '__main__':
    if running_as_root():
        myApp = MyApplication()
        myApp.run()
    else:
        print("Please run as root")
        sys.exit(1)