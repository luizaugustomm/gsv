
import requests
import shutil
import os


class Client():

    def __init__(self, api_key):
        self.api_key = api_key
        self.url = 'https://maps.googleapis.com/maps/api/streetview'

    def get_view(self, location, size='600x600', heading=0, fov=90, pitch=0):
        """location: can be either a text string (such as Chagrin Falls, OH) or a lat/lng value (40.457375,-80.009353)
           size: specifies the output size of the image in pixels
           heading: indicates the compass heading of the camera (min=0, max=360) [0 or 360 = north; 90 = east; 180 = south]
           fov (zoom): determines the horizontal field of view of the image (min=0, max=120, default=90)
           pitch = specifies the up or down angle of the camera relative to the Street View vehicle (default=0)"""
        return requests.get(self.url, params={'location': location,
                                              'size': size,
                                              'heading': heading,
                                              'fov': fov,
                                              'pitch': pitch},
                                      stream=True)

    def save_view(self, location, size='600x600', heading=0, filename=None, **kwords):
        if not filename:
            filename = 'gsv-{}-{}-{}.jpg'.format(location.strip(), heading, size)
        directory = 'gsv-out'
        if not os.path.exists(directory):
            os.mkdir(directory)
        response = self.get_view(location.strip(), size=size, heading=heading, **kwords)
        if response.status_code == 200:
            with open(directory+'/'+filename, 'wb') as f:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, f)
            print '{} saved in "{}"'.format(filename, directory)
        else:
            print 'Something went wrong!'
