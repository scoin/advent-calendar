from django.conf.urls import patterns, include, url
from django.contrib import admin
from advent.views import FrontPage

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', FrontPage.as_view(), name="login")
)
