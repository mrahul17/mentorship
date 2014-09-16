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
    url(r'^home$',home),
    url(r'^login',login),
    url(r'^register',register),
    url(r'^editProfile',editProfile),
    url(r'^showProfile',showProfile),
    url(r'^mentorlist',mentorlist),
    url(r'^dashboard',dashboard),
    url(r'^logout',logout),
    url(r'^selectmentor',selectmentor),
    url(r'^coordinator$',coordinator),
    url(r'^coordinator/list/(mentee|mentor)',showlist)
    
)
