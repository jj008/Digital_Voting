from django.urls import path
from . import views

urlpatterns = [
    path('register_vid', views.register_vid, name='register_vid'),
    path('otp', views.otp, name='otp'),
    path('register', views.register, name='register'),
    path('vhome', views.vhome, name='vhome'),
    path('vprocess', views.vprocess, name='vprocess'),
    path('vchangepassword', views.vchangepassword, name='vchangepassword'),
    path('vchange_password', views.vchange_password, name='vchange_password'),
    path('vprofile', views.vprofile, name='vprofile'),
    path('velection', views.velection, name='velection'),
    path('vote', views.vote, name='vote'),
    path('subvoteotp', views.subvoteotp, name='subvoteotp'),
    path('subvoteemailotp', views.subvoteemailotp, name='subvoteemailotp'),
    path('vviewcandidate', views.vviewcandidate, name='vviewcandidate'),
    path('vview_candidate', views.vview_candidate, name='vview_candidate'),
    path('vviewresult', views.vviewresult, name='vviewresult'),
    path('vview_result', views.vview_result, name='vview_result'),
    path('vview_result_filter', views.vview_result_filter, name='vview_result_filter'),
    path('vviewreport', views.vviewreport, name='vviewreport'),
    path('vview_report', views.vview_report, name='vview_report'),
    path('vcomplain', views.vcomplain, name='vcomplain'),
    path('submitcomplain', views.submitcomplain, name='submitcomplain'),
]