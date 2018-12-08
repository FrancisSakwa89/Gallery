from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    # url('^$',views.photos_today,name='photosToday'),
    url(r'^search/', views.search_results,name = 'search_results'),
    url(r'^location/(\d+)', views.location, name='location'),
    # url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_photos,name = 'pastPhotos'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)