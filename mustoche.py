import face_recognition
import cv2
import PIL.Image
import PIL.ImageDraw
import os
from PIL import Image, ImageDraw
a="kn.png"
image=cv2.imread(a)
pil_image = PIL.Image.fromarray(image)
face_landmarks_list = face_recognition.face_landmarks(image)
d = ImageDraw.Draw(pil_image)
print(face_landmarks_list)

k = face_landmarks_list[0]['top_lip']
left =right=face_landmarks_list[0]['top_lip'][0][0]
bottom = face_landmarks_list[0]['top_lip'][0][1]
for k1 in k :
    if(left>k1[0]):
        left = k1[0]
    if(right<k1[0]):
        right = k1[0]
    if(bottom>k1[1]):
        bottom=k1[1]
k = face_landmarks_list[0]['nose_tip']
top =face_landmarks_list[0]['nose_tip'][0][1]
for k1 in k :
    if(top<k1[1]):
        top=k1[1]
	
print("ss")

#top,right,bottom,left =98, 613, 284, 428
#top,right,bottom,left =176,160,183,116
print(top,right,bottom,left)

draw_shape = PIL.ImageDraw.Draw(pil_image)
im = PIL.Image.open(a)
im = im.crop((left, top, right, bottom))
im.save("m9.png")
print("sn")
draw_shape.rectangle([left, top, right, bottom],outline="blue")
