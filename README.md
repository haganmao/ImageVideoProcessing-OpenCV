# ImageVideoProcessing-OpenCV
The project is for videos or images processing demostration, with using cv2 library from OpenCV.
The purpose of the script is for extracting iimages BGR channels, and also using cannyEdge for picture's edge detection.




## Blue Channel Demo imgs Feed from Camera

![d1](https://github.com/haganmao/ImageVideoProcessing-OpenCV/blob/master/BlueChannel%20deno.png "d1") 

<br>
<br>


## Green Channel Demo 

![d2](https://github.com/haganmao/ImageVideoProcessing-OpenCV/blob/master/GreenChannel%20demo.png "d2") 

<br>
<br>

## Red Channel Demo 

![d3](https://github.com/haganmao/ImageVideoProcessing-OpenCV/blob/master/RedChannel%20deno.png "d3") 

<br>
<br>

## Canny Edge Detection

![d4](https://github.com/haganmao/ImageVideoProcessing-OpenCV/blob/master/CannyEdge%20demo.png "d4") 

<br>
<br>


## Code demo Partial

'Read imgs

```Python
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

```

<br>

<br>

<br>

`Key Options check

```Python
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




```







