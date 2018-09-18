from django.urls import path
from .views import index,sign_up

app_name = 'account'

urlpatterns = [
    path('', index, name='index'),
    path('sign_up/',sign_up,name='sign_up'),
]