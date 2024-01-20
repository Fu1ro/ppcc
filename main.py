from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, \
    QHBoxLayout, QVBoxLayout, QFormLayout
from PIL import Image, ImageFilter

class ImageEditor():
     def __init__(self, name):
          self.name = name
          self.original = None
          self.changed = list()
     def open(self):
       try:
          self.original = Image.open(self.name)
          self.original.show()
       except FileNotFoundError as err:
          print(err)
     def do_cropped(self):
       box = (100, 100, 400, 450)
       cropped = self.original.crop(box)
       cropped.save("cropped.jpg")
       cropped.show()
     def do_left(self):
       rotate = self.original.transform(Image.ROTATE_90)
       rotate.save("rotate.jpg")
       rotate.show()
    

im = ImageEditor("tiger.jpg")
im.open()
im.do_cropped()
im.do_left()
#ith Image.open("tiger.jpg") as im:
 #   print(f' Розмір: {im.size} \n Формат: {im.format}')
  #   pic_gray = im.convert('L')
   #  pic_blured = im.filter(ImageFilter.BLUR)
    # pic_up = im.transform(Image.ROTATE_180)
     #pic_gray.save("gray.jpg")
     #pic_blured.save("blured.jpg")
     #pic_up.save("up.jpg")