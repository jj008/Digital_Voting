from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('registervidpage', views.registervidpage, name='registervidpage'),
    path('forgotpassword', views.forgotpassword, name='forgotpassword'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('forgotpassotp', views.forgotpassotp, name='forgotpassotp'),
    path('setnewpassword', views.setnewpassword, name='setnewpassword'),
    path('logout', views.logout, name='logout'),
]