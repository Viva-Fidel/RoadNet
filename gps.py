import serial

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Rodatec")

class Gps:
    def check_gps():
        try:
            gps = serial.Serial('com4', baudrate=9600)

            while True:
                ser_bytes = gps.readline()
                decoded_bytes = ser_bytes.decode('utf-8')
                data = decoded_bytes.split(',')

                if data[0] == '$GPRMS':
                    lat_nmea = data[3]
                    lat_degrees = lat_nmea[:2]

                    if data[6] == 'S':
                        latitude_degrees = float(lat_degrees) * -1
                    else:
                         latitude_degrees = float(lat_degrees)

                    latitude_degrees = str(latitude_degrees).strip('.0')
                    lat_ddd = lat_nmea[2:10]
                    lat_mmm = float(lat_ddd) / 60
                    lat_mmm = str(lat_mmm).strip('.0')[:8]
                    latitude = latitude_degrees + '.' + lat_mmm

                    long_nmea = data[5]
                    long_degrees = long_nmea[1:3]

                    if data[6] == 'W':
                        longitude_degrees = float(long_degrees) * -1
                    else:
                        longitude_degrees = float(long_degrees)

                    longitude_degrees = str(longitude_degrees).strip('.0')
                    long_ddd = long_nmea[3:10]
                    long_mmm = float(long_ddd) / 60
                    long_mmm = str(long_mmm).strip('.0')[:8]
                    longitude = longitude_degrees + '.' + long_mmm

                    location = geolocator.reverse(latitude, longitude)

                    return latitude, longitude, location.address

        except serial.SerialException:
            return ('No GPS connected')






