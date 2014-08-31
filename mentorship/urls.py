from django.conf.urls import patterns, include, url
from program.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mentorship.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'home$',home),
    url(r'alumnilogin',alumnilogin),
    url(r'alumniregister',alumniregister),
    url(r'studentlogin',studentlogin),
    url(r'studentregister',studentregister),
)
