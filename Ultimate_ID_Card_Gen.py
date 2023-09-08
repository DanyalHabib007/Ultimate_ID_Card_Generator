# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 20:58:09 2023

@author: HP
"""

import random
import os
import datetime
import qrcode

import cv2 as ast
from PIL import Image, ImageDraw, ImageFont

import mysql.connector as m

image = Image.new('RGB', (1000, 900), (255, 255, 255))
draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size=45)

os.system("Title: ID CARD Generator by Grasp Coding")

d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\t ID CARD Generator\t\t\t\t\t  %I:%M:%S %p")
print(
    '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(reg_format_date)
print(
    '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

# starting position of the message
(x, y) = (50, 50)
message = input('\nEnter Your Company Name: ')
company = message
color = 'rgb(0, 0, 0)'
font = ImageFont.truetype('arial.ttf', size=80)
draw.text((x, y), message, fill=color, font=font)

# adding an unique id number. You can manually take it from user
(x, y) = (600, 75)
idno = random.randint(10000000, 90000000)
message = str('ID: ' + str(idno))
color = 'rgb(0, 0, 0)'  # black color
font = ImageFont.truetype('arial.ttf', size=60)
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 250)
message = input('Enter Your Full Name: ')
name = message
message = str('Name: ' + str(message))
color = 'rgb(0, 0, 0)'  # black color
font = ImageFont.truetype('arial.ttf', size=45)
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 350)
message = input('Enter Your Gender: ')
gender = message
message = str('Gender: ' + str(message))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), message, fill=color, font=font)

(x, y) = (400, 350)
message = int(input('Enter Your Age: '))
age = message
message = str('Age: ' + str(message))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 450)
message = input('Enter Your Date Of Birth: ')
dob = message
message = str('Date of Birth: ' + str(message))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 550)
message = input('Enter Your Blood Group: ')
bldgp = message
message = str('Blood Group: ' + str(message))
color = 'rgb(255, 0, 0)'  # black color
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 650)
message = int(input('Enter Your Mobile Number: '))
temp = message
message = str('Mobile Number: ' + str(message))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 750)
message = input('Enter Your Address: ')
address = message
message = str('Address: ' + str(message))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), message, fill=color, font=font)


# save the edited image

image.save(str(name)+ ".png")

img = qrcode.make(str(company)+" "+ str(idno))  # this info. is added in QR code, also add other things
img.save(str(idno)+ ".bmp")

til = Image.open((name)+ ".png")
im = Image.open(str(idno) +".bmp")  # 25x25
til.paste(im, (650, 500))
til.save(name +".png")

#click photo 
cam_port = 0
cam = ast.VideoCapture(cam_port)

result, image = cam.read()

if result:
  
    # showing result, it take frame name and image 
    # output
    #ast.imshow(str(name)+"_photo", image)
  
    # saving image in local storage
    ast.imwrite(str(name)+"_photo"+".png", image)
  
    # If keyboard interrupt occurs, destroy image 
    # window
    ast.waitKey(0)
    #ast.destroyWindow("Cam Capture")
  
# If captured image is corrupted, moving to else part
else:
    print("No image detected. Please! try again")
    
# Resize Image

with Image.open(str(name)+"_photo.png") as im:
    im.thumbnail((200,200))
    im.save(str(name)+"_photo_copy.png")
    
#Pasting photo
til = Image.open((name)+ ".png")
im = Image.open(str(name)+"_photo_copy.png")  
til.paste(im, (700, 200))
til.save(name +".png")
    
#storing data in mysql
cnn = m.connect(host='localhost',password='hUnder@n0te', user='root', database='employee_details')

if cnn.is_connected():
    print("Connected to Database")
else:
    print("Connection not Established")
    


mycursor = cnn.cursor()

sql = "INSERT INTO employee (idno, company, name, gender, age, dob, bldgp, phn_no, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = (str(idno),str(company),str(name),str(gender),str(age),str(dob),str(bldgp),str(temp),str(address))
mycursor.execute(sql, val)

cnn.commit()

print(('\n\n\nYour ID Card Successfully created in a PNG file ' + name + '.png'))
input('\n\nPress any key to Close program...')
