import cv2
import geocoder
g = geocoder.ip('me')
print(g.latlng)
print(g.city)
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="pothole")
location = geolocator.reverse(f'{g.latlng[0]}, {g.latlng[1]}')
print(location.address)
#cap = cv2.VideoCapture('rtsp://admin:vhhv837sm4V123!@192.168.1.103:554/profile2/media.smp')

while True:

    #print('About to start the Read command')
    ret, frame = cap.read()
    #print('About to show frame of Video.')
    cv2.imshow("Capturing",frame)
    #print('Running..')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()