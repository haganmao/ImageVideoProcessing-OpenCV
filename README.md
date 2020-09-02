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


## Code

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



