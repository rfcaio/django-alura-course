from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.recipe, name='recipe'),
    path('search', views.search, name='search'),
]
