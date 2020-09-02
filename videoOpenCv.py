import cv2
import argparse
import numpy as np
import time
import matplotlib.pyplot as plt

#ndex to save the capture video
i = 1

#create a VideoCapture object to read from the camera (pass 0)
cap =  cv2.VideoCapture(0)


#default state set to zero for  display original BGR frame 
#state = 1 display edgeCanny frame
#state = 2 display blueChannel frame
#state = 3 display greenChannel frame
#state = 4 display redChannel frame
#state = 5 pause video
#state = 6 quit video
state = 0 


#default code set to zero for saving bgr channel video
code = 0

#set default s key pressed is false
s_key_pressed = False

#fourcc code which is 'MJPG' for mac OS
fourcc = cv2.VideoWriter_fourcc(*'MJPG')

#saving video width and height
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


#These four function is used to write the video into specified folder
def outBGR_channel(bgr_Frame):
    outBGRchannel.write(bgr_Frame)
   

def outCanny_Edge(edge_Frame):
    outCannyEdge.write(edge_Frame)

def outBlue_Channel(blue_c):
    outBlueChannel.write(blue_c)

def outGreen_Channel(green_c):
    outGreenChannel.write(green_c)

def outRed_Channel(red_c):
    outRedChannel.write(red_c)



#call the VideoWriter to save the new video
outBGRchannel = cv2.VideoWriter('./Part_B/output_BGRchannel_Video_{}.avi'.format(i),fourcc, 15.0, (width, height),True)
outCannyEdge = cv2.VideoWriter('./Part_B/output_CannyEdge_Video_{}.avi'.format(i),fourcc, 12.0, (width, height),False)
outBlueChannel = cv2.VideoWriter('./Part_B/output_BlueChannel_Video_{}.avi'.format(i),fourcc, 15.0, (width, height),True)
outGreenChannel = cv2.VideoWriter('./Part_B/output_GreenChannel_Video_{}.avi'.format(i),fourcc, 15.0, (width, height),True)
outRedChannel = cv2.VideoWriter('./Part_B/output_RedChannel_Video_{}.avi'.format(i),fourcc, 15.0, (width, height),True)



#Check if camera opened successfully
if cap.isOpened() is False:
    print('error opening the video file!')




#Read until video is completed
while cap.isOpened():
    #Capture frame-by-frame from the camera
    ret, frame = cap.read()
    key = cv2.waitKey(30)
    
    #copy blue, green, red channels
    b = frame.copy()
    g = frame.copy()
    r = frame.copy()

    #The matrix used for storing any channel image consists of 3 channels. 
    #2 of which are set to zero and the remaining one shows the output in corresponding colour
    #b for blue channel, g for green channel, r for red channel
    b[:,:,1]=0
    b[:,:,2]=0
    g[:,:,0]=0
    g[:,:,2]=0
    r[:,:,0]=0
    r[:,:,1]=0


    #Convert the frame captured from the camera to grayscale
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #Convert the grayscale frame to CannyEdge frame :
    cannyEdge = cv2.Canny(gray_frame,70, 150)

    #restore the 3 channels 
    bgrFrame = frame[:,:,:]



    #display current frame
    cv2.imshow('frame', frame)    

    #check if next frame is true
    if ret is True:


        #dict for calling different fuctions
        switch = {
            0: outBGR_channel, 
            1: outCanny_Edge,
            2: outBlue_Channel,
            3: outGreen_Channel,
            4: outRed_Channel
        }


        #state value used for displaying proper frame, default is 0 which used for present bgr channel images
        #set up the state value to each key
        #check if press 'd' key, set state = 0
            #  elif press 'c' key, set state = 1, which used for present video anny edge 
            #  elif press 'b', set state = 2, which used for present video blue channel 
            #  elif press 'g', set state = 3, which used for present video greem channel 
            #  elif press 'r', set state = 4, which used for present video red channel 
            #  elif press 's', set state = 7, which used for saving video 
            #  elif press 'p', set state = 5, which used for pause video
            #  elif press 'q', set state = 6, which used for quite video

        if ord('d') == key & 0xFF:
            state = 0
        elif ord('c') == key & 0xFF:
            state = 1
        elif ord('b') == key & 0xFF:
            state = 2
        elif ord('g') == key & 0xFF:
            state = 3
        elif ord('r') == key & 0xFF:
            state = 4 
        elif ord('s') == key & 0xFF:
            state = 7
        elif ord('p') == key & 0xFF:
            state = 5          
        elif ord('q') == key & 0xFF:
            state = 6
     
        #show video in same window name as 'frame', then copy the state values to 'code'
        # check if state == 0, show bgr frame video 
                #elif state == 1, show canny edge video  
                #elif state == 2, show blue channel video  
                #elif state == 3, show green channel video  
                #elif state == 4, show red channel video  
                #elif state == 5, pause the video until the 'p' key press again
                #elif state == 6, quit the video
                  
        if state == 0:
            cv2.imshow('frame', bgrFrame)
            code = state
        elif state == 1:  
            cv2.imshow('frame', cannyEdge)
            code = state     
        elif state == 2:
            cv2.imshow('frame', b)
            code = state 
        elif state == 3:        
            cv2.imshow('frame', g)
            code = state 
        elif state == 4:
            cv2.imshow('frame', r)
            code = state 
        elif state == 5:
            if ord('p') == key:
                cv2.waitKey(-1)
        elif state == 6:
            break


        #save video 
        # check if the s key is pressed first
        # Then check saving code and the booling value s_key_pressed 
        # if code == 0 and s_key_pressed is false, then copy the BGRchannel, starting to record, then cope the code 
        # elif code == 1 and s_key_pressed is false, then copy the canny edge, starting to record, then cope the code 
        # elif code == 2 and s_key_pressed is false, then copy the blue channel, starting to record, then cope the code 
        # elif code == 3 and s_key_pressed is false, then copy the green channel, starting to record, then cope the code 
        # elif code == 4 and s_key_pressed is false, then copy the red channel, starting to record, then cope the code 
        
        if key & 0xFF == ord('s'):
            if s_key_pressed == False and code == 0:
                outBGRchannel = outBGRchannel
                s_key_pressed = True
                code = code              
            elif s_key_pressed == False and code == 1:
                outCannyEdge = outCannyEdge
                s_key_pressed = True
                code = code
            elif s_key_pressed == False and code == 2:
                outBlueChannel = outBlueChannel
                s_key_pressed = True
                code = code
            elif s_key_pressed == False and code == 3:
                outGreenChannel = outGreenChannel
                s_key_pressed = True
                code = code
            elif s_key_pressed == False and code == 4:
                outRedChannel = outRedChannel
                s_key_pressed = True
                code = code            
            else:
                s_key_pressed = False

        #write the video, check the code and s_key_pressed must be true then calling the dict 'switch', pass the arg
        # for example switch[i](arg) 
        if s_key_pressed and code == 0:
            switch[0](bgrFrame)
        elif s_key_pressed and code == 1:
            switch[1](cannyEdge)
        elif s_key_pressed and code == 2:
            switch[2](b)
        elif s_key_pressed and code == 3:
            switch[3](g)
        elif s_key_pressed and code == 4:
            switch[4](r)

    #if ret is false which means no any frame can be feed, break the while loop then destory the window     
    else:
        break


#Release everything and destory the window
cap.release()
outBGRchannel.release()
outCannyEdge.release()
outBlueChannel.release()
outGreenChannel.release()
outRedChannel.release()
cv2.destroyAllWindows()


