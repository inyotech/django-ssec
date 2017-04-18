from django.conf.urls import url

import weather.views

urlpatterns = [
    url(r'^latest_images/(?P<number>\d+)/$', weather.views.latest_images, name='latest_with_count'),
    url(r'^latest_images/$', weather.views.latest_images, name='latest'),
]
