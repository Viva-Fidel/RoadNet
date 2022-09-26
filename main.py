import cv2
import geocoder
import imutils
import time
from detection import Pothole_detection

g = geocoder.ip('me')
print(g.latlng)
print(g.city)
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="pothole")
location = geolocator.reverse(f'{g.latlng[0]}, {g.latlng[1]}')
print(location.address)

cap = cv2.VideoCapture('test.mp4', cv2.CAP_FFMPEG)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 2)

#pd = Pothole_detection()

while cap.isOpened():
    #FPS = 1/cap.get(cv2.CAP_PROP_FPS)
    FPS = 0.02

    #print('About to start the Read command')
    ret, frame = cap.read()
    time.sleep(FPS)
    #Pothole_detection(frame)
    #frame = imutils.resize(frame, width=640)
    #print('About to show frame of Video.')
    cv2.imshow("Capturing",frame)
    #print('Running..')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()