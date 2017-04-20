from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

import weather.views

urlpatterns = [
    url(r'^latest_images/(?P<number>\d+)/$', weather.views.latest_images, name='latest_with_count'),
    url(r'^latest_images/$', weather.views.latest_images, name='latest'),
]

urlpatterns += static(settings.IMAGES_URL, document_root=settings.IMAGES_PATH)
