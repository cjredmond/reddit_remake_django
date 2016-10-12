
from django.conf.urls import url
from django.contrib import admin
from app.views import example_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^example/$', example_view),
]
