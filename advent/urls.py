from django.conf.urls import patterns, include, url
from django.contrib import admin
from advent.views import FrontPage, CalendarView
from django.views.decorators.csrf import csrf_exempt 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', FrontPage.as_view(), name="login"),
    url(r'^calendar/(?P<name>\w+)$', csrf_exempt(CalendarView.as_view()), name="calendar"),
)
