#!/usr/bin/python
import RPi.GPIO as GPIO # gia na dosei prosvasi sta pins
import time # gia to timer 

import pygame #gia to sound

import tkinter as tk
from PIL import ImageTk, Image
root = tk.Tk()
root.attributes('-fullscreen', True)
img = ImageTk.PhotoImage(Image.open("/home/pi/Pictures/colors/introsound.png"))
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

#sound setup
pygame.mixer.init()
pygame.mixer.music.load("/home/pi/Music/putthecot.mp3")


#GPIO SETUP
pin = 4 # o arithmos twn pins
a=0
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)
start = time.time()

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)   

red = "/home/pi/Pictures/colors/red.png" # prepei na ftiaxtei to path
green = "/home/pi/Pictures/colors/green.png"
yellow = "/home/pi/Pictures/colors/yellow.png"



def callback(pin):


        global a
        global start 
        
        #print(start) arxiki wra se seconds linux
        print("Arxh")
        
        if GPIO.input(pin):
            #print ("Sound High")
            a=a+1
            print ("High, se epiasa, milas fores:")
            print (a)
            end = time.time()
            #time.sleep(1)
            b = (end-start)
            print("O xronos pu metraw einai:")
            print(b)
            #print("Telos")
            if (a > 3) and (b <= 10):
                print("Poly Milas")
                start = time.time()
                a=0
                #na paiksei o ixos
                pygame.mixer.music.play()
                #time.sleep(10) kati ginetai lathos giati synexizei na paizei
                image(red)

                time.sleep(10)
                
                
                                 
            elif (a <= 3) and (b > 10):
                print("Den Milaei Polu")
                start = time.time()#midenizo ton xrono
                a=0 #midenizo ton aritmo ton omiliwn
                image(yellow)

            elif (a > 3) and (b > 10):
                print ("midenizume giati perase polus xronos")
                a = 0
                start=time.time()
                image(green)

            else:
                print("Akoma ypoferesai High")
                image(green)
                



        else:
            #print ("Sound Low")
            a=a+1
            print ("Low, se epiasa, milas fores:")
            print (a)
            end = time.time()
            #time.sleep(1)
            b = (end-start)
            print("O xronos pu metraw einai:")
            print(b)
            #print("Telos")
            if (a > 3) and (b <= 10):
                print("Poly Milas")
                start = time.time()
                a=0
                #na paiksei o ixos
                pygame.mixer.music.play()
                #time.sleep(10) kati ginetai lathos giati meta kanei allo ena action
                image(red)

                time.sleep(10)
                
                
            elif (a <= 3) and (b > 10):
                print("Den Milaei Polu")
                start = time.time()#midenizo ton xrono
                a=0 #midenizo ton aritmo ton omiliwn
                image(yellow)

            elif (a > 3) and (b > 10):
                print ("midenizume giati perase polus xronos")
                a = 0
                start=time.time()
                image(green)

            
            else:
                print("Akoma ypoferesai Low")

                image(green)
            


GPIO.add_event_detect(pin, GPIO.BOTH, bouncetime=2000)  # o xrono apokrisis se kathe "xtupuma"/sound detection# let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(pin, callback)  # assign function to GPIO PIN, Run function on change

#infinite loop
def image(fasi):
    img2 = ImageTk.PhotoImage(Image.open(fasi))
    panel.configure(image=img2)
    panel.image = img2

while True:

    #root.bind("<Return>", image)
    root.mainloop()

    time.sleep(10)



    
    
