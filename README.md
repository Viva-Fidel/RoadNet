# RoadNet
## Introduction
The programme detects 4 types of road damage: Pothole, Aligator crack, Transverse crack, Longitudinal crack using pretrained [Yolov7](https://github.com/WongKinYiu/yolov7) weights

## Installing

>!git clone https://github.com/Viva-Fidel/Yolov7-with-pytorch-weights.git

Additionally install CUDA if you want to use GPU for processing

## Requirements

opencv-python~=4.6.0.66  
numpy~=1.23.4  
torch~=1.12.1  
torchvision~=0.13.1  
requests~=2.28.1  
pyserial~=3.5  
geopy~=2.2. 

>!pip install -r requirements.txt

## Usage

#### Using video or camera
<b>self.source</b> - provide a path to your video file or camera

Example of good pistioning of camera  
<p></p>
<img src="https://user-images.githubusercontent.com/98227548/197174707-53b5e5d7-7535-4805-97c3-dd2f4a6f3a1c.png" height="160" width="540">

Example of detection  
<p></p>
<img src="https://user-images.githubusercontent.com/98227548/197181728-51741055-8ca8-42f9-b79b-9977b0678071.gif" height="360" width="540">  
<img src="https://user-images.githubusercontent.com/98227548/197185014-5034db7e-953c-4525-88c0-7345205a61bd.jpeg" height="360" width="540">

#### Using GPS
To use GPS detection is needed a USB GPS receiver. Next GPS receiver was used for this project: VK-172
<p></p>
<img src="https://user-images.githubusercontent.com/98227548/197186675-bf82cdfe-364e-404f-97a6-075151b170c2.png" height="360" width="540">

To configure GPS it is needed to introduce COM port where the GPS receiver is installed in gps.py  
<p></p>  
<img src="https://user-images.githubusercontent.com/98227548/197187087-2519577f-e7a4-44bb-91d4-8baae81e2436.png"> 

#### Saving data
By default the application will save scrennshots, video and GPS data in the folder where the application is installed. The folder would have a name with todays date. 
Example of saved images and video  
<p></p>  
<img src="https://user-images.githubusercontent.com/98227548/197189170-583d2165-bec0-4682-9e65-fa26912e39c7.png"> 
Example of saved GPS data  
If GPS is not connected correctly  
<p></p>  
<img src="https://user-images.githubusercontent.com/98227548/197189407-7e417885-ba77-468c-a883-237937fa3aed.png"> 
  
If GPS is connected correctly (latitude, longitude and location address)  
<p></p>  
<img src="https://user-images.githubusercontent.com/98227548/197191299-fd2458cf-39c4-437d-80fc-76881cf9126e.png"> 



