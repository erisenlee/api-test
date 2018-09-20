from django.urls import path
from . import views

#app namespace
app_name = 'account'

urlpatterns = [
    path('',views.index, name='index'),
    path('sign_up/',views.sign_up,name='sign_up'),
    path('sign_in/',views.sign_in,name='sign_in'),
]