from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^trader/$', views.reg_test, name='trader'),
    url(r'^index/$', views.registration, name='index'),
    url(r'^investor/$', views.reg_test, name='investor')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)