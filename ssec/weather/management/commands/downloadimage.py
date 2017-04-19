import os
import shutil
import datetime

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

import requests

class Command(BaseCommand):
    help = "Download the latest satellite composite image from SSEC"

    url = "http://www.ssec.wisc.edu/data/us_comp/image7.jpg"

    base_path = settings.IMAGES_PATH


    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        r = requests.get(self.url, stream=True)

        if r.status_code != 200:
            raise CommandError('download failed')

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

        image_filename = download_time.strftime(os.path.join(self.base_path, 'ssec/image_%Y_%m_%d_%H_%M.jpg'))

        with open(image_filename, 'wb') as output:
            shutil.copyfileobj(r.raw, output)

        self.stdout.write(self.style.SUCCESS('Saved latetest image as %s' % (image_filename,)))
