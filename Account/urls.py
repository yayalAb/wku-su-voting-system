from .views import RegisterAPI
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI
from django.urls import path,include
from .views import ChangePasswordView,signUp,Loginpage,logoutpage,change_password
from django.contrib.auth import  views as auth_views

urlpatterns = [
    path('',Loginpage,name="Loginpage"),
    path('signUp',signUp,name="signUp"),
    path ('logout', logoutpage, name="logoutpage"),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('change_password/', change_password, name='change_password'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path ('accounts/', include ('django.contrib.auth.urls')),

    path('reset_password',
         auth_views.PasswordResetView.as_view(template_name="account/password_reset.html"),name="reset_password"),

    path('password_reset_sent',
         auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_form.html"),
         name="password_reset_confirm"),

    path('password_reset_complete'
         ,auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset_done.html")
         ,name="password_reset_complete"),
]