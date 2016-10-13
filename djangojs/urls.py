
from django.conf.urls import url

from djangojs.views import UrlsJsonView


urlpatterns = [
    url(r'^urls\.json$', UrlsJsonView.as_view(), name='djangojs_urls'),
]
