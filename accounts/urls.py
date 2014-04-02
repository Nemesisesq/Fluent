from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',


                       url(r'login/$', 'accounts.views.login_view', name='login'),
                       url(r'^auth/$', 'accounts.views.auth_view',name = 'auth'),
                       url(r'^logout/', 'accounts.views.logout_view', name='logout'),
                       url(r'^loggedin/$', 'accounts.views.loggedin_view',name='loggedin'),
                       url(r'^invalid/$', 'accounts.views.invalid_view', name='invalid_login'),
                       url(r'^register/$', 'accounts.views.register_user', name='register_user'),
                       url(r'^register_success/$', 'accounts.views.register_success', name='register_success')

)
