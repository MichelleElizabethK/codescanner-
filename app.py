#Code Scanner

#Accessing camera
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        camera.export_to_png("input.png")
        print("Captured")


class TestCamera(App):

    def build(self):
        return CameraClick()

TestCamera().run()

#OCR recognition
import pytesseract
from PIL import Image
text=(pytesseract.image_to_string(Image.open('/home/michelle/Kivy-1.10.1/examples/angelhack/download.png')))
f = open('code.c','w')
f.write(text)
f.close()

#Text Editor
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

import os


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
       content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
       self._popup = Popup(title="Load file", content="code.c",
                           size_hint=(0.9, 0.9))
       self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content="code.c",
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path):
        filename="code.c"
        with open(os.path.join(path, filename[0])) as stream:
            self.text_input.text = stream.read()

        self.dismiss_popup()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.text_input.text)

        self.dismiss_popup()


class Editor(App):
    def factory(self):
	Factory.register('Root', cls=Root)
	Factory.register('LoadDialog', cls=LoadDialog)
	Factory.register('SaveDialog', cls=SaveDialog)

Editor().run()


import subprocess
import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.label import Label


import sys
f = open("output.txt", 'w')
sys.stdout = f

cmd = "code.c"

print ("C code output\n")
#Compile the code
subprocess.call(["gcc",cmd])
subprocess.call("./a.out")
f.close()


