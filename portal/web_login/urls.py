from django.urls import path

from . import views

app_name = "login_web"
urlpatterns = [
    path('', views.InicioView.as_view(), name="inicio"),
    path('login', views.BasicLoginView.as_view(), name='login'),
    path('registro', views.RegistroView.as_view(), name='registro'),
    path('logout', views.LogoutView.as_view(), name='logout')
]
