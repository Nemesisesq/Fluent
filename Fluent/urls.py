from django.conf.urls import patterns, include, url
from Main.views import *

from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', TemplateView.as_view(template_name='Main/home.html')),
                       url(r'^contact/', ContactFormView.as_view()),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^new_customer/', CustomerCreateView.as_view()),
                       url(r'^new_campaign/', CampaignCreateView.as_view()),
                       url(r'^new_ambassador/', AmbassadorCreateView.as_view()),
                       url(r'^new_points/', PointsCreateView.as_view()),
                       url(r'^update_customer/', CustomerUpdateView.as_view()),
                       url(r'^update_campaign/', CampaignUpdateView.as_view()),
                       url(r'^update_ambassador/', AmbassadorUpdateView.as_view()),
                       url(r'^update_points/', PointsUpdateView.as_view()),
                       url(r'^delete_customer/,', CustomerDeleteView.as_view()),
                       url(r'^delete_campaign/', CampaignrDeleteView.as_view()),
                       url(r'^delete_ambassador/', AmbassadorDeleteView.as_view()),
                       url(r'^delete_points/', PointsDeleteView.as_view()),
)