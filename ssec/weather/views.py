import os
import glob

from django.conf import settings
from django.shortcuts import render
from django.contrib.staticfiles.templatetags.staticfiles import static

def latest_images(request, number=48):

    number = int(number)

    path = os.path.join(settings.IMAGES_PATH, 'image_*.jpg')

    images = glob.glob(path)
    images.reverse()
    images = [os.path.basename(name) for name in images[:number]]

    image_urls = ['"{0}"'.format(static('weather/images/'+image)) for image in images]

    return render(request, 'weather/index.html', {'image_urls': image_urls})
