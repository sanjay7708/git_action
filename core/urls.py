from django.urls import path
from . views import LoginView,home

urlpatterns=[
    path('login/',LoginView.as_view(),name='login'),
    path('home/',home,name='home'),
]