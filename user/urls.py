from django.urls import path

from . import views


urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
]
