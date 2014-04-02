from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
     # Examples:
     # url(r'^blog/', include('blog.urls')),

     url(r'^', include('core.urls')),
     url(r'^accounts/', include('accounts.urls')),
     url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
     url(r'^admin/', include(admin.site.urls)),
)