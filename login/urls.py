from django.urls import path
from . import views


app_name='login'
urlpatterns=[
path('',views.index,name='index'),
path('auth',views.auth,name='auth'),
path('logout',views.logout,name='logout')

]
