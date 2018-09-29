from . import views
from django.urls import path


urlpatterns = [

    path('', views.index, name="index"),
    path('category', views.category, name='category'),

]