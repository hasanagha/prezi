"""prezi URL Configuration"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

from search.views import PresentationsView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/$', csrf_exempt(PresentationsView.as_view())),
]
