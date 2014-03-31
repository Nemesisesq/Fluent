from django.conf.urls import patterns, include, url
from core.views import *
from django.views.generic import TemplateView

urlpatterns = patterns('',
     url(r'contact/', ContactFormView.as_view()),
     url(r'^dashboard/', TemplateView.as_view(template_name='core/dashboard.html'),name='dashboard'),

     url(r'new_customer/', CustomerCreateView.as_view()),
     url(r'new_campaign/', CampaignCreateView.as_view()),
     url(r'new_ambassador/', AmbassadorCreateView.as_view()),
     url(r'new_points/', PointsCreateView.as_view()),
     url(r'update_customer/(?P<pk>\d+)', CustomerUpdateView.as_view()),
     url(r'update_campaign/(?P<pk>\d+)', CampaignUpdateView.as_view()),
     url(r'update_ambassador/(?P<pk>\d+)', AmbassadorUpdateView.as_view()),
     url(r'update_points/(?P<pk>\d+)', PointsUpdateView.as_view()),
     url(r'delete_customer/(?P<pk>\d+)', CustomerDeleteView.as_view()),
     url(r'delete_campaign/(?P<pk>\d+)', CampaignrDeleteView.as_view()),
     url(r'delete_ambassador/(?P<pk>\d+)', AmbassadorDeleteView.as_view()),
     url(r'delete_points/(?P<pk>\d+)', PointsDeleteView.as_view()),
)