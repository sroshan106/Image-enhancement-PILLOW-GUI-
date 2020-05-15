def rotate():
    global image
    image = image.rotate(90,expand = True)
    image.show()
    

def color_image():
    global image
    enhancer = ImageEnhance.Color(image)
    factor = 4
    enhancer.enhance(factor).show("color %f" % factor)

    
def sharpness_image():
    global image
    enhancer = ImageEnhance.Sharpness(image)
    factor = 20
    enhancer.enhance(factor).show("Sharpness %f" % factor)
    

def contrast_image():
    global image
    enhancer = ImageEnhance.Contrast(image)
    factor = 20
    enhancer.enhance(factor).show("contrast %f" % factor)
    
    
def brightness_image():
    global image
    enhancer = ImageEnhance.Brightness(image)
    factor = 0.4
    enhancer.enhance(factor).show("brightness %f" % factor)
    
    
def blur():
    global image
    image = image.filter(ImageFilter.BLUR)
    image.show()

def edges():
    global image
    image = image.filter(ImageFilter.FIND_EDGES)
    image.show()

def smooth():
    global image
    image = image.filter(ImageFilter.SMOOTH_MORE)
    image.show()

def emboss():
    global image
    image = image.filter(ImageFilter.EMBOSS)
    image.show()

def autoEnhance():
    global image
    image= ImageOps.autocontrast(image, cutoff=0, ignore=None)
    image.show()


def image_size():
    global image
    size = image.size
    print(size)
    
def flip_vertical():
    global image
    image = ImageOps.flip(image)
    image.show()

def grayscale():
    global image
    image = ImageOps.grayscale(image)
    image.show()

def mirror_image():
    global image
    image = ImageOps.mirror(image)
    image.show()

def compress():
    global image
    image.save("Converted_Image.jpeg","JPEG",optimize=True,quality=65)
    print("Image saved ")
    
def Directory():
    global image
    global path
    path = askopenfilename()
    image = Image.open(path)
   

def addButtons():
    button1 = tkinter.Button(root,text="Select Image",command=Directory)
    button1.place(relx=0.5,rely=0.5,anchor=CENTER)

    button3 = tkinter.Button(root,text="rotate",command=rotate)
    button3.place(relx=0.1,rely=0.6,anchor=CENTER)
    
    button4 = tkinter.Button(root,text="Color",command=color_image)
    button4.place(relx=0.32,rely=0.6,anchor=CENTER)
    
    button5 = tkinter.Button(root,text="Sharpen",command=sharpness_image)
    button5.place(relx=0.54,rely=0.6,anchor=CENTER)
    
    button6 = tkinter.Button(root,text="Contrast",command=contrast_image)
    button6.place(relx=0.76,rely=0.6,anchor=CENTER)
    
    button8 = tkinter.Button(root,text="Blur",command=blur)
    button8.place(relx=0.25,rely=0.9,anchor=CENTER)
    
    button9 = tkinter.Button(root,text="smoothen",command=smooth)
    button9.place(relx=0.50,rely=0.9,anchor=CENTER)
    
    button10 = tkinter.Button(root,text="Edge",command=edges)
    button10.place(relx=0.75,rely=0.9,anchor=CENTER)
    
    button11 = tkinter.Button(root,text="Emboss",command=emboss)
    button11.place(relx=0.1,rely=0.7,anchor=CENTER)
    
    button12 = tkinter.Button(root,text="Auto Enhance",command=autoEnhance)
    button12.place(relx=0.32,rely=0.7,anchor=CENTER)
    
    button13 = tkinter.Button(root,text="Get Image size",command=image_size)
    button13.place(relx=0.54,rely=0.7,anchor=CENTER)
    
    button14 = tkinter.Button(root,text="flip Vertical",command=flip_vertical)
    button14.place(relx=0.76,rely=0.7,anchor=CENTER)
    
    button7 = tkinter.Button(root,text="Brightness",command=brightness_image)
    button7.place(relx=0.1,rely=0.8,anchor=CENTER)
    
    button15 = tkinter.Button(root,text="Gray",command=grayscale)
    button15.place(relx=0.32,rely=0.8,anchor=CENTER)
    
    button16 = tkinter.Button(root,text="Mirror Image",command=mirror_image)
    button16.place(relx=0.54,rely=0.8,anchor=CENTER)
    
    button17 = tkinter.Button(root,text="Compress",command= compress)
    button17.place(relx=0.76,rely=0.8,anchor=CENTER)
    
def addImages(root):
    startframe = tkinter.Frame(root)
    canvas = tkinter.Canvas(startframe,width=250,height=250)
    startframe.place(relx = 0.5, rely = 0.3, anchor = CENTER)
    canvas.pack()
    root.one=one=tkinter.PhotoImage(file=r'Logo.png')
    canvas.create_image((0,0), image=one, anchor=NW)
    
from tkinter import *
import tkinter 
import tkinter.messagebox as tkMessageBox
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image,ImageEnhance,ImageFilter,ImageOps
import PIL

image=''

root = tkinter.Tk()
root.title("Image Blending tool")
root.geometry("700x700+200+100")
addButtons()
addImages(root)
root.mainloop()
