import cv2
import numpy as np
import os
import string

# Create the directory structure
if not os.path.exists("data"):
    os.makedirs("data")
if not os.path.exists("data/train"):
    os.makedirs("data/train")
if not os.path.exists("data/test"):
    os.makedirs("data/test")

for i in range(7): #change the value = number of integer
    if not os.path.exists("data/train/" + str(i)):
        os.makedirs("data/train/" + str(i))
    if not os.path.exists("data/test/" + str(i)):
        os.makedirs("data/test/" + str(i))

for i in string.ascii_uppercase:
    if not os.path.exists("data/train/" + i):
        os.makedirs("data/train/" + i)
    if not os.path.exists("data/test/" + i):
        os.makedirs("data/test/" + i)
    
# train or test 
mode = 'train'
directory = 'data/'+mode+'/'
minValue = 70

cap = cv2.VideoCapture(0)
interrupt = -1  

while True:
    _, frame = cap.read()

    # Simulating mirror image
    frame = cv2.flip(frame, 1)
    
    # Getting count of existing images
    count = {
             'zero': len(os.listdir(directory+"/0")),
             'one': len(os.listdir(directory+"/1")),
             'two': len(os.listdir(directory+"/2")),
             'three': len(os.listdir(directory+"/3")),
             'four': len(os.listdir(directory+"/4")),
             'five': len(os.listdir(directory+"/5")),
             'six': len(os.listdir(directory+"/6")),
             'a': len(os.listdir(directory+"/A")),
             'b': len(os.listdir(directory+"/B")),
             'c': len(os.listdir(directory+"/C")),
             'd': len(os.listdir(directory+"/D")),
             'e': len(os.listdir(directory+"/E")),
             'f': len(os.listdir(directory+"/F")),
             'g': len(os.listdir(directory+"/G")),
             'h': len(os.listdir(directory+"/H")),
             'i': len(os.listdir(directory+"/I")),
             'j': len(os.listdir(directory+"/J")),
             'k': len(os.listdir(directory+"/K")),
             'l': len(os.listdir(directory+"/L")),
             'm': len(os.listdir(directory+"/M")),
             'n': len(os.listdir(directory+"/N")),
             'o': len(os.listdir(directory+"/O")),
             'p': len(os.listdir(directory+"/P")),
             'q': len(os.listdir(directory+"/Q")),
             'r': len(os.listdir(directory+"/R")),
             's': len(os.listdir(directory+"/S")),
             't': len(os.listdir(directory+"/T")),
             'u': len(os.listdir(directory+"/U")),
             'v': len(os.listdir(directory+"/V")),
             'w': len(os.listdir(directory+"/W")),
             'x': len(os.listdir(directory+"/X")),
             'y': len(os.listdir(directory+"/Y")),
             'z': len(os.listdir(directory+"/Z"))
             }
    
    # Printing the count in each set to the screen
    cv2.putText(frame, "ZERO : "+str(count['zero']), (10, 70), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "ONE : "+str(count['one']), (10, 80), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "TWO : "+str(count['two']), (10, 90), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "THREE : "+str(count['three']), (10, 110), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "FOUR : "+str(count['four']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "FIVE : "+str(count['five']), (10, 130), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "SIX : "+str(count['six']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "a : "+str(count['a']), (10, 150), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "b : "+str(count['b']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "c : "+str(count['c']), (10, 170), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "d : "+str(count['d']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "e : "+str(count['e']), (10, 190), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "f : "+str(count['f']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "g : "+str(count['g']), (10, 210), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "h : "+str(count['h']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "i : "+str(count['i']), (10, 230), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "k : "+str(count['k']), (10, 240), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "l : "+str(count['l']), (10, 250), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "m : "+str(count['m']), (10, 260), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "n : "+str(count['n']), (10, 270), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "o : "+str(count['o']), (10, 280), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "p : "+str(count['p']), (10, 290), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "q : "+str(count['q']), (10, 300), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "r : "+str(count['r']), (10, 310), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "s : "+str(count['s']), (10, 320), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "t : "+str(count['t']), (10, 330), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "u : "+str(count['u']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "v : "+str(count['v']), (10, 350), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "w : "+str(count['w']), (10, 360), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "x : "+str(count['x']), (10, 370), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "y : "+str(count['y']), (10, 380), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "z : "+str(count['z']), (10, 390), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)

    # Coordinates of the ROI
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])

    # Drawing the ROI
    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (220-1, 9), (620+1, 419), (255,0,0) ,1)

    # Extracting the ROI
    roi = frame[10:410, 220:520]
    #roi = cv2.resize(roi, (310, 310))
    
    cv2.imshow("Frame", frame)
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),2)
    th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
    ret, test_image = cv2.threshold(th3, minValue, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    cv2.imshow("Test", test_image)
    test_image = cv2.resize(test_image, (128,128))
     
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key for exit
        break
    if interrupt & 0xFF == ord('0'): # press 0
        cv2.imwrite(directory+'0/'+str(count['zero'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('1'): # press 1
        cv2.imwrite(directory+'1/'+str(count['one'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('2'): # press 2
        cv2.imwrite(directory+'2/'+str(count['two'])+'.jpg', test_image)       
    if interrupt & 0xFF == ord('3'): # press 3
        cv2.imwrite(directory+'3/'+str(count['three'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('4'): # press 4
        cv2.imwrite(directory+'4/'+str(count['four'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('5'): # press 5
        cv2.imwrite(directory+'5/'+str(count['five'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('6'): # press 6
        cv2.imwrite(directory+'6/'+str(count['six'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('a'): # press a
        cv2.imwrite(directory+'A/'+str(count['a'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('b'): # press b
        cv2.imwrite(directory+'B/'+str(count['b'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('c'): # press c
        cv2.imwrite(directory+'C/'+str(count['c'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('d'): # press d
        cv2.imwrite(directory+'D/'+str(count['d'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('e'): # press e
        cv2.imwrite(directory+'E/'+str(count['e'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('f'): # press f
        cv2.imwrite(directory+'F/'+str(count['f'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('g'): # press g
        cv2.imwrite(directory+'G/'+str(count['g'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('h'): # press h
        cv2.imwrite(directory+'H/'+str(count['h'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('i'): # press i
        cv2.imwrite(directory+'I/'+str(count['i'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('j'): # press j
        cv2.imwrite(directory+'J/'+str(count['j'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('k'): # press k
        cv2.imwrite(directory+'K/'+str(count['k'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('l'): # press l
        cv2.imwrite(directory+'L/'+str(count['l'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('m'): # press m
        cv2.imwrite(directory+'M/'+str(count['m'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('n'): # press n
        cv2.imwrite(directory+'N/'+str(count['n'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('o'): # press o
        cv2.imwrite(directory+'O/'+str(count['o'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('p'): # press p
        cv2.imwrite(directory+'P/'+str(count['p'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('q'): # press q
        cv2.imwrite(directory+'Q/'+str(count['q'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('r'): # press r
        cv2.imwrite(directory+'R/'+str(count['r'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('s'): # press s
        cv2.imwrite(directory+'S/'+str(count['s'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('t'): # press t
        cv2.imwrite(directory+'T/'+str(count['t'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('u'): # press u
        cv2.imwrite(directory+'U/'+str(count['u'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('v'): # press v
        cv2.imwrite(directory+'V/'+str(count['v'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('w'): # press w
        cv2.imwrite(directory+'W/'+str(count['w'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('x'): # press x
        cv2.imwrite(directory+'X/'+str(count['x'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('y'): # press y
        cv2.imwrite(directory+'Y/'+str(count['y'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('z'): # press z
        cv2.imwrite(directory+'Z/'+str(count['z'])+'.jpg', test_image)        
    
cap.release()
cv2.destroyAllWindows()