import sys
import datetime
import shutil
import pprint

import requests

url = "http://www.ssec.wisc.edu/data/us_comp/image7.jpg"
base_path = "/Users/scottb/PycharmProjects/ssec/ssec/weather/static/weather/images"

r = requests.get(url, stream=True)

if r.status_code != 200:
    raise Exception('download failed')

# Calculate the image time based on the current time.  It appears that
# the images are produced every 1/2 hour and labeled at 15 and 45
# after the hour.  Each image seems to become available about 15
# minutes after its labeled time.

download_time = datetime.datetime.utcnow()

if download_time.minute < 30:
    download_time = download_time - datetime.timedelta(hours=1)
    download_time = download_time.replace(minute=30)
else:
    download_time = download_time.replace(minute=0)

image_filename = download_time.strftime(base_path + '/image_%Y_%m_%d_%H_%M.jpg')

pprint.pprint(image_filename)

with open(image_filename, 'wb') as output:
    shutil.copyfileobj(r.raw, output)
