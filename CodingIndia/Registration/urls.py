from django.urls import path

from . import views


urlpatterns = [
    path('', views.SignUpView, name='signup_view'),
    path('Login/', views.LoginView, name='login_view'),
    path('Logout/', views.signout, name='logout_view'),

    
    path('VerifySignUpEmail/', views.VerifyOTP, name="verifyEmail"),
    path('VerifyLoginOTP/', views.VerifyLoginOTP, name="loginotp"),

    path('getUsername/', views.Getusername, name="getusername"),
    path('getEmail/', views.GetEmail, name="getEmail"),
]