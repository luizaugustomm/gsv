# GSV (Google Street View package)

Third-party package that accesses Google Street View API and downloads images according to given parameters.

## How to install

You can install `gsv` using pip:
```
pip install gsv
```

## How to configure

- In order to access Google Street View Image API, you need to get a [key](https://developers.google.com/maps/documentation/streetview/get-api-key) before.
- Create a config.py file and write the following:
```
SECRET_KEY = #Your secret key from Google Street View Image API
```
**Important**: Remember to hide your `config.py` file if you intend to publish your code publically. In case of publishing that on Github, add `config.py` in the `.gitignore` file.

## How to use

```
import gsv

from config import SECRET_KEY

client = gsv.Client(SECRET_KEY)

locations = ['-7.215781,-35.899323',
             '-7.218945,-35.89079',
             '-7.223492,-35.884135',
             '-7.218858,-35.891135',
             '-7.215756,-35.899508',
             '-7.224195,-35.893263']

for location in locations:
    client.save_view(location)
```

The code above has some locations based on `[latitude, longitude]` and downloads the images from each of these locations.

The images are automatically saved in a folder named `gsv-out`.
