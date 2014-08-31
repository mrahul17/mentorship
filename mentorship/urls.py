from django.conf.urls import patterns, include, url
from program.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mentorship.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',home),
    url(r'^admin/', include(admin.site.urls)),
    url(r'home$',home),
    url(r'login',login),
    url(r'register',register),
    
)
